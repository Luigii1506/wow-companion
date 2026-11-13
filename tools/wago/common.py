"""Constantes y utilidades compartidas del adaptador de wago.tools."""

from __future__ import annotations

import csv
import io
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "data" / "wago"
DB_PATH = DATA_DIR / "forever.sqlite"

BASE_URL = "https://wago.tools"
PRODUCT = "wowf"
USER_AGENT = (
    "wow-companion-wago-adapter/0.1 "
    "(personal research tool; follows https://wago.tools/llms.txt)"
)

CAVEAT = (
    "Datos del cliente de WoW Forever extraidos de wago.tools (tablas DB2). "
    "Blizzard oculta en el cliente una parte de los objetos de Forever (~40% segun "
    "informes de la comunidad) hasta que se descubren, asi que estas tablas estan "
    "incompletas. No incluyen datos del servidor: misiones, botin, tasas de caida, "
    "vendedores ni precios."
)

DEFAULT_TABLES = [
    "ItemSparse",
    "Item",
    "ItemClass",
    "ItemSubClass",
    "Spell",
    "SpellName",
    "SpellMisc",
    "SkillLine",
    "SkillLineAbility",
    "ItemSet",
    "Faction",
    "AreaTable",
    "ChrClasses",
    "ChrRaces",
    "TalentTab",
    "Talent",
]

_VERSION_RE = re.compile(r"^\d+(\.\d+){3}$")
_TABLE_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_]*$")


def valid_version(version: str) -> bool:
    """Una version valida es la cadena completa con cuatro componentes."""
    return bool(_VERSION_RE.match(version or ""))


def valid_table(name: str) -> bool:
    return bool(_TABLE_RE.match(name or ""))


def parse_csv_text(text: str) -> tuple[list[str], list[list[str]]]:
    """Devuelve (cabecera, filas). Lanza ValueError si no parece un CSV de DB2."""
    if text.startswith("﻿"):
        text = text[1:]
    stripped = text.lstrip()
    if not stripped:
        raise ValueError("respuesta vacia")
    if stripped[:1] == "<" or stripped[:1] == "{":
        raise ValueError("la respuesta no es CSV (HTML o JSON)")
    reader = csv.reader(io.StringIO(text, newline=""))
    rows = list(reader)
    header = rows[0]
    if not header or any(not c.strip() or "<" in c for c in header):
        raise ValueError(f"cabecera inesperada: {header[:5]}")
    body = [r for r in rows[1:] if r]
    return header, body
