---
type: spec
tags: [forever, hunter, marksmanship, endgame]
level_min: 10
level_max: 60
faction: both
status: confirmed_forever
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://www.method.gg/wow-forever/class-guides/marksmanship-hunter
  - https://www.method.gg/wow-forever/class-guides/marksmanship-hunter/talents
  - https://www.method.gg/wow-forever/class-guides/marksmanship-hunter/rotation-and-playstyle
  - https://www.method.gg/wow-forever/class-guides/marksmanship-hunter/bis-gear-and-stats
  - https://www.method.gg/wow-forever/class-guides/marksmanship-hunter/enchants-and-consumables
  - https://www.method.gg/wow-forever/class-guides/marksmanship-hunter/races-professions-and-other
  - https://www.method.gg/wow-forever/class-guides/marksmanship-hunter/interface-addons-and-macros
  - https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json
  - https://foreverdb.net/class/Hunter/talents
related: ["[[Hunter]]", "[[Hunter-Leveling]]", "[[Beast-Mastery-Hunter]]", "[[Survival-Hunter]]"]
---

# Marksmanship Hunter

> [!success] Confirmado en Forever
> Guía de Method (Vareion, 2026-11-05, parche 1.60.1). Dos builds decodificadas. BiS "Work In Progress".

## Resumen
- Para Method, **probablemente la mejor spec de endgame** de Hunter: burst a distancia con capstone **Sniper Shot** (40). `confirmed_forever`
- Dos versiones: **Lone Wolf 5/33/13** (sin mascota, +20 % daño; probablemente la mejor en endgame) y **Pet Build 16/35/0**.
- Apertura: Rapid Fire + racial → Sniper Shot → Arcane Shot → Multi-Shot.
- Stats como BM: **Agility = Intellect (con Careful Aim) > Strength**.
- Razas S: Night Elf y Skyborne (Haste).

## Talentos

### Build "Lone Wolf" (Method) — 5/33/13
| Nivel | Talento | Árbol |
|---|---|---|
| 10–14 | Lethal Attacks 5/5 | MM |
| 15–19 | Careful Aim 5/5 | MM |
| 20 | Lone Wolf | MM |
| 21–23 | Hawk Eye 3/3 | MM |
| 24, 26 | Rapid Killing 2/2 | MM |
| 25 | Trueshot Aura | MM |
| 27–31 | Mortal Shots 5/5 | MM |
| 32–33 | Rapid Recuperation 2/2 | MM |
| 34, 41–42 | Barrage 3/3 | MM |
| 35–39 | Ranged Weapon Specialization 5/5 | MM |
| 40 | Sniper Shot | MM |
| 43–47 | Deadly Aspects 5/5 | BM |
| 48–52 | Improved Tracking 5/5 | Survival |
| 53–57 | Entrapment 5/5 | Survival |
| 58–60 | Surefooted 3/3 | Survival |

### Build "Pet" (Method) — 16/35/0
MM igual pero sin Lone Wolf: Lethal Attacks 5, Careful Aim 5, Hawk Eye 3, Rapid Killing 2, Trueshot Aura, Mortal Shots 5, Barrage 3, Rapid Recuperation 2, Ranged Weapon Spec. 5, Sniper Shot (40); luego Deadly Aspects 5, Focused Fire 2, Imp. Revive Pet 2, Endurance Training 1, Unleashed Fury 5, Bestial Swiftness, Efficiency 3/5.

- Para tener Lone Wolf antes, mover un punto de Rapid Killing.
- Improved Tracking solo da +5 % si rastreas el tipo de criatura correcto.
- Trueshot Aura: uno por raid; si no, punto a Efficiency. Legacy: Reagent Economy, Gourmand, Permanence.

### Talentos clave (texto del cliente, ForeverDB)
| Talento | Efecto | Estado |
|---|---|---|
| Lone Wolf (nuevo) | +20 % daño con todos los ataques sin mascota activa | confirmed_forever |
| Sniper Shot (nuevo) | Disparo de largo alcance (daño a distancia + 320) y +10 m de alcance a los 3 siguientes disparos 10 s | confirmed_forever |
| Careful Aim (nuevo) | +AP igual al 100 % de tu Intellect | confirmed_forever |
| Rapid Killing (nuevo) | Rapid Fire −2 min de CD; matar (o con Serpent Sting) da +20 % al siguiente disparo | confirmed_forever |
| Rapid Recuperation (nuevo) | Serpent Sting: 50 % de regeneración al lanzar 15 s (100 % al consumir Rapid Killing) | confirmed_forever |
| Mortal Shots | +30 % bonus crítico a distancia | confirmed_forever |
| Improved Tracking | +5 % daño al tipo de criatura rastreado | confirmed_forever |

## Rotación
| Build | Prioridad (Method) | Estado |
|---|---|---|
| Lone Wolf | Hunter's Mark + Trueshot Aura → Rapid Fire + racial → Sniper Shot → Arcane Shot → Multi-Shot | confirmed_forever |
| Pet | Hunter's Mark, mascota alimentada, Trueshot Aura → mascota → Rapid Fire + racial → Sniper Shot → Arcane Shot → Multi-Shot | confirmed_forever |

- Sin mascota, las trampas (Freezing, Frost) y Concussive Shot mantienen a los mobs lejos. Trampas en combate con CD compartido.
- Serpent Sting solo en jefes. Mascota (si la llevas): jabalí; Tallstrider en endgame.

## Stats y equipo
- **Agility = Intellect > Strength** con Careful Aim; sin él, Agility > Strength > Intellect.
- Pre-raid BiS, BiS, tier y trinkets: **desconocido** ("Work In Progress").

## Encantamientos y consumibles
- Tabla idéntica a [[Beast-Mastery-Hunter]]: Agility en arma (+ Biznicks 247x128 Accurascope), capa, muñecas, botas y collar; Greater Stats; cabeza, hombros y piernas TBD.
- Flask of Natural Aggression (alt. Natural Accuracy), Elixir of Cunning, Poached Sunscale Salmon, Major Frenzy Potion. Basado en la beta.

## Razas y profesiones
- ~15 DPS entre la mejor y la peor. Tiers: **S Night Elf, Skyborne** · A Human, Troll · B Dwarf, Orc · C Tauren.
- Leatherworking + Skinning (PvE) o Engineering + Mining (PvP).

## Interfaz, addons y macros
- Mascota en pasivo con Shift+rueda. Macros de Auto Shot, Hunter's Mark + `/petattack` y Raptor Strike + Mongoose Bite. Sin addons.

## En grupo con un Rogue
Burst a distancia y mucho control (trampas, Concussive Shot) si algo se suelta. Sin buff para el Rogue (Trueshot Aura es solo a distancia). Puede robar amenaza al tanque con el burst de apertura.

## Qué dicen las guías
- [[src-method-class-guides-marksmanship-hunter]], [[src-method-class-guides-marksmanship-hunter-talents]], [[src-method-class-guides-marksmanship-hunter-rotation-and-playstyle]], [[src-method-class-guides-marksmanship-hunter-bis-gear-and-stats]], [[src-method-class-guides-marksmanship-hunter-enchants-and-consumables]], [[src-method-class-guides-marksmanship-hunter-races-professions-and-other]], [[src-method-class-guides-marksmanship-hunter-interface-addons-and-macros]].
- Leveling: [[src-method-wow-forever-hunter-leveling-guide-and-talents]] usa BM y solo 20 puntos de MM.

## Fuentes
| URL | Tipo | Fecha de la página | Consultada | ¿Anterior al parche del 02-11? |
|---|---|---|---|---|
| https://www.method.gg/wow-forever/class-guides/marksmanship-hunter (+ 6 subpáginas) | guide | 2026-11-05 | 2026-11-13 | No |
| https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json | datos de la calculadora (Method) | 2026-11-02 | 2026-11-13 | No |
| https://foreverdb.net/class/Hunter/talents | datos de cliente | sin fecha | 2026-11-13 | No |

[Data from ForeverDB.net](https://foreverdb.net)

## Preguntas pendientes
- ¿Cuánto más hace Lone Wolf que la build con mascota? Sin cifras.
- BiS y armas: pendiente.
