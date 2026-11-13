"""Pruebas del adaptador del addon ForeverDB con fixtures pequenos y ficticios (no los archivos reales)."""

from __future__ import annotations

import contextlib
import io
import shutil
import sqlite3
import tempfile
import unittest
from pathlib import Path

from tools.fdb_addon import build, common, lua_table, query

FIXTURES = {
    "ForeverDB/Data/Meta.lua": """-- Data: test
local _, ns = ...
ns.meta = {version="2099-01-01.test",built=1,build="1.60.1.0",cap=60,site="x",addon="0.0.1"}
""",
    "ForeverDB/Data/QuestForever.lua": """local _, ns = ...
-- [quest] = "title|level|min level|objective|starts|ends|players|new|prev|lowest|side"
ns.qfQuests = {
[100]="Boar Trouble|5|2|Kill 8 boars.|n10|n10|12|0|0|4|h",
[90001]="Brand New Thing|8|5|Do the new thing.|n11|n10|3|1|100|7|h",
}
ns.qfSeen = {
[100]={s="ncbnxw",e="ncbnxw"},
}
ns.qfNpcNames = {
[10]="Test Giver",
[11]="New Giver",
}
ns.qfNpcSpots = {
[11]="ncds4z",
}
ns.qfItems = {
[5001]="Quest Blade",
}
""",
    "ForeverDB/Data/QuestClassic.lua": """local _, ns = ...
ns.qcQuests = {
[100]="Boar Trouble|5|2|h|0|178|||0|n10|n10|c1:8||",
[200]="Old Classic Quest|12|8|h|0|178|||0|n12|n12|||",
}
ns.qcNpc = {
[12]="Classic Guy|ndmumy",
}
ns.qcGone = {
[200]=1,
}
""",
    "ForeverDB/Data/QuestGuide.lua": """local _, ns = ...
ns.qgS = {
"Durotar",
"Kill 8 boars.",
"Orgrimmar",
}
ns.qgQuests = {
[100]="1||2|ff|250|f|450:5|118:2|5001 5002|f|3:150||||||ROGUE=/5001;WARRIOR=/5002",
}
ns.qgItems = {
[5002]="Quest Axe|2",
[5001]="Quest Blade|2",
}
""",
    "ForeverDB/Data/QuestXP.lua": """local _, ns = ...
ns.qxp = {
q={[100]=460},
curve={40,85,250,280,300,460,625,625,625,650,650,725},
dmul=2,
src="players' captures + curve",
}
""",
    "ForeverDB/Data/QuestOffers.lua": """local _, ns = ...
ns.questOffers = {
[100]={";PRIEST;"},
}
""",
    "ForeverDB/Data/Gather.lua": """local _, ns = ...
ns.gatherData = {
  v = 1, built = "2099-01-01",
  kinds = {
    [30] = { n = "Copper Vein", p = "mine", sk = 1, item = 2770, o = { 1731 } },
  },
  zones = {
    [1411] = { fish = 25, k = {
      [30] = { c = "9w9va07b", f = "auh8", w = 6 },
    } },
  },
}
""",
    "ForeverDB/Data/Recipes.lua": """local _, ns = ...
ns.recipes = {Engineering={{3918,"Rough Blasting Powder",1,20,30,40,4357,1,"2835:1","a",0,0,0},{3922,"Handful of Copper Bolts",30,45,52,60,4359,1,"2840:1","t",0,0,1}},Mining={{2657,"Smelt Copper",1,25,47,70,2840,1,"2770:1","a",0,0,0}}}
ns.names = {[2835]="Rough Stone",[2840]="Copper Bar",[4357]="Rough Blasting Powder",[4359]="Handful of Copper Bolts",[2770]="Copper Ore"}
ns.recipeInfo = {[3922]={tc=115,tf=1,tn={8,8}}}
""",
    "ForeverDB/Data/NPCs.lua": """local _, ns = ...
ns.npcs = {[20]={"Shop Keeper","Trade Supplies",1454,50.5,60.25,"H",1}}
ns.sold = {[2880]={20,100,1,0}}
ns.soldNames = {[2880]="Weak Flux"}
ns.profTrainers = {Engineering={20}}
ns.classTrainers = {ROGUE={21}}
""",
    "ForeverDB/Data/Items.lua": """local _, ns = ...
ns.items = {[5001]="n|qBoar Trouble~0"}
""",
    "ForeverDB/Data/Gear.lua": """local _, ns = ...
ns.gear = {[5001]="13;2;15;4;3:2,7:1;45;0"}
""",
    "ForeverDB/Data/Rares.lua": """local _, ns = ...
ns.rareRows = {
[300]="Big Boar|9|9|s|4|s|Beast|3600|7200|1|1||1411:43.2,39.3|1411:43.2,49.6|x|5571,1,1,s,Small Black Pouch|",
}
ns.rareByMap = {[1411]="300"}
""",
    "ForeverDB_Helper/Data/Professions.lua": """local _, ns = ...
ns.profs = {
["engineering"]={n="Engineering",line=202,kind="craft",top=300},
}
ns.profSrc = {
["engineering"]=[=[return {ranks={{r="Apprentice",max=75,sk=0,lv=5,cost=10,tr={a={1},h={2}}}},h={steps={{s=3918,a=1,b=33,y=20,g=40,o=1,n="Rough Blasting Powder",r={{2835,1}},mk={4357,1},L={how="a"}}}}}]=],
}
ns.profNpcSrc = [=[return {[2]={"Horde Engineer","Journeyman Engineer","h",1454,75.1,25.2,1}}]=]
ns.profZones = {
[1411]="Durotar",
[1454]="Orgrimmar",
}
""",
}


class LuaTableTests(unittest.TestCase):
    def test_scalars_and_tables(self):
        v = lua_table.parse_value('{1, -2.5, "a\\"b", true, nil, x=0x10, ["k"]={}, [3]=\'z\'}')
        self.assertEqual(v[1], 1)
        self.assertEqual(v[2], -2.5)
        self.assertEqual(v["x"], 16)
        self.assertEqual(v["k"], [])
        # [3]= explicito gana a la posicion 3
        self.assertEqual(v[3], "z")

    def test_pure_array_is_list(self):
        self.assertEqual(lua_table.parse_value("{ {1,2}, {3} }"), [[1, 2], [3]])

    def test_long_strings_and_comments(self):
        text = """-- comentario con { llaves
--[[ bloque
ns.no = 1 ]]
local _, ns = ...
ns.a = [=[return {[1]="x"}]=]
ns.b.c = { 'q' } -- cola
for v, s in pairs(packed) do lv[id] = v end
"""
        d = lua_table.parse_assignments(text)
        self.assertNotIn("ns.no", d)
        self.assertEqual(d["ns.b.c"], ["q"])
        self.assertEqual(lua_table.parse_value(d["ns.a"]), {1: "x"})

    def test_escapes(self):
        self.assertEqual(lua_table.parse_value(r'"a\nb\65\\"'), "a\nbA\\")

    def test_error_on_garbage(self):
        with self.assertRaises(lua_table.LuaParseError):
            lua_table.parse_value("{1 2}")


class DecodeTests(unittest.TestCase):
    def test_gather_points(self):
        self.assertEqual(common.decode_gather_points("9w9va07b"), [(35.6, 35.5), (36.0, 26.3)])
        self.assertEqual(common.decode_gather_points(""), [])

    def test_spot(self):
        self.assertEqual(common.decode_spot("ncbnxw"), (1411, 42.1, 68.4))


class BuildAndQueryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp())
        for rel, text in FIXTURES.items():
            p = cls.tmp / "src" / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text, encoding="utf-8")
        cls.db = cls.tmp / "addon.sqlite"
        cls.counts = build.Builder(cls.tmp / "src").build(cls.db)
        cls.con = sqlite3.connect(str(cls.db))
        cls.con.row_factory = sqlite3.Row

    @classmethod
    def tearDownClass(cls):
        cls.con.close()
        shutil.rmtree(cls.tmp)

    def q1(self, sql, *args):
        return self.con.execute(sql, args).fetchone()

    def test_meta(self):
        self.assertEqual(self.q1("SELECT value FROM meta WHERE key='data_version'")[0], "2099-01-01.test")
        self.assertIn("foreverdb.net", self.q1("SELECT value FROM meta WHERE key='credit'")[0])

    def test_quest_merged(self):
        q = self.q1("SELECT * FROM quests WHERE id=100")
        self.assertEqual(q["title"], "Boar Trouble")
        self.assertEqual(q["zone"], "Durotar")
        self.assertEqual(q["xp"], 460)
        self.assertEqual(q["xp_src"], "forever")
        self.assertEqual(q["money"], 250)
        self.assertEqual(q["giver_name"], "Test Giver")
        self.assertEqual((q["giver_map"], q["giver_x"], q["giver_y"]), (1411, 42.1, 68.4))
        self.assertEqual(q["giver_spot_src"], "forever")
        self.assertEqual(q["confirmed_forever"], 1)
        self.assertEqual(q["in_classic"], 1)
        self.assertEqual(q["reputation"], "Orgrimmar 150")
        self.assertEqual(q["not_offered_to"], ";PRIEST;")
        self.assertEqual(q["reward_items"], "? (118) x2")  # sin nombre en el fixture
        self.assertIn("Quest Blade (5001)", q["choice_items"])

    def test_class_rewards(self):
        rows = self.con.execute("SELECT class, item_id FROM quest_rewards WHERE quest_id=100 AND class!=''"
                                " ORDER BY class").fetchall()
        self.assertEqual([(r[0], r[1]) for r in rows], [("ROGUE", 5001), ("WARRIOR", 5002)])

    def test_new_and_classic_only(self):
        n = self.q1("SELECT * FROM quests WHERE id=90001")
        self.assertEqual(n["new_in_forever"], 1)
        self.assertEqual(n["in_classic"], 0)
        self.assertEqual(n["giver_spot_src"], "forever")  # desde qfNpcSpots
        self.assertEqual(n["xp_src"], "curve_estimate")
        self.assertEqual(n["xp"], 625)
        c = self.q1("SELECT * FROM quests WHERE id=200")
        self.assertEqual(c["confirmed_forever"], 0)
        self.assertEqual(c["classic_gone"], 1)
        self.assertEqual(c["giver_spot_src"], "classic")
        self.assertEqual(c["giver_zone"], "The Barrens")  # nombre de respaldo

    def test_gather(self):
        rows = self.con.execute("SELECT source, x, y FROM gather_nodes ORDER BY source, x").fetchall()
        self.assertEqual([tuple(r) for r in rows],
                         [("classic", 35.6, 35.5), ("classic", 36.0, 26.3), ("forever", 39.0, 62.0)])
        z = self.q1("SELECT * FROM gather_zones")
        self.assertEqual((z["zone"], z["classic_points"], z["forever_points"]), ("Durotar", 2, 1))

    def test_recipes(self):
        r = self.q1("SELECT * FROM recipes WHERE spell_id=3922")
        self.assertEqual(r["profession"], "Engineering")
        self.assertEqual((r["skill_req"], r["yellow"], r["green"], r["grey"]), (30, 45, 52, 60))
        self.assertEqual(r["reagents"], "Copper Bar x1")
        self.assertEqual(r["trainer_cost"], 115)
        self.assertEqual(r["skill_req_classic_trainer"], 1)
        self.assertEqual(self.q1("SELECT COUNT(*) FROM recipes WHERE profession='Mining'")[0], 1)

    def test_professions_and_npcs(self):
        st = self.q1("SELECT * FROM prof_route")
        self.assertEqual((st["profession"], st["side"], st["name"]), ("Engineering", "h", "Rough Blasting Powder"))
        self.assertEqual(st["reagents"], "Rough Stone x1")
        rk = self.q1("SELECT * FROM prof_ranks")
        self.assertEqual((rk["rank"], rk["trainers_h"]), ("Apprentice", "2"))
        npc = self.q1("SELECT * FROM npcs WHERE id=2")
        self.assertEqual((npc["name"], npc["zone"], npc["side"], npc["seen_forever"]),
                         ("Horde Engineer", "Orgrimmar", "H", 1))
        v = self.q1("SELECT * FROM vendor_items")
        self.assertEqual((v["item_name"], v["npc_id"], v["price"]), ("Weak Flux", 20, 100))
        t = self.con.execute("SELECT kind, what FROM trainers ORDER BY kind").fetchall()
        self.assertEqual([tuple(r) for r in t], [("class", "ROGUE"), ("profession", "Engineering")])

    def test_items_and_rares(self):
        it = self.q1("SELECT * FROM items WHERE id=5001")
        self.assertEqual((it["inv_type"], it["item_class"], it["subclass"], it["req_level"]), (13, 2, 15, 4))
        self.assertEqual(it["stats"], "Agi 2, Sta 1")
        self.assertEqual(it["dps"], 4.5)
        self.assertEqual(it["new_in_forever"], 1)
        r = self.q1("SELECT * FROM rares WHERE id=300")
        self.assertEqual((r["name"], r["zones"], r["level_src"]), ("Big Boar", "Durotar", "forever"))
        self.assertIn("Small Black Pouch", r["loot"])

    def test_missing_files_are_empty_tables(self):
        self.assertEqual(self.q1("SELECT COUNT(*) FROM loot")[0], 0)
        self.assertEqual(self.counts["loot"], 0)

    def run_cli(self, *argv):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            query.main(["--db", str(self.db)] + list(argv))
        return buf.getvalue()

    def test_cli(self):
        out = self.run_cli("quest", "Boar Trouble")
        self.assertIn("XP: 460 [forever]", out)
        self.assertIn("ForeverDB.net", out)
        self.assertIn("Copper Vein", self.run_cli("nodes", "Copper Vein", "--zone", "Durotar", "--points"))
        self.assertIn("F(39.0,62.0)", self.run_cli("nodes", "Copper", "--points", "--source", "forever"))
        self.assertIn("Handful of Copper Bolts", self.run_cli("recipe", "engineering", "--max-skill", "50"))
        self.assertIn("Shop Keeper vende: Weak Flux 1s", self.run_cli("npc", "Shop Keeper"))
        out = self.run_cli("zone-quests", "Durotar", "--side", "h")
        self.assertIn("Boar Trouble", out)
        self.assertIn("Big Boar", self.run_cli("rares", "Durotar"))

    def test_money(self):
        self.assertEqual(query.money(12345), "1g 23s 45c")
        self.assertEqual(query.money(0), "0c")


if __name__ == "__main__":
    unittest.main()
