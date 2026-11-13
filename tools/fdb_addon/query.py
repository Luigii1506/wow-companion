"""Consultas sobre data/foreverdb/addon.sqlite (datos del addon ForeverDB).

Uso:
    python3 -m tools.fdb_addon.query quest "Cutting Teeth"
    python3 -m tools.fdb_addon.query nodes "Copper Vein" --zone Durotar [--source forever] [--points]
    python3 -m tools.fdb_addon.query recipe engineering [--max-skill 150]
    python3 -m tools.fdb_addon.query npc "Gornek"
    python3 -m tools.fdb_addon.query zone-quests "The Barrens" [--side h] [--min-level 10 --max-level 20]
    python3 -m tools.fdb_addon.query item "Rough Boomstick"
    python3 -m tools.fdb_addon.query rares "Durotar"
    python3 -m tools.fdb_addon.query meta

Origen de cada dato: forever = visto por jugadores en Forever; client = cliente de Forever;
classic = CMaNGOS classic-db (hipotesis); curve_estimate = XP estimada por nivel, sin captura.
Data from ForeverDB.net (https://foreverdb.net)
"""

from __future__ import annotations

import argparse
import sqlite3
import sys
from pathlib import Path
from typing import List, Optional, Sequence

from .common import CREDIT, DB_PATH


def connect(path: Path) -> sqlite3.Connection:
    if not Path(path).exists():
        raise SystemExit("No existe %s. Ejecuta: python3 -m tools.fdb_addon.build" % path)
    con = sqlite3.connect(str(path))
    con.row_factory = sqlite3.Row
    return con


def money(c: Optional[int]) -> str:
    if c is None:
        return "?"
    neg = c < 0
    c = abs(c)
    g, s, cu = c // 10000, (c // 100) % 100, c % 100
    parts = []
    if g:
        parts.append("%dg" % g)
    if s:
        parts.append("%ds" % s)
    if cu or not parts:
        parts.append("%dc" % cu)
    return ("-" if neg else "") + " ".join(parts)


def table(rows: Sequence[Sequence], headers: Sequence[str]) -> str:
    rows = [["" if v is None else str(v) for v in r] for r in rows]
    widths = [len(h) for h in headers]
    for r in rows:
        for i, v in enumerate(r):
            widths[i] = min(max(widths[i], len(v)), 60)
    fmt = "  ".join("%%-%ds" % w for w in widths)
    out = [fmt % tuple(headers), fmt % tuple("-" * w for w in widths)]
    for r in rows:
        out.append(fmt % tuple(v[:60] for v in r))
    return "\n".join(out)


def cmd_quest(con, a) -> str:
    rows = con.execute(
        "SELECT * FROM quests WHERE title LIKE ? OR CAST(id AS TEXT) = ? ORDER BY level, id LIMIT ?",
        ("%" + a.name + "%", a.name, a.limit)).fetchall()
    if not rows:
        return "Sin resultados."
    out = []
    for q in rows:
        status = "confirmada en Forever" if q["confirmed_forever"] else "sin confirmar en Forever"
        lines = [
            "[%d] %s  (nivel %s, min %s, lado %s, zona %s)" % (q["id"], q["title"], q["level"],
                                                           q["min_level"], q["side"] or "?", q["zone"] or "?"),
            "  estado: %s; origen: %s; jugadores que la vieron: %s; nueva en Forever: %s; en Classic: %s%s" % (
                status, q["source"], q["players_seen"], "si" if q["new_in_forever"] else "no",
                "si" if q["in_classic"] else "no", " (Classic: probablemente retirada)" if q["classic_gone"] else ""),
            "  da: %s %s %s  @ %s %s,%s [%s]" % (q["giver_type"] or "", q["giver_id"] or "", q["giver_name"] or "",
                                               q["giver_map"] or "", q["giver_x"] or "", q["giver_y"] or "",
                                               q["giver_spot_src"] or "-"),
            "  entrega: %s %s" % (q["ender_id"] or "", q["ender_name"] or ""),
            "  XP: %s [%s]  visto: %s   dinero: %s [%s]" % (q["xp"], q["xp_src"], q["xp_seen"] or "-",
                                                          money(q["money"]) if q["money"] is not None else "?",
                                                          q["money_src"] or "-"),
            "  recompensa: %s" % (q["reward_items"] or "-"),
            "  a elegir:   %s  [%s]" % (q["choice_items"] or "-", q["reward_src"] or "-"),
        ]
        if q["reputation"]:
            lines.append("  reputacion: %s" % q["reputation"])
        if q["prev_quests"] or q["next_quests"]:
            lines.append("  antes: %s  despues: %s" % (q["prev_quests"] or "-", q["next_quests"] or "-"))
        if q["not_offered_to"]:
            lines.append("  no se ofrece a: %s" % q["not_offered_to"])
        if q["objective"]:
            lines.append("  objetivo: %s" % q["objective"])
        cls = con.execute("SELECT class, kind, item_name, item_id FROM quest_rewards "
                          "WHERE quest_id=? AND class != '' ORDER BY class", (q["id"],)).fetchall()
        if cls:
            lines.append("  por clase (visto en Forever): " + "; ".join(
                "%s %s %s(%d)" % (c["class"], c["kind"], c["item_name"], c["item_id"]) for c in cls))
        out.append("\n".join(lines))
    return "\n\n".join(out)


def cmd_nodes(con, a) -> str:
    args: List = ["%" + a.kind + "%"]
    where = "k.name LIKE ?"
    if a.zone:
        where += " AND z.zone LIKE ?"
        args.append("%" + a.zone + "%")
    rows = con.execute(
        "SELECT k.name, k.profession, k.skill, z.zone, z.ui_map, z.classic_points, z.forever_points, z.w, z.kind_id "
        "FROM gather_zones z JOIN gather_kinds k USING(kind_id) WHERE %s "
        "ORDER BY z.forever_points DESC, z.classic_points DESC" % where, args).fetchall()
    if not rows:
        return "Sin resultados."
    out = [table([(r["name"], r["profession"], r["skill"], r["zone"], r["classic_points"],
                   r["forever_points"], r["w"]) for r in rows],
                 ["nodo", "prof", "skill", "zona", "puntos_classic", "puntos_forever", "w"])]
    if a.points:
        for r in rows:
            q = "SELECT source, x, y FROM gather_nodes WHERE kind_id=? AND ui_map=?"
            p = [r["kind_id"], r["ui_map"]]
            if a.source:
                q += " AND source=?"
                p.append(a.source)
            pts = con.execute(q + " ORDER BY source DESC, x, y", p).fetchall()
            out.append("\n%s en %s:" % (r["name"], r["zone"]))
            out.append(" ".join("%s(%.1f,%.1f)" % ("F" if t["source"] == "forever" else "c", t["x"], t["y"])
                                for t in pts))
        out.append("\nF = visto en Forever, c = punto de Classic (CMaNGOS).")
    return "\n".join(out)


def cmd_recipe(con, a) -> str:
    args: List = [a.profession]
    where = "LOWER(profession) = LOWER(?)"
    if a.max_skill is not None:
        where += " AND skill_req <= ?"
        args.append(a.max_skill)
    if a.min_skill is not None:
        where += " AND skill_req >= ?"
        args.append(a.min_skill)
    if a.name:
        where += " AND name LIKE ?"
        args.append("%" + a.name + "%")
    rows = con.execute("SELECT * FROM recipes WHERE %s ORDER BY skill_req, yellow" % where, args).fetchall()
    if not rows:
        return "Sin resultados."
    return table([(r["skill_req"], "%s/%s/%s" % (r["yellow"], r["green"], r["grey"]), r["name"],
                   ("%g" % r["makes"]) if r["makes"] not in (None, 1) else "", r["reagents"], r["learned_from"],
                   money(r["trainer_cost"]) if r["trainer_cost"] else "",
                   "nueva" if r["new_in_forever"] else ("cambiada:" + r["forever_changed"] if r["forever_changed"] else ""),
                   "classic" if r["skill_req_classic_trainer"] else "")
                  for r in rows],
                 ["skill", "amar/verde/gris", "receta", "n", "reactivos", "origen", "coste", "forever", "skill_src"])


def cmd_npc(con, a) -> str:
    rows = con.execute("SELECT * FROM npcs WHERE name LIKE ? OR CAST(id AS TEXT)=? ORDER BY seen_forever DESC, name LIMIT ?",
                       ("%" + a.name + "%", a.name, a.limit)).fetchall()
    if not rows:
        return "Sin resultados."
    out = [table([(r["id"], r["name"], r["title"], r["zone"], r["x"], r["y"], r["side"],
                   "forever" if r["seen_forever"] else "classic", r["src"]) for r in rows],
                 ["id", "nombre", "titulo", "zona", "x", "y", "lado", "lugar", "archivo"])]
    for r in rows[:5]:
        tr = con.execute("SELECT kind, what FROM trainers WHERE npc_id=?", (r["id"],)).fetchall()
        if tr:
            out.append("%s entrena: %s" % (r["name"], ", ".join("%s %s" % (t["kind"], t["what"]) for t in tr)))
        items = con.execute("SELECT item_name, price, limited FROM vendor_items WHERE npc_id=? ORDER BY item_name",
                            (r["id"],)).fetchall()
        if items:
            out.append("%s vende: %s" % (r["name"], "; ".join(
                "%s %s%s" % (i["item_name"], money(i["price"]), " (limitado)" if i["limited"] else "") for i in items)))
    return "\n".join(out)


def cmd_zone_quests(con, a) -> str:
    args: List = ["%" + a.zone + "%", "%" + a.zone + "%"]
    where = "(zone LIKE ? OR giver_zone LIKE ?)"
    if a.side:
        where += " AND (side = ? OR side = '')"
        args.append(a.side.lower()[0])
    if a.min_level is not None:
        where += " AND level >= ?"
        args.append(a.min_level)
    if a.max_level is not None:
        where += " AND level <= ?"
        args.append(a.max_level)
    if a.confirmed:
        where += " AND confirmed_forever = 1"
    rows = con.execute("SELECT * FROM quests WHERE %s ORDER BY level, id" % where, args).fetchall()
    if not rows:
        return "Sin resultados."
    return table([(r["id"], r["level"], r["side"], r["title"], r["giver_name"], r["xp"],
                   "F" if r["xp_src"] == "forever" else "~", money(r["money"]) if r["money"] else "",
                   (r["reward_items"] + " | " if r["reward_items"] else "") + (r["choice_items"] or ""),
                   "F" if r["confirmed_forever"] else ("C" if r["in_classic"] else "?"))
                  for r in rows],
                 ["id", "nv", "lado", "mision", "la da", "xp", "xp_src", "dinero", "recompensas", "estado"])


def cmd_item(con, a) -> str:
    rows = con.execute("SELECT * FROM items WHERE name LIKE ? OR CAST(id AS TEXT)=? ORDER BY id LIMIT ?",
                       ("%" + a.name + "%", a.name, a.limit)).fetchall()
    if not rows:
        return "Sin resultados."
    out = [table([(r["id"], r["name"], r["quality"], r["inv_type"], r["req_level"], r["stats"], r["dps"],
                   r["armor"], "nuevo" if r["new_in_forever"] else ("cambiado" if r["changed_in_forever"] else ""))
                  for r in rows],
                 ["id", "nombre", "cal", "inv", "req", "stats", "dps", "armor", "forever"])]
    for r in rows[:5]:
        src = con.execute("SELECT quest_id, kind, class FROM quest_rewards WHERE item_id=?", (r["id"],)).fetchall()
        if src:
            out.append("%s: recompensa de mision %s" % (r["name"], ", ".join(
                "%d(%s%s)" % (s["quest_id"], s["kind"], " " + s["class"] if s["class"] else "") for s in src)))
        lt = con.execute("SELECT instance, boss, pct, src FROM loot WHERE item_id=? LIMIT 5", (r["id"],)).fetchall()
        if lt:
            out.append("%s: botin %s" % (r["name"], "; ".join(
                "%s/%s %s%% [%s]" % (l["instance"], l["boss"], l["pct"], l["src"]) for l in lt)))
    return "\n".join(out)


def cmd_rares(con, a) -> str:
    rows = con.execute("SELECT * FROM rares WHERE zones LIKE ? OR name LIKE ? ORDER BY level_lo",
                       ("%" + a.zone + "%", "%" + a.zone + "%")).fetchall()
    if not rows:
        return "Sin resultados."
    return table([(r["id"], r["name"], "%s-%s" % (r["level_lo"], r["level_hi"]), r["level_src"], r["zones"],
                   r["seen_spots"] or r["classic_spawns"], r["loot"]) for r in rows],
                 ["id", "nombre", "nivel", "src", "zonas", "lugares (vistos o Classic)", "botin"])


def cmd_meta(con, a) -> str:
    return "\n".join("%s: %s" % (r["key"], r["value"]) for r in con.execute("SELECT * FROM meta"))


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Consulta los datos del addon ForeverDB.")
    ap.add_argument("--db", type=Path, default=DB_PATH)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("quest")
    p.add_argument("name")
    p.add_argument("--limit", type=int, default=10)
    p = sub.add_parser("nodes")
    p.add_argument("kind")
    p.add_argument("--zone")
    p.add_argument("--source", choices=["forever", "classic"])
    p.add_argument("--points", action="store_true", help="lista las coordenadas")
    p = sub.add_parser("recipe")
    p.add_argument("profession")
    p.add_argument("--name")
    p.add_argument("--max-skill", type=int)
    p.add_argument("--min-skill", type=int)
    p = sub.add_parser("npc")
    p.add_argument("name")
    p.add_argument("--limit", type=int, default=20)
    p = sub.add_parser("zone-quests")
    p.add_argument("zone")
    p.add_argument("--side", choices=["h", "a", "horde", "alliance"])
    p.add_argument("--min-level", type=int)
    p.add_argument("--max-level", type=int)
    p.add_argument("--confirmed", action="store_true", help="solo confirmadas en Forever")
    p = sub.add_parser("item")
    p.add_argument("name")
    p.add_argument("--limit", type=int, default=20)
    p = sub.add_parser("rares")
    p.add_argument("zone")
    sub.add_parser("meta")
    a = ap.parse_args(argv)
    con = connect(a.db)
    try:
        fn = {"quest": cmd_quest, "nodes": cmd_nodes, "recipe": cmd_recipe, "npc": cmd_npc,
              "zone-quests": cmd_zone_quests, "item": cmd_item, "rares": cmd_rares, "meta": cmd_meta}[a.cmd]
        print(fn(con, a))
        ver = con.execute("SELECT value FROM meta WHERE key='data_version'").fetchone()
        print("\n%s; datos %s" % (CREDIT, ver[0] if ver else "?"))
    finally:
        con.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
