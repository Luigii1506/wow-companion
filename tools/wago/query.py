"""Consulta la base SQLite de tablas del cliente de WoW Forever.

Uso:
    python3 -m tools.wago.query item "Jagged Dagger"
    python3 -m tools.wago.query item --id 4947
    python3 -m tools.wago.query spell "Shank"
    python3 -m tools.wago.query spell --id 1329283

Solo se decodifica lo verificable en las propias tablas (nombres, clase y subclase
via ItemClass/ItemSubClass, lineas de habilidad via SkillLineAbility/SkillLine) y los
nombres de estadistica (Enum.BonusStatIndex del propio cliente, ver BONUS_STAT_NAMES).
El resto se imprime en bruto.
"""

from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path

from .common import DB_PATH

# Etiquetas de enums publicos de la API de Blizzard (Enum.ItemQuality,
# Enum.InventoryType). Conocimiento externo: NO estan en las tablas descargadas.
# Se muestran siempre junto al valor bruto y marcadas con "*".
QUALITY_LABELS = {
    0: "Poor", 1: "Common", 2: "Uncommon", 3: "Rare", 4: "Epic",
    5: "Legendary", 6: "Artifact", 7: "Heirloom",
}
INVTYPE_LABELS = {
    0: "Non-equip", 1: "Head", 2: "Neck", 3: "Shoulder", 4: "Shirt", 5: "Chest",
    6: "Waist", 7: "Legs", 8: "Feet", 9: "Wrist", 10: "Hands", 11: "Finger",
    12: "Trinket", 13: "One-Hand", 14: "Shield", 15: "Ranged (bow)", 16: "Back",
    17: "Two-Hand", 18: "Bag", 19: "Tabard", 20: "Chest (robe)", 21: "Main Hand",
    22: "Off Hand", 23: "Held in Off-hand", 24: "Ammo", 25: "Thrown",
    26: "Ranged (gun/crossbow/wand)", 27: "Quiver", 28: "Relic",
}
EXTERNAL_NOTE = "* etiqueta de enum publico de la API de Blizzard (conocimiento externo, no verificado en estas tablas)"

# Enum.BonusStatIndex (valores de StatModifier_bonusStat_N). Fuente verificada: archivo
# de Blizzard Interface/AddOns/Blizzard_APIDocumentationGenerated/ItemConstantsDocumentation.lua
# (FileDataID 4637111) del propio cliente wowf 1.60.1.70938, descargado el 2026-11-13 con
# GET https://wago.tools/api/casc/4637111?version=1.60.1.70938
# (sha256 ae3b654c4d551234e97562552e6aeb9736672f2458945efe19645b387f4b092e).
# 142 valores (0-141). Solo da el NOMBRE de la estadistica; la cantidad final no se calcula.
# Enum.ItemBind (campo Bonding), mismo archivo y misma build que BONUS_STAT_NAMES.
BIND_NAMES = {
    0: "None", 1: "OnAcquire", 2: "OnEquip", 3: "OnUse", 4: "Quest", 5: "Unused1", 6: "Unused2",
    7: "ToWoWAccount", 8: "ToBnetAccount", 9: "ToBnetAccountUntilEquipped",
}
STAT_SOURCE = ("Enum.BonusStatIndex de Blizzard_APIDocumentationGenerated/ItemConstantsDocumentation.lua "
               "(FileDataID 4637111, cliente wowf 1.60.1.70938)")
BONUS_STAT_NAMES = {
    0: "Mana", 1: "Health", 2: "Endurance", 3: "Agility", 4: "Strength", 5: "Intellect",
    6: "Spirit", 7: "Stamina", 8: "Energy", 9: "Rage", 10: "Focus", 11: "WeaponSkillRating",
    12: "DefenseSkillRating", 13: "DodgeRating", 14: "ParryRating", 15: "BlockRating",
    16: "HitMeleeRating", 17: "HitRangedRating", 18: "HitSpellRating", 19: "CritMeleeRating",
    20: "CritRangedRating", 21: "CritSpellRating", 22: "Corruption", 23: "CorruptionResistance",
    24: "ModifiedCraftingStat_1", 25: "ModifiedCraftingStat_2",
    26: "CritTakenRangedRatingObsolete", 27: "CritTakenSpellRatingObsolete",
    28: "HasteMeleeRatingObsolete", 29: "HasteRangedRatingObsolete",
    30: "HasteSpellRatingObsolete", 31: "HitRating", 32: "CritRating",
    33: "HitTakenRatingObsolete", 34: "CritTakenRatingObsolete", 35: "ResilienceRating",
    36: "HasteRating", 37: "ExpertiseRating", 38: "AttackPower", 39: "RangedAttackPower",
    40: "Versatility", 41: "SpellHealingDone", 42: "SpellDamageDone", 43: "ManaRegeneration",
    44: "ArmorPenetrationRating", 45: "SpellPower", 46: "HealthRegen", 47: "SpellPenetration",
    48: "BlockValue", 49: "MasteryRating", 50: "ExtraArmor", 51: "FireResistance",
    52: "FrostResistance", 53: "HolyResistance", 54: "ShadowResistance", 55: "NatureResistance",
    56: "ArcaneResistance", 57: "PvPPower", 58: "CombatRatingUnused_0", 59: "CombatRatingUnused_2",
    60: "CombatRatingUnused_3", 61: "CombatRatingSpeed", 62: "CombatRatingLifesteal",
    63: "CombatRatingAvoidance", 64: "CombatRatingSturdiness", 65: "CombatRatingUnused_7",
    66: "CombatRatingUnused_27", 67: "CombatRatingUnused_9", 68: "CombatRatingUnused_10",
    69: "CombatRatingUnused_11", 70: "CombatRatingUnused_12", 71: "AgilityOrStrengthOrIntellect",
    72: "AgilityOrStrength", 73: "AgilityOrIntellect", 74: "StrengthOrIntellect",
    75: "ProfessionInspiration", 76: "ProfessionResourcefulness", 77: "ProfessionFinesse",
    78: "ProfessionDeftness", 79: "ProfessionPerception", 80: "ProfessionCraftingSpeed",
    81: "ProfessionMulticraft", 82: "ProfessionIngenuity", 83: "PhysicalDamageDone",
    84: "HolyDamageDone", 85: "FireDamageDone", 86: "NatureDamageDone", 87: "FrostDamageDone",
    88: "ShadowDamageDone", 89: "ArcaneDamageDone", 90: "TwohandedAxesSkill",
    91: "TwohandedMacesSkill", 92: "TwohandedSwordsSkill", 93: "AxesSkill", 94: "BowsSkill",
    95: "CrossbowsSkill", 96: "DaggersSkill", 97: "DualWieldSkill", 98: "FistWeaponsSkill",
    99: "GunsSkill", 100: "MacesSkill", 101: "PolearmsSkill", 102: "StavesSkill",
    103: "SwordsSkill", 104: "ThrownSkill", 105: "WandsSkill", 106: "AlchemySkill",
    107: "BlacksmithingSkill", 108: "EnchantingSkill", 109: "EngineeringSkill",
    110: "JewelcraftingSkill", 111: "LeatherworkingSkill", 112: "HerbalismSkill",
    113: "MiningSkill", 114: "SkinningSkill", 115: "CookingSkill", 116: "FirstAidSkill",
    117: "FishingSkill", 118: "TailoringSkill", 119: "FirePenetration", 120: "NaturePenetration",
    121: "FrostPenetration", 122: "ShadowPenetration", 123: "ArcanePenetration",
    124: "SpellResistanceAllSchools", 125: "AttackPowerVsHumanoid", 126: "AttackPowerVsElemental",
    127: "AttackPowerVsDemon", 128: "AttackPowerVsUndead", 129: "AttackPowerVsDragonkin",
    130: "AttackPowerVsGiant", 131: "AttackPowerVsBeast", 132: "AttackPowerVsMechanical",
    133: "SpellDamageVsHumanoid", 134: "SpellDamageVsElemental", 135: "SpellDamageVsDemon",
    136: "SpellDamageVsUndead", 137: "SpellDamageVsDragonkin", 138: "SpellDamageVsGiant",
    139: "SpellDamageVsBeast", 140: "SpellDamageVsMechanical", 141: "Reserved_141",
}


class QueryError(Exception):
    pass


def connect(db_path: Path = DB_PATH) -> sqlite3.Connection:
    if not db_path.exists():
        raise QueryError(f"No existe {db_path}. Ejecuta fetch y build_db antes.")
    con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    return con


def has_table(con: sqlite3.Connection, name: str) -> bool:
    return con.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?", (name,)).fetchone() is not None


def build_info(con: sqlite3.Connection, tables: list[str]) -> dict:
    """Producto, version, fechas de extraccion de las tablas usadas y advertencia."""
    rows = con.execute(
        f"SELECT * FROM meta WHERE table_name IN ({','.join('?' for _ in tables)})", tables
    ).fetchall()
    any_row = rows[0] if rows else con.execute("SELECT * FROM meta LIMIT 1").fetchone()
    if any_row is None:
        raise QueryError("La tabla meta esta vacia: reconstruye la base.")
    return {
        "product": any_row["product"],
        "version": any_row["version"],
        "fetched_at": {r["table_name"]: r["fetched_at"] for r in rows},
        "caveat": any_row["caveat"],
    }


def stat_name(stat_id) -> str:
    """Nombre de un bonusStat segun Enum.BonusStatIndex del cliente; '?' si no esta."""
    return BONUS_STAT_NAMES.get(stat_id, f"desconocido ({stat_id})")


def _label(value, labels: dict) -> str:
    if value in labels:
        return f"{value} ({labels[value]}*)"
    return f"{value} (sin etiqueta)"


# ---------------------------------------------------------------- objetos

def find_items(con, name: str | None = None, item_id: int | None = None, limit: int = 10) -> list[int]:
    if item_id is not None:
        found = con.execute("SELECT ID FROM ItemSparse WHERE ID=?", (item_id,)).fetchall()
        if not found and has_table(con, "Item"):
            found = con.execute("SELECT ID FROM Item WHERE ID=?", (item_id,)).fetchall()
        return [r["ID"] for r in found]
    exact = con.execute(
        "SELECT ID FROM ItemSparse WHERE Display_lang = ? COLLATE NOCASE ORDER BY ID", (name,)
    ).fetchall()
    if exact:
        return [r["ID"] for r in exact]
    like = con.execute(
        "SELECT ID FROM ItemSparse WHERE Display_lang LIKE ? ORDER BY ID LIMIT ?", (f"%{name}%", limit)
    ).fetchall()
    return [r["ID"] for r in like]


def item_details(con, item_id: int) -> dict:
    sparse = con.execute("SELECT * FROM ItemSparse WHERE ID=?", (item_id,)).fetchone()
    item = con.execute("SELECT * FROM Item WHERE ID=?", (item_id,)).fetchone() if has_table(con, "Item") else None
    d: dict = {"id": item_id, "in_sparse": sparse is not None, "in_item": item is not None}
    if sparse is not None:
        d.update(
            name=sparse["Display_lang"],
            description=sparse["Description_lang"],
            quality=sparse["OverallQualityID"],
            item_level=sparse["ItemLevel"],
            required_level=sparse["RequiredLevel"],
            inventory_type=sparse["InventoryType"],
            bonding=sparse["Bonding"],
            item_delay=sparse["ItemDelay"],
            sell_price=sparse["SellPrice"],
            buy_price=sparse["BuyPrice"],
            allowable_class=sparse["AllowableClass"],
            required_skill=sparse["RequiredSkill"],
            required_skill_rank=sparse["RequiredSkillRank"],
            stats=[
                (sparse[f"StatModifier_bonusStat_{i}"], sparse[f"StatPercentEditor_{i}"])
                for i in range(10)
                if sparse[f"StatModifier_bonusStat_{i}"] not in (-1, None)
            ],
        )
    if item is not None:
        d["class_id"], d["subclass_id"] = item["ClassID"], item["SubclassID"]
        d.setdefault("inventory_type", item["InventoryType"])
        if has_table(con, "ItemClass"):
            r = con.execute("SELECT ClassName_lang FROM ItemClass WHERE ClassID=?", (item["ClassID"],)).fetchone()
            d["class_name"] = r[0] if r else None
        if has_table(con, "ItemSubClass"):
            r = con.execute(
                "SELECT DisplayName_lang, VerboseName_lang FROM ItemSubClass WHERE ClassID=? AND SubClassID=?",
                (item["ClassID"], item["SubclassID"]),
            ).fetchone()
            d["subclass_name"] = (r["VerboseName_lang"] or r["DisplayName_lang"]) if r else None
    return d


def format_item(d: dict) -> str:
    out = []
    if d["in_sparse"]:
        out.append(f"{d['name']} (ID {d['id']})")
    else:
        out.append(f"Objeto ID {d['id']}: sin fila en ItemSparse, el cliente no tiene su nombre ni sus datos "
                   "(posible objeto oculto hasta descubrirse o retirado; no se puede saber desde aqui)")
    if d.get("class_id") is not None:
        out.append(f"  Clase/subclase:  {d.get('class_name')} / {d.get('subclass_name')} "
                   f"(ClassID {d['class_id']}, SubclassID {d['subclass_id']})")
    if d["in_sparse"]:
        out.append(f"  Calidad:         {_label(d['quality'], QUALITY_LABELS)}")
        out.append(f"  Nivel de objeto: {d['item_level']}")
        req = d["required_level"]
        out.append(f"  Nivel requerido: {req}" + ("  (0 en ItemSparse: sin requisito en el cliente o definido en otra tabla)" if req == 0 else ""))
    if d.get("inventory_type") is not None:
        out.append(f"  Ranura:          {_label(d['inventory_type'], INVTYPE_LABELS)}")
    if d["in_sparse"]:
        if d["description"]:
            out.append(f"  Descripcion:     {d['description']}")
        if d["stats"]:
            raw = ", ".join(f"{stat_name(s)} (bonusStat={s} pct={p})" for s, p in d["stats"])
            out.append(f"  Estadisticas:    {raw}")
            out.append(f"    Nombres: {STAT_SOURCE}. Cantidades sin calcular: pct es el reparto del presupuesto "
                       "(StatPercentEditor) y el valor final depende de tablas por nivel de objeto que no se descargan.")
        else:
            out.append("  Estadisticas:    ninguna en StatModifier_bonusStat_*")
        out.append("  Campos en bruto: "
                   f"Bonding={d['bonding']} ({BIND_NAMES.get(d['bonding'], 'sin etiqueta')}, Enum.ItemBind) ItemDelay={d['item_delay']} SellPrice={d['sell_price']} "
                   f"BuyPrice={d['buy_price']} AllowableClass={d['allowable_class']} "
                   f"RequiredSkill={d['required_skill']} RequiredSkillRank={d['required_skill_rank']}")
        out.append("    (SellPrice/BuyPrice son valores del cliente para vendedor, no precios de subasta)")
    return "\n".join(out)


# ---------------------------------------------------------------- hechizos

def find_spells(con, name: str | None = None, spell_id: int | None = None, limit: int = 10) -> list[int]:
    if spell_id is not None:
        rows = con.execute("SELECT ID FROM SpellName WHERE ID=?", (spell_id,)).fetchall()
        return [r["ID"] for r in rows]
    rows = con.execute(
        "SELECT ID FROM SpellName WHERE Name_lang = ? COLLATE NOCASE ORDER BY ID LIMIT ?", (name, limit)
    ).fetchall()
    if not rows:
        rows = con.execute(
            "SELECT ID FROM SpellName WHERE Name_lang LIKE ? ORDER BY ID LIMIT ?", (f"%{name}%", limit)
        ).fetchall()
    return [r["ID"] for r in rows]


def spell_details(con, spell_id: int) -> dict:
    d: dict = {"id": spell_id}
    r = con.execute("SELECT Name_lang FROM SpellName WHERE ID=?", (spell_id,)).fetchone()
    d["name"] = r[0] if r else None
    if has_table(con, "Spell"):
        r = con.execute("SELECT NameSubtext_lang, Description_lang FROM Spell WHERE ID=?", (spell_id,)).fetchone()
        if r:
            d["subtext"], d["description"] = r["NameSubtext_lang"], r["Description_lang"]
    if has_table(con, "SpellMisc"):
        r = con.execute("SELECT SchoolMask, CastingTimeIndex, RangeIndex FROM SpellMisc WHERE SpellID=?",
                        (spell_id,)).fetchone()
        if r:
            d["misc"] = dict(r)
    d["skill_lines"] = []
    if has_table(con, "SkillLineAbility") and has_table(con, "SkillLine"):
        rows = con.execute(
            "SELECT sl.ID, sl.DisplayName_lang, sla.ClassMask, sla.MinSkillLineRank, sla.SupercedesSpell "
            "FROM SkillLineAbility sla LEFT JOIN SkillLine sl ON sl.ID = sla.SkillLine "
            "WHERE sla.Spell=? ORDER BY sl.ID", (spell_id,)
        ).fetchall()
        d["skill_lines"] = [dict(x) for x in rows]
    return d


def format_spell(d: dict) -> str:
    title = f"{d['name']} (ID {d['id']})"
    if d.get("subtext"):
        title += f" [{d['subtext']}]"
    out = [title]
    if d.get("description"):
        out.append(f"  Descripcion (plantilla sin resolver): {d['description']}")
    for sl in d["skill_lines"]:
        out.append(f"  Linea de habilidad: {sl['DisplayName_lang']} (SkillLine {sl['ID']}); bruto: "
                   f"ClassMask={sl['ClassMask']} MinSkillLineRank={sl['MinSkillLineRank']} "
                   f"SupercedesSpell={sl['SupercedesSpell']}")
    if not d["skill_lines"]:
        out.append("  Linea de habilidad: ninguna en SkillLineAbility")
    if d.get("misc"):
        m = d["misc"]
        out.append(f"  SpellMisc (bruto): SchoolMask={m['SchoolMask']} CastingTimeIndex={m['CastingTimeIndex']} "
                   f"RangeIndex={m['RangeIndex']}")
    return "\n".join(out)


# ---------------------------------------------------------------- CLI

def _footer(info: dict, external: bool) -> str:
    fetched = ", ".join(f"{t} {f}" for t, f in sorted(info["fetched_at"].items()))
    lines = [
        "---",
        f"Fuente: wago.tools, producto {info['product']}, build {info['version']}. Extraido (UTC): {fetched}.",
        f"Confianza: alta para lo que el cliente contiene; no es estado del personaje ni del servidor.",
        f"Advertencia: {info['caveat']}",
    ]
    if external:
        lines.append(EXTERNAL_NOTE)
    return "\n".join(lines)


def run(argv: list[str] | None = None, db_path: Path = DB_PATH) -> str:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="kind", required=True)
    for kind in ("item", "spell"):
        sp = sub.add_parser(kind)
        sp.add_argument("name", nargs="?")
        sp.add_argument("--id", type=int)
        sp.add_argument("--limit", type=int, default=10)
    args = p.parse_args(argv)
    if args.name is None and args.id is None:
        p.error("indica un nombre o --id")

    con = connect(db_path)
    try:
        if args.kind == "item":
            ids = find_items(con, args.name, args.id, args.limit)
            blocks = [format_item(item_details(con, i)) for i in ids]
            info = build_info(con, ["ItemSparse", "Item", "ItemClass", "ItemSubClass"])
        else:
            ids = find_spells(con, args.name, args.id, args.limit)
            blocks = [format_spell(spell_details(con, i)) for i in ids]
            info = build_info(con, ["SpellName", "Spell", "SpellMisc", "SkillLineAbility", "SkillLine"])
    finally:
        con.close()

    target = f"--id {args.id}" if args.id is not None else repr(args.name)
    if not blocks:
        body = (f"Sin resultados para {target} en las tablas del cliente. Que no aparezca no significa que no "
                "exista en Forever: puede estar oculto en el cliente.")
    else:
        body = f"{len(blocks)} resultado(s) para {target}:\n\n" + "\n\n".join(blocks)
    return body + "\n" + _footer(info, external=(args.kind == "item" and bool(blocks)))


def main(argv: list[str] | None = None) -> int:
    try:
        print(run(argv))
    except QueryError as e:
        print(str(e), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
