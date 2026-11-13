---
type: spec
tags: [forever, hunter, survival, endgame]
level_min: 10
level_max: 60
faction: both
status: confirmed_forever
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://www.method.gg/wow-forever/class-guides/survival-hunter
  - https://www.method.gg/wow-forever/class-guides/survival-hunter/talents
  - https://www.method.gg/wow-forever/class-guides/survival-hunter/rotation-and-playstyle
  - https://www.method.gg/wow-forever/class-guides/survival-hunter/bis-gear-and-stats
  - https://www.method.gg/wow-forever/class-guides/survival-hunter/enchants-and-consumables
  - https://www.method.gg/wow-forever/class-guides/survival-hunter/races-professions-and-other
  - https://www.method.gg/wow-forever/class-guides/survival-hunter/interface-addons-and-macros
  - https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json
  - https://foreverdb.net/class/Hunter/talents
related: ["[[Hunter]]", "[[Hunter-Leveling]]", "[[Beast-Mastery-Hunter]]", "[[Marksmanship-Hunter]]"]
---

# Survival Hunter

> [!success] Confirmado en Forever
> Guía de Method (Vareion, 2026-11-05, parche 1.60.1). Dos builds decodificadas. BiS "Work In Progress".

## Resumen
- **La spec más débil pero más original** de Hunter en PvE: cuerpo a cuerpo y distancia. Exige más trabajo para igualar a BM y MM. `confirmed_forever`
- No despega hasta el **30** (Strider Kick y Expose Prey); antes es un BM peor.
- Builds: **Ranged/Melee Weaving 15/10/26** (más daño, probablemente la mejor en endgame) y **Full Melee 16/10/25** (más fácil, con Summon Hawk y Counterattack).
- Hay que vigilar Improved Tracking (+5 % solo con el rastreo correcto) y gastar Expose Prey al momento.
- Stats como BM: **Agility = Intellect (con Careful Aim) > Strength**.

## Talentos

### Build "Ranged / Melee Weaving" (Method) — 15/10/26
| Nivel | Talento | Árbol |
|---|---|---|
| 10–14 | Improved Tracking 5/5 | Survival |
| 15–16 | Savage Strikes 2/2 | Survival |
| 17–19 | Survivalist 3/5 | Survival |
| 20 | Deterrence | Survival |
| 21–23 | Surefooted 3/3 | Survival |
| 24, 60 | Clever Traps 2/2 | Survival |
| 25–29 | Predator's Edge 5/5 | Survival |
| 30 | Strider Kick | Survival |
| 31–32 | Expose Prey 2/2 | Survival |
| 33–34 | Resourcefulness 2/2 | Survival |
| 35–39 | Lethal Attacks 5/5 | MM |
| 40–44 | Careful Aim 5/5 | MM |
| 45–49 | Deadly Aspects 5/5 | BM |
| 50–51 | Focused Fire 2/2 | BM |
| 52–53 | Improved Revive Pet 2/2 | BM |
| 54 | Endurance Training 1/5 | BM |
| 55–59 | Unleashed Fury 5/5 | BM |

### Build "Full Melee" (Method) — 16/10/25
Improved Tracking 5, Savage Strikes 2, Deflection 4 (17–19 y 24), Deterrence, Surefooted 3, Counterattack (25), Predator's Edge 4, Strider Kick (30), Expose Prey 2, Resourcefulness 2; luego Deadly Aspects 5, Focused Fire 2, Imp. Revive Pet 2, Endurance Training 1, Unleashed Fury 5, Summon Hawk (50), Lethal Attacks 5, Careful Aim 5.

- No se toma Lacerating Strikes (capstone): depende de procs de Expose Prey, demasiado aleatorios.
- Legacy: Reagent Economy, Gourmand, Permanence.

### Talentos clave (texto del cliente, ForeverDB)
| Talento | Efecto | Estado |
|---|---|---|
| Expose Prey (nuevo) | Ataques contra objetivos con Hunter's Mark: 10 % de habilitar Mongoose Bite | confirmed_forever |
| Strider Kick (nuevo) | Patada de 100 % de daño de arma y +30 % velocidad 3 s | confirmed_forever |
| Predator's Edge (nuevo) | +30 % bonus crítico cuerpo a cuerpo y +50 % daño de mano izquierda | confirmed_forever |
| Resourcefulness (nuevo) | −60 % maná de trampas y melé; crits dan 50 % de regeneración al lanzar 30 s | confirmed_forever |
| Savage Strikes | +4 % crit a todas las habilidades cuerpo a cuerpo | confirmed_forever |
| Surefooted | +3 % hit y −30 % duración de ralentizaciones | confirmed_forever |
| Improved Tracking | +5 % daño al tipo de criatura rastreado | confirmed_forever |
| Counterattack | Tras parar: 50 % de daño de arma + 26 e inmoviliza 5 s | confirmed_forever |

## Rotación
| Build | Prioridad (Method) | Estado |
|---|---|---|
| Antes del pull | Hunter's Mark, mascota alimentada, Trueshot Aura, rastreo correcto | confirmed_forever |
| Weaving | Mascota → Rapid Fire + racial → Aimed Shot → Multi-Shot → Raptor Strike y Strider Kick en CD → Mongoose Bite siempre que se pueda → Explosive Trap (área) / Immolation Trap (uno) | confirmed_forever |
| Full Melee | Igual, más Counterattack siempre que esté disponible | confirmed_forever |

- Expose Prey no acumula: gastar Mongoose Bite enseguida.
- Weaving puede requerir Frost Trap si la mascota pierde la amenaza.
- Mascota: jabalí; Tallstrider en endgame. Cuidado con la amenaza de las trampas de daño.

## Stats y equipo
- **Agility = Intellect > Strength** con Careful Aim.
- Pre-raid BiS, BiS, tier y trinkets: **desconocido** ("Work In Progress").

## Encantamientos y consumibles
- Tabla de encantamientos idéntica a [[Beast-Mastery-Hunter]].
- Flask of Natural Aggression (alt. **Flask of Natural Precision**, distinta de BM/MM), Elixir of Cunning, Poached Sunscale Salmon, Major Frenzy Potion.

## Razas y profesiones
- ~15 DPS entre razas. Tiers: **S Night Elf** · A Human, Skyborne, Troll, Orc · B Dwarf · C Tauren.
- Leatherworking + Skinning (PvE) o Engineering + Mining (PvP).

## Interfaz, addons y macros
- Mascota en pasivo con Shift+rueda. Macros: Auto Shot; Hunter's Mark + `/petattack`; Raptor Strike + Strider's Kick; Mongoose Bite + Counterattack. Sin addons.

## En grupo con un Rogue
Comparte el cuerpo a cuerpo con el Rogue y valora los mismos stats (Agility, crit), así que pueden competir por algunas piezas (inferido, Method no lo dice). Aporta mascota y trampas para control; sin buff para el Rogue.

## Qué dicen las guías
- [[src-method-class-guides-survival-hunter]], [[src-method-class-guides-survival-hunter-talents]], [[src-method-class-guides-survival-hunter-rotation-and-playstyle]], [[src-method-class-guides-survival-hunter-bis-gear-and-stats]], [[src-method-class-guides-survival-hunter-enchants-and-consumables]], [[src-method-class-guides-survival-hunter-races-professions-and-other]], [[src-method-class-guides-survival-hunter-interface-addons-and-macros]].
- [[Hunter]] marcaba Survival como "sin detalle": estas fichas lo completan.

## Fuentes
| URL | Tipo | Fecha de la página | Consultada | ¿Anterior al parche del 02-11? |
|---|---|---|---|---|
| https://www.method.gg/wow-forever/class-guides/survival-hunter (+ 6 subpáginas) | guide | 2026-11-05 | 2026-11-13 | No |
| https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json | datos de la calculadora (Method) | 2026-11-02 | 2026-11-13 | No |
| https://foreverdb.net/class/Hunter/talents | datos de cliente | sin fecha | 2026-11-13 | No |

[Data from ForeverDB.net](https://foreverdb.net)

## Preguntas pendientes
- ¿Qué armas cuerpo a cuerpo usa Survival? Method no lo dice.
- ¿Cuánta diferencia hay entre Weaving y Full Melee? Sin cifras.
