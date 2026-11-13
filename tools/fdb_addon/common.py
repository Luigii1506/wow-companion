"""Rutas, credito y utilidades compartidas del adaptador del addon ForeverDB."""

from __future__ import annotations

from pathlib import Path
from typing import Iterator, List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = REPO_ROOT / "data" / "foreverdb" / "addon_zip" / "extracted"
DB_PATH = REPO_ROOT / "data" / "foreverdb" / "addon.sqlite"

CREDIT = "Data from ForeverDB.net (https://foreverdb.net)"
CREDIT_MD = "[Data from ForeverDB.net](https://foreverdb.net)"

CAVEAT = (
    "Datos del addon ForeverDB (GPL-3.0 con clausula de atribucion). Cada fila indica su "
    "origen: 'forever' = visto por jugadores en WoW Forever, 'client' = tablas del cliente "
    "de Forever, 'classic' = CMaNGOS classic-db (Classic 1.12, solo hipotesis en Forever). "
    + CREDIT
)

# Nombres de zona (uiMap) por si los archivos no los traen; los del addon tienen prioridad.
FALLBACK_ZONES = {
    1411: "Durotar", 1412: "Mulgore", 1413: "The Barrens", 1420: "Tirisfal Glades",
    1421: "Silverpine Forest", 1440: "Ashenvale", 1441: "Thousand Needles",
    1442: "Stonetalon Mountains", 1454: "Orgrimmar", 1456: "Thunder Bluff",
    1458: "Undercity",
}

PROFESSIONS = [
    "Alchemy", "Blacksmithing", "Enchanting", "Engineering", "Leatherworking", "Tailoring",
    "Herbalism", "Mining", "Skinning", "Cooking", "First Aid", "Fishing",
]

STAT_NAMES = {
    3: "Agi", 4: "Str", 5: "Int", 6: "Spi", 7: "Sta", 12: "Defense", 13: "Dodge",
    14: "Parry", 15: "Block", 31: "Hit", 32: "Crit", 36: "Haste", 37: "Expertise",
    38: "AP", 39: "RAP", 41: "Healing", 42: "SpellDmg", 43: "MP5", 45: "SpellPower",
    47: "SpellPen", 48: "BlockValue", 50: "Armor+",
}

INV_TYPES = {
    0: "", 1: "Head", 2: "Neck", 3: "Shoulder", 4: "Shirt", 5: "Chest", 6: "Waist",
    7: "Legs", 8: "Feet", 9: "Wrist", 10: "Hands", 11: "Finger", 12: "Trinket",
    13: "One-Hand", 14: "Shield", 15: "Ranged", 16: "Back", 17: "Two-Hand", 18: "Bag",
    19: "Tabard", 20: "Chest", 21: "Main Hand", 22: "Off Hand", 23: "Held In Off-hand",
    24: "Ammo", 25: "Thrown", 26: "Ranged", 28: "Relic",
}

WEAPON_SUBCLASS = {
    0: "Axe", 1: "Two-Handed Axe", 2: "Bow", 3: "Gun", 4: "Mace", 5: "Two-Handed Mace",
    6: "Polearm", 7: "Sword", 8: "Two-Handed Sword", 10: "Staff", 13: "Fist Weapon",
    14: "Miscellaneous", 15: "Dagger", 16: "Thrown", 18: "Crossbow", 19: "Wand",
    20: "Fishing Pole",
}
ARMOR_SUBCLASS = {0: "Misc", 1: "Cloth", 2: "Leather", 3: "Mail", 4: "Plate", 6: "Shield"}


def b36(s: str) -> int:
    return int(s, 36)


def decode_gather_points(s: Optional[str]) -> List[Tuple[float, float]]:
    """Puntos de Gather.lua: 4 caracteres base-36 cada uno (x luego y, decimas de %)."""
    out: List[Tuple[float, float]] = []
    s = (s or "").strip()
    for i in range(0, len(s) - 3, 4):
        chunk = s[i:i + 4]
        out.append((b36(chunk[:2]) / 10.0, b36(chunk[2:]) / 10.0))
    return out


def decode_spot(tok: str) -> Optional[Tuple[int, float, float]]:
    """Token base-36 de las misiones: map*1e6 + x*10*1e3 + y*10 -> (uiMap, x, y)."""
    try:
        v = int(tok, 36)
    except ValueError:
        return None
    m = v // 1000000
    r = v - m * 1000000
    return m, (r // 1000) / 10.0, (r % 1000) / 10.0


def decode_spots(s: Optional[str]) -> Iterator[Tuple[int, float, float]]:
    for tok in (s or "").split():
        sp = decode_spot(tok)
        if sp:
            yield sp


def item_kind(item_class: Optional[int], subclass: Optional[int]) -> str:
    if item_class == 2:
        return WEAPON_SUBCLASS.get(subclass or 0, "Weapon")
    if item_class == 4:
        return ARMOR_SUBCLASS.get(subclass or 0, "Armor")
    return ""
