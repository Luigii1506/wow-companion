---
type: spec
tags: [forever, priest, discipline, leveling, healer]
level_min: 10
level_max: 60
faction: both
status: unknown
confidence: low
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://www.method.gg/wow-forever/wow-forever-priest-leveling-guide-and-talents
  - https://www.method.gg/wow-forever/class-guides/holy-priest/talents
  - https://www.method.gg/dfc/ForeverTalentsData-1.60.1.json
  - https://nether.wowhead.com/forever/tooltip/spell/402174
  - https://nether.wowhead.com/forever/tooltip/spell/402000
  - https://nether.wowhead.com/forever/tooltip/spell/1225132
  - https://nether.wowhead.com/forever/tooltip/spell/425280
  - https://nether.wowhead.com/forever/tooltip/spell/431622
  - https://worldofwarcraft.blizzard.com/news/24301514
  - https://timesaver.gg/tools/wow-forever/talent-calculator/priest
  - https://www.warcrafttavern.com/forever/guides/priest-leveling/
related: ["[[Priest]]", "[[Priest-Talents]]", "[[Priest-Leveling]]", "[[Holy-Priest]]", "[[Shadow-Priest]]"]
---

# Discipline Priest

> [!question] Sin evidencia suficiente
> Method **no publica guía Discipline de endgame** para Forever: las 7 URLs `class-guides/discipline-priest…` devolvieron 404 el 2026-11-13 y el índice de guías lista "Discipline Priest" sin enlace. Lo que hay es Discipline como **spec de leveling 10–39** y una build híbrida Disc/Holy dentro de la guía Holy.

## Resumen
- **Para el personaje (nivel ~9)**: Discipline/híbrido es la spec de leveling que recomienda Method hasta el 39: **Wand Specialization 2/2 (10–11) → Spirit Tap 5/5 (12–16) → Improved SW:Pain 2/2 (17–18) → Twin Disciplines (19–23)**, Penance al 37, respec a Shadow al 40.
- Talentos clave de Forever en Disc: **Penance** (21 puntos), **Soul Warding** (PW:S sin CD de 4 s y −15 % de coste), **Twin Disciplines** (+5 % a instantáneos), Renewed Hope, Divine Aegis, Power Infusion (31 puntos).
- En endgame, Method usa Disc como **híbrido 21/30/0** (Penance + Soul Warding + Holy) para mazmorras y raids de 10.
- Rotación, stats, BiS, encantamientos y addons específicos de Disc de endgame: **desconocido** (no hay guía).

## Talentos

### Leveling 10–39 (23/0/7), Method (2026-11-06)
Nivel inferido: punto n = nivel 9+n. Estado: `confirmed_forever` (guía post-parche).

| Nivel | Talento | Rangos tras el punto |
|---|---|---|
| 10–11 | Wand Specialization | 2/2 |
| 12–16 | Spirit Tap (Shadow) | 5/5 |
| 17–18 | Improved Shadow Word: Pain (Shadow) | 2/2 |
| 19–23 | Twin Disciplines | 5/5 |
| 24–25 | Martyrdom | 2/2 |
| 26 | Mental Strength | 1/5 |
| 27 | Inner Focus | 1/1 |
| 28–30 | Meditation | 3/3 |
| 31–32 | Mental Agility | 2/3 |
| 33–35 | Improved Inner Fire | 3/3 |
| 36 | Improved Power Word: Shield | 1/3 |
| 37 | **Penance** | 1/1 |
| 38–39 | Improved Power Word: Shield | 3/3 |

Method la describe como muy eficiente en maná y resistente; el daño cae a mediados o finales de los 30.

### Híbrido Disc/Holy 21/30/0, Method (guía Holy, 2026-11-10)
| Árbol | Talentos |
|---|---|
| Discipline (21) | Twin Disciplines 5, Silent Resolve 3, Mental Strength 3, Mental Agility 1, Inner Focus 1, Improved PW:Shield 3, Meditation 3, Soul Warding 1, Penance 1 |
| Holy (30) | Improved Renew 3, Holy Specialization 5, Divine Fury 5, Twilight Focus 2, Holy Nova 1, Inspiration 3, Improved Healing 3, Holy Binding 1, Litany of Light 2, Spiritual Guidance 5 |

Lógica (Method): Penance es una cura instantánea por ticks; Improved Healing 3/3 abarata Penance un 15 %; alternar Penance con Greater/Flash Heal activa Litany of Light; Improved PW:S 3/3 (+20 % absorción) + Soul Warding protegen al grupo.

### Árbol Discipline completo (datos 1.60.1)
F1 Power in Light 5, Wand Specialization 2, Twin Disciplines 5 · F2 Silent Resolve 3, Holy Precision 3, Mental Strength 5, Martyrdom 2 · F3 Mental Agility 3, Inner Focus 1, Improved PW:Shield 3, Meditation 3 · F4 Improved Inner Fire 3, Improved Mana Burn 2, Soul Warding 1 · F5 Penance 1, Renewed Hope 5 · F6 Divine Aegis 3 · F7 Power Infusion 1. Ver [[Priest-Talents]].

| Talento | Efecto (tooltip Wowhead Forever; rango mostrado sin indicar) | Estado |
|---|---|---|
| Penance | Canal 2 s, CD 12 s, daña o cura al instante y cada segundo; requiere nivel 30 | confirmed_forever |
| Soul Warding | −4 s de CD a PW:S y −15 % de coste | confirmed_forever |
| Renewed Hope | +10 % crit de Flash/Lesser/Heal/Greater Heal/Penance sobre objetivos con Weakened Soul y −5 s de Weakened Soul | confirmed_forever |
| Divine Aegis | Crit de cura no periódica: escudo del 15 % de lo curado, 12 s | confirmed_forever |
| Power Infusion | +20 % daño y curación 15 s, CD 3 min; requiere nivel 40 | confirmed_forever |
| Power in Light | +15 % a Smite y Penance contra objetivos con tu Holy Fire o SW:Pain | confirmed_forever |
| Improved Inner Fire | +45 % armadura de Inner Fire y +12 cargas | confirmed_forever |

## Rotación
- Leveling 10–39 (Method): PW:S → Mind Blast → SW:Pain → wand; refrescar PW:S y SW:P en mobs duros. Ver [[Priest-Leveling]].
- Disc 30+ (Warcraft Tavern, beta): PW:S → Smite → SW:Pain → Penance → wand/DoT para rematar. `probable_classic`/beta.
- Endgame: **desconocido**.

## Stats, BiS, encantamientos, razas, addons
- **Desconocido** para Disc de endgame. Para el híbrido de curación sirve la guía Holy ([[Holy-Priest]]): Healing Power ≥ Spirit > MP5 > Int.

## Qué dicen las guías
- Method leveling ([[src-method-wow-forever-priest-leveling-guide-and-talents]]) y Maxroll vía Timesaver coinciden en 10–16 (WS 2/2, Spirit Tap 5/5) y en terminar Disc ~23 puntos con respec al 40. Difieren desde el 17: Method toma Improved SW:Pain y Martyrdom y pone Penance al **37**; Maxroll toma Twin Disciplines, Holy Precision y Mental Strength y pone Penance al **35**. Ver [[Priest-Talents]].
- El híbrido 21/30/0 sale de [[src-method-class-guides-holy-priest-talents]].
- El árbol completo, de [[src-method-talent-calculator]].

## Fuentes

| URL | Tipo | Fecha de la página | Consultada | ¿Anterior al parche del 02-11? |
|---|---|---|---|---|
| https://www.method.gg/wow-forever/wow-forever-priest-leveling-guide-and-talents | guide | 2026-11-06 | 2026-11-13 | No |
| https://www.method.gg/wow-forever/class-guides/holy-priest/talents | guide | 2026-11-10 | 2026-11-13 | No |
| https://www.method.gg/dfc/ForeverTalentsData-1.60.1.json | datos | 1.60.1 | 2026-11-13 | No |
| https://nether.wowhead.com/forever/tooltip/spell/<id> | community DB | sin fecha | 2026-11-13 | Desconocido |
| https://worldofwarcraft.blizzard.com/news/24301514 | official | 30-09 | 2026-11-10 (nota previa) | Sí |
| https://timesaver.gg/tools/wow-forever/talent-calculator/priest | community tool | 04-11 | 2026-11-10 (nota previa) | No |
| https://www.warcrafttavern.com/forever/guides/priest-leveling/ | guide | beta | 2026-11-10 (nota previa) | Probablemente sí |
| https://www.method.gg/wow-forever/class-guides/discipline-priest (y 6 subpáginas) | guide | — | 2026-11-13: **404** | — |

## Preguntas pendientes
- ¿Publicará Method una guía Discipline de endgame?
- ¿Es Disc viable como healer principal de raid en Forever (Divine Aegis, Power Infusion, Renewed Hope)?
- ¿Cuál es el efecto real por rango de Martyrdom en Forever? El tooltip muestra "0%".
