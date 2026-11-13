---
type: source-digest
tags: [forever, source, priest, talents]
site: method.gg
url: https://www.method.gg/wow-forever/talent-calculator
author: Method
published: desconocido
updated: desconocido (datos versión 1.60.1)
ingested: 2026-11-13
status: confirmed_forever
confidence: medium
feeds: ["[[Priest-Talents]]", "[[Priest]]"]
---

# Method — Talent Calculator (WoW Forever)

## Puntos clave
- El texto de la página no muestra los árboles de Priest (se cargan con JavaScript). Solo se ve el selector de clases y "Warrior 0/51": **51 puntos en total** (niveles 10–60).
- Los árboles salen de `https://www.method.gg/dfc/ForeverTalentsData-1.60.1.json` (versión 1.60.1), el mismo archivo que alimenta los widgets de las guías.
- Árbol Priest (fila: talentos y rangos máx.; fila n exige 5·(n−1) puntos):
  - **Discipline**: F1 Power in Light 5, Wand Specialization 2, Twin Disciplines 5 · F2 Silent Resolve 3, Holy Precision 3, Mental Strength 5, Martyrdom 2 · F3 Mental Agility 3, Inner Focus 1, Improved PW:Shield 3, Meditation 3 · F4 Improved Inner Fire 3, Improved Mana Burn 2, Soul Warding 1 · F5 Penance 1, Renewed Hope 5 · F6 Divine Aegis 3 · F7 Power Infusion 1.
  - **Holy**: F1 Twilight Focus 3, Improved Renew 3, Holy Specialization 5 · F2 Spell Warding 5, Divine Fury 5 · F3 Holy Nova 1, Blessed Recovery 3, Inspiration 3 · F4 Holy Reach 2, Improved Healing 3, Searing Light 2, Holy Binding 1 · F5 Litany of Light 2, Spirit of Redemption 1, Spiritual Guidance 5 · F6 Spiritual Healing 3 · F7 Prayer of Mending 1.
  - **Shadow**: F1 Shadow Focus 5, Blackout 5, Spirit Tap 5 · F2 Improved Mind Blast 5, Improved SW:Pain 2, Shadow Reach 2 · F3 Improved Psychic Scream 2, Mind Flay 1, Improved Mind Flay 2 · F4 Dark Inspiration 5, Vampiric Embrace 1, Shadow Weaving 3 · F5 Silence 1, Devouring Contagion 2 · F6 Early Demise 2, Darkness 5 · F7 Shadowform 1.
- Los nombres se resolvieron con el tooltip de Wowhead Forever (`nether.wowhead.com/forever/tooltip/spell/<id>`). Hay un nodo duplicado de Holy Specialization fuera del árbol (artefacto de datos).

## Fiabilidad
- Datos marcados 1.60.1 (versión de lanzamiento). Fecha exacta desconocida.
- Huecos: no da prerequisitos legibles ni efectos por rango; los tooltips muestran a veces "0%" (Spirit Tap, Martyrdom, Inspiration).

## Alimenta
- [[Priest-Talents]], [[Priest]]
