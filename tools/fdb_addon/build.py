"""Construye data/foreverdb/addon.sqlite a partir de los Data/*.lua del addon ForeverDB.

Lee solo datos (parser propio, nunca ejecuta Lua). Cada tabla conserva el origen de
cada dato en columnas: 'forever' (visto por jugadores en Forever), 'client' (cliente de
Forever) o 'classic' (CMaNGOS classic-db: hipotesis). La base se reconstruye entera.

Uso:
    python3 -m tools.fdb_addon.build
    python3 -m tools.fdb_addon.build --src data/foreverdb/addon_zip/extracted --out /tmp/x.sqlite

Credito obligatorio donde se muestren estos datos: Data from ForeverDB.net (https://foreverdb.net)
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

from .common import (
    CAVEAT, CREDIT, DB_PATH, FALLBACK_ZONES, PROFESSIONS, SRC_DIR, STAT_NAMES,
    decode_gather_points, decode_spot, decode_spots,
)
from .lua_table import parse_file, parse_value

SCHEMA = """
CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT);
CREATE TABLE zones (ui_map INTEGER PRIMARY KEY, name TEXT, continent TEXT, side TEXT,
  level_src TEXT, levels TEXT, levels_a TEXT, levels_h TEXT);
CREATE TABLE quests (id INTEGER PRIMARY KEY, title TEXT, level INTEGER, min_level INTEGER,
  side TEXT, zone TEXT, objective TEXT,
  giver_type TEXT, giver_id INTEGER, giver_name TEXT, giver_map INTEGER, giver_x REAL, giver_y REAL,
  giver_zone TEXT, giver_spot_src TEXT, ender_type TEXT, ender_id INTEGER, ender_name TEXT,
  xp INTEGER, xp_src TEXT, xp_seen TEXT, money INTEGER, money_src TEXT,
  reward_items TEXT, choice_items TEXT, reward_src TEXT, reputation TEXT,
  prev_quests TEXT, next_quests TEXT, group_size INTEGER, flags TEXT,
  in_forever_client INTEGER, players_seen INTEGER, new_in_forever INTEGER,
  lowest_level_seen INTEGER, in_classic INTEGER, classic_gone INTEGER,
  confirmed_forever INTEGER, text_src TEXT, not_offered_to TEXT, source TEXT);
CREATE INDEX quests_title ON quests(title);
CREATE INDEX quests_zone ON quests(zone);
CREATE TABLE quest_rewards (quest_id INTEGER, kind TEXT, item_id INTEGER, item_name TEXT,
  quality INTEGER, count INTEGER, class TEXT, src TEXT);
CREATE INDEX quest_rewards_q ON quest_rewards(quest_id);
CREATE TABLE gather_kinds (kind_id INTEGER PRIMARY KEY, name TEXT, profession TEXT, skill INTEGER,
  item_id INTEGER, level_lo INTEGER, level_hi INTEGER);
CREATE TABLE gather_zones (kind_id INTEGER, ui_map INTEGER, zone TEXT, classic_points INTEGER,
  forever_points INTEGER, w INTEGER);
CREATE TABLE gather_nodes (kind_id INTEGER, ui_map INTEGER, zone TEXT, source TEXT, x REAL, y REAL);
CREATE INDEX gather_nodes_k ON gather_nodes(kind_id, ui_map);
CREATE TABLE recipes (profession TEXT, spell_id INTEGER, name TEXT, skill_req INTEGER,
  yellow INTEGER, green INTEGER, grey INTEGER, item_id INTEGER, item_name TEXT, makes REAL,
  makes_min INTEGER, makes_max INTEGER, reagents TEXT, learned_from TEXT, camp_tier INTEGER,
  new_in_forever INTEGER, skill_req_classic_trainer INTEGER, trainer_cost INTEGER,
  seen_at_forever_trainer INTEGER, forever_changed TEXT, classic_reagents TEXT, classic_colors TEXT,
  tools TEXT, station TEXT, vendors TEXT, drops TEXT, quests TEXT, info_json TEXT);
CREATE INDEX recipes_prof ON recipes(profession, skill_req);
CREATE TABLE recipe_reagents (spell_id INTEGER, item_id INTEGER, item_name TEXT, count INTEGER);
CREATE TABLE prof_ranks (profession TEXT, rank TEXT, max_skill INTEGER, skill_req INTEGER,
  level INTEGER, cost INTEGER, classic_std INTEGER, trainers_a TEXT, trainers_h TEXT, extra_json TEXT);
CREATE TABLE prof_route (profession TEXT, side TEXT, step INTEGER, spell_id INTEGER, name TEXT,
  skill_from INTEGER, skill_to INTEGER, yellow INTEGER, grey INTEGER, learn_skill INTEGER,
  reagents TEXT, makes TEXT, how TEXT, cost INTEGER, trainers TEXT, seen_trainers TEXT,
  new_in_forever INTEGER, forever_changed INTEGER, tools TEXT, station TEXT, alt TEXT);
CREATE TABLE prof_best_zones (profession TEXT, skill_from INTEGER, skill_to INTEGER,
  rank INTEGER, ui_map INTEGER, zone TEXT, score INTEGER);
CREATE TABLE npcs (id INTEGER PRIMARY KEY, name TEXT, title TEXT, ui_map INTEGER, zone TEXT,
  x REAL, y REAL, side TEXT, seen_forever INTEGER, src TEXT);
CREATE INDEX npcs_name ON npcs(name);
CREATE TABLE trainers (npc_id INTEGER, kind TEXT, what TEXT);
CREATE TABLE vendor_items (item_id INTEGER, item_name TEXT, npc_id INTEGER, price INTEGER,
  stack INTEGER, limited INTEGER);
CREATE INDEX vendor_items_npc ON vendor_items(npc_id);
CREATE TABLE items (id INTEGER PRIMARY KEY, name TEXT, quality INTEGER, inv_type INTEGER,
  item_class INTEGER, subclass INTEGER, item_level INTEGER, req_level INTEGER, stats TEXT,
  dps REAL, armor INTEGER, new_in_forever INTEGER, changed_in_forever INTEGER, facts TEXT);
CREATE INDEX items_name ON items(name);
CREATE TABLE rares (id INTEGER PRIMARY KEY, name TEXT, level_lo INTEGER, level_hi INTEGER,
  level_src TEXT, rank INTEGER, rank_src TEXT, creature_type TEXT, respawn_lo INTEGER,
  respawn_hi INTEGER, classic_spawns TEXT, seen_spots TEXT, seen_info TEXT, loot TEXT,
  zones TEXT, inst TEXT);
CREATE TABLE loot (instance_id INTEGER, instance TEXT, kind TEXT, levels TEXT, boss TEXT,
  npc_id INTEGER, item_id INTEGER, item_name TEXT, pct REAL, src TEXT, hidden INTEGER,
  kills INTEGER, seen INTEGER);
CREATE INDEX loot_item ON loot(item_id);
CREATE TABLE dungeons (id INTEGER PRIMARY KEY, name TEXT, kind TEXT, size INTEGER, levels TEXT,
  zone TEXT, bosses TEXT, quests TEXT, guide TEXT);
CREATE TABLE level_routes (side TEXT, level INTEGER, chars INTEGER, median_secs INTEGER,
  fast_secs INTEGER, best_map INTEGER, best_zone TEXT, ok INTEGER, qs REAL);
CREATE TABLE level_route_zones (side TEXT, level INTEGER, ui_map INTEGER, zone TEXT,
  players INTEGER, xp_per_hour INTEGER, fastest_quarter INTEGER);
CREATE TABLE consumables (item_id INTEGER, name TEXT, kind TEXT, effect TEXT, level INTEGER,
  strength REAL, made_by TEXT, sold_by_vendor INTEGER, sod_leftover INTEGER);
CREATE TABLE supplies (category TEXT, key TEXT, data_json TEXT);
CREATE TABLE special_quest_steps (chain TEXT, chain_name TEXT, category TEXT, step INTEGER,
  quest_id INTEGER, item_id INTEGER, title TEXT, side TEXT, text TEXT, tip TEXT, ui_map INTEGER,
  x REAL, y REAL, seen_forever INTEGER);
"""


def _load(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return parse_file(path)


def _src_flag(c: str) -> str:
    return {"f": "forever", "c": "classic", "s": "forever", "k": "classic"}.get(c, c or "")


def _int(v: Any, default: Optional[int] = None) -> Optional[int]:
    try:
        return int(v)
    except (TypeError, ValueError):
        try:
            return int(float(v))
        except (TypeError, ValueError):
            return default


def _float(v: Any) -> Optional[float]:
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _as_list(t: Any) -> List[Any]:
    if t is None:
        return []
    if isinstance(t, list):
        return t
    if isinstance(t, dict):
        return [t[k] for k in sorted(k for k in t if isinstance(k, int))]
    return [t]


class Builder:
    def __init__(self, src: Path):
        self.src = Path(src)
        self.data = self.src / "ForeverDB" / "Data"
        self.helper = self.src / "ForeverDB_Helper" / "Data"
        self.zone_names: Dict[int, str] = dict(FALLBACK_ZONES)
        self.item_names: Dict[int, str] = {}
        self.item_quality: Dict[int, int] = {}
        self.npc_names: Dict[int, str] = {}
        self.counts: Dict[str, int] = {}
        self.meta: Dict[str, Any] = {}

    # ------------------------------------------------------------------ util
    def zone(self, ui_map: Optional[int]) -> str:
        if not ui_map:
            return ""
        return self.zone_names.get(int(ui_map), str(ui_map))

    def iname(self, item_id: Optional[int]) -> str:
        return self.item_names.get(item_id or 0, "")

    def insert(self, con: sqlite3.Connection, table: str, rows: Iterable[tuple]) -> int:
        rows = list(rows)
        if not rows:
            return 0
        ph = ",".join("?" * len(rows[0]))
        con.executemany("INSERT OR IGNORE INTO %s VALUES (%s)" % (table, ph), rows)
        return len(rows)

    # ------------------------------------------------------------- lookups
    def load_lookups(self) -> None:
        meta = _load(self.data / "Meta.lua").get("ns.meta") or {}
        self.meta = meta if isinstance(meta, dict) else {}
        prof = _load(self.helper / "Professions.lua")
        self.helper_prof = prof
        for k, v in (prof.get("ns.profZones") or {}).items():
            self.zone_names[int(k)] = v
        pg = _load(self.helper / "ProfGuides.lua")
        self.helper_guides = pg
        for k, v in (pg.get("ns.profGuideNames") or {}).items():
            if isinstance(k, int) and k < 0 and isinstance(v, str):
                self.zone_names.setdefault(-k, v)
        # nombres de objetos, de menor a mayor prioridad
        sources = [
            (_load(self.data / "SearchNames.lua").get("ns.searchItemNames"), None),
            (_load(self.data / "NPCs.lua").get("ns.soldNames"), None),
        ]
        self.npcs_file = _load(self.data / "NPCs.lua")
        self.recipes_file = _load(self.data / "Recipes.lua")
        self.qf = _load(self.data / "QuestForever.lua")
        self.qc = _load(self.data / "QuestClassic.lua")
        self.qg = _load(self.data / "QuestGuide.lua")
        self.dg = _load(self.data / "Dungeons.lua")
        self.hitems = _load(self.helper / "Items.lua").get("ns.items") or {}
        sources += [
            (self.recipes_file.get("ns.names"), None),
            (self.qf.get("ns.qfItems"), None),
        ]
        for table, _ in sources:
            for k, v in (table or {}).items():
                if isinstance(v, str) and v:
                    self.item_names[int(k)] = v
        for table in (self.dg.get("ns.dgItems"), self.qg.get("ns.qgItems")):
            for k, v in (table or {}).items():
                if isinstance(v, str):
                    name, _, q = v.partition("|")
                    if name:
                        self.item_names[int(k)] = name
                    if q.isdigit():
                        self.item_quality[int(k)] = int(q)
        for k, v in self.hitems.items():
            if isinstance(v, list) and v:
                self.item_names[int(k)] = v[0]
                if len(v) > 1 and isinstance(v[1], int):
                    self.item_quality[int(k)] = v[1]
        # nombres de PNJ: Classic primero, Forever encima
        for k, v in (self.qc.get("ns.qcNpc") or {}).items():
            self.npc_names[int(k)] = str(v).split("|")[0]
        for k, v in (self.qf.get("ns.qfNpcNames") or {}).items():
            self.npc_names[int(k)] = v
        for k, v in (self.npcs_file.get("ns.npcs") or {}).items():
            if isinstance(v, list) and v:
                self.npc_names[int(k)] = v[0]

    # ----------------------------------------------------------------- zones
    def build_zones(self, con) -> None:
        zd = _load(self.data / "Zones.lua").get("ns.zoneData") or {}
        rows = []
        for m, s in zd.items():
            f = str(s).split("|")
            lv = (f[4].split(",") + ["", ""])[:2] if len(f) > 4 else ["", ""]
            rows.append((int(m), self.zone(m), f[0] if f else "", f[1] if len(f) > 1 else "",
                         f[2] if len(f) > 2 else "", f[3] if len(f) > 3 else "", lv[0], lv[1]))
        known = {r[0] for r in rows}
        for m, n in self.zone_names.items():
            if m not in known:
                rows.append((m, n, "", "", "", "", "", ""))
        self.counts["zones"] = self.insert(con, "zones", rows)

    # ---------------------------------------------------------------- quests
    def _ref(self, tok: str):
        """'n3143' -> ('npc', 3143, nombre)."""
        tok = (tok or "").strip()
        if not tok:
            return "", None, ""
        kind = {"n": "npc", "o": "object", "i": "item"}.get(tok[0], "")
        rid = _int(tok[1:])
        if kind == "npc":
            name = self.npc_names.get(rid or 0, "")
        elif kind == "object":
            name = str((self.qc.get("ns.qcObj") or {}).get(rid, "")).split("|")[0]
        elif kind == "item":
            name = self.iname(rid)
        else:
            name = ""
        return kind, rid, name

    def _items_field(self, s: str):
        out = []
        for tok in (s or "").split():
            iid, _, cnt = tok.partition(":")
            iid_i = _int(iid)
            if iid_i:
                out.append((iid_i, _int(cnt, 1) or 1))
        return out

    def build_quests(self, con) -> None:
        qf = self.qf.get("ns.qfQuests") or {}
        qc = self.qc.get("ns.qcQuests") or {}
        qg = self.qg.get("ns.qgQuests") or {}
        strings = _as_list(self.qg.get("ns.qgS"))
        seen = self.qf.get("ns.qfSeen") or {}
        npc_spots_f = self.qf.get("ns.qfNpcSpots") or {}
        qc_npc = self.qc.get("ns.qcNpc") or {}
        gone = self.qc.get("ns.qcGone") or {}
        xpq = (_load(self.data / "QuestXP.lua").get("ns.qxp") or {})
        xp_capt = xpq.get("q") or {}
        curve = _as_list(xpq.get("curve"))
        offers = _load(self.data / "QuestOffers.lua").get("ns.questOffers") or {}
        new_quests = _load(self.data / "Quests.lua").get("ns.newQuests") or []
        new_by_id = {}
        for row in _as_list(new_quests):
            if isinstance(row, list) and row:
                new_by_id[_int(row[0])] = row
        titles_extra = self.qg.get("ns.qgTitles") or {}

        def S(idx: str) -> str:
            i = _int(idx)
            if i and 0 < i <= len(strings):
                return strings[i - 1]
            return ""

        ids = set(qf) | set(qc) | set(qg) | set(new_by_id)
        qrows, rrows = [], []
        for qid in sorted(i for i in ids if isinstance(i, int)):
            f = str(qf.get(qid, "")).split("|") if qid in qf else []
            c = str(qc.get(qid, "")).split("|") if qid in qc else []
            g = str(qg.get(qid, "")).split("|") if qid in qg else []
            nq = new_by_id.get(qid)

            def F(lst, i, default=""):
                return lst[i] if len(lst) > i else default

            title = F(f, 0) or F(c, 0) or (nq[1] if nq else "") or titles_extra.get(qid, "")
            level = _int(F(f, 1)) or _int(F(c, 1)) or (_int(nq[2]) if nq else None)
            min_level = _int(F(f, 2)) or _int(F(c, 2))
            side = F(f, 10) or F(c, 3)
            objective = F(f, 3) or S(F(g, 2))
            starts = F(f, 4) or F(c, 9)
            ends = F(f, 5) or F(c, 10)
            gtype, gid, gname = self._ref(starts.split()[0] if starts else "")
            etype, eid, ename = self._ref(ends.split()[0] if ends else "")
            # donde esta quien la da: visto en Forever > PNJ visto > Classic
            gmap = gx = gy = None
            gsrc = ""
            sp = seen.get(qid) or {}
            first = next(iter(decode_spots(sp.get("s") if isinstance(sp, dict) else None)), None)
            if first:
                (gmap, gx, gy), gsrc = first, "forever"
            elif gtype == "npc" and gid in npc_spots_f:
                first = next(iter(decode_spots(npc_spots_f[gid])), None)
                if first:
                    (gmap, gx, gy), gsrc = first, "forever"
            if gmap is None and gtype == "npc" and gid in qc_npc:
                parts = str(qc_npc[gid]).split("|")
                first = next(iter(decode_spots(parts[1] if len(parts) > 1 else "")), None)
                if first:
                    (gmap, gx, gy), gsrc = first, "classic"
            if gmap is None and nq and _int(nq[4]):
                gmap, gx, gy, gsrc = _int(nq[4]), _float(nq[5]), _float(nq[6]), "forever"
                if not gname:
                    gname = nq[7] if len(nq) > 7 else ""
            zone = S(F(g, 0)) or (nq[3] if nq else "") or (self.zone(gmap) if gmap else "")
            # experiencia
            xp, xp_src = None, ""
            if qid in xp_capt:
                xp, xp_src = _int(xp_capt[qid]), "forever"
            elif level and 0 < level <= len(curve):
                xp, xp_src = _int(curve[level - 1]), "curve_estimate"
            money = _int(F(g, 4)) if g else None
            money_src = _src_flag(F(g, 5)) if g else ""
            if not money_src and not money:
                money = None  # la guia no sabe el dinero: desconocido, no 0
            get_items = self._items_field(F(g, 7))
            choose_items = self._items_field(F(g, 8))
            rsrc = _src_flag(F(g, 9)) if F(g, 9) not in ("", "-") else ""
            rep = []
            for tok in F(g, 10).split():
                t, _, v = tok.partition(":")
                rep.append("%s %s" % (S(t), v))
            for kind, items in (("get", get_items), ("choose", choose_items)):
                for iid, cnt in items:
                    rrows.append((qid, kind, iid, self.iname(iid), self.item_quality.get(iid),
                                  cnt, "", rsrc))
            for part in F(g, 16).split(";"):
                if "=" not in part:
                    continue
                cls, _, lists = part.partition("=")
                gl, _, cl = lists.partition("/")
                for kind, items in (("get", self._items_field(gl)), ("choose", self._items_field(cl))):
                    for iid, cnt in items:
                        rrows.append((qid, kind, iid, self.iname(iid),
                                      self.item_quality.get(iid), cnt, cls, "forever"))

            def fmt(items):
                return "; ".join("%s (%d)%s" % (self.iname(i) or "?", i, " x%d" % n if n > 1 else "")
                                 for i, n in items)

            players_seen = _int(F(f, 6), 0) if f else 0
            new_flag = 1 if (F(f, 7) == "1" or nq) else 0
            flags = F(c, 13)
            group = _int(F(g, 15)) or None
            src_parts = []
            if f:
                src_parts.append("client")
            if players_seen:
                src_parts.append("forever")
            if c:
                src_parts.append("classic")
            confirmed = 1 if (players_seen > 0 or nq or xp_src == "forever") else 0
            off = offers.get(qid)
            qrows.append((
                qid, title, level, min_level, side, zone, objective,
                gtype, gid, gname, gmap, gx, gy, self.zone(gmap) if gmap else "", gsrc, etype, eid, ename,
                xp, xp_src, F(g, 6), money, money_src,
                fmt(get_items), fmt(choose_items), rsrc, "; ".join(rep),
                F(g, 11), F(g, 12), group, flags,
                1 if f else 0, players_seen, new_flag, _int(F(f, 9)) if f else None,
                1 if c else 0, 1 if qid in gone else 0, confirmed, F(g, 3),
                ", ".join(_as_list(off)) if off else "", "+".join(src_parts),
            ))
        self.counts["quests"] = self.insert(con, "quests", qrows)
        self.counts["quest_rewards"] = self.insert(con, "quest_rewards", rrows)

    # ---------------------------------------------------------------- gather
    def build_gather(self, con) -> None:
        gd = _load(self.data / "Gather.lua").get("ns.gatherData") or {}
        kinds = gd.get("kinds") or {}
        krows = []
        for kid, k in kinds.items():
            lv = _as_list(k.get("lv"))
            krows.append((int(kid), k.get("n"), k.get("p"), _int(k.get("sk")), _int(k.get("item")),
                          _int(lv[0]) if lv else None, _int(lv[1]) if len(lv) > 1 else None))
        self.counts["gather_kinds"] = self.insert(con, "gather_kinds", krows)
        zrows, nrows = [], []
        for m, z in (gd.get("zones") or {}).items():
            for kid, e in ((z or {}).get("k") or {}).items():
                cpts = decode_gather_points(e.get("c"))
                fpts = decode_gather_points(e.get("f"))
                zname = self.zone(m)
                zrows.append((int(kid), int(m), zname, len(cpts), len(fpts), _int(e.get("w"))))
                nrows += [(int(kid), int(m), zname, "classic", x, y) for x, y in cpts]
                nrows += [(int(kid), int(m), zname, "forever", x, y) for x, y in fpts]
        self.counts["gather_zones"] = self.insert(con, "gather_zones", zrows)
        self.counts["gather_nodes"] = self.insert(con, "gather_nodes", nrows)

    # --------------------------------------------------------------- recipes
    def build_recipes(self, con) -> None:
        rec = self.recipes_file.get("ns.recipes") or {}
        info = self.recipes_file.get("ns.recipeInfo") or {}
        rrows, grows = [], []
        for prof, lst in rec.items():
            for r in _as_list(lst):
                r = _as_list(r)
                if len(r) < 10:
                    continue
                spell = _int(r[0])
                reag = []
                for tok in str(r[8] or "").split(","):
                    iid, _, n = tok.partition(":")
                    if _int(iid):
                        reag.append((_int(iid), _int(n, 1)))
                        grows.append((spell, _int(iid), self.iname(_int(iid)), _int(n, 1)))
                inf = info.get(spell) or {}
                inf = inf if isinstance(inf, dict) else {}

                def J(v):
                    if v is None or v == "":
                        return ""
                    return v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)

                rrows.append((
                    prof, spell, r[1], _int(r[2]), _int(r[3]), _int(r[4]), _int(r[5]),
                    _int(r[6]), self.iname(_int(r[6])), _float(r[7]),
                    _int(r[13]) if len(r) > 13 else None, _int(r[14]) if len(r) > 14 else None,
                    ", ".join("%s x%d" % (self.iname(i) or i, n) for i, n in reag),
                    r[9], _int(r[10]) if len(r) > 10 else None, _int(r[11]) if len(r) > 11 else None,
                    _int(r[12]) if len(r) > 12 else None, _int(inf.get("tc")), _int(inf.get("tf")),
                    J(inf.get("c")), J(inf.get("w")), J(inf.get("ws")), J(inf.get("t")), J(inf.get("fo")),
                    J(inf.get("v")), J(inf.get("dr")), J(inf.get("q")),
                    json.dumps(inf, ensure_ascii=False, default=str) if inf else "",
                ))
        self.counts["recipes"] = self.insert(con, "recipes", rrows)
        self.counts["recipe_reagents"] = self.insert(con, "recipe_reagents", grows)

    def build_professions(self, con) -> None:
        prof = self.helper_prof
        src = prof.get("ns.profSrc") or {}
        names = {k: (v.get("n") if isinstance(v, dict) else k) for k, v in (prof.get("ns.profs") or {}).items()}
        npc_src = prof.get("ns.profNpcSrc")
        self.prof_npcs = parse_value(npc_src) if isinstance(npc_src, str) else {}
        rank_rows, route_rows, best_rows = [], [], []
        for slug, code in src.items():
            try:
                d = parse_value(code) if isinstance(code, str) else (code or {})
            except Exception as exc:  # noqa: BLE001 - un perfil roto no debe parar la base
                print("aviso: no se pudo leer profSrc[%s]: %s" % (slug, exc), file=sys.stderr)
                continue
            pname = names.get(slug, slug)
            for rk in _as_list(d.get("ranks")):
                tr = rk.get("tr") or {}
                extra = {k: v for k, v in rk.items() if k in ("book", "q")}
                rank_rows.append((pname, rk.get("r"), _int(rk.get("max")), _int(rk.get("sk")),
                                  _int(rk.get("lv")), _int(rk.get("cost")), _int(rk.get("std"), 0),
                                  " ".join(str(x) for x in _as_list(tr.get("a")) if x is not None) if isinstance(tr, dict) else "",
                                  " ".join(str(x) for x in _as_list(tr.get("h")) if x is not None) if isinstance(tr, dict) else "",
                                  json.dumps(extra, default=str) if extra else ""))
            for side in ("a", "h"):
                route = d.get(side)
                if not isinstance(route, dict):
                    continue
                for i, st in enumerate(_as_list(route.get("steps")), 1):
                    L = st.get("L") or {}
                    reag = ", ".join("%s x%s" % (self.iname(_int(p[0])) or p[0], p[1])
                                     for p in _as_list(st.get("r")) if isinstance(p, list) and len(p) > 1)
                    mk = _as_list(st.get("mk"))
                    makes = ("%s x%s" % (self.iname(_int(mk[0])) or mk[0], mk[1])) if len(mk) > 1 else ""
                    alt = _as_list(st.get("alt"))
                    route_rows.append((
                        pname, side, i, _int(st.get("s")), st.get("n"), _int(st.get("a")), _int(st.get("b")),
                        _int(st.get("y")), _int(st.get("g")), _int(st.get("o")), reag, makes,
                        L.get("how", ""), _int(L.get("cost")),
                        " ".join(str(x) for x in _as_list(L.get("tr"))),
                        ", ".join(str(x) for x in _as_list(L.get("fv"))),
                        _int(st.get("new"), 0), _int(st.get("chg"), 0),
                        ", ".join(_as_list(st.get("tools"))), st.get("focus") or "",
                        ("%s (%s)" % (alt[1], alt[0])) if len(alt) > 1 else "",
                    ))
            for band in _as_list(d.get("best")):
                band = _as_list(band)
                if len(band) < 3:
                    continue
                for rank, z in enumerate(_as_list(band[2]), 1):
                    z = _as_list(z)
                    if len(z) >= 2:
                        best_rows.append((pname, _int(band[0]), _int(band[1]), rank, _int(z[0]),
                                          self.zone(_int(z[0])), _int(z[1])))
        self.counts["prof_ranks"] = self.insert(con, "prof_ranks", rank_rows)
        self.counts["prof_route"] = self.insert(con, "prof_route", route_rows)
        self.counts["prof_best_zones"] = self.insert(con, "prof_best_zones", best_rows)

    # ------------------------------------------------------------------ npcs
    def build_npcs(self, con) -> None:
        rows = []
        for nid, v in (self.npcs_file.get("ns.npcs") or {}).items():
            v = _as_list(v)
            if len(v) >= 6:
                rows.append((int(nid), v[0], v[1], _int(v[2]), self.zone(_int(v[2])), _float(v[3]),
                             _float(v[4]), v[5], _int(v[6] if len(v) > 6 else 0, 0), "NPCs.lua"))
        for nid, v in (self.prof_npcs or {}).items():
            v = _as_list(v)
            if len(v) >= 6:
                rows.append((int(nid), v[0], v[1], _int(v[3]), self.zone(_int(v[3])), _float(v[4]),
                             _float(v[5]), str(v[2]).upper(), _int(v[6] if len(v) > 6 else 0, 0),
                             "Helper Professions.lua"))
        sup = _load(self.data / "Supplies.lua").get("ns.supplies") or {}
        self.supplies = sup
        for cat in ("vendors", "repair"):
            for nid, v in (sup.get(cat) or {}).items():
                v = _as_list(v)
                if len(v) >= 6:
                    rows.append((int(nid), v[0], v[1], _int(v[2]), self.zone(_int(v[2])), _float(v[3]),
                                 _float(v[4]), v[5], _int(v[6] if len(v) > 6 else 0, 0), "Supplies.lua"))
        # PNJ de misiones: lugar visto en Forever si existe, si no el de Classic
        spots_f = self.qf.get("ns.qfNpcSpots") or {}
        for nid, name in (self.qf.get("ns.qfNpcNames") or {}).items():
            sp = next(iter(decode_spots(spots_f.get(nid))), None)
            if sp:
                rows.append((int(nid), name, "", sp[0], self.zone(sp[0]), sp[1], sp[2], "", 1,
                             "QuestForever.lua"))
            else:
                rows.append((int(nid), name, "", None, "", None, None, "", 0, "QuestForever.lua"))
        for nid, s in (self.qc.get("ns.qcNpc") or {}).items():
            parts = str(s).split("|")
            sp = next(iter(decode_spots(parts[1] if len(parts) > 1 else "")), None)
            rows.append((int(nid), parts[0], "", sp[0] if sp else None, self.zone(sp[0]) if sp else "",
                         sp[1] if sp else None, sp[2] if sp else None, "", 0, "QuestClassic.lua"))
        self.counts["npcs"] = self.insert(con, "npcs", rows)
        trows = []
        for kind, key in (("class", "ns.classTrainers"), ("profession", "ns.profTrainers")):
            for what, lst in (self.npcs_file.get(key) or {}).items():
                for nid in _as_list(lst):
                    trows.append((_int(nid), kind, what))
        self.counts["trainers"] = self.insert(con, "trainers", trows)
        vrows = []
        sold = self.npcs_file.get("ns.sold") or {}
        names = self.npcs_file.get("ns.soldNames") or {}
        for iid, flat in sold.items():
            flat = _as_list(flat)
            for i in range(0, len(flat) - 3, 4):
                vrows.append((int(iid), names.get(iid) or self.iname(int(iid)), _int(flat[i]),
                              _int(flat[i + 1]), _int(flat[i + 2]), _int(flat[i + 3])))
        self.counts["vendor_items"] = self.insert(con, "vendor_items", vrows)
        srows = []
        for cat, v in sup.items():
            if cat in ("vendors", "repair"):
                continue
            if isinstance(v, dict):
                for k, val in v.items():
                    srows.append((cat, str(k), json.dumps(val, ensure_ascii=False)))
        self.counts["supplies"] = self.insert(con, "supplies", srows)

    # ----------------------------------------------------------------- items
    def build_items(self, con) -> None:
        facts = _load(self.data / "Items.lua").get("ns.items") or {}
        gear = _load(self.data / "Gear.lua").get("ns.gear") or {}
        ids = set(self.item_names) | set(facts) | set(gear) | set(self.hitems)
        rows = []
        for iid in sorted(i for i in ids if isinstance(i, int)):
            h = _as_list(self.hitems.get(iid))
            g = str(gear.get(iid, "")).split(";") if iid in gear else []
            fx = str(facts.get(iid, ""))
            flags = fx.split("|")
            stats = []
            if len(g) > 4:
                for tok in g[4].split(","):
                    sid, _, val = tok.partition(":")
                    if _int(sid) is not None and val:
                        stats.append("%s %s" % (STAT_NAMES.get(_int(sid), "stat%s" % sid), val))
            inv = _int(g[0]) if g else (_int(h[3]) if len(h) > 3 else None)
            rows.append((
                iid, self.item_names.get(iid, ""), self.item_quality.get(iid),
                inv, _int(g[1]) if len(g) > 1 else (_int(h[6]) if len(h) > 6 else None),
                _int(g[2]) if len(g) > 2 else (_int(h[7]) if len(h) > 7 else None),
                _int(h[4]) if len(h) > 4 else None,
                _int(g[3]) if len(g) > 3 and g[3] != "" else (_int(h[5]) if len(h) > 5 else None),
                ", ".join(stats),
                (_int(g[5], 0) or 0) / 10.0 if len(g) > 5 and g[5] else None,
                _int(g[6]) if len(g) > 6 else None,
                1 if ("n" in flags or (len(h) > 8 and h[8] == 1)) else 0,
                1 if "c" in flags else 0, fx,
            ))
        self.counts["items"] = self.insert(con, "items", rows)

    # ----------------------------------------------------------------- rares
    def build_rares(self, con) -> None:
        r = _load(self.data / "Rares.lua")
        by_map: Dict[int, List[str]] = {}
        for m, s in (r.get("ns.rareByMap") or {}).items():
            for rid in str(s).split(","):
                by_map.setdefault(_int(rid) or 0, []).append(self.zone(m))
        by_inst: Dict[int, List[str]] = {}
        for m, s in (r.get("ns.rareByInst") or {}).items():
            for rid in str(s).split(","):
                by_inst.setdefault(_int(rid) or 0, []).append(str(m))
        rows = []
        for rid, s in (r.get("ns.rareRows") or {}).items():
            f = str(s).split("|") + [""] * 17
            loot = []
            for part in f[15].split("~"):
                p = part.split(",")
                if len(p) >= 5:
                    loot.append("%s (%s) %s%% [%s]" % (p[4], p[0], p[2], _src_flag(p[3])))
            rows.append((int(rid), f[0], _int(f[1]), _int(f[2]), _src_flag(f[3]), _int(f[4]),
                         _src_flag(f[5]), f[6], _int(f[7]), _int(f[8]), f[12], f[13], f[14],
                         "; ".join(loot), ", ".join(by_map.get(int(rid), [])),
                         ", ".join(by_inst.get(int(rid), []))))
        self.counts["rares"] = self.insert(con, "rares", rows)

    # ------------------------------------------------------------------ loot
    def build_loot(self, con) -> None:
        db = _load(self.data / "Loot.lua").get("ns.lootDB") or {}
        rows = []

        def add(inst, boss, npc, s):
            for tok in str(s or "").split(";"):
                p = tok.split(":")
                if not p or not _int(p[0]):
                    continue
                iid = _int(p[0])
                rows.append((_int(inst.get("id")), inst.get("name"), inst.get("kind"), inst.get("lv"),
                             boss, npc, iid, self.iname(iid), _float(p[1]) if len(p) > 1 else None,
                             _src_flag(p[2]) if len(p) > 2 else "", _int(p[3]) if len(p) > 3 else None,
                             _int(p[4]) if len(p) > 4 else None, _int(p[5]) if len(p) > 5 else None))

        for inst in _as_list(db.get("inst")):
            if not isinstance(inst, dict):
                continue
            for b in _as_list(inst.get("bosses")):
                if isinstance(b, dict):
                    add(inst, b.get("name"), _int(b.get("npc")), b.get("loot"))
            add(inst, "(trash)", None, inst.get("trash"))
        self.counts["loot"] = self.insert(con, "loot", rows)
        drows = []
        for did, d in (self.dg.get("ns.dungeons") or {}).items():
            if not isinstance(d, dict):
                continue
            bosses = [b.split(":")[-1] for b in str(d.get("boss", "")).split("|") if b]
            drows.append((int(did), d.get("n"), d.get("kind"), _int(d.get("size")), d.get("lv"),
                          d.get("zone"), ", ".join(bosses), d.get("q", ""), d.get("guide", "")))
        self.counts["dungeons"] = self.insert(con, "dungeons", drows)

    # ---------------------------------------------------------------- routes
    def build_routes(self, con) -> None:
        lr = _load(self.data / "LevelRoutes.lua").get("ns.levelRouteData") or {}
        rows, zrows = [], []
        for side in ("A", "H"):
            for lv, r in (lr.get(side) or {}).items():
                if not isinstance(r, dict):
                    continue
                fz = set(_as_list(r.get("fz")))
                rows.append((side, _int(lv), _int(r.get("n")), _int(r.get("med")), _int(r.get("fast")),
                             _int(r.get("best")), self.zone(_int(r.get("best"))), 1 if r.get("ok") else 0,
                             _float(r.get("qs"))))
                for z in _as_list(r.get("z")):
                    z = _as_list(z)
                    if len(z) >= 3:
                        zrows.append((side, _int(lv), _int(z[0]), self.zone(_int(z[0])), _int(z[1]),
                                      _int(z[2]), 1 if z[0] in fz else 0))
        self.counts["level_routes"] = self.insert(con, "level_routes", rows)
        self.counts["level_route_zones"] = self.insert(con, "level_route_zones", zrows)

    def build_consumables(self, con) -> None:
        c = _load(self.data / "Consumables.lua").get("ns.consumables") or []
        rows = []
        for r in _as_list(c):
            r = _as_list(r)
            if len(r) < 9:
                continue
            mb = _int(r[6], 0) or 0
            rows.append((_int(r[0]), r[1], r[2], r[3], _int(r[4]), _float(r[5]),
                         PROFESSIONS[mb - 1] if 0 < mb <= len(PROFESSIONS) else "",
                         _int(r[7]), _int(r[8])))
        self.counts["consumables"] = self.insert(con, "consumables", rows)

    def build_special(self, con) -> None:
        sq = _load(self.data / "SpecialQuests.lua").get("ns.specialQuests") or {}
        rows = []
        for ch in _as_list(sq.get("chains")):
            if not isinstance(ch, dict):
                continue
            for i, st in enumerate(_as_list(ch.get("steps")), 1):
                if not isinstance(st, dict):
                    continue
                seen = st.get("seen")
                rows.append((ch.get("key"), ch.get("name"), ch.get("cat"), i, _int(st.get("q")),
                             _int(st.get("item")), st.get("title", ""), st.get("side", ""),
                             st.get("t", ""), st.get("tip", ""), _int(st.get("m")),
                             _float(st.get("x")), _float(st.get("y")),
                             None if seen is None else (1 if seen else 0)))
        self.counts["special_quest_steps"] = self.insert(con, "special_quest_steps", rows)

    # ------------------------------------------------------------------ main
    def build(self, out: Path) -> Dict[str, int]:
        out = Path(out)
        out.parent.mkdir(parents=True, exist_ok=True)
        tmp = out.with_suffix(".tmp")
        if tmp.exists():
            tmp.unlink()
        con = sqlite3.connect(str(tmp))
        try:
            con.executescript(SCHEMA)
            self.load_lookups()
            self.build_zones(con)
            self.build_quests(con)
            self.build_gather(con)
            self.build_recipes(con)
            self.build_professions(con)
            self.build_npcs(con)
            self.build_items(con)
            self.build_rares(con)
            self.build_loot(con)
            self.build_routes(con)
            self.build_consumables(con)
            self.build_special(con)
            # filas reales (INSERT OR IGNORE descarta duplicados de clave)
            for (tname,) in con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name != 'meta'"):
                self.counts[tname] = con.execute('SELECT COUNT(*) FROM "%s"' % tname).fetchone()[0]
            meta = {
                "data_version": self.meta.get("version", ""),
                "client_build": self.meta.get("build", ""),
                "addon_version": self.meta.get("addon", ""),
                "built_epoch": self.meta.get("built", ""),
                "credit": CREDIT,
                "caveat": CAVEAT,
                "counts": json.dumps(self.counts),
            }
            self.insert(con, "meta", [(k, str(v)) for k, v in meta.items()])
            con.commit()
        finally:
            con.close()
        tmp.replace(out)
        return self.counts


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Construye la base SQLite del addon ForeverDB.")
    ap.add_argument("--src", type=Path, default=SRC_DIR, help="carpeta con ForeverDB/ y ForeverDB_Helper/")
    ap.add_argument("--out", type=Path, default=DB_PATH)
    args = ap.parse_args(argv)
    if not (args.src / "ForeverDB" / "Data").is_dir():
        print("No existe %s/ForeverDB/Data" % args.src, file=sys.stderr)
        return 1
    counts = Builder(args.src).build(args.out)
    for k, v in counts.items():
        print("%-22s %d" % (k, v))
    print("-> %s" % args.out)
    print(CREDIT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
