"""Consulta la API de ForeverDB desde la terminal (con cache local de 7 dias).

Uso:
    python3 -m tools.foreverdb.query meta
    python3 -m tools.foreverdb.query item 4947
    python3 -m tools.foreverdb.query item --q "Jagged Dagger"
    python3 -m tools.foreverdb.query quests --zone Durotar --side horde --min 10 --max 20
    python3 -m tools.foreverdb.query vendor --q "Wuark"
    python3 -m tools.foreverdb.query gathering mining --zone Durotar
    python3 -m tools.foreverdb.query changes --kind quest --verified 1
    python3 -m tools.foreverdb.query profession engineering
    python3 -m tools.foreverdb.query get /dungeons limit=10     # cualquier otro endpoint

Opciones comunes: --refresh (ignora la cache), --limit, --offset, --all N (pagina hasta N
filas), --json (respuesta en bruto), --md (fragmento markdown para una nota).
La salida siempre termina con la build y el credito obligatorio a ForeverDB.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse

from .client import ForeverDBClient, ForeverDBError, collect
from .common import CREDIT_LINE, GATHERING_SLUGS

PREFERRED_COLUMNS = [
    "id", "name", "title", "slug", "quality", "level", "itemLevel", "requiredLevel",
    "minLevel", "maxLevel", "side", "zone", "class", "slot", "kind", "verified", "skill",
]
MAX_COLUMNS = 7
MAX_CELL = 60


def _seg(value) -> str:
    return urllib.parse.quote(str(value), safe="")


# ---------------------------------------------------------------- render

def _scalar(v) -> bool:
    return v is None or isinstance(v, (str, int, float, bool))


def _cell(v) -> str:
    if v is None:
        return ""
    if isinstance(v, dict):
        for k in ("name", "title", "slug", "id"):
            if k in v and _scalar(v[k]):
                return _cell(v[k])
    s = v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
    s = " ".join(str(s).split())
    return s if len(s) <= MAX_CELL else s[: MAX_CELL - 1] + "…"


def pick_columns(rows: list[dict]) -> list[str]:
    keys: list[str] = []
    for r in rows:
        for k in r:
            if k not in keys:
                keys.append(k)
    cols = [k for k in PREFERRED_COLUMNS if k in keys]
    for k in keys:
        if len(cols) >= MAX_COLUMNS:
            break
        if k not in cols and all(_scalar(r.get(k)) or isinstance(r.get(k), dict) for r in rows):
            cols.append(k)
    return cols[:MAX_COLUMNS]


def render_table(rows: list[dict], columns: list[str] | None = None) -> str:
    columns = columns or pick_columns(rows)
    table = [[str(c) for c in columns]] + [[_cell(r.get(c)) for c in columns] for r in rows]
    widths = [max(len(row[i]) for row in table) for i in range(len(columns))]
    lines = ["  ".join(cell.ljust(widths[i]) for i, cell in enumerate(row)).rstrip() for row in table]
    lines.insert(1, "  ".join("-" * w for w in widths))
    return "\n".join(lines)


def render_record(record: dict, indent: str = "") -> str:
    out = []
    for k, v in record.items():
        if _scalar(v):
            out.append(f"{indent}{k}: {'' if v is None else v}")
        elif isinstance(v, list) and v and all(isinstance(x, dict) for x in v):
            out.append(f"{indent}{k}: ({len(v)})")
            out.append("\n".join(indent + "  " + line for line in render_table(v).splitlines()))
        else:
            out.append(f"{indent}{k}: {json.dumps(v, ensure_ascii=False)}")
    return "\n".join(out)


def render_data(data) -> str:
    if isinstance(data, list):
        if not data:
            return "Sin resultados."
        if all(isinstance(r, dict) for r in data):
            return f"{len(data)} resultado(s):\n\n" + render_table(data)
        return "\n".join(_cell(x) for x in data)
    if isinstance(data, dict):
        return render_record(data)
    return str(data)


def footer(resp: dict) -> str:
    meta = resp.get("meta") or {}
    origin = "cache local" if resp.get("from_cache") else "red"
    lines = ["---", f"URL: {resp['url']}"]
    total = meta.get("total") if isinstance(meta, dict) else None
    if total is not None:
        lines.append(f"Total en ForeverDB: {total}")
    lines += [
        f"Obtenido (UTC): {resp['fetched_at']} ({origin}). No es estado en tiempo real.",
        "Confianza: datos de una base de datos comunitaria de WoW Forever (conocimiento externo); "
        "no es estado del personaje.",
        f"Build: {resp.get('build') or 'desconocida (meta sin build)'}",
        CREDIT_LINE,
    ]
    return "\n".join(lines)


def render_response(resp: dict) -> str:
    return render_data(resp["data"]) + "\n" + footer(resp)


# ---------------------------------------------------------------- CLI

def _parse_kv(pairs: list[str]) -> dict:
    out = {}
    for p in pairs:
        if "=" not in p:
            raise SystemExit(f"parametro no valido (usa clave=valor): {p}")
        k, v = p.split("=", 1)
        out[k] = v
    return out


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="python3 -m tools.foreverdb.query", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--refresh", action="store_true", help="ignora la cache y consulta la API")
    common.add_argument("--limit", type=int, help="filas por pagina (1-100)")
    common.add_argument("--offset", type=int)
    common.add_argument("--all", type=int, metavar="N", help="pagina hasta N filas (una peticion por pagina)")
    out = common.add_mutually_exclusive_group()
    out.add_argument("--json", action="store_true", help="imprime la respuesta en bruto")
    out.add_argument("--md", action="store_true", help="fragmento markdown para una nota")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("meta", parents=[common])

    sp = sub.add_parser("item", parents=[common])
    sp.add_argument("id", nargs="?")
    sp.add_argument("--q")
    sp.add_argument("--quality")
    sp.add_argument("--class", dest="item_class")
    sp.add_argument("--slot")
    sp.add_argument("--min", dest="min_level", type=int)
    sp.add_argument("--max", dest="max_level", type=int)

    sp = sub.add_parser("spell", parents=[common])
    sp.add_argument("id", nargs="?")
    sp.add_argument("--q")

    sp = sub.add_parser("quests", aliases=["quest"], parents=[common])
    sp.add_argument("id", nargs="?")
    sp.add_argument("--q")
    sp.add_argument("--zone")
    sp.add_argument("--side", choices=["horde", "alliance"])
    sp.add_argument("--min", dest="min_level", type=int)
    sp.add_argument("--max", dest="max_level", type=int)

    sp = sub.add_parser("vendor", aliases=["vendors"], parents=[common])
    sp.add_argument("id", nargs="?")
    sp.add_argument("--q")
    sp.add_argument("--zone")
    sp.add_argument("--seen")

    sp = sub.add_parser("gathering", parents=[common])
    sp.add_argument("slug", choices=GATHERING_SLUGS)
    sp.add_argument("--zone")

    sp = sub.add_parser("changes", parents=[common])
    sp.add_argument("--kind")
    sp.add_argument("--verified")

    sp = sub.add_parser("profession", aliases=["professions"], parents=[common])
    sp.add_argument("slug", nargs="?")
    sp.add_argument("--q")
    sp.add_argument("--new", action="store_true")
    sp.add_argument("--changed", action="store_true")

    sp = sub.add_parser("get", parents=[common], help="cualquier endpoint: get /dungeons zone=X")
    sp.add_argument("endpoint")
    sp.add_argument("params", nargs="*", help="clave=valor")
    return p


def request_for(args) -> tuple[str, dict, bool]:
    """Traduce los argumentos a (endpoint, parametros, es_lista)."""
    cmd = args.cmd
    if cmd == "meta":
        return "/meta", {}, False
    if cmd == "item":
        if args.id:
            return f"/items/{_seg(args.id)}", {}, False
        return "/items", {"q": args.q, "quality": args.quality, "class": args.item_class, "slot": args.slot,
                          "minLevel": args.min_level, "maxLevel": args.max_level}, True
    if cmd == "spell":
        if args.id:
            return f"/spells/{_seg(args.id)}", {}, False
        return "/spells", {"q": args.q}, True
    if cmd in ("quests", "quest"):
        if args.id:
            return f"/quests/{_seg(args.id)}", {}, False
        return "/quests", {"q": args.q, "zone": args.zone, "side": args.side,
                           "minLevel": args.min_level, "maxLevel": args.max_level}, True
    if cmd in ("vendor", "vendors"):
        if args.id:
            return f"/vendors/{_seg(args.id)}", {}, False
        return "/vendors", {"q": args.q, "zone": args.zone, "seen": args.seen}, True
    if cmd == "gathering":
        return f"/gathering/{_seg(args.slug)}", {"zone": args.zone}, True
    if cmd == "changes":
        return "/changes-seen", {"kind": args.kind, "verified": args.verified}, True
    if cmd in ("profession", "professions"):
        endpoint = f"/professions/{_seg(args.slug)}" if args.slug else "/professions"
        return endpoint, {"q": args.q, "new": "1" if args.new else None,
                          "changed": "1" if args.changed else None}, not args.slug
    if cmd == "get":
        endpoint = "/" + "/".join(_seg(s) for s in args.endpoint.strip("/").split("/") if s)
        return endpoint, _parse_kv(args.params), True
    raise SystemExit(f"comando desconocido: {cmd}")


def run(argv: list[str] | None = None, client: ForeverDBClient | None = None) -> str:
    args = build_parser().parse_args(argv)
    endpoint, params, is_list = request_for(args)
    if args.limit is not None:
        if not 1 <= args.limit <= 100:
            raise SystemExit("--limit debe estar entre 1 y 100")
        params["limit"] = args.limit
    if args.offset is not None:
        params["offset"] = args.offset
    client = client or ForeverDBClient()
    if args.all and is_list:
        resp = collect(client, endpoint, params, max_items=args.all, refresh=args.refresh)
    else:
        resp = client.get(endpoint, params, refresh=args.refresh)
    if args.md:
        from .export import render_markdown
        return render_markdown(resp)
    if args.json:
        raw = json.dumps({"data": resp["data"], "meta": resp["meta"]}, indent=2, ensure_ascii=False)
        return raw + "\n" + footer(resp)
    return render_response(resp)


def main(argv: list[str] | None = None) -> int:
    try:
        print(run(argv))
    except ForeverDBError as e:
        print(str(e), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
