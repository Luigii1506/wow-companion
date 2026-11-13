"""Cliente HTTP de la API de ForeverDB: clave, limites, cache en disco y errores.

Reglas que aplica (terminos leidos en https://foreverdb.net/developers, 2026-11-13):
- Clave personal en FOREVERDB_API_KEY (entorno o `.env` en la raiz). Nunca se imprime,
  ni se guarda en la cache, ni aparece en los mensajes de error.
- Como maximo 25 peticiones por minuto (limite real: 30) y 4500 al dia (limite real:
  5000), contadas en `data/foreverdb/usage.json`.
- 429: respeta Retry-After. 402: suscripcion necesaria. 403: clave o User-Agent.
- Cache local de 7 dias en `data/foreverdb/cache/`; los datos no salen de esta maquina.

Solo biblioteca estandar.
"""

from __future__ import annotations

import email.utils
import hashlib
import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import deque
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Callable, Iterator, Mapping

from .common import (
    BASE_URL,
    CACHE_DIR,
    DEFAULT_TTL_DAYS,
    ENV_FILE,
    ENV_VAR,
    MAX_LIMIT,
    MAX_PER_DAY,
    MAX_PER_MINUTE,
    MAX_RETRY_WAIT_S,
    USAGE_PATH,
    USER_AGENT,
)


# ---------------------------------------------------------------- errores

class ForeverDBError(Exception):
    def __init__(self, message: str, status: int | None = None):
        super().__init__(message)
        self.status = status


class MissingKeyError(ForeverDBError):
    pass


class AuthError(ForeverDBError):
    pass


class SubscriptionRequiredError(ForeverDBError):
    pass


class ForbiddenError(ForeverDBError):
    pass


class RateLimitError(ForeverDBError):
    pass


class DailyLimitError(ForeverDBError):
    pass


class NotFoundError(ForeverDBError):
    pass


# ---------------------------------------------------------------- clave

def parse_env_file(path: Path) -> dict[str, str]:
    """Lee un `.env` sencillo: KEY=valor, comentarios con #, comillas opcionales."""
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export "):].lstrip()
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key, value = key.strip(), value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
            value = value[1:-1]
        elif " #" in value:
            value = value.split(" #", 1)[0].rstrip()
        values[key] = value
    return values


def load_api_key(env: Mapping[str, str] | None = None, env_file: Path = ENV_FILE) -> str:
    """Clave desde la variable de entorno o, si falta, desde `.env`. Lanza MissingKeyError."""
    env = os.environ if env is None else env
    key = (env.get(ENV_VAR) or "").strip()
    if not key:
        key = parse_env_file(env_file).get(ENV_VAR, "").strip()
    if not key:
        raise MissingKeyError(
            f"Falta la clave de la API de ForeverDB. Copia .env.example a .env en la raiz del "
            f"repositorio y pon tu clave en {ENV_VAR}= (o exporta la variable {ENV_VAR}). "
            "La clave se obtiene en https://foreverdb.net/developers. No la subas a git."
        )
    return key


# ---------------------------------------------------------------- limites

class RateLimiter:
    """Ventana deslizante: como maximo `max_calls` peticiones en `period` segundos."""

    def __init__(self, max_calls: int = MAX_PER_MINUTE, period: float = 60.0,
                 clock: Callable[[], float] = time.monotonic, sleep: Callable[[float], None] = time.sleep):
        self.max_calls = max_calls
        self.period = period
        self._clock = clock
        self._sleep = sleep
        self._stamps: deque[float] = deque()

    def wait(self) -> None:
        now = self._clock()
        while self._stamps and now - self._stamps[0] >= self.period:
            self._stamps.popleft()
        if len(self._stamps) >= self.max_calls:
            delay = self.period - (now - self._stamps[0])
            if delay > 0:
                self._sleep(delay)
            now = self._clock()
            while self._stamps and now - self._stamps[0] >= self.period:
                self._stamps.popleft()
        self._stamps.append(self._clock())


class DailyCounter:
    """Contador local por dia UTC guardado en usage.json. Rechaza pasar de `max_per_day`."""

    def __init__(self, path: Path = USAGE_PATH, max_per_day: int = MAX_PER_DAY,
                 now: Callable[[], datetime] = lambda: datetime.now(timezone.utc)):
        self.path = path
        self.max_per_day = max_per_day
        self._now = now

    def _today(self) -> str:
        return self._now().astimezone(timezone.utc).date().isoformat()

    def read(self) -> dict:
        today = self._today()
        if not self.path.exists():
            return {"date": today, "count": 0}
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
            count = int(data.get("count", 0))
        except (ValueError, TypeError, AttributeError):
            raise ForeverDBError(
                f"{self.path} esta danado. Revisalo o borralo (perderas el recuento de hoy)."
            ) from None
        if data.get("date") != today:
            return {"date": today, "count": 0}
        return {"date": today, "count": count}

    def remaining(self) -> int:
        return max(0, self.max_per_day - self.read()["count"])

    def consume(self) -> int:
        """Anota una peticion antes de enviarla. Devuelve el total de hoy."""
        state = self.read()
        if state["count"] >= self.max_per_day:
            raise DailyLimitError(
                f"Tope diario local alcanzado ({state['count']}/{self.max_per_day} peticiones hoy, "
                f"dia UTC {state['date']}). El limite de ForeverDB es 5000/dia; paramos antes. "
                "Usa la cache o espera a manana (UTC)."
            )
        state["count"] += 1
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(state) + "\n", encoding="utf-8")
        tmp.replace(self.path)
        return state["count"]


# ---------------------------------------------------------------- cache

def cache_key(endpoint: str, params: Mapping | None) -> str:
    return endpoint + "?" + urllib.parse.urlencode(sorted(clean_params(params).items()))


def clean_params(params: Mapping | None) -> dict[str, str]:
    out: dict[str, str] = {}
    for k, v in (params or {}).items():
        if v is None or v == "":
            continue
        if isinstance(v, bool):
            v = "1" if v else "0"
        out[str(k)] = str(v)
    return out


class DiskCache:
    """Un JSON por consulta: endpoint, parametros, URL, fetched_at (UTC), build y respuesta."""

    def __init__(self, directory: Path = CACHE_DIR, ttl: timedelta = timedelta(days=DEFAULT_TTL_DAYS),
                 now: Callable[[], datetime] = lambda: datetime.now(timezone.utc)):
        self.directory = directory
        self.ttl = ttl
        self._now = now

    def path_for(self, endpoint: str, params: Mapping | None) -> Path:
        digest = hashlib.sha256(cache_key(endpoint, params).encode("utf-8")).hexdigest()[:24]
        slug = re.sub(r"[^A-Za-z0-9]+", "_", endpoint).strip("_")[:60] or "root"
        return self.directory / f"{slug}__{digest}.json"

    def get(self, endpoint: str, params: Mapping | None) -> dict | None:
        path = self.path_for(endpoint, params)
        if not path.exists():
            return None
        try:
            entry = json.loads(path.read_text(encoding="utf-8"))
            fetched = datetime.fromisoformat(entry["fetched_at"].replace("Z", "+00:00"))
        except (ValueError, KeyError, TypeError):
            return None
        if self._now() - fetched > self.ttl:
            return None
        return entry

    def put(self, entry: dict) -> Path:
        path = self.path_for(entry["endpoint"], entry["params"])
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(entry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        tmp.replace(path)
        return path


# ---------------------------------------------------------------- HTTP

def urllib_transport(url: str, headers: dict[str, str], timeout: float = 30.0) -> tuple[int, dict, bytes]:
    """GET. Devuelve (status, cabeceras en minusculas, cuerpo) tambien para 4xx/5xx."""
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, {k.lower(): v for k, v in resp.headers.items()}, resp.read()
    except urllib.error.HTTPError as e:
        hdrs = {k.lower(): v for k, v in (e.headers or {}).items()}
        return e.code, hdrs, e.read()
    except urllib.error.URLError as e:
        raise ForeverDBError(f"error de red: {e.reason}") from None


def parse_retry_after(value: str | None, now: Callable[[], datetime]) -> float | None:
    if not value:
        return None
    value = value.strip()
    try:
        return max(0.0, float(value))
    except ValueError:
        pass
    try:
        when = email.utils.parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return None
    if when.tzinfo is None:
        when = when.replace(tzinfo=timezone.utc)
    return max(0.0, (when - now()).total_seconds())


def extract_build(meta: Mapping | None) -> str | None:
    """La documentacion dice que meta trae la build del juego, sin fijar el nombre del campo."""
    if not isinstance(meta, Mapping):
        return None
    for k in ("build", "gameBuild", "game_build", "version"):
        v = meta.get(k)
        if isinstance(v, (str, int)) and str(v):
            return str(v)
        if isinstance(v, Mapping):
            for kk in ("build", "version", "id", "name"):
                if isinstance(v.get(kk), (str, int)):
                    return str(v[kk])
    return None


def _error_detail(body: bytes) -> str:
    text = body[:400].decode("utf-8", "replace")
    try:
        data = json.loads(text)
    except ValueError:
        return text.strip()[:200]
    if isinstance(data, dict):
        err = data.get("error") or data.get("message") or data
        if isinstance(err, dict):
            err = err.get("message") or err.get("code") or err
        return str(err)[:200]
    return str(data)[:200]


class ForeverDBClient:
    def __init__(
        self,
        api_key: str | None = None,
        transport: Callable = urllib_transport,
        cache: DiskCache | None = None,
        limiter: RateLimiter | None = None,
        counter: DailyCounter | None = None,
        sleep: Callable[[float], None] = time.sleep,
        now: Callable[[], datetime] = lambda: datetime.now(timezone.utc),
        env: Mapping[str, str] | None = None,
        env_file: Path = ENV_FILE,
        max_retries: int = 2,
        base_url: str = BASE_URL,
    ):
        self._api_key = api_key
        self._env = env
        self._env_file = env_file
        self.transport = transport
        self.cache = cache if cache is not None else DiskCache(now=now)
        self.limiter = limiter if limiter is not None else RateLimiter()
        self.counter = counter if counter is not None else DailyCounter(now=now)
        self._sleep = sleep
        self._now = now
        self.max_retries = max_retries
        self.base_url = base_url.rstrip("/")
        self.network_calls = 0

    def __repr__(self) -> str:  # nunca mostrar la clave
        return f"ForeverDBClient(base_url={self.base_url!r})"

    # La clave se carga solo cuando hace falta red: las consultas en cache funcionan sin ella.
    def _key(self) -> str:
        if not self._api_key:
            self._api_key = load_api_key(self._env, self._env_file)
        return self._api_key

    def _scrub(self, text: str) -> str:
        return text.replace(self._api_key, "[clave oculta]") if self._api_key else text

    def url_for(self, endpoint: str, params: Mapping | None = None) -> str:
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint
        query = urllib.parse.urlencode(clean_params(params))
        return f"{self.base_url}{endpoint}" + (f"?{query}" if query else "")

    def get(self, endpoint: str, params: Mapping | None = None, refresh: bool = False) -> dict:
        """Devuelve {endpoint, params, url, fetched_at, build, data, meta, from_cache}."""
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint
        params = clean_params(params)
        if not refresh:
            hit = self.cache.get(endpoint, params)
            if hit is not None:
                return {**hit, "from_cache": True}
        body = self._request(self.url_for(endpoint, params))
        try:
            payload = json.loads(body.decode("utf-8"))
        except (UnicodeDecodeError, ValueError):
            raise ForeverDBError("La respuesta de ForeverDB no es JSON.") from None
        if not isinstance(payload, dict) or "data" not in payload:
            raise ForeverDBError("Respuesta inesperada: falta el campo 'data'.")
        meta = payload.get("meta") or {}
        entry = {
            "endpoint": endpoint,
            "params": params,
            "url": self.url_for(endpoint, params),
            "fetched_at": self._now().astimezone(timezone.utc).replace(microsecond=0)
                          .isoformat().replace("+00:00", "Z"),
            "build": extract_build(meta),
            "data": payload["data"],
            "meta": meta,
        }
        self.cache.put(entry)
        return {**entry, "from_cache": False}

    def _request(self, url: str) -> bytes:
        headers = {
            "X-API-Key": self._key(),
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
        }
        attempt = 0
        while True:
            self.counter.consume()
            self.limiter.wait()
            self.network_calls += 1
            status, resp_headers, body = self.transport(url, headers)
            if 200 <= status < 300:
                return body
            detail = self._scrub(_error_detail(body))
            if status == 429:
                wait = parse_retry_after(resp_headers.get("retry-after"), self._now)
                if wait is None:
                    wait = 60.0
                if attempt >= self.max_retries or wait > MAX_RETRY_WAIT_S:
                    raise RateLimitError(
                        f"ForeverDB devolvio 429 (limite de peticiones). Pide esperar {wait:.0f} s. "
                        "Vuelve a intentarlo mas tarde o usa la cache.", status=429)
                self._sleep(wait)
                attempt += 1
                continue
            if status == 401:
                raise AuthError(
                    f"ForeverDB rechazo la clave (401): {detail}. Revisa {ENV_VAR} en .env.", status=401)
            if status == 402:
                raise SubscriptionRequiredError(
                    "ForeverDB devolvio 402 subscription_required: este endpoint o este volumen no "
                    f"esta incluido en el plan gratuito. Detalle: {detail}", status=402)
            if status == 403:
                if "1010" in detail:
                    raise ForbiddenError(
                        "403 de Cloudflare (error 1010): ha bloqueado el User-Agent del cliente. "
                        "Este adaptador envia uno descriptivo; si persiste, revisa USER_AGENT en common.py.",
                        status=403)
                raise ForbiddenError(
                    f"ForeverDB devolvio 403 (prohibido): {detail}. Puede ser una clave invalida, "
                    "revocada o sin permiso para este endpoint.", status=403)
            if status == 404:
                raise NotFoundError(f"No encontrado (404): {url}", status=404)
            raise ForeverDBError(f"HTTP {status} de ForeverDB: {detail}", status=status)

    def paginate(self, endpoint: str, params: Mapping | None = None, max_items: int = 100,
                 page_size: int = MAX_LIMIT, refresh: bool = False) -> Iterator[dict]:
        """Recorre una lista con limit/offset hasta `max_items` o el final. Cada pagina es una peticion."""
        params = dict(clean_params(params))
        offset = int(params.pop("offset", 0) or 0)
        page_size = max(1, min(MAX_LIMIT, page_size))
        yielded = 0
        while yielded < max_items:
            limit = min(page_size, max_items - yielded)
            page = self.get(endpoint, {**params, "limit": limit, "offset": offset}, refresh=refresh)
            rows = page["data"] if isinstance(page["data"], list) else []
            yield page
            yielded += len(rows)
            offset += len(rows)
            total = page_total(page.get("meta"))
            if not rows or len(rows) < limit or (total is not None and offset >= total):
                return


def page_total(meta: Mapping | None) -> int | None:
    if not isinstance(meta, Mapping):
        return None
    for k in ("total", "totalCount", "total_count", "count"):
        v = meta.get(k)
        if isinstance(v, int):
            return v
    pag = meta.get("pagination")
    if isinstance(pag, Mapping):
        return page_total(pag)
    return None


def collect(client: ForeverDBClient, endpoint: str, params: Mapping | None = None,
            max_items: int = 100, refresh: bool = False) -> dict:
    """Une varias paginas en una sola respuesta (data = lista concatenada)."""
    pages = list(client.paginate(endpoint, params, max_items=max_items, refresh=refresh))
    first, last = pages[0], pages[-1]
    rows: list = []
    for p in pages:
        if isinstance(p["data"], list):
            rows.extend(p["data"])
    return {**last, "url": first["url"], "data": rows, "pages": len(pages),
            "from_cache": all(p["from_cache"] for p in pages)}
