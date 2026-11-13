"""Descarga tablas DB2 de WoW Forever desde wago.tools como CSV.

Normas de la fuente (https://wago.tools/llms.txt, robots.txt):
- Solo rutas /api/ y /db2/{tabla}/csv. Nunca las paginas HTML del navegador DB2.
- Fijar una version exacta (cadena completa) sin selector de producto, y registrar
  producto y version con los resultados.
- Reutilizar las descargas en lugar de repetirlas.

Uso:
    python3 -m tools.wago.fetch                     # ultima build de wowf
    python3 -m tools.wago.fetch --version 1.60.1.70938 --tables ItemSparse SpellName
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

from .common import (
    BASE_URL,
    DATA_DIR,
    DEFAULT_TABLES,
    PRODUCT,
    USER_AGENT,
    parse_csv_text,
    valid_table,
    valid_version,
)

MIN_DELAY_S = 1.0


class FetchError(Exception):
    def __init__(self, message: str, status: int | None = None):
        super().__init__(message)
        self.status = status


def http_get(url: str, timeout: float = 120.0) -> tuple[int, str, bytes]:
    """GET sencillo. Devuelve (status, content_type, cuerpo). Lanza FetchError."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.headers.get("Content-Type", ""), resp.read()
    except urllib.error.HTTPError as e:
        body = e.read()[:300].decode("utf-8", "replace")
        raise FetchError(f"HTTP {e.code}: {body}", status=e.code) from None
    except urllib.error.URLError as e:
        raise FetchError(f"error de red: {e.reason}") from None


class Throttle:
    """Garantiza al menos `delay` segundos entre peticiones consecutivas."""

    def __init__(self, delay: float = MIN_DELAY_S, clock=time.monotonic, sleep=time.sleep):
        self.delay = max(delay, MIN_DELAY_S)
        self._clock = clock
        self._sleep = sleep
        self._last: float | None = None

    def wait(self) -> None:
        if self._last is not None:
            remaining = self.delay - (self._clock() - self._last)
            if remaining > 0:
                self._sleep(remaining)
        self._last = self._clock()


def resolve_latest_version(get: Callable = http_get, product: str = PRODUCT) -> str:
    """Ultima build procesada (no descarga en segundo plano) del producto."""
    url = f"{BASE_URL}/api/builds/{urllib.parse.quote(product)}/latest"
    _, _, body = get(url)
    data = json.loads(body)
    version = data.get("version", "")
    if data.get("product") != product or not valid_version(version):
        raise FetchError(f"respuesta inesperada de {url}: {data}")
    return version


def csv_url(table: str, version: str) -> str:
    return f"{BASE_URL}/db2/{urllib.parse.quote(table)}/csv?" + urllib.parse.urlencode(
        {"version": version}
    )


def load_manifest(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {}


def save_manifest(path: Path, manifest: dict) -> None:
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(path)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def fetch_tables(
    version: str,
    tables: list[str],
    data_dir: Path = DATA_DIR,
    product: str = PRODUCT,
    get: Callable = http_get,
    throttle: Throttle | None = None,
    log: Callable[[str], None] = print,
    force: bool = False,
) -> dict:
    """Descarga las tablas que falten y actualiza manifest.json. Devuelve el manifest."""
    if not valid_version(version):
        raise ValueError(f"version no valida (se necesita la cadena completa): {version!r}")
    throttle = throttle or Throttle()
    out_dir = data_dir / version
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = out_dir / "manifest.json"
    manifest = load_manifest(manifest_path)
    manifest.setdefault("product", product)
    manifest.setdefault("version", version)
    manifest.setdefault("source", BASE_URL)
    manifest.setdefault("tables", {})
    manifest.setdefault("missing", {})

    for table in tables:
        if not valid_table(table):
            log(f"[omitida] nombre de tabla no valido: {table!r}")
            continue
        csv_path = out_dir / f"{table}.csv"
        entry = manifest["tables"].get(table)
        if not force and entry and csv_path.exists() and sha256_file(csv_path) == entry.get("sha256"):
            log(f"[cache] {table}: {entry['rows']} filas")
            continue

        url = csv_url(table, version)
        throttle.wait()
        try:
            status, ctype, body = get(url)
            text = body.decode("utf-8")
            header, rows = parse_csv_text(text)
        except (FetchError, ValueError, UnicodeDecodeError) as e:
            status_code = getattr(e, "status", None)
            log(f"[falta] {table}: {e}")
            manifest["missing"][table] = {
                "url": url,
                "error": str(e)[:300],
                "status": status_code,
                "checked_at": _now(),
            }
            save_manifest(manifest_path, manifest)
            continue

        csv_path.write_bytes(body)
        manifest["tables"][table] = {
            "product": product,
            "version": version,
            "table": table,
            "url": url,
            "fetched_at": _now(),
            "sha256": hashlib.sha256(body).hexdigest(),
            "rows": len(rows),
            "columns": len(header),
        }
        manifest["missing"].pop(table, None)
        save_manifest(manifest_path, manifest)
        log(f"[ok] {table}: {len(rows)} filas, {len(header)} columnas")

    return manifest


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--version", help="version completa (p. ej. 1.60.1.70938); por defecto la ultima de wowf")
    p.add_argument("--tables", nargs="+", default=DEFAULT_TABLES)
    p.add_argument("--delay", type=float, default=1.5, help="segundos entre peticiones (minimo 1)")
    p.add_argument("--force", action="store_true", help="volver a descargar aunque este en cache")
    p.add_argument("--data-dir", type=Path, default=DATA_DIR)
    args = p.parse_args(argv)

    throttle = Throttle(args.delay)
    version = args.version
    if version is None:
        throttle.wait()
        version = resolve_latest_version()
        print(f"Ultima build de {PRODUCT}: {version}")
    manifest = fetch_tables(version, args.tables, data_dir=args.data_dir, throttle=throttle, force=args.force)
    print(f"Manifest: {args.data_dir / version / 'manifest.json'}")
    if manifest["missing"]:
        print("Tablas no disponibles:", ", ".join(sorted(manifest["missing"])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
