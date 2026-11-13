"""Carga los CSV en cache de una version en SQLite (data/wago/forever.sqlite).

La base contiene una sola version a la vez: reconstruir sustituye por completo las
tablas DB2 y la tabla `meta`. Cada tabla DB2 conserva sus columnas originales; el
tipo (INTEGER, REAL o TEXT) se infiere de los valores de cada columna.

Uso:
    python3 -m tools.wago.build_db                  # version mas reciente en cache
    python3 -m tools.wago.build_db --version 1.60.1.70938
"""

from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

from .common import CAVEAT, DATA_DIR, DB_PATH, parse_csv_text, valid_table, valid_version

# Indices para las uniones que usa query.py: (tabla, columna)
INDEXES = [
    ("ItemSparse", "ID"),
    ("Item", "ID"),
    ("SpellName", "ID"),
    ("Spell", "ID"),
    ("SpellMisc", "SpellID"),
    ("SkillLineAbility", "Spell"),
    ("SkillLine", "ID"),
    ("ItemSubClass", "ClassID"),
]


def q(identifier: str) -> str:
    return '"' + identifier.replace('"', '""') + '"'


_LEADING_ZERO = re.compile(r"^-?0\d")  # "007" debe seguir siendo texto


def _is_int(v: str) -> bool:
    try:
        int(v)
    except ValueError:
        return False
    return not _LEADING_ZERO.match(v)


def _is_float(v: str) -> bool:
    try:
        float(v)
    except ValueError:
        return False
    return not _LEADING_ZERO.match(v) and v.lower() not in ("nan", "inf", "-inf", "infinity", "-infinity")


def infer_types(header: list[str], rows: list[list[str]]) -> list[str]:
    types = []
    for i, _ in enumerate(header):
        values = [r[i] for r in rows if i < len(r) and r[i] != ""]
        if values and all(_is_int(v) for v in values):
            types.append("INTEGER")
        elif values and all(_is_float(v) for v in values):
            types.append("REAL")
        else:
            types.append("TEXT")
    return types


def _convert(value: str, typ: str):
    if value == "":
        return None if typ != "TEXT" else ""
    if typ == "INTEGER":
        return int(value)
    if typ == "REAL":
        return float(value)
    return value


def latest_cached_version(data_dir: Path = DATA_DIR) -> str | None:
    versions = [
        p.name for p in data_dir.glob("*") if p.is_dir() and valid_version(p.name) and (p / "manifest.json").exists()
    ]
    if not versions:
        return None
    return max(versions, key=lambda v: tuple(int(x) for x in v.split(".")))


def build(version: str, data_dir: Path = DATA_DIR, db_path: Path = DB_PATH, log=print) -> dict[str, int]:
    """Construye la base para `version`. Devuelve {tabla: filas cargadas}."""
    src = data_dir / version
    manifest = json.loads((src / "manifest.json").read_text(encoding="utf-8"))
    product = manifest.get("product", "")
    loaded: dict[str, int] = {}
    built_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    db_path.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(db_path)
    try:
        with con:  # una sola transaccion: o se sustituye todo o nada
            # Borrar todo lo anterior (tablas DB2 de cualquier version y meta)
            existing = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")]
            for name in existing:
                con.execute(f"DROP TABLE IF EXISTS {q(name)}")
            con.execute(
                "CREATE TABLE meta (product TEXT, version TEXT, table_name TEXT PRIMARY KEY, "
                "url TEXT, fetched_at TEXT, sha256 TEXT, rows INTEGER, built_at TEXT, caveat TEXT)"
            )
            for table, entry in sorted(manifest.get("tables", {}).items()):
                csv_path = src / f"{table}.csv"
                if not valid_table(table) or not csv_path.exists():
                    log(f"[omitida] {table}: CSV no encontrado")
                    continue
                header, rows = parse_csv_text(csv_path.read_text(encoding="utf-8"))
                types = infer_types(header, rows)
                cols = ", ".join(f"{q(c)} {t}" for c, t in zip(header, types))
                con.execute(f"CREATE TABLE {q(table)} ({cols})")
                placeholders = ", ".join("?" for _ in header)
                width = len(header)
                con.executemany(
                    f"INSERT INTO {q(table)} VALUES ({placeholders})",
                    (
                        [_convert(v, t) for v, t in zip((r + [""] * width)[:width], types)]
                        for r in rows
                    ),
                )
                con.execute(
                    "INSERT INTO meta VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (product, version, table, entry.get("url"), entry.get("fetched_at"),
                     entry.get("sha256"), len(rows), built_at, CAVEAT),
                )
                loaded[table] = len(rows)
                log(f"[db] {table}: {len(rows)} filas")
            for table, col in INDEXES:
                if table in loaded:
                    con.execute(f"CREATE INDEX {q('idx_' + table + '_' + col)} ON {q(table)} ({q(col)})")
    finally:
        con.close()
    return loaded


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--version")
    p.add_argument("--data-dir", type=Path, default=DATA_DIR)
    p.add_argument("--db", type=Path, default=DB_PATH)
    args = p.parse_args(argv)
    version = args.version or latest_cached_version(args.data_dir)
    if not version:
        print("No hay versiones en cache. Ejecuta antes: python3 -m tools.wago.fetch", file=sys.stderr)
        return 1
    loaded = build(version, args.data_dir, args.db)
    print(f"Base {args.db} construida para wowf {version}: {len(loaded)} tablas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
