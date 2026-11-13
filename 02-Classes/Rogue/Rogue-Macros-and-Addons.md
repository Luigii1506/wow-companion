---
type: topic
tags: [forever, rogue, macros, addons, ui]
faction: both
status: unknown
confidence: low
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://www.method.gg/wow-forever/class-guides/combat-rogue/interface-addons-and-macros
  - https://www.method.gg/wow-forever/class-guides/assassination-rogue/interface-addons-and-macros
  - https://www.method.gg/wow-forever/class-guides/subtlety-rogue/interface-addons-and-macros
  - https://www.method.gg/wow-forever/wow-forever-rogue-leveling-guide-and-talents
  - https://foreverdb.net/class/Rogue/macros
  - https://foreverdb.net/macros
  - https://foreverdb.net/addons/best
related: ["[[Rogue]]", "[[Rogue-Poisons]]", "[[Addons]]", "[[Rogue-Leveling]]"]
---

# Macros y addons de Rogue

> [!question] Sin evidencia suficiente
> Ninguna macro ni addon de esta nota se ha probado en el juego del jugador. ForeverDB dice que la mayoría de sus macros "no se han probado". No declarar que funcionan hasta probarlas.

## Resumen
- Interfaz sin addons: **Cooldown Manager** de Blizzard (admite Rogue desde el 01-10) y **Personal Resource Display**; nameplates. Method no considera ningún addon obligatorio.
- Macros útiles ya a nivel 11: `!Stealth` (no sale del sigilo por doble pulsación), Pick Pocket + apertura (Pick Pocket no tiene GCD en los datos del cliente), Kick al focus (12+), Sap con mouseover (10+).
- Para más adelante: Vanish con `/stopattack` (22), Distract al cursor (22), aplicar veneno al slot 16/17 (20+), Blind al focus (34).
- Addons citados: boss mods (Method Raid Tools, BigWigs) y DungeonJournal; ForeverDB tiene su propio "Companion addon". Todo `unknown` hasta probarlo; solo addons permitidos por Blizzard.

## Macros para nivel 11–20
| Macro | Qué hace | Nivel | Fuente | Estado |
|---|---|---|---|---|
| `#showtooltip` / `/cast !Stealth` | Entra en sigilo; volver a pulsar no lo quita | 1 | ForeverDB | unknown (sin probar) |
| `/cast [stealth] Pick Pocket` + `/cast [stealth] Garrote; Sinister Strike` | Roba y abre; fuera de sigilo es Sinister Strike | 14 (Garrote) | ForeverDB (variante), Method (Pick Pocket + Garrote) | unknown |
| `/cast [stealth,mod:shift] Cheap Shot; [stealth,mod:ctrl] Garrote; [stealth] Ambush; Sinister Strike` + `/startattack [nostealth]` | Apertura y generador en una tecla | 18 (Ambush, daga) | ForeverDB | unknown |
| `/cast [@focus,harm,nodead][@mouseover,harm,nodead][] Kick` | Kick al focus, mouseover u objetivo | 12 | ForeverDB | unknown |
| `/cast [nostealth] !Stealth; [@mouseover,harm,nodead][@focus,harm,nodead][] Sap` | Sigilo y Sap al mouseover | 10 | ForeverDB | unknown |
| `/castsequence reset=target/5 Gouge, Backstab` | Gouge y luego Backstab por detrás (daga) | 6 | ForeverDB | unknown |

Sin daga, sustituir Ambush por Garrote (Ambush necesita daga en mano principal).

## Macros para más adelante
| Macro | Nivel | Fuente | Estado |
|---|---|---|---|
| `#showtooltip 16` / `/use Deadly Poison` / `/use 16` (o 17 para la secundaria) | 20–30 | Method | unknown |
| `/stopattack` + `/cast Vanish` | 22 | ForeverDB | unknown |
| `/cast [@cursor] Distract` | 22 | ForeverDB | unknown |
| `/stopattack [nomod]` + `/cast [mod:shift,@focus,harm,nodead][nomod] Blind` | 34 | ForeverDB | unknown |

## Interfaz y addons
| Elemento | Para qué | Fuente | Estado |
|---|---|---|---|
| Cooldown Manager (Blizzard) | Seguir CDs; Rogue soportado desde el 01-10. Blizzard dijo en septiembre que no seguía encantamientos temporales (venenos) y no consta arreglado | Method, ForeverDB | unknown |
| Personal Resource Display | Energía centrada; en la beta no mostraba combo points (problema conocido, sin confirmación de arreglo) | Method, ForeverDB | unknown |
| Method Raid Tools / BigWigs | Boss mods | Method | unknown |
| DungeonJournal | Buscar mejoras por mazmorra | Method | unknown |
| ForeverDB Companion addon | Muestra dónde va cada punto de talento y la rotación | ForeverDB | unknown |

## Macros generales de ForeverDB (añadido el 2026-11-13)
> [!question] Sin probar
> Del índice general de macros de ForeverDB (194 macros, comprobadas por script contra el cliente build 1.60.1.70888). La propia página dice que **la mayoría no se han probado en el juego**. Las 22 de Rogue ya están arriba (ficha [[src-foreverdb-class-rogue-macros]]); aquí solo lo que añade la página general. Ficha: [[src-foreverdb-macros]].

| Macro | Qué hace | Nivel | Estado |
|---|---|---|---|
| `#showtooltip` / `/use 13` / `/use 14` / `/cast Blood Fury` | Abalorios con efecto de uso + racial Orc en una tecla (ninguno activa el GCD) | 1 | unknown (sin probar) |
| `#showtooltip` / `/stopcasting` / `/cast Shatter Curse` | Racial Orc de limpiar maldiciones al momento | 1 | unknown |
| `/targetenemy [noharm][dead]` | Busca enemigo solo si no tienes uno vivo; no salta de objetivo como Tab | 1 | unknown |
| `/targetenemyplayer [noharm][dead]` | Igual, solo jugadores (BG y PvP en el mundo) | 1 | unknown |
| Cadena de `/use` de pociones de mejor a peor (Greater Healing → Healing → Perishable Healing → Lesser → Minor) | Bebe la mejor poción que tengas | 1 | unknown |

Datos útiles de la página (del cliente):
- Todas las pociones de vida, maná y rejuvenecimiento comparten **un CD de 2 min** (incluidas las nuevas Discolored y Perishable); las healthstones tienen otro CD de 2 min; las vendas no comparten CD.
- Forever usa la **sintaxis moderna**: existen focus, `[@mouseover]`, `[@focus]`, `[@cursor]`, `[mod:…]`, `[stealth]`. Classic Era oculta el focus.
- Rangos: `/cast Sinister Strike(Rank 1)` sin espacio antes del paréntesis.
- `/castsequence` solo avanza si el hechizo se lanza bien; se reinicia con `reset=` (segundos, target, combat, shift/ctrl/alt) y al morir.
- 255 caracteres por macro; 120 macros generales de cuenta y 30 por personaje.
- Una macro de Classic Era con `[equipped:Fishing Poles]` falla: el cliente dice "Fishing Pole".

## Addons según /addons/best (añadido el 2026-11-13)
> [!question] Sin probar
> Lista de ForeverDB revisada el **2026-10-11** (archivos de CurseForge previos al lanzamiento). ForeverDB pone su propio addon primero. Ninguno se ha probado en el juego del jugador. Ficha: [[src-foreverdb-addons-best]].

| Tarea | Addons citados | Nota |
|---|---|---|
| Misiones y leveling | RestedXP (gratis hasta ~20), Questie, QuestTrail, GnomeLevelUp | Questie usa su base de Classic con correcciones para Forever |
| Viaje y mapas | Shortest Path Forever, Leatrix Maps, TomTom | — |
| Profesiones y AH | SkillUp Forever, Forever Fishing, Auctionator | SkillUp muestra probabilidad de skill-up |
| Bolsas y vendedores | Extended Vendor Forever, Delete Cheapest Item, Bagnon | — |
| Mazmorras | DungeonJournal, AtlasLoot Classic Forever, Details! | — |
| Interfaz | Forever Move, FontMagic, DarkMode, ClassicUI Forever, FDB Chat, Better Forever Chat, Leatrix Plus, EllesmereUI | — |

## Qué dicen las guías
- [[src-method-class-guides-combat-rogue-interface-addons-and-macros]] (igual en [[src-method-class-guides-assassination-rogue-interface-addons-and-macros]] y [[src-method-class-guides-subtlety-rogue-interface-addons-and-macros]]): pocas macros y ningún addon obligatorio.
- [[src-method-wow-forever-rogue-leveling-guide-and-talents]]: Pick Pocket + Ambush.
- [[src-foreverdb-class-rogue-macros]]: 22 macros comprobadas contra el cliente, casi todas sin probar en juego.
- [[src-foreverdb-macros]]: 194 macros para todas las clases; añade las de racial Orc, objetivo y pociones.
- [[src-foreverdb-addons-best]]: lista de addons por tarea, de antes del lanzamiento.
- Lista general de addons de la bóveda: [[Addons]].

## Fuentes
| URL | Tipo | Fecha página | Consultada | ¿Pre-parche? |
|---|---|---|---|---|
| https://www.method.gg/wow-forever/class-guides/combat-rogue/interface-addons-and-macros | Guía Method | 2026-11-04 | 2026-11-13 | No |
| https://www.method.gg/wow-forever/class-guides/assassination-rogue/interface-addons-and-macros | Guía Method | 2026-11-04 | 2026-11-13 | No |
| https://www.method.gg/wow-forever/class-guides/subtlety-rogue/interface-addons-and-macros | Guía Method | 2026-11-04 | 2026-11-13 | No |
| https://www.method.gg/wow-forever/wow-forever-rogue-leveling-guide-and-talents | Guía Method | 2026-11-07 | 2026-11-13 | No |
| https://foreverdb.net/class/Rogue/macros | Macros ForeverDB | sin fecha (build 70888) | 2026-11-13 | No |
| https://foreverdb.net/macros | Macros ForeverDB (todas las clases) | 2026-11-13 (build 70888) | 2026-11-13 | No |
| https://foreverdb.net/addons/best | Lista de addons ForeverDB | 2026-10-11 | 2026-11-13 | Sí (prelanzamiento) |

[Data from ForeverDB.net](https://foreverdb.net)

## Preguntas pendientes
- Probar en el juego `!Stealth` y Pick Pocket + Garrote y anotar el resultado.
- ¿El Cooldown Manager ya muestra los venenos del arma?
