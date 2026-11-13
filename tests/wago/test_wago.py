"""Pruebas del adaptador de wago.tools. Sin red: las descargas se simulan.

Los CSV de tests/wago/fixtures/ estan hechos a mano con valores ficticios.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import sqlite3
import tempfile
import unittest
from pathlib import Path

from tools.wago import build_db, common, fetch, query

FIXTURES = Path(__file__).parent / "fixtures"
VERSION = "1.60.1.99999"


class FakeServer:
    """Sustituye a http_get: sirve los fixtures y responde 400 a tablas inexistentes."""

    def __init__(self):
        self.calls: list[str] = []

    def __call__(self, url: str):
        self.calls.append(url)
        if url.endswith("/api/builds/wowf/latest"):
            return 200, "application/json", json.dumps({"product": "wowf", "version": VERSION}).encode()
        table = url.split("/db2/")[1].split("/csv")[0]
        path = FIXTURES / f"{table}.csv"
        if not path.exists():
            raise fetch.FetchError('HTTP 400: {"errors":"Table not found."}', status=400)
        return 200, "text/csv", path.read_bytes()


class FakeClock:
    def __init__(self):
        self.now = 0.0
        self.sleeps: list[float] = []

    def clock(self):
        return self.now

    def sleep(self, s):
        self.sleeps.append(s)
        self.now += s


def quiet(_msg):
    pass


class TempDirTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        self.data_dir = self.tmp / "wago"
        self.db = self.data_dir / "forever.sqlite"

    def populate(self, tables=None):
        tables = tables or sorted(p.stem for p in FIXTURES.glob("*.csv"))
        clock = FakeClock()
        return fetch.fetch_tables(
            VERSION, tables, data_dir=self.data_dir, get=FakeServer(),
            throttle=fetch.Throttle(1.0, clock=clock.clock, sleep=clock.sleep), log=quiet,
        )


class TestParsing(unittest.TestCase):
    def test_parses_quoted_fields_and_newlines(self):
        header, rows = common.parse_csv_text((FIXTURES / "ItemSparse.csv").read_text())
        self.assertEqual(header[0], "ID")
        self.assertEqual(len(rows), 3)
        names = {r[0]: r[header.index("Display_lang")] for r in rows}
        self.assertEqual(names["101"], 'Test Dagger of Testing, "Quoted"')
        desc = {r[0]: r[header.index("Description_lang")] for r in rows}
        self.assertEqual(desc["102"], "Line one\nline two")

    def test_strips_bom(self):
        header, rows = common.parse_csv_text("\ufeffID,Name_lang\n1,A\n")
        self.assertEqual(header, ["ID", "Name_lang"])
        self.assertEqual(rows, [["1", "A"]])

    def test_rejects_html_json_and_empty(self):
        for bad in ("<!DOCTYPE html><html></html>", '{"errors":"Table not found."}', "   "):
            with self.assertRaises(ValueError):
                common.parse_csv_text(bad)

    def test_version_validation(self):
        self.assertTrue(common.valid_version("1.60.1.70938"))
        for bad in ("70938", "1.60.1", "1.60.1.70938; DROP", ""):
            self.assertFalse(common.valid_version(bad))

    def test_type_inference(self):
        header = ["a", "b", "c", "d"]
        rows = [["1", "0.5", "x", "007"], ["-2", "3", "y", "8"]]
        self.assertEqual(build_db.infer_types(header, rows), ["INTEGER", "REAL", "TEXT", "TEXT"])


class TestFetch(TempDirTest):
    def test_url_pins_exact_version_without_product(self):
        url = fetch.csv_url("SpellName", "1.60.1.70938")
        self.assertEqual(url, "https://wago.tools/db2/SpellName/csv?version=1.60.1.70938")
        self.assertNotIn("product", url)

    def test_resolve_latest(self):
        self.assertEqual(fetch.resolve_latest_version(get=FakeServer()), VERSION)

    def test_resolve_latest_rejects_wrong_product(self):
        def get(url):
            return 200, "application/json", b'{"product":"wow","version":"11.0.0.1"}'
        with self.assertRaises(fetch.FetchError):
            fetch.resolve_latest_version(get=get)

    def test_rejects_partial_version(self):
        with self.assertRaises(ValueError):
            fetch.fetch_tables("70938", ["SpellName"], data_dir=self.data_dir, get=FakeServer(), log=quiet)

    def test_manifest_and_missing_tables(self):
        manifest = self.populate(["SpellName", "ItemSparse", "NoSuchTable"])
        self.assertEqual(manifest["product"], "wowf")
        self.assertEqual(manifest["version"], VERSION)
        entry = manifest["tables"]["SpellName"]
        self.assertEqual(entry["rows"], 3)
        self.assertEqual(entry["url"], f"https://wago.tools/db2/SpellName/csv?version={VERSION}")
        expected_sha = hashlib.sha256((FIXTURES / "SpellName.csv").read_bytes()).hexdigest()
        self.assertEqual(entry["sha256"], expected_sha)
        self.assertRegex(entry["fetched_at"], r"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        self.assertIn("NoSuchTable", manifest["missing"])
        self.assertEqual(manifest["missing"]["NoSuchTable"]["status"], 400)
        on_disk = json.loads((self.data_dir / VERSION / "manifest.json").read_text())
        self.assertEqual(on_disk, manifest)
        self.assertTrue((self.data_dir / VERSION / "ItemSparse.csv").exists())

    def test_cache_skips_download(self):
        self.populate(["SpellName"])
        server = FakeServer()
        fetch.fetch_tables(VERSION, ["SpellName"], data_dir=self.data_dir, get=server, log=quiet)
        self.assertEqual(server.calls, [])

    def test_corrupted_cache_is_refetched(self):
        self.populate(["SpellName"])
        (self.data_dir / VERSION / "SpellName.csv").write_text("ID,Name_lang\n1,tampered\n")
        server = FakeServer()
        clock = FakeClock()
        fetch.fetch_tables(VERSION, ["SpellName"], data_dir=self.data_dir, get=server, log=quiet,
                           throttle=fetch.Throttle(1.0, clock=clock.clock, sleep=clock.sleep))
        self.assertEqual(len(server.calls), 1)

    def test_throttle_waits_between_requests(self):
        clock = FakeClock()
        fetch.fetch_tables(VERSION, ["SpellName", "Spell", "SkillLine"], data_dir=self.data_dir,
                           get=FakeServer(), log=quiet,
                           throttle=fetch.Throttle(1.0, clock=clock.clock, sleep=clock.sleep))
        self.assertEqual(clock.sleeps, [1.0, 1.0])

    def test_throttle_minimum_is_one_second(self):
        self.assertEqual(fetch.Throttle(0.1).delay, 1.0)

    def test_user_agent_has_no_email(self):
        self.assertNotIn("@", common.USER_AGENT)


class TestBuildDb(TempDirTest):
    def test_build_and_idempotency(self):
        self.populate()
        first = build_db.build(VERSION, self.data_dir, self.db, log=quiet)
        second = build_db.build(VERSION, self.data_dir, self.db, log=quiet)
        self.assertEqual(first, second)
        con = sqlite3.connect(self.db)
        self.assertEqual(con.execute("SELECT COUNT(*) FROM ItemSparse").fetchone()[0], 3)
        self.assertEqual(con.execute("SELECT COUNT(*) FROM Item").fetchone()[0], 4)
        meta = con.execute("SELECT product, version, caveat FROM meta WHERE table_name='ItemSparse'").fetchone()
        self.assertEqual(meta[:2], ("wowf", VERSION))
        self.assertIn("oculta", meta[2])
        self.assertEqual(con.execute("SELECT COUNT(*) FROM meta").fetchone()[0], len(first))
        cols = [r[1] for r in con.execute("PRAGMA table_info(ItemSparse)")]
        header, _ = common.parse_csv_text((FIXTURES / "ItemSparse.csv").read_text())
        self.assertEqual(cols, header)
        con.close()

    def test_rebuild_replaces_previous_version(self):
        self.populate()
        build_db.build(VERSION, self.data_dir, self.db, log=quiet)
        other = "1.60.1.100000"
        fetch.fetch_tables(other, ["SpellName"], data_dir=self.data_dir, get=FakeServer(), log=quiet,
                           throttle=fetch.Throttle(1.0, clock=FakeClock().clock, sleep=lambda s: None))
        build_db.build(other, self.data_dir, self.db, log=quiet)
        con = sqlite3.connect(self.db)
        tables = {r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        self.assertEqual(tables, {"meta", "SpellName"})
        self.assertEqual({r[0] for r in con.execute("SELECT version FROM meta")}, {other})
        con.close()
        self.assertEqual(build_db.latest_cached_version(self.data_dir), other)


class TestQuery(TempDirTest):
    def setUp(self):
        super().setUp()
        self.populate()
        build_db.build(VERSION, self.data_dir, self.db, log=quiet)

    def q(self, *argv):
        return query.run(list(argv), db_path=self.db)

    def test_item_by_name(self):
        out = self.q("item", "test dagger")
        self.assertIn("1 resultado(s)", out)  # coincidencia exacta gana a la parcial
        self.assertIn("Test Dagger (ID 100)", out)
        self.assertIn("Weapon / Daggers", out)
        self.assertIn("Calidad:         2 (Uncommon*)", out)
        self.assertIn("Nivel de objeto: 11", out)
        self.assertIn("Nivel requerido: 6", out)
        self.assertIn("13 (One-Hand*)", out)
        self.assertIn("Strength (bonusStat=4 pct=10000)", out)
        self.assertIn("Enum.BonusStatIndex", out)
        self.assertIn("Cantidades sin calcular", out)
        self.assertIn(f"build {VERSION}", out)
        self.assertIn("producto wowf", out)

    def test_bonus_stat_names_match_client_enum(self):
        # Valores comprobados en ItemConstantsDocumentation.lua (FDID 4637111, wowf 1.60.1.70938)
        self.assertEqual(len(query.BONUS_STAT_NAMES), 142)
        self.assertEqual(set(query.BONUS_STAT_NAMES), set(range(142)))
        expected = {0: "Mana", 3: "Agility", 4: "Strength", 5: "Intellect", 6: "Spirit", 7: "Stamina",
                    31: "HitRating", 32: "CritRating", 38: "AttackPower", 41: "SpellHealingDone",
                    42: "SpellDamageDone", 45: "SpellPower", 54: "ShadowResistance"}
        for k, v in expected.items():
            self.assertEqual(query.stat_name(k), v)
        self.assertEqual(query.stat_name(999), "desconocido (999)")
        self.assertEqual(query.BIND_NAMES[1], "OnAcquire")
        self.assertEqual(query.BIND_NAMES[2], "OnEquip")

    def test_item_partial_match(self):
        out = self.q("item", "Dagger")
        self.assertIn("2 resultado(s)", out)
        self.assertIn('Test Dagger of Testing, "Quoted" (ID 101)', out)

    def test_item_by_id_and_unknown_quality(self):
        out = self.q("item", "--id", "102")
        self.assertIn("Plain Cloth Robe", out)
        self.assertIn("Armor / Cloth", out)  # VerboseName vacio: usa DisplayName
        self.assertIn("99 (sin etiqueta)", out)

    def test_item_only_in_item_table(self):
        out = self.q("item", "--id", "200")
        self.assertIn("sin fila en ItemSparse", out)
        self.assertIn("Weapon / Daggers", out)

    def test_item_not_found(self):
        out = self.q("item", "Nonexistent Sword")
        self.assertIn("Sin resultados", out)
        self.assertIn("oculto", out)

    def test_spell_by_name(self):
        out = self.q("spell", "Test Strike")
        self.assertIn("2 resultado(s)", out)
        self.assertIn("Test Strike (ID 10) [Rank 1]", out)
        self.assertIn("Testing (SkillLine 38)", out)
        self.assertIn("SupercedesSpell=10", out)
        self.assertIn("SchoolMask=1", out)

    def test_spell_by_id_without_skill_line(self):
        out = self.q("spell", "--id", "12")
        self.assertIn("Other Spell (ID 12)", out)
        self.assertIn("ninguna en SkillLineAbility", out)

    def test_missing_db(self):
        with self.assertRaises(query.QueryError):
            query.run(["item", "x"], db_path=self.tmp / "nope.sqlite")


if __name__ == "__main__":
    unittest.main()
