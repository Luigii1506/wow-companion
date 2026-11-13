"""Pruebas del adaptador de ForeverDB. Sin red y sin clave real: HTTP simulado.

Las respuestas son ficticias y solo imitan la forma documentada {data, meta}.
"""

from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from tools.foreverdb import client as fdb
from tools.foreverdb import common, export, query

FAKE_KEY = "fdb_test_not_a_real_key"
BUILD = "1.60.1.99999"


class FakeTime:
    def __init__(self):
        self.mono = 0.0
        self.wall = datetime(2026, 11, 13, 12, 0, tzinfo=timezone.utc)
        self.sleeps: list[float] = []

    def clock(self):
        return self.mono

    def now(self):
        return self.wall

    def sleep(self, s):
        self.sleeps.append(s)
        self.mono += s
        self.wall += timedelta(seconds=s)


class FakeTransport:
    """Cola de respuestas; si se vacia, responde 200 con un objeto ficticio."""

    def __init__(self, responses=None):
        self.responses = list(responses or [])
        self.calls: list[tuple[str, dict]] = []

    def __call__(self, url, headers, timeout=30.0):
        self.calls.append((url, dict(headers)))
        if self.responses:
            r = self.responses.pop(0)
            return r if not callable(r) else r(url)
        return ok({"id": 1, "name": "Test"})


def ok(data, **meta):
    meta.setdefault("build", BUILD)
    return 200, {"content-type": "application/json"}, json.dumps({"data": data, "meta": meta}).encode()


def err(status, body, headers=None):
    return status, headers or {}, json.dumps(body).encode() if not isinstance(body, bytes) else body


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        self.t = FakeTime()

    def make(self, responses=None, api_key=FAKE_KEY, max_per_day=common.MAX_PER_DAY, env=None):
        transport = FakeTransport(responses)
        c = fdb.ForeverDBClient(
            api_key=api_key,
            transport=transport,
            cache=fdb.DiskCache(self.tmp / "cache", now=self.t.now),
            limiter=fdb.RateLimiter(clock=self.t.clock, sleep=self.t.sleep),
            counter=fdb.DailyCounter(self.tmp / "usage.json", max_per_day=max_per_day, now=self.t.now),
            sleep=self.t.sleep,
            now=self.t.now,
            env=env if env is not None else {},
            env_file=self.tmp / ".env",
        )
        return c, transport


class TestKey(Base):
    def test_env_var_wins(self):
        (self.tmp / ".env").write_text("FOREVERDB_API_KEY=fdb_from_file\n")
        self.assertEqual(fdb.load_api_key({"FOREVERDB_API_KEY": "fdb_env"}, self.tmp / ".env"), "fdb_env")

    def test_env_file_parsing(self):
        (self.tmp / ".env").write_text(
            "# comentario\nOTHER=1\nexport FOREVERDB_API_KEY=\"fdb_quoted\"\n")
        self.assertEqual(fdb.load_api_key({}, self.tmp / ".env"), "fdb_quoted")
        (self.tmp / ".env").write_text("FOREVERDB_API_KEY=fdb_x # nota\n")
        self.assertEqual(fdb.load_api_key({}, self.tmp / ".env"), "fdb_x")

    def test_missing_key_message(self):
        (self.tmp / ".env").write_text("FOREVERDB_API_KEY=\n")
        with self.assertRaises(fdb.MissingKeyError) as cm:
            fdb.load_api_key({}, self.tmp / ".env")
        msg = str(cm.exception)
        self.assertIn("FOREVERDB_API_KEY", msg)
        self.assertIn(".env", msg)

    def test_missing_key_on_network_call_sends_nothing(self):
        c, transport = self.make(api_key=None)
        with self.assertRaises(fdb.MissingKeyError):
            c.get("/meta")
        self.assertEqual(transport.calls, [])

    def test_cache_hit_needs_no_key(self):
        c, _ = self.make()
        c.get("/meta")
        c2, transport2 = self.make(api_key=None)
        self.assertTrue(c2.get("/meta")["from_cache"])
        self.assertEqual(transport2.calls, [])

    def test_repr_hides_key(self):
        c, _ = self.make()
        self.assertNotIn(FAKE_KEY, repr(c))


class TestRequest(Base):
    def test_auth_header_and_user_agent(self):
        c, transport = self.make()
        c.get("/items/4947")
        url, headers = transport.calls[0]
        self.assertEqual(url, "https://foreverdb.net/api/v1/items/4947")
        self.assertEqual(headers["X-API-Key"], FAKE_KEY)
        self.assertEqual(headers["User-Agent"], common.USER_AGENT)
        self.assertIn("wow-companion", headers["User-Agent"])
        self.assertNotIn("Python-urllib", headers["User-Agent"])
        self.assertNotIn("@", headers["User-Agent"])

    def test_params_encoded_and_none_dropped(self):
        c, transport = self.make()
        c.get("/quests", {"zone": "Durotar", "side": "horde", "minLevel": 10, "q": None})
        self.assertEqual(transport.calls[0][0],
                         "https://foreverdb.net/api/v1/quests?zone=Durotar&side=horde&minLevel=10")

    def test_response_fields(self):
        c, _ = self.make([ok({"id": 4947, "name": "Jagged Dagger"})])
        r = c.get("/items/4947")
        self.assertEqual(r["data"]["name"], "Jagged Dagger")
        self.assertEqual(r["build"], BUILD)
        self.assertEqual(r["fetched_at"], "2026-11-13T12:00:00Z")
        self.assertFalse(r["from_cache"])

    def test_non_json_rejected(self):
        c, _ = self.make([(200, {}, b"<html>")])
        with self.assertRaises(fdb.ForeverDBError):
            c.get("/meta")


class TestErrors(Base):
    def test_429_honors_retry_after(self):
        c, transport = self.make([err(429, {"error": "rate_limited"}, {"retry-after": "7"}), ok([])])
        r = c.get("/items", {"q": "x"})
        self.assertEqual(r["data"], [])
        self.assertIn(7.0, self.t.sleeps)
        self.assertEqual(len(transport.calls), 2)

    def test_429_http_date(self):
        when = self.t.wall + timedelta(seconds=30)
        from email.utils import format_datetime
        c, _ = self.make([err(429, {}, {"retry-after": format_datetime(when, usegmt=True)}), ok([])])
        c.get("/items")
        self.assertAlmostEqual(self.t.sleeps[0], 30.0, delta=1)

    def test_429_gives_up_after_retries(self):
        c, transport = self.make([err(429, {}, {"retry-after": "1"})] * 5)
        with self.assertRaises(fdb.RateLimitError):
            c.get("/items")
        self.assertEqual(len(transport.calls), 3)

    def test_429_long_wait_not_blocking(self):
        c, transport = self.make([err(429, {}, {"retry-after": "86400"})])
        with self.assertRaises(fdb.RateLimitError) as cm:
            c.get("/items")
        self.assertEqual(self.t.sleeps, [])
        self.assertIn("86400", str(cm.exception))

    def test_402_subscription_required(self):
        c, _ = self.make([err(402, {"error": "subscription_required"})])
        with self.assertRaises(fdb.SubscriptionRequiredError) as cm:
            c.get("/posts")
        self.assertIn("subscription_required", str(cm.exception))

    def test_403_forbidden(self):
        c, _ = self.make([err(403, {"error": "invalid key " + FAKE_KEY})])
        with self.assertRaises(fdb.ForbiddenError) as cm:
            c.get("/meta")
        self.assertIn("403", str(cm.exception))
        self.assertNotIn(FAKE_KEY, str(cm.exception))

    def test_403_cloudflare_1010(self):
        c, _ = self.make([err(403, b"error code: 1010")])
        with self.assertRaises(fdb.ForbiddenError) as cm:
            c.get("/meta")
        self.assertIn("User-Agent", str(cm.exception))

    def test_401_and_404(self):
        c, _ = self.make([err(401, {"error": "unauthorized"}), err(404, {"error": "not_found"})])
        with self.assertRaises(fdb.AuthError):
            c.get("/meta")
        with self.assertRaises(fdb.NotFoundError):
            c.get("/items/1")

    def test_errors_not_cached(self):
        c, transport = self.make([err(500, {"error": "boom"}), ok({"id": 1})])
        with self.assertRaises(fdb.ForeverDBError):
            c.get("/items/1")
        self.assertEqual(c.get("/items/1")["data"], {"id": 1})
        self.assertEqual(len(transport.calls), 2)


class TestLimits(Base):
    def test_throttle_25_per_minute(self):
        limiter = fdb.RateLimiter(clock=self.t.clock, sleep=self.t.sleep)
        for _ in range(25):
            limiter.wait()
        self.assertEqual(self.t.sleeps, [])
        limiter.wait()
        self.assertEqual(len(self.t.sleeps), 1)
        self.assertAlmostEqual(self.t.sleeps[0], 60.0)

    def test_throttle_never_exceeds_window(self):
        limiter = fdb.RateLimiter(clock=self.t.clock, sleep=self.t.sleep)
        stamps = []
        for _ in range(80):
            limiter.wait()
            stamps.append(self.t.mono)
            self.t.mono += 0.5
        for i in range(len(stamps)):
            in_window = [s for s in stamps if stamps[i] <= s < stamps[i] + 60]
            self.assertLessEqual(len(in_window), 25)

    def test_client_uses_throttle(self):
        c, _ = self.make()
        for i in range(26):
            c.get(f"/items/{i}")
        self.assertEqual(len(self.t.sleeps), 1)

    def test_daily_cap(self):
        c, transport = self.make(max_per_day=3)
        for i in range(3):
            c.get(f"/items/{i}")
        with self.assertRaises(fdb.DailyLimitError):
            c.get("/items/99")
        self.assertEqual(len(transport.calls), 3)
        usage = json.loads((self.tmp / "usage.json").read_text())
        self.assertEqual(usage, {"date": "2026-11-13", "count": 3})
        # Las respuestas en cache no gastan cupo.
        self.assertTrue(c.get("/items/1")["from_cache"])

    def test_daily_cap_default_and_reset(self):
        self.assertEqual(common.MAX_PER_DAY, 4500)
        (self.tmp / "usage.json").write_text(json.dumps({"date": "2026-11-13", "count": 4500}))
        c, _ = self.make()
        with self.assertRaises(fdb.DailyLimitError):
            c.get("/meta")
        self.t.wall += timedelta(days=1)
        c.get("/meta")
        self.assertEqual(json.loads((self.tmp / "usage.json").read_text())["count"], 1)

    def test_retries_count_against_daily_cap(self):
        c, _ = self.make([err(429, {}, {"retry-after": "1"}), ok([])])
        c.get("/items")
        self.assertEqual(json.loads((self.tmp / "usage.json").read_text())["count"], 2)


class TestCache(Base):
    def test_hit_and_miss(self):
        c, transport = self.make()
        self.assertFalse(c.get("/items", {"q": "a"})["from_cache"])
        self.assertTrue(c.get("/items", {"q": "a"})["from_cache"])
        self.assertFalse(c.get("/items", {"q": "b"})["from_cache"])
        self.assertEqual(len(transport.calls), 2)

    def test_param_order_irrelevant(self):
        c, transport = self.make()
        c.get("/quests", {"zone": "Durotar", "side": "horde"})
        self.assertTrue(c.get("/quests", {"side": "horde", "zone": "Durotar"})["from_cache"])

    def test_ttl_expiry(self):
        c, transport = self.make()
        c.get("/meta")
        self.t.wall += timedelta(days=6, hours=23)
        self.assertTrue(c.get("/meta")["from_cache"])
        self.t.wall += timedelta(hours=2)
        self.assertFalse(c.get("/meta")["from_cache"])
        self.assertEqual(len(transport.calls), 2)

    def test_refresh_bypasses(self):
        c, transport = self.make()
        c.get("/meta")
        self.assertFalse(c.get("/meta", refresh=True)["from_cache"])
        self.assertEqual(len(transport.calls), 2)

    def test_cache_file_contents_without_key(self):
        c, _ = self.make()
        c.get("/items/4947")
        files = list((self.tmp / "cache").glob("*.json"))
        self.assertEqual(len(files), 1)
        entry = json.loads(files[0].read_text())
        self.assertEqual(entry["fetched_at"], "2026-11-13T12:00:00Z")
        self.assertEqual(entry["build"], BUILD)
        self.assertEqual(entry["endpoint"], "/items/4947")
        self.assertNotIn(FAKE_KEY, files[0].read_text())

    def test_build_field_variants(self):
        self.assertEqual(fdb.extract_build({"gameBuild": "1.2.3.4"}), "1.2.3.4")
        self.assertEqual(fdb.extract_build({"build": {"version": "5"}}), "5")
        self.assertIsNone(fdb.extract_build({}))


class TestPagination(Base):
    def test_paginates_until_total(self):
        pages = [ok([{"id": i} for i in range(100)], total=230),
                 ok([{"id": i} for i in range(100, 200)], total=230),
                 ok([{"id": i} for i in range(200, 230)], total=230)]
        c, transport = self.make(pages)
        r = fdb.collect(c, "/items", {"q": "x"}, max_items=500)
        self.assertEqual(len(r["data"]), 230)
        self.assertEqual(r["pages"], 3)
        urls = [u for u, _ in transport.calls]
        self.assertIn("limit=100&offset=0", urls[0])
        self.assertIn("limit=100&offset=100", urls[1])
        self.assertIn("limit=100&offset=200", urls[2])

    def test_respects_max_items(self):
        c, transport = self.make([ok([{"id": i} for i in range(100)], total=1000),
                                  ok([{"id": i} for i in range(50)], total=1000)])
        r = fdb.collect(c, "/items", max_items=150)
        self.assertEqual(len(r["data"]), 150)
        self.assertIn("limit=50&offset=100", transport.calls[1][0])

    def test_stops_on_short_page_without_total(self):
        c, transport = self.make([ok([{"id": 1}, {"id": 2}])])
        r = fdb.collect(c, "/zones", max_items=100, )
        self.assertEqual(len(r["data"]), 2)
        self.assertEqual(len(transport.calls), 1)


class TestQueryCli(Base):
    def run_cli(self, argv, responses=None):
        c, transport = self.make(responses)
        return query.run(argv, client=c), transport

    def test_item_by_id(self):
        out, t = self.run_cli(["item", "4947"], [ok({"id": 4947, "name": "Jagged Dagger", "quality": 1})])
        self.assertEqual(t.calls[0][0], "https://foreverdb.net/api/v1/items/4947")
        self.assertIn("Jagged Dagger", out)

    def test_item_search(self):
        _, t = self.run_cli(["item", "--q", "Jagged Dagger"], [ok([])])
        self.assertEqual(t.calls[0][0], "https://foreverdb.net/api/v1/items?q=Jagged+Dagger")

    def test_quests_filters(self):
        _, t = self.run_cli(["quests", "--zone", "Durotar", "--side", "horde", "--min", "10", "--max", "20"],
                            [ok([])])
        self.assertEqual(t.calls[0][0], "https://foreverdb.net/api/v1/quests?"
                                        "zone=Durotar&side=horde&minLevel=10&maxLevel=20")

    def test_other_commands(self):
        cases = [
            (["meta"], "/meta"),
            (["vendor", "--q", "Wuark"], "/vendors?q=Wuark"),
            (["gathering", "mining", "--zone", "Durotar"], "/gathering/mining?zone=Durotar"),
            (["changes", "--kind", "quest", "--verified", "1"], "/changes-seen?kind=quest&verified=1"),
            (["profession", "engineering"], "/professions/engineering"),
            (["get", "/dungeons", "limit=10"], "/dungeons?limit=10"),
        ]
        for argv, path in cases:
            _, t = self.run_cli(argv, [ok([])])
            self.assertEqual(t.calls[0][0], "https://foreverdb.net/api/v1" + path, argv)

    def test_path_segments_escaped(self):
        _, t = self.run_cli(["item", "../meta"], [ok({})])
        self.assertEqual(t.calls[0][0], "https://foreverdb.net/api/v1/items/..%2Fmeta")

    def test_output_ends_with_build_and_credit(self):
        for argv, resp in ((["item", "4947"], ok({"id": 4947, "name": "Jagged Dagger"})),
                           (["item", "--q", "zzz"], ok([])),
                           (["item", "--q", "x", "--json"], ok([{"id": 1, "name": "A"}]))):
            out, _ = self.run_cli(argv, [resp])
            lines = out.rstrip("\n").splitlines()
            self.assertEqual(lines[-1], "Data from ForeverDB.net (https://foreverdb.net)")
            self.assertEqual(lines[-2], f"Build: {BUILD}")

    def test_table_render(self):
        out, _ = self.run_cli(["item", "--q", "x"], [ok([{"id": 1, "name": "A|B", "quality": 2},
                                                         {"id": 2, "name": "C", "quality": 1}])])
        self.assertIn("2 resultado(s)", out)
        self.assertIn("id", out.splitlines()[2])


class TestExport(Base):
    def test_markdown_snippet(self):
        c, _ = self.make([ok([{"id": 4947, "name": "Jagged | Dagger"}])])
        resp = c.get("/items", {"q": "Jagged Dagger"})
        md = export.render_markdown(resp)
        self.assertIn("| id | name |", md)
        self.assertIn("Jagged \\| Dagger", md)
        self.assertIn("## Fuentes", md)
        self.assertIn("[Data from ForeverDB.net](https://foreverdb.net)", md)
        self.assertIn("https://foreverdb.net/api/v1/items?q=Jagged+Dagger", md)
        self.assertIn(BUILD, md)
        self.assertIn("2026-11-13", md)
        self.assertNotIn(FAKE_KEY, md)

    def test_md_flag_in_query(self):
        c, _ = self.make([ok({"id": 1, "name": "A"})])
        md = query.run(["item", "1", "--md"], client=c)
        self.assertIn("## Fuentes", md)
        self.assertIn("[Data from ForeverDB.net](https://foreverdb.net)", md)

    def test_empty_result(self):
        c, _ = self.make([ok([])])
        md = export.render_markdown(c.get("/items", {"q": "zzz"}))
        self.assertIn("Sin resultados", md)
        self.assertIn("## Fuentes", md)


class TestRepoHygiene(unittest.TestCase):
    def test_gitignore_covers_key_and_data(self):
        lines = (common.REPO_ROOT / ".gitignore").read_text().splitlines()
        self.assertIn(".env", lines)
        self.assertIn("data/foreverdb/", lines)

    def test_env_example_has_no_value(self):
        text = (common.REPO_ROOT / ".env.example").read_text()
        self.assertIn("FOREVERDB_API_KEY=", text)
        self.assertEqual(fdb.parse_env_file(common.REPO_ROOT / ".env.example").get("FOREVERDB_API_KEY"), "")


if __name__ == "__main__":
    unittest.main()
