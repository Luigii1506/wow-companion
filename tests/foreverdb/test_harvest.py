import json
import tempfile
import unittest
from pathlib import Path

from tools.foreverdb.harvest import Budget, Harvester, strip_markers


class FakeClient:
    def __init__(self, pages):
        self.pages = pages
        self.network_calls = 0
        self.calls = []

    def get(self, endpoint, params=None):
        self.network_calls += 1
        self.calls.append((endpoint, dict(params or {})))
        data, meta = self.pages(endpoint, params or {})
        return {"endpoint": endpoint, "params": params or {}, "url": "u", "fetched_at": "t",
                "build": "b", "data": data, "meta": meta}


def pages(endpoint, params):
    off = int(params.get("offset", 0))
    rows = [{"id": i} for i in range(off, min(off + 100, 250))]
    return rows, {"total": 250}


class HarvestTest(unittest.TestCase):
    def test_strip_markers(self):
        self.assertEqual(strip_markers({"a": ["x⁣​y‌"]}), {"a": ["xy"]})

    def test_paged_and_resume(self):
        with tempfile.TemporaryDirectory() as d:
            c = FakeClient(pages)
            h = Harvester(c, budget=10, store=Path(d))
            rows = h.paged("quests", "/quests")
            self.assertEqual(len(rows), 250)
            self.assertEqual(c.network_calls, 3)
            h2 = Harvester(c, budget=10, store=Path(d))
            h2.paged("quests", "/quests")
            self.assertEqual(c.network_calls, 3)  # todo desde el almacen
            saved = json.loads((Path(d) / "quests" / "page-000000.json").read_text())
            self.assertEqual(saved["meta"]["total"], 250)

    def test_budget_stops(self):
        with tempfile.TemporaryDirectory() as d:
            h = Harvester(FakeClient(pages), budget=2, store=Path(d))
            with self.assertRaises(Budget):
                h.paged("quests", "/quests")
            self.assertEqual(len(list((Path(d) / "quests").glob("*.json"))), 2)


if __name__ == "__main__":
    unittest.main()
