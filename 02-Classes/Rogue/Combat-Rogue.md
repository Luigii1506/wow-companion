---
type: spec
tags: [forever, rogue, combat]
level_min: 10
level_max: 60
faction: both
status: confirmed_forever
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://www.method.gg/wow-forever/class-guides/combat-rogue
  - https://foreverdb.net/class/Rogue/pvp
  - https://foreverdb.net/buffs-and-nerfs/rogue
  - https://www.method.gg/wow-forever/class-guides/combat-rogue/talents
  - https://www.method.gg/wow-forever/class-guides/combat-rogue/rotation-and-playstyle
  - https://www.method.gg/wow-forever/wow-forever-rogue-leveling-guide-and-talents
  - https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json
  - https://foreverdb.net/class/Rogue/talents
  - https://foreverdb.net/class/Rogue/builds
  - https://theforeverera.com/es/guides/classes/rogue/
  - https://theforeverera.com/es/bis/rogue/combat/20/
  - https://theforeverera.com/es/bis/rogue/combat/30/
  - https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696/9
related: ["[[Rogue]]", "[[Rogue-Leveling]]", "[[Assassination-Rogue]]", "[[Subtlety-Rogue]]", "[[Rogue-Gear-and-Stats]]", "[[Rogue-Poisons]]"]
---

# Combat Rogue

> [!success] Confirmado en Forever
> Árbol del cliente 1.60.1 (parche del 02-11). Builds de Method (Reholy, 04-11 y 07-11) decodificadas del widget; guías de ForeverDB y The Forever Era coinciden en usarla para subir.

## Resumen
- **La spec de leveling** del Orc: Sinister Strike desde cualquier ángulo y con cualquier arma 1M; Riposte, Blade Flurry (30) y Adrenaline Rush (40). `confirmed_forever` (medium)
- Dos variantes: **Sinister Strike** (sin dagas) y **Backstab** (con daga en mano principal y Puncturing Wounds).
- Daño de autoataque: depende poco de venenos y sangrados; buen cleave con Blade Flurry. Débil en tiempos muertos y utilidad.
- Hack and Slash cambia según arma: hacha o espada = ataque extra (siempre de mano principal); daga o puño = +5 % crit en esa ranura; maza = ignora 15 % de armadura (en ambas armas).
- Rotación endgame: Garrote → Riposte → Shank en CD con < 5 CP → SS o Backstab → SnD a 5 → (Expose Armor si no hay Sunder) → Eviscerate a 5.

## Talentos clave
| Talento | Fila | Efecto (cliente) | Estado |
|---|---|---|---|
| Coup de Grace | 1 | +20 % daño de Eviscerate (y Death Mark) | confirmed_forever (high) |
| Efficient Strikes | 1 | −5 energía Sinister Strike y Hemorrhage | confirmed_forever (high) |
| Precision | 2 | +3 % hit (también venenos) | confirmed_forever (high) |
| Deflection → Riposte | 2 → 3 | +6 % parry; Riposte 150 % daño y desarma 6 s | confirmed_forever (high) |
| Puncturing Wounds | 2 | Backstab +30 % crit y 45 % de CP extra (variante dagas) | confirmed_forever (high) |
| Endurance | 3 | −60 % CD de Sprint y Evasion | confirmed_forever (high) |
| Composure | 3 | +10 a la reducción de Poised | confirmed_forever (high) |
| Flawless Execution | 4 | Eviscerate −15 energía | confirmed_forever (high) |
| Aggression | 4 | +15 % SS y Eviscerate (ya no Backstab) | confirmed_forever (high) |
| Weapon Expertise | 4 | −2 % esquiva y parada del objetivo | confirmed_forever (high) |
| Blade Flurry | 5 | +20 % velocidad y golpea a un segundo objetivo 15 s | confirmed_forever (high) |
| Dual Wield Spec. / Hack and Slash | 5 | +50 % daño de mano izquierda / bono por arma | confirmed_forever (high) |
| Flash of Steel | 6 | Shank +15 energía y −2 s de CD | confirmed_forever (high) |
| Adrenaline Rush | 7 | +100 % regeneración de energía 15 s | confirmed_forever (high) |

## Builds de Method (decodificadas)
| Build | Reparto | Orden (nivel) | Estado |
|---|---|---|---|
| Leveling (guía de leveling) | 16/35/0 | RA 10–11, ES 12–13, CdG 14–16, Defl 17–19, Prec 20–21, Riposte 22, Prec 23, End 24–25, LR 26, FE 27, Aggr 28–30, WE 31, BF 32, WE 33, DWS 34–35, H&S 36–40, FoS 41, AR 42, luego Assassination | confirmed_forever (medium) |
| Sinister Strike (endgame) | 15/36/0 | ES 10–11, CdG 12–14, Prec 15–17, Defl 18–20, Riposte 21, End 22–23, Composure 24–25, FE 26, WE 27–28, Aggr 29–31, BF 32, H&S 33–37, DWS 38–39, AR 40, FoS 41–45, Malice 5, Imp. SnD 3, Ruthl. 2, Blood Splatter, Vigor 2, Lethality 2 | confirmed_forever (medium) |
| Backstab (endgame) | 13/33/5 | CdG 10–12, LR 13–14, Prec 15–17, PW 18–20, End 21–22, FE 23, WE 24–25, Aggr 26–28, BF 29, H&S 30–34, FoS 35–38, DWS 39–40, AR 41, Malice 5, Imp. SnD 3, Ruthl. 2, Lethality 2, Opportunity 5, FoS, Blood Splatter | confirmed_forever (medium) |

ForeverDB publica builds a 20/30/40/50/60 sin orden por punto ([[Rogue-Leveling]]).

## Armas
| Nivel | Mano derecha | Mano izquierda | Fuente | Estado |
|---|---|---|---|---|
| 20 | Cruel Barb (Deadmines) | "Hoja de asesino" (SFK; nombre en inglés no dado) | The Forever Era BiS 20 | probable_classic (drops de Classic) |
| 30 | "Puño de Dorsacerado" (maza, SM; no estaba en la beta) | Bloody Brass Knuckles (puño, SM) | The Forever Era BiS 30 | probable_classic |

The Forever Era: mano derecha lenta (más daño por Sinister Strike), izquierda rápida (más procs).

ForeverDB (2026-11-13) ha registrado en Forever el drop de Cruel Barb (VanCleef, 40 % de 15 muertes), Assassin's Blade (Nandos, SFK, 14 % de 7) y Bloody Brass Knuckles (Vishas, SM, 20 % de 10): las tres existen en el servidor aunque no estén en el cliente. `confirmed_forever` (medium). Más en [[Dungeons-1-30]].

## PvP (ForeverDB)
- Combat es el Rogue que castiga a los melés: Deflection da paradas y Riposte desarma tras una parada; contra casters, Kick al heal (bloquea esa escuela 5 s), Gouge y Eviscerate rápido.
- A 30 la build PvP añade Endurance (Evasion y Sprint más a menudo) e Improved Sprint (limpia ralentizaciones).
- Slice and Dice es opcional en PvP; en muertes rápidas todo a Eviscerate. Con espada, maza, hacha o puño se pega desde cualquier ángulo con Sinister Strike.
- Pesos PvP propios: DPS de arma 3,5, hit 1,2, Agility 1, Stamina 0,9, crit 0,9, expertise 0,9, dodge 0,5, parry 0,2.
- Cambios recientes que tocan a Combat: Flawless Execution (−15 de energía a Eviscerate), Adrenaline Rush ahora exige Blade Flurry, Aggression y Weapon Expertise bajan a nivel 25 (build del 04-11).

## Qué dicen las guías
- [[src-method-class-guides-combat-rogue]], [[src-method-class-guides-combat-rogue-talents]], [[src-method-class-guides-combat-rogue-rotation-and-playstyle]]: builds y rotación endgame.
- [[src-method-wow-forever-rogue-leveling-guide-and-talents]]: build de leveling.
- [[src-foreverdb-class-rogue-builds]], [[src-foreverdb-class-rogue-talents]]: valores del cliente y builds por nivel.
- [[src-theforeverera-es-guides-classes-rogue]], [[src-theforeverera-es-bis-rogue-combat-20]], [[src-theforeverera-es-bis-rogue-combat-30]]: Combat del 10 al 60; pesos de stats; BiS algorítmico.
- [[src-blizzard-forum-beta-development-notes-november-2-2360696]]: cambios de talentos del lanzamiento.
- [[src-foreverdb-class-rogue-pvp]] y [[src-foreverdb-buffs-and-nerfs-rogue]]: PvP y cambios por build.
- Discrepancia menor: ForeverDB a 30 toma Lightning Reflexes 2 y Blade Flurry; Method toma Composure o Remorseless Attacks y retrasa Blade Flurry a 32.

## Fuentes
- [Data from ForeverDB.net](https://foreverdb.net)
| URL | Tipo | Fecha página | Consultada | ¿Pre-parche? |
|---|---|---|---|---|
| https://www.method.gg/wow-forever/class-guides/combat-rogue | Guía Method | 2026-11-04 | 2026-11-13 | No |
| https://www.method.gg/wow-forever/class-guides/combat-rogue/talents | Guía Method | 2026-11-04 | 2026-11-13 | No |
| https://www.method.gg/wow-forever/class-guides/combat-rogue/rotation-and-playstyle | Guía Method | 2026-11-04 | 2026-11-13 | No |
| https://www.method.gg/wow-forever/wow-forever-rogue-leveling-guide-and-talents | Guía Method | 2026-11-07 | 2026-11-13 | No |
| https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json | Datos Method | 02-11 | 2026-11-13 | No |
| https://foreverdb.net/class/Rogue/talents | Datos de cliente | 2026-11-13 | 2026-11-13 | No |
| https://foreverdb.net/class/Rogue/builds | Builds | sin fecha | 2026-11-13 | No |
| https://foreverdb.net/class/Rogue/pvp | Guía PvP | build 70938 | 2026-11-13 | No |
| https://foreverdb.net/buffs-and-nerfs/rogue | Cambios por build | 2026-11-13 | 2026-11-13 | No |
| https://theforeverera.com/es/guides/classes/rogue/ | Guía fan (es) | 2026-10-25 | 2026-11-13 | Sí (cuerpo) |
| https://theforeverera.com/es/bis/rogue/combat/20/ | BiS algorítmico | 2026-11-13 | 2026-11-13 | No |
| https://theforeverera.com/es/bis/rogue/combat/30/ | BiS algorítmico | sin fecha | 2026-11-13 | Desconocido |
| https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696/9 | Notas oficiales | 2026-11-03 | 2026-11-13 | Es el parche |

## Preguntas pendientes
- ¿Compensa Remorseless Attacks a 10–11 frente a Coup de Grace? Sin datos medidos.
- Nombres en inglés de "Hoja de asesino" y "Puño de Dorsacerado".
