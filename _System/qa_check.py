#!/usr/bin/env python3
"""Control de calidad de la bóveda.

Uso: python3 _System/qa_check.py   (desde la raíz)

Genera 07-Research/Knowledge-QA.md con:
- enlaces [[...]] a notas que no existen (huecos o enlaces rotos)
- notas de conocimiento sin `sources`, sin `status` o sin `type`
- notas con `last_verified` de hace más de 14 días
- notas con datos de ForeverDB sin el crédito obligatorio
Solo biblioteca estándar. No modifica ninguna nota salvo el informe.
"""
from __future__ import annotations

import datetime as dt
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".obsidian", "data", "tools", "tests", "node_modules", "07-Research/inbox"}
KNOWLEDGE = ("02-Classes", "03-Professions", "04-Economy", "05-World", "06-Items", "09-Systems", "10-Tips")
STALE_DAYS = 14
LINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")


def notes() -> list[Path]:
    out = []
    for p in ROOT.rglob("*.md"):
        rel = p.relative_to(ROOT).as_posix()
        if any(rel == d or rel.startswith(d + "/") for d in SKIP_DIRS):
            continue
        out.append(p)
    return out


def frontmatter(text: str) -> str:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return m.group(1) if m else ""


def field(fm: str, name: str) -> str | None:
    m = re.search(rf"^{name}:\s*(.*)$", fm, re.M)
    return m.group(1).strip().strip('"') if m else None


def main() -> None:
    files = notes()
    names = {p.stem for p in files} | {p.relative_to(ROOT).with_suffix("").as_posix() for p in files}
    names |= {p.stem for p in ROOT.rglob("*.base")} | {p.name for p in ROOT.rglob("*.base")}
    missing: dict[str, set[str]] = defaultdict(set)
    no_sources, no_status, no_type, stale, no_credit = [], [], [], [], []
    today = dt.date.today()

    for p in files:
        text = p.read_text(encoding="utf-8")
        rel = p.relative_to(ROOT).as_posix()
        for target in LINK.findall(text):
            t = target.strip()
            if t and t not in names and t.split("/")[-1] not in names:
                missing[t].add(p.stem)
        if not rel.startswith(KNOWLEDGE):
            continue
        fm = frontmatter(text)
        ntype = field(fm, "type")
        if ntype == "moc":
            continue
        if not ntype:
            no_type.append(p.stem)
        if not field(fm, "status"):
            no_status.append(p.stem)
        src = field(fm, "sources")
        has_list = re.search(r"^sources:\s*\n\s+- ", fm, re.M)
        if not has_list and (src is None or src in ("[]", "")):
            no_sources.append(p.stem)
        lv = field(fm, "last_verified")
        try:
            if lv and (today - dt.date.fromisoformat(lv[:10])).days > STALE_DAYS:
                stale.append(f"{p.stem} ({lv[:10]})")
        except ValueError:
            pass
        if "foreverdb.net" in text and "Data from ForeverDB.net" not in text:
            no_credit.append(p.stem)

    def block(title: str, items: list[str]) -> list[str]:
        lines = [f"## {title} ({len(items)})", ""]
        lines += [f"- [[{i.split(' (')[0]}]]" + (f" {i[len(i.split(' (')[0]):]}" if " (" in i else "") for i in sorted(items)] or ["_Ninguna._"]
        return lines + [""]

    top = Counter({k: len(v) for k, v in missing.items()}).most_common()
    out = [
        "---", "type: moc", "tags: [moc, research]", f"last_updated: {today.isoformat()}", "---", "",
        "# Control de calidad de la bóveda", "",
        "Generado por `python3 _System/qa_check.py`. Un enlace a una nota inexistente no siempre es un error: "
        "según [[Vault-Guide]] marca algo pendiente de escribir. Los más enlazados son los mejores candidatos para la próxima investigación.", "",
        f"**Notas revisadas:** {len(files)} · **Destinos sin nota:** {len(missing)} · "
        f"**Sin fuentes:** {len(no_sources)} · **Sin estado:** {len(no_status)} · **Antiguas:** {len(stale)} · "
        f"**ForeverDB sin crédito:** {len(no_credit)}", "",
        f"## Notas enlazadas que no existen ({len(top)})", "",
        "| Destino | Veces enlazado | Desde (ejemplos) |", "|---|---|---|",
    ]
    for target, n in top[:150]:
        out.append(f"| {target} | {n} | {', '.join(sorted(missing[target])[:3])} |")
    out.append("")
    out += block("Notas de conocimiento sin fuentes", no_sources)
    out += block("Notas de conocimiento sin estado", no_status)
    out += block("Notas de conocimiento sin tipo", no_type)
    out += block(f"Notas sin verificar en más de {STALE_DAYS} días", stale)
    out += block("Notas con datos de ForeverDB sin el crédito obligatorio", no_credit)
    (ROOT / "07-Research/Knowledge-QA.md").write_text("\n".join(out), encoding="utf-8")
    print(f"Revisadas {len(files)} notas · {len(missing)} destinos sin nota · {len(no_sources)} sin fuentes · "
          f"{len(no_status)} sin estado · {len(stale)} antiguas · {len(no_credit)} ForeverDB sin crédito")


if __name__ == "__main__":
    main()
