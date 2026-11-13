---
type: spec
tags: [forever, rogue, assassination]
level_min: 10
level_max: 60
faction: both
status: conflicting
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://www.method.gg/wow-forever/class-guides/assassination-rogue
  - https://www.method.gg/wow-forever/class-guides/assassination-rogue/talents
  - https://www.method.gg/wow-forever/class-guides/assassination-rogue/rotation-and-playstyle
  - https://www.method.gg/wow-forever/wow-forever-rogue-leveling-guide-and-talents
  - https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json
  - https://foreverdb.net/class/Rogue/talents
  - https://foreverdb.net/class/Rogue/builds
  - https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696/9
  - https://news.blizzard.com/en-us/article/24310968/world-of-warcraft-forever-class-deep-dives-rogue-and-warlock
related: ["[[Rogue]]", "[[Rogue-Leveling]]", "[[Combat-Rogue]]", "[[Subtlety-Rogue]]", "[[Rogue-Poisons]]"]
---

# Assassination Rogue

> [!warning] Datos en conflicto: ver [[Conflicts]]
> Venom: el artículo de Blizzard de octubre, la rotación de Method y The Forever Era lo tratan como remate; las notas del 02-11 y el cliente lo dan como **talento pasivo** que activa Shank. Se sigue a las notas del 02-11.

## Resumen
- Spec de venenos y críticos: Malice, Lethality, Cold Blood, Improved/Vile Poisons, **Venom** (Shank → +30 % daño de venenos y +20 % aplicación 6 s), Seal Fate, **Mutilate a 40** (dos dagas). `confirmed_forever` (high)
- No es spec de leveling temprano: necesita dagas y crit; Mutilate llega al 40 y ForeverDB la ve como opción si te gustan los críticos.
- Builds de Method: **Combat Mutilate 35/11/5** (venenos) y **Assa Shank 21/30/0** (menos venenos, para jefes con resistencias a Nature).
- Débil ante inmunidad a Nature; la que menos pierde al usar Expose Armor.

## Talentos clave
| Talento | Fila | Efecto (cliente) | Estado |
|---|---|---|---|
| Malice | 1 | +5 % crit en ataques y venenos | confirmed_forever (high) |
| Remorseless Attacks | 1 | +40 % crit al siguiente generador tras matar | confirmed_forever (high) |
| Ruthlessness | 2 | 60 % de CP extra al rematar | confirmed_forever (high) |
| Improved Slice and Dice | 2 | +45 % duración | confirmed_forever (high) |
| Lethality / Vigor / Blood Splatter | 3 | +20 % daño crítico / +10 energía máx. / +6 s Rupture, +9 s Garrote | confirmed_forever (high) |
| Cold Blood | 4 | +100 % crit al siguiente golpe | confirmed_forever (high) |
| Vile Poisons / Improved Poisons | 4 | +20 % daño de venenos / +10 % aplicación y 50 % de no gastar carga | confirmed_forever (high) |
| Relentless Strikes / Venom | 5 | 20 % por CP de recuperar 25 energía / pasivo de Shank | confirmed_forever (high) |
| Seal Fate | 6 | Crit de generador = CP extra | confirmed_forever (high) |
| Mutilate | 7 | Ambas armas 90 % + bonus, +20 % contra envenenados, 2 CP | confirmed_forever (high) |

## Builds de Method (decodificadas)
| Build | Reparto | Orden (nivel) | Estado |
|---|---|---|---|
| Leveling "Assassination" (guía de leveling) | 31/16/4 | RA 10–11, ES 12–13, CdG 14–16, Puncturing Wounds 17–19, Prec 20–22, Malice 23–25, Imp. SnD 26–28, Ruthl. 29–30, Malice 31–32, Lethality 33–34, Ruthl. 35, Cold Blood 36, End 37–38, Defl 39–40, FE 41, Imp. Poisons 42–45, Venom 46, Relentless 47–51, Seal Fate 52–54, Imp. Poisons 55, Mutilate 56, Opportunity 57–60 | confirmed_forever (medium) |
| Combat Mutilate (endgame) | 35/11/5 | Malice 10–14, Imp. SnD 15–17, Ruthl. 18–19, Lethality 20–21, Blood Splatter 22, Vigor 23–24, Cold Blood 25, Vile Poisons 26–30, Venom 31, Relentless 32–36, Seal Fate 37–39, Mutilate 40, CdG 41–43, LR 44–45, Prec 46–48, PW 49–51, Opportunity 52–56, Imp. Poisons 57–60 | confirmed_forever (medium) |
| Assa Shank (endgame) | 21/30/0 | Igual hasta Cold Blood 25, Imp. Poisons 26–29, Venom 30, luego Combat: ES, CdG, Prec, Defl, Riposte, Composure, End 1, FE, WE, Aggr, BF, DWS, H&S 1, FoS 5 | confirmed_forever (medium) |

Curiosidad: la build de leveling de Method es Combat (con Puncturing Wounds) hasta el 22 y solo después pasa a Assassination.

## Rotación
| Variante | Prioridad | Estado |
|---|---|---|
| Poison Mutilate | Deadly + Instant → sigilo → Garrote → Shank en CD → SnD → Mutilate → (Expose Armor) → Eviscerate a 5 | confirmed_forever (medium) |
| Combat Shank | Igual con Riposte y Sinister Strike | confirmed_forever (medium) |
| Leveling (ForeverDB, 30) | Shank entre remates para mantener Venom; Cold Blood para un Eviscerate a 5 en un mob duro | confirmed_forever (medium) |

## Qué dicen las guías
- [[src-method-class-guides-assassination-rogue]], [[src-method-class-guides-assassination-rogue-talents]], [[src-method-class-guides-assassination-rogue-rotation-and-playstyle]].
- [[src-foreverdb-class-rogue-builds]]: leveling a 20 (Malice, RA, Ruthlessness, Lethality) y a 30 (+ Vigor, Cold Blood, Improved Poisons, Venom).
- [[src-blizzard-forum-beta-development-notes-november-2-2360696]] frente a [[src-blizzard-class-deep-dives-rogue-and-warlock-24310968]]: Venom pasivo (02-11) frente a remate (octubre).

## Fuentes
- [Data from ForeverDB.net](https://foreverdb.net)
| URL | Tipo | Fecha página | Consultada | ¿Pre-parche? |
|---|---|---|---|---|
| https://www.method.gg/wow-forever/class-guides/assassination-rogue | Guía Method | 2026-11-04 | 2026-11-13 | No |
| https://www.method.gg/wow-forever/class-guides/assassination-rogue/talents | Guía Method | 2026-11-04 | 2026-11-13 | No |
| https://www.method.gg/wow-forever/class-guides/assassination-rogue/rotation-and-playstyle | Guía Method | 2026-11-04 | 2026-11-13 | No |
| https://www.method.gg/wow-forever/wow-forever-rogue-leveling-guide-and-talents | Guía Method | 2026-11-07 | 2026-11-13 | No |
| https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json | Datos Method | 02-11 | 2026-11-13 | No |
| https://foreverdb.net/class/Rogue/talents | Datos de cliente | 2026-11-13 | 2026-11-13 | No |
| https://foreverdb.net/class/Rogue/builds | Builds | sin fecha | 2026-11-13 | No |
| https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696/9 | Notas oficiales | 2026-11-03 | 2026-11-13 | Es el parche |
| https://news.blizzard.com/en-us/article/24310968/world-of-warcraft-forever-class-deep-dives-rogue-and-warlock | Artículo oficial | ≈ 2026-10-07 | 2026-11-13 | Sí |

## Preguntas pendientes
- ¿Rinde Assassination antes del 40 frente a Combat? Sin datos.
