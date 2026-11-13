---
type: topic
tags: [forever, rogue, poisons]
level_min: 20
level_max: 60
faction: both
status: conflicting
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://foreverdb.net/class/Rogue/poisons
  - https://foreverdb.net/guide/leveling-rogue
  - https://www.method.gg/wow-forever/wow-forever-rogue-leveling-guide-and-talents
  - https://www.method.gg/wow-forever/class-guides/combat-rogue/rotation-and-playstyle
  - https://www.method.gg/wow-forever/class-guides/assassination-rogue/rotation-and-playstyle
  - https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696/9
  - https://news.blizzard.com/en-us/article/24310968/world-of-warcraft-forever-class-deep-dives-rogue-and-warlock
  - https://news.blizzard.com/en-us/article/24315281/wow-forever-hotfixes-november-11-2026
  - https://theforeverera.com/es/guides/classes/rogue/
  - "Cliente WoW Forever 1.60.1.70938 vía wago.tools (consulta local, 2026-11-13)"
related: ["[[Rogue]]", "[[Rogue-Leveling]]", "[[Assassination-Rogue]]", "[[Combat-Rogue]]", "[[Consumables]]", "[[Conflicts]]"]
---

# Venenos de Rogue

> [!warning] Datos en conflicto: ver [[Conflicts]]
> **Cómo se aprenden** está en conflicto: ForeverDB (página de venenos) dice que con la misión *Hinott's Assistance* para la Horde; su guía de leveling dice que no está confirmado y apunta a la cadena *Deep Cover* → *Mission: Possible But Not Probable*. Method solo dice "a nivel 20". Comprobar en el juego.

## Resumen
- Skill de venenos a **nivel 20**. Instant y Crippling 20, Mind-numbing 24, Instant II 28, **Deadly 30** (cliente). `confirmed_forever` (high)
- Recomendación de todas las guías: **Deadly + Instant** cuando tengas ambos (30); hasta entonces, Instant. El resto (Crippling, Mind-numbing, Wound), casi solo PvP.
- Forever: **más cargas**, compatibles con piedras de afilar y de peso y con Windfury Totem; coeficiente de AP doblado en Deadly (0,009) e Instant (0,01). `confirmed_forever` (high)
- Horde: vendedor **Rekkul** (Orgrimmar 42.2, 49.6, visto en Forever); entrenadores Ormok y Shenthul en Orgrimmar.
- La misión de Rogue "Mission: Possible not Probable" existe en Forever (Blizzard la arregló en un hotfix).

## Cómo se aprenden
| Versión | Qué dice | Fuente | Estado |
|---|---|---|---|
| A | Misión de clase a 20: *Hinott's Assistance* (Horde); Instant viene con la skill, el resto lo enseña el entrenador | ForeverDB, página de venenos | conflicting |
| B | Skill a 20 en el cliente; en Classic la cadena Horde era *Deep Cover* (Shenthul, Orgrimmar, 20) → *Mission: Possible But Not Probable* (24, Taskmaster Fizzule, Barrens); "nadie ha confirmado" que enseñe venenos en Forever | ForeverDB, guía de leveling | conflicting |
| C | "A nivel 20 tenemos venenos" (sin mecanismo) | Method | confirmed_forever (low) |

## Venenos hasta 40
| Veneno | Nivel | Reactivos | Coste en entrenador (Forever) | Estado | Cliente (1.60.1.70938) |
|---|---|---|---|---|---|
| Instant Poison | 20 | Dust of Decay, Empty Vial | Viene con la skill (según A) | confirmed_forever (medium) | ID 6947 · Common · ilvl 20 · req 20 · Other · venta 5c |
| Crippling Poison | 20 | Essence of Pain, Empty Vial | 30 s | confirmed_forever (medium) | ID 3775 · Common · ilvl 20 · req 20 · Other · venta 13c |
| Mind-numbing Poison | 24 | Dust of Decay, Essence of Pain, Empty Vial | 63 s 16 c | confirmed_forever (medium) | ID 5237 · Common · ilvl 24 · req 24 · Other · venta 18c |
| Instant Poison II | 28 | Dust of Decay ×3, Leaded Vial | 84 s 21 c | confirmed_forever (medium) | ID 6949 · Common · ilvl 28 · req 28 · Other · venta 20c |
| Deadly Poison | 30 | Deathweed, Leaded Vial | 94 s 74 c | confirmed_forever (medium) | ID 2892 · Common · ilvl 30 · req 30 · Other · venta 30c |
| Wound Poison | 32 | Essence of Pain, Deathweed, Leaded Vial | 1 g 36 s 84 c | confirmed_forever (medium) | ID 10918 · Common · ilvl 32 · req 32 · Other · venta 42c |
| Blinding Powder | 34 | Fadeleaf | 1 g 47 s 37 c | confirmed_forever (medium) | ID 5530 · Common · ilvl 34 · Junk · venta 1s 25c |
| Instant Poison III | 36 | Dust of Deterioration, Leaded Vial | 1 g 57 s 89 c | confirmed_forever (medium) | ID 6950 · Common · ilvl 36 · req 36 · Other · venta 30c |
| Deadly II / Mind-numbing II | 38 | — | 1 g 68 s 42 c | confirmed_forever (medium) | Deadly Poison II: ID 2893 · Common · ilvl 38 · req 38 · Other · venta 55c; Mind-numbing Poison II: ID 6951 · Common · ilvl 38 · req 38 · Other · venta 75c |
| Wound Poison II | 40 | — | 2 g | confirmed_forever (medium) | ID 10920 · Common · ilvl 40 · req 40 · Other · venta 67c |

Precios: observados por el addon de ForeverDB a precio completo; no son precios de subasta. Tooltips (ForeverDB, guía de leveling): Instant 20 % de 13–17 de daño Nature; Crippling 30 % de −50 % velocidad 12 s; Deadly 30 % de 24 daño en 12 s, hasta 5 acumulaciones; duran 30 min en el arma.

## Reactivos (Rekkul, Orgrimmar)
| Reactivo | Precio | Estado | Cliente (1.60.1.70938) |
|---|---|---|---|
| Dust of Decay | 20 c | confirmed_forever (medium) | ID 2928 · Common · ilvl 20 · Reagent · venta 5c |
| Essence of Pain | 50 c | confirmed_forever (medium) | ID 2930 · Common · ilvl 22 · Reagent · venta 12c |
| Empty Vial | 20 c | confirmed_forever (medium) | ID 3371 · Common · ilvl 1 · Other · venta 1c |
| Leaded Vial | 2 s | confirmed_forever (medium) | ID 3372 · Common · ilvl 25 · Other · venta 10c |
| Deathweed | 1 s | confirmed_forever (medium) | ID 5173 · Common · ilvl 30 · Reagent · venta 25c |

> [!info] Datos del cliente (cliente 1.60.1.70938)
> Columna "Cliente": tablas DB2 del cliente WoW Forever build 1.60.1.70938 (wago.tools, extraídas 2026-11-13; ItemSparse, Item, ItemSubClass). Son datos de los archivos del juego, no del servidor: un objeto puede cambiar por hotfix. Calidad y ranura: etiquetas de enums públicos de Blizzard; nombres de stats: `Enum.BonusStatIndex` del propio cliente (solo el nombre, sin cantidad); "req" solo si el cliente da nivel requerido distinto de 0; "vel." = ItemDelay en segundos; "venta" = SellPrice para vendedor, no subasta. Blizzard oculta en el cliente ~40 % de los objetos de Forever hasta que se descubren: "no está en el cliente" no prueba que no exista.

Contraste con el cliente (cliente 1.60.1.70938): el nivel requerido de cada veneno coincide con la tabla (Instant y Crippling 20, Mind-numbing 24, Instant II 28, Deadly 30, Wound 32, Instant III 36, Deadly II y Mind-numbing II 38, Wound II 40). Blinding Powder no trae nivel requerido en el cliente (ilvl 34). Los precios de Rekkul coinciden con el BuyPrice del cliente (Dust of Decay 20c, Essence of Pain 50c, Empty Vial 20c, Leaded Vial 2s, Deathweed 1s). Los reactivos de las filas sin tabla propia: Fadeleaf ID 3818 (venta 1s 25c), Dust of Deterioration ID 8924 (venta 25c).

## Talentos que tocan venenos
Malice (crit de venenos), Precision (hit de venenos), Vile Poisons, Improved Poisons, **Venom** (Shank), Improved Kidney Shot. Ver [[Assassination-Rogue]].

## Macros
Aplicar veneno al slot 16 (mano principal) o 17 (secundaria): ver [[Rogue-Macros-and-Addons]].

## Qué dicen las guías
- Consenso: Deadly + Instant; otros venenos para PvP. [[src-method-class-guides-combat-rogue-rotation-and-playstyle]], [[src-method-class-guides-assassination-rogue-rotation-and-playstyle]], [[src-foreverdb-class-rogue-poisons]].
- Aprendizaje: [[src-foreverdb-class-rogue-poisons]] frente a [[src-foreverdb-guide-leveling-rogue]] y [[src-method-wow-forever-rogue-leveling-guide-and-talents]].
- Cambios: [[src-blizzard-class-deep-dives-rogue-and-warlock-24310968]] (cargas, piedras), [[src-blizzard-forum-beta-development-notes-november-2-2360696]] (coeficientes), [[src-blizzard-hotfixes-24315281]] (misión arreglada), [[src-theforeverera-es-guides-classes-rogue]] (correcciones de octubre).
- Venenos de Season of Discovery en el cliente (Occult, Atrophic, Numbing, Sebacious): sin entrenador visto. `unknown`

## Fuentes
- [Data from ForeverDB.net](https://foreverdb.net)
| URL | Tipo | Fecha página | Consultada | ¿Pre-parche? |
|---|---|---|---|---|
| https://foreverdb.net/class/Rogue/poisons | Datos de cliente + addon | 2026-11-13 | 2026-11-13 | No |
| https://foreverdb.net/guide/leveling-rogue | Guía ForeverDB | 2026-11-05 | 2026-11-13 | No |
| https://www.method.gg/wow-forever/wow-forever-rogue-leveling-guide-and-talents | Guía Method | 2026-11-07 | 2026-11-13 | No |
| https://www.method.gg/wow-forever/class-guides/combat-rogue/rotation-and-playstyle | Guía Method | 2026-11-04 | 2026-11-13 | No |
| https://www.method.gg/wow-forever/class-guides/assassination-rogue/rotation-and-playstyle | Guía Method | 2026-11-04 | 2026-11-13 | No |
| https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696/9 | Notas oficiales | 2026-11-03 | 2026-11-13 | Es el parche |
| https://news.blizzard.com/en-us/article/24310968/world-of-warcraft-forever-class-deep-dives-rogue-and-warlock | Artículo oficial | ≈ 2026-10-07 | 2026-11-13 | Sí |
| https://news.blizzard.com/en-us/article/24315281/wow-forever-hotfixes-november-11-2026 | Hotfixes oficiales | 05-11 a 11-11 | 2026-11-13 | No |
| https://theforeverera.com/es/guides/classes/rogue/ | Guía fan (es) | 2026-10-25 | 2026-11-13 | Sí (cuerpo) |

## Preguntas pendientes
- ¿Qué misión enseña los venenos a la Horde? Comprobar con Shenthul al llegar a 20.
- ¿Cuántas cargas tiene cada veneno en Forever? Blizzard no da cifras.
