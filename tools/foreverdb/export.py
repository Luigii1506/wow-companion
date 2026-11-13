"""Genera un fragmento markdown con datos de ForeverDB para pegar en una nota de la boveda.

No escribe en ninguna nota: imprime el texto y la persona decide donde va.
El fragmento incluye siempre `## Fuentes` con el enlace visible obligatorio
[Data from ForeverDB.net](https://foreverdb.net) y la URL exacta consultada.

Uso (mismos argumentos que query):
    python3 -m tools.foreverdb.export item --q "Jagged Dagger"
    python3 -m tools.foreverdb.export gathering mining --zone Durotar
"""

from __future__ import annotations

import sys

from .client import ForeverDBError
from .common import CREDIT_MD
from .query import _cell, pick_columns


def _md_cell(v) -> str:
    return _cell(v).replace("\\", "\\\\").replace("|", "\\|")


def markdown_table(rows: list[dict], columns: list[str] | None = None) -> str:
    columns = columns or pick_columns(rows)
    lines = ["| " + " | ".join(_md_cell(c) for c in columns) + " |",
             "|" + "|".join("---" for _ in columns) + "|"]
    for r in rows:
        lines.append("| " + " | ".join(_md_cell(r.get(c)) for c in columns) + " |")
    return "\n".join(lines)


def sources_section(resp: dict) -> str:
    date = (resp.get("fetched_at") or "")[:10]
    build = resp.get("build") or "desconocida"
    return (
        "## Fuentes\n\n"
        f"- {CREDIT_MD} — API `{resp['url']}` (build {build}, consultado {date}; "
        "conocimiento externo, no estado del personaje)."
    )


def render_markdown(resp: dict, columns: list[str] | None = None, title: str | None = None) -> str:
    data = resp["data"]
    parts = []
    if title:
        parts.append(f"## {title}")
    if isinstance(data, dict):
        data = [data]
    if isinstance(data, list) and data and all(isinstance(r, dict) for r in data):
        parts.append(markdown_table(data, columns))
    elif isinstance(data, list) and not data:
        parts.append("_Sin resultados en ForeverDB para esta consulta._")
    else:
        parts.append(_md_cell(data))
    parts.append(sources_section(resp))
    return "\n\n".join(parts) + "\n"


def main(argv: list[str] | None = None) -> int:
    from .query import run
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--md" not in argv:
        argv.append("--md")
    try:
        print(run(argv), end="")
    except ForeverDBError as e:
        print(str(e), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
