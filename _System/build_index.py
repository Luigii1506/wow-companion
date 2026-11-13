#!/usr/bin/env python3
"""Regenera los índices de la bóveda y el catálogo de guías.

Uso: python3 _System/build_index.py   (desde la raíz de la bóveda)

- Rellena la sección entre <!-- index:start --> y <!-- index:end --> de cada
  índice de área con una línea por nota: enlace, tipo, nivel, estado y la
  primera viñeta de su "## Resumen".
- Genera 07-Research/Guide-Catalog.md a partir de _System/catalog/*-urls.txt,
  marcando como ingerida cada URL que ya tenga ficha src-<sitio>-<slug>.md.
Solo usa la biblioteca estándar.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MOCS = {
    "02-Classes": "02-Classes/Classes.md",
    "03-Professions": "03-Professions/Professions.md",
    "04-Economy": "04-Economy/Economy.md",
    "05-World": "05-World/World.md",
    "06-Items": "06-Items/Items.md",
    "09-Systems": "09-Systems/Systems.md",
    "10-Tips": "10-Tips/Tips.md",
}
START, END = "<!-- index:start -->", "<!-- index:end -->"
STATUS_ICON = {
    "confirmed_forever": "✅",
    "probable_classic": "🟦",
    "conflicting": "⚠️",
    "unknown": "❔",
}


def frontmatter(text: str) -> dict[str, str]:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    data = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if km:
            data[km.group(1)] = km.group(2).strip().strip('"')
    return data


def first_summary_bullet(text: str) -> str:
    m = re.search(r"^## Resumen\s*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    if not m:
        return ""
    for line in m.group(1).splitlines():
        line = line.strip()
        if line.startswith(("- ", "* ")) and len(line) > 2:
            line = re.sub(r"\[\[([^]|]+\|)?([^]]+)\]\]", r"\2", line[2:])
            line = line.replace("**", "")
            return (line[:140] + "…") if len(line) > 140 else line
    return ""


def build_moc(folder: str, moc_rel: str) -> int:
    moc = ROOT / moc_rel
    if not moc.exists():
        return 0
    rows = []
    for path in sorted((ROOT / folder).rglob("*.md")):
        if path == moc:
            continue
        text = path.read_text(encoding="utf-8")
        fm = frontmatter(text)
        if fm.get("type") in ("moc", "source-digest"):
            continue
        sub = path.parent.relative_to(ROOT / folder).as_posix()
        lvl = ""
        if fm.get("level_min") or fm.get("level_max"):
            lvl = f" · nv {fm.get('level_min', '?')}–{fm.get('level_max', '?')}"
        icon = STATUS_ICON.get(fm.get("status", ""), "")
        summary = first_summary_bullet(text)
        line = f"- {icon} [[{path.stem}]] · {fm.get('type', '?')}{lvl}"
        if summary:
            line += f" — {summary}"
        rows.append((sub if sub != "." else "", line))
    out, current = [], None
    for sub, line in rows:
        if sub != current:
            out.append(f"\n### {sub}" if sub else "")
            current = sub
        out.append(line)
    body = "\n".join(out).strip() or "_Sin notas todavía._"
    legend = "Leyenda: ✅ confirmado en Forever · ⚠️ en conflicto · 🟦 hipótesis de Classic · ❔ sin evidencia"
    text = moc.read_text(encoding="utf-8")
    new = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        f"{START}\n{legend}\n\n{body}\n{END}",
        text,
        flags=re.S,
    )
    moc.write_text(new, encoding="utf-8")
    return len(rows)


def category(url: str) -> tuple[str, str]:
    path = url.split("/wow-forever", 1)[1].strip("/")
    if path.startswith("class-guides/"):
        spec = path.split("/")[1]
        prio = "alta" if spec.endswith(("-rogue", "-priest")) else "baja"
        return "Clases: guías por especialización", prio
    if re.search(r"-leveling-guide-and-talents$", path):
        return "Clases: leveling", "alta" if ("rogue" in path or "priest" in path) else "media"
    if path.startswith("dungeons"):
        return "Mazmorras", "alta"
    prof = ("alchemy", "blacksmithing", "cooking", "enchanting", "first-aid", "fishing",
            "herbalism", "leatherworking", "skinning", "tailoring", "herb-seeds")
    if any(p in path for p in prof):
        return "Profesiones", "alta"
    if any(k in path for k in ("legacy", "library", "darkmoon", "camping", "transmog", "pvp",
                               "might-of", "blood-shards", "reputation", "waylaid", "ui",
                               "datamining", "beta-access", "ruleset", "fps")):
        return "Sistemas", "media"
    if any(k in path for k in ("weapons", "bags", "consumables", "torch", "root", "banner",
                               "pouch", "satchel", "sleeping-bag", "savory", "itemization",
                               "hit-chance", "gearing", "snake-form", "comprehension")):
        return "Objetos y equipo", "media"
    if any(k in path for k in ("mount", "bank-alts")):
        return "Economía", "alta"
    if any(k in path for k in ("travel", "starting-zones", "raids", "party", "races", "race",
                               "quests", "leveling")):
        return "Mundo y leveling", "alta"
    return "Índices del sitio", "baja"


def build_catalog() -> tuple[int, int]:
    digests = {p.stem for p in (ROOT / "07-Research/Guides").rglob("src-*.md")}
    lines = [
        "---", "type: moc", "tags: [moc, research]", "---", "",
        "# Catálogo de guías", "",
        "Todas las páginas conocidas de cada sitio, con su prioridad y si ya tienen ficha.",
        "Se regenera con `python3 _System/build_index.py`.", "",
    ]
    total = done = 0
    for src in sorted((ROOT / "_System/catalog").glob("*-urls.txt")):
        site = src.stem.replace("-urls", "")
        groups: dict[str, list[str]] = {}
        for url in src.read_text().split():
            slug = url.split("/wow-forever", 1)[1].strip("/").replace("/", "-") or "index"
            name = f"src-{site}-{slug}"
            cat, prio = category(url)
            ok = name in digests
            total += 1
            done += ok
            state = f"✅ [[{name}]]" if ok else "pendiente"
            short = url.split("/wow-forever", 1)[1] or "/"
            groups.setdefault(cat, []).append(f"| [{short}]({url}) | {prio} | {state} |")
        lines.append(f"## {site}\n")
        for cat in sorted(groups):
            lines += [f"### {cat}\n", "| Página | Prioridad | Estado |", "|---|---|---|"]
            lines += sorted(groups[cat])
            lines.append("")
    lines.insert(9, f"**Progreso:** {done} de {total} páginas con ficha.\n")
    (ROOT / "07-Research/Guide-Catalog.md").write_text("\n".join(lines), encoding="utf-8")
    return done, total


if __name__ == "__main__":
    for folder, moc in MOCS.items():
        print(f"{moc}: {build_moc(folder, moc)} notas")
    done, total = build_catalog()
    print(f"Catálogo: {done}/{total} páginas con ficha")
