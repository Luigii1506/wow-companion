"""Descarga por lotes de la API de ForeverDB a un almacen local permanente.

Uso (desde la raiz):
    python3 -m tools.foreverdb.harvest --budget 2500            # todas las fases, en orden
    python3 -m tools.foreverdb.harvest --phase quests --budget 100
    python3 -m tools.foreverdb.harvest --status

Guarda cada respuesta en data/foreverdb/store/<fase>/<nombre>.json (fuera de git) y no la vuelve
a pedir si ya existe: se puede cortar y reanudar. Usa ForeverDBClient, asi que respeta sus
limites (25/min, 4500/dia) ademas del presupuesto de esta ejecucion.

Uso personal: los datos no se redistribuyen y toda nota que los use cita
"Data from ForeverDB.net" con enlace (condiciones de https://foreverdb.net/developers).
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from tools.foreverdb.client import ForeverDBClient, ForeverDBError

ROOT = Path(__file__).resolve().parents[2]
STORE = ROOT / "data" / "foreverdb" / "store"
PAGE = 100
HORDE_OK = {"h", "horde", "both", "b", "n", "neutral", "none", ""}


# Las respuestas llevan marcas invisibles (caracteres de ancho cero) que identifican la clave.
# El almacen guarda la respuesta tal cual; quien copie texto a notas o a git debe pasarlo por strip_markers().
_MARKERS = dict.fromkeys(map(ord, "\u200b\u200c\u200d\u2060\u2061\u2062\u2063\u2064\ufeff"))


def strip_markers(obj):
    """Quita los caracteres de ancho cero de cadenas, listas y diccionarios."""
    if isinstance(obj, str):
        return obj.translate(_MARKERS)
    if isinstance(obj, list):
        return [strip_markers(x) for x in obj]
    if isinstance(obj, dict):
        return {k: strip_markers(v) for k, v in obj.items()}
    return obj


class Budget(Exception):
    pass


class Harvester:
    def __init__(self, client: ForeverDBClient, budget: int, store: Path = STORE):
        self.c = client
        self.budget = budget
        self.store = store
        self.used = 0
        self.failed: list[str] = []
        self._sleep = time.sleep

    def _path(self, phase: str, name: str) -> Path:
        return self.store / phase / f"{name}.json"

    def fetch(self, phase: str, name: str, endpoint: str, params: dict | None = None) -> dict:
        path = self._path(phase, name)
        if path.exists():
            return json.loads(path.read_text(encoding="utf-8"))
        if self.used >= self.budget:
            raise Budget()
        resp = None
        for attempt in range(4):
            before = self.c.network_calls
            try:
                resp = self.c.get(endpoint, params)
                self.used += self.c.network_calls - before
                break
            except ForeverDBError as e:
                self.used += self.c.network_calls - before
                status = getattr(e, "status", None)
                if status is None or status < 500:
                    raise
                if attempt == 3:
                    self.failed.append(f"{phase}/{name}")
                    return {"data": [], "meta": {}}
                self._sleep(15 * (attempt + 1))
        entry = {k: resp[k] for k in ("endpoint", "params", "url", "fetched_at", "build", "data", "meta")}
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".tmp")
        tmp.write_text(json.dumps(entry, ensure_ascii=False), encoding="utf-8")
        tmp.replace(path)
        return entry

    def paged(self, phase: str, endpoint: str, extra: dict | None = None) -> list:
        rows, offset = [], 0
        while True:
            e = self.fetch(phase, f"page-{offset:06d}", endpoint, {**(extra or {}), "limit": PAGE, "offset": offset})
            data = e["data"] if isinstance(e["data"], list) else []
            rows += data
            total = (e.get("meta") or {}).get("total")
            offset += PAGE
            if not data or (total is not None and offset >= total):
                return rows

    # ------------------------------------------------------------------ fases
    def quests(self):
        self.paged("quests", "/quests")

    def vendors(self):
        rows = self.paged("vendors", "/vendors")
        for v in rows:
            side = str(v.get("side") or "").strip().lower()
            if side in HORDE_OK and v.get("id") is not None:
                self.fetch("vendor", str(v["id"]), f"/vendors/{v['id']}")

    def professions(self):
        e = self.fetch("professions", "index", "/professions")
        slugs = [p.get("slug") for p in (e["data"] if isinstance(e["data"], list) else []) if p.get("slug")]
        for s in slugs:
            first = self.fetch("profession", f"{s}-p0", f"/professions/{s}")
            meta = first.get("meta") or {}
            total, limit = meta.get("total"), meta.get("limit")
            if total and limit:
                for off in range(limit, total, limit):
                    self.fetch("profession", f"{s}-p{off}", f"/professions/{s}", {"offset": off, "limit": limit})
        for g in ("mining", "herbalism", "skinning", "fishing"):
            self.fetch("gathering", g, f"/gathering/{g}")

    def misc(self):
        for name, ep in (("disenchant", "/disenchant"), ("merchants-favor", "/merchants-favor"),
                         ("poisons", "/poisons"), ("classes", "/classes"), ("zones", "/zones"),
                         ("battlegrounds", "/battlegrounds"), ("buffs-nerfs", "/buffs-nerfs"),
                         ("changes-seen", "/changes-seen"), ("builds", "/builds")):
            self.fetch("misc", name, ep)
        d = self.paged("dungeons", "/dungeons")
        for x in d:
            if x.get("id") is not None:
                self.fetch("dungeon", str(x["id"]), f"/dungeons/{x['id']}")

    def items(self):
        self.paged("items", "/items")


PHASES = ["quests", "misc", "professions", "vendors", "items"]


def status(store: Path = STORE) -> None:
    if not store.exists():
        print("Almacen vacio.")
        return
    for d in sorted(p for p in store.iterdir() if p.is_dir()):
        print(f"{d.name:12} {len(list(d.glob('*.json'))):6} archivos")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--phase", choices=PHASES)
    ap.add_argument("--budget", type=int, default=500, help="peticiones de red maximas en esta ejecucion")
    ap.add_argument("--status", action="store_true")
    a = ap.parse_args(argv)
    if a.status:
        status()
        return 0
    client = ForeverDBClient()
    h = Harvester(client, a.budget)
    try:
        for ph in ([a.phase] if a.phase else PHASES):
            print(f"fase {ph}...", flush=True)
            getattr(h, ph)()
            print(f"  ok (peticiones usadas: {h.used})", flush=True)
    except Budget:
        print(f"Presupuesto agotado ({h.used}). Vuelve a ejecutar para seguir donde se quedo.")
    except ForeverDBError as e:
        print(f"Error de ForeverDB: {e}", file=sys.stderr)
        return 1
    if h.failed:
        print(f"Fallaron tras reintentos (se pediran en la proxima ejecucion): {len(h.failed)}: {', '.join(h.failed[:10])}")
    print(f"Peticiones de red: {h.used} · quedan hoy: {client.counter.remaining()}")
    print("Data from ForeverDB.net (https://foreverdb.net)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
