---
type: spec
tags: [forever, druid, feral, cat, endgame]
level_min: 60
level_max: 60
faction: both
status: confirmed_forever
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://www.method.gg/wow-forever/class-guides/feral-dps-druid
  - https://www.method.gg/wow-forever/class-guides/feral-dps-druid/talents
  - https://www.method.gg/wow-forever/class-guides/feral-dps-druid/rotation-and-playstyle
  - https://www.method.gg/wow-forever/class-guides/feral-dps-druid/bis-gear-and-stats
  - https://www.method.gg/wow-forever/class-guides/feral-dps-druid/enchants-and-consumables
  - https://www.method.gg/wow-forever/class-guides/feral-dps-druid/races-professions-and-other
  - https://www.method.gg/wow-forever/class-guides/feral-dps-druid/interface-addons-and-macros
  - https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json
  - https://foreverdb.net/class/Druid/talents
related: ["[[Druid]]", "[[Druid-Leveling]]", "[[Feral-Tank-Druid]]", "[[Balance-Druid]]", "[[Restoration-Druid]]"]
---

# Feral DPS Druid

> [!success] Confirmado en Forever
> Guía de endgame de Method (Aprikat, 2026-11-04, parche 1.60.1). El autor avisa de que está incompleta. Builds decodificadas del widget. BiS sin publicar. Un dato choca con la guía de Feral Tank: el multiplicador del daño del arma (×1 frente a ×2,5). Está pendiente de registrar en [[Conflicts]].

## Resumen
- Gato de **sangrados y combo points**: Rake y Rip mantenidos, Shred de generador, Ferocious Bite con energía de sobra. Buen daño a un objetivo, poco cleave. `confirmed_forever`
- En Forever **el daño del arma cuenta para la zarpa**. Omen of Clarity es baseline y aparece Shifting Power (maná a energía), que sustituye al "powershifting" con Furor.
- Dos builds 9/32/10: **Mono Cat** (máximo daño) y **Cat/Bear Hybrid** (~95 % en ambos roles).
- Stats: **Weapon Damage > Strength > Agility > Hit (cap 8 %) > Expertise (cap 6,5 %) > Haste > Spirit**.
- Razas: Skyborne y Night Elf casi empatan (NE algo mejor en sims; Skyborne mucho mejor contra elementales); Tauren para tanque y PvP.
- **Leader of the Pack ahora es de toda la raid** (no se acumula con Moonkin Aura).

## Talentos

Decodificadas del widget de Method (datos 1.60.1-2nov; nombres de ForeverDB). Estado `confirmed_forever`.

Fijos en las dos (fuera de Feral): Genesis 5, Nature's Majesty 2, Nature's Reach 2 (+4 % hit, Method); Heart of the Wild 5, Naturalist 5 (+10 % daño).

| Talento (Feral) | Mono Cat | Hybrid | Efecto (ForeverDB / Method) |
|---|---|---|---|
| Ferocity | 5 | 5 | |
| Furor | 3 | — | Ya no da energía al cambiar a gato |
| Feral Swiftness | 2 | 2 | |
| Shredding Attacks | 3 | — | Mejora Shred |
| Feral Instinct | — | 3 | +30 % daño de Swipe |
| Thick Hide | — | 3 | Armadura |
| Savage Fury | 2 | 2 | |
| Feral Charge | 1 | 1 | Ahora con salto en gato que te deja detrás |
| Sharpened Claws | 2 | 2 | |
| Predatory Strikes | 3 | 3 | |
| Predatory Discipline | 1 | 1 | Ferocious Bite da el daño extra por energía sin gastarla |
| Blood Frenzy | 2 | — | Combo point doble en críticos de gato |
| Lacerate | — | 1 | Sangrado acumulable de oso |
| Leader of the Pack | 1 | 1 | Crit de raid |
| Natural Instinct | 2 | 2 | |
| Rend and Tear | 4 | 4 | +15 % daño cuerpo a cuerpo a objetivos sangrando (máx.) |
| Primal Bite | — | 1 | Ataque de oso con mucha amenaza |
| Shifting Power | 1 | 1 | Maná → energía |

Orden del widget:
- **Mono Cat**: Ferocity 10–14 → Furor 15–17 → Feral Swiftness 18–19 → Shredding Attacks 20–22 → Savage Fury 23–24 → Feral Charge 25 → Sharpened Claws 26–27 → Predatory Strikes 28–30 → Predatory Discipline 31 → Blood Frenzy 32–33 → Natural Instinct 34–35 → LotP 36 → Rend and Tear 37–40 → Shifting Power 41 → HotW 42–46 → Genesis 47–51 → Nature's Majesty 52–53 → Nature's Reach 54–55 → Naturalist 56–60.
- **Hybrid**: Ferocity 10–14 → Feral Swiftness 15–16 → Feral Instinct 17–19 → Savage Fury 20–21 → Feral Charge 22 → Sharpened Claws 23–24 → Lacerate 25 → Predatory Strikes 26–28 → Predatory Discipline 29 → LotP 30 → Natural Instinct 31–32 → Thick Hide 33–34 → Rend and Tear 35–38 → Thick Hide 39 → Primal Bite 40 → Shifting Power 41 → HotW 42–46 → Naturalist 47–51 → Genesis 52–56 → Nature's Majesty 57–58 → Nature's Reach 59–60.

Otros cambios que cita Method: Heart of the Wild da 10 % Strength en gato (antes 20 %); Feline Swiftness funciona en interiores; Nature's Grasp y Faerie Fire son baseline (Faerie Fire usable en todas las formas); Entangling Roots y Nature's Grasp funcionan en interiores.

Legacy útiles: Gourmand, Reagent Economy, The Quick and the Dead, Reinforce.

## Rotación

| Build | Prioridad (Method) | Estado |
|---|---|---|
| Mono Cat | Faerie Fire → Ferocious Bite a 4–5 CP si Rip ≥3 s y hay energía → Shifting Power si no desborda (≤55 energía) → Shred con Omen → Rip (mejor a 5 CP; a 4 CP escala igual con AP) → Rake sin sobrescribir → Shred (Claw si no estás detrás) | confirmed_forever |
| Hybrid OT | Faerie Fire → Shifting Power → Shred con Omen → Rip → Rake → Claw de relleno; Ferocious Bite casi nunca | confirmed_forever |
| AoE | Shifting Power bajo 55 energía → Rip a 5 CP en prioritarios → Rake en todos los posibles → Shred/Claw → Rip si sobran 5 CP | confirmed_forever |

| Umbral de Ferocious Bite | Mono Cat | Hybrid |
|---|---|---|
| 4 CP | 75 energía (45 con Clearcasting) | 90 energía |
| 5 CP | 70 (40 con Clearcasting) | 70 (35 con Clearcasting) |
| Ventana de Rip | ≥3 s | ≥4 s |

- No ponerse delante del enemigo (cleave y parry haste).

## Stats y equipo

| Stat | Equivalencia (Method, guía Feral DPS) |
|---|---|
| Weapon DPS | Zarpa = DPS del arma × 1 (conflicto: ×2,5 en [[Feral-Tank-Druid]]) |
| Strength | 1 = 2 AP (sube con HotW y Kings) |
| Agility | 1 = 1 AP; 20 = 1 % crit |
| Hit | 10 = 1 %; cap 8 % |
| Expertise | 10 = 1 % menos esquivas; cap 6,5 % |
| Haste | 10 = 1 % velocidad de ataque |

- Pre-raid BiS, BiS, tier y abalorios: **desconocido** (no se sabe qué equipo habrá).

## Encantamientos y consumibles
- Encantamientos (sin los nuevos de Forever): cabeza y piernas Lesser Arcanum of Voracity o Constitution; collar Agility o Strength; capa Lesser Agility; muñecas Greater Agility o Superior Strength; guantes Superior Strength o Superior Agility; pies Greater Agility; arma Crusader; pecho Forceful Rugged Armor Kit o Greater Stats.
- Consumibles: se acumulan por stat si no pisan un buff mejor. BiS: Steaming Stag Steak o Swiftstrike Steak; Dense Sharpening Stone o Weightstone; Elixir of the Grizzly, Mongoose, Owl, Whale, Fortitude, Major Troll's Blood; Juju Might; Flask of Natural Aggression; Goblin Sapper Charge; Mighty Rage Potion; Manual Crowd Pummeler; runas y Major Mana; Thistle Tea; buffs de Blasted Lands.

## Razas y profesiones
- Skyborne (Wind Blessed 2 % haste), Night Elf (Elune's Light +10 % crit 15 s, CD 3 min), Tauren (Endurance +5 % vida).
- Profesiones: el idol BiS de endgame se hace con **Enchanting**; el resto pendiente.

## Interfaz, addons y macros
- Leatrix Plus, DBM o BigWigs, Threat Classic 2 (sin probar).
- Macros: Feral Charge (Cat) + `[nostealth] Prowl`; power shift contra ralentizaciones; Travel/Aquatic/Cat según el entorno.

## En grupo con un Rogue
- **Leader of the Pack** da crit al Rogue y **Faerie Fire** reduce armadura (más daño físico). Ambos buscan cuero con Agility y Strength: se pisan el equipo. *Buffs según Method; el reparto de equipo es inferido.*

## Qué dicen las guías
- [[src-method-class-guides-feral-dps-druid]], [[src-method-class-guides-feral-dps-druid-talents]], [[src-method-class-guides-feral-dps-druid-rotation-and-playstyle]], [[src-method-class-guides-feral-dps-druid-bis-gear-and-stats]], [[src-method-class-guides-feral-dps-druid-enchants-and-consumables]], [[src-method-class-guides-feral-dps-druid-races-professions-and-other]], [[src-method-class-guides-feral-dps-druid-interface-addons-and-macros]].
- **Conflicto**: zarpa = DPS del arma × 1 (Aprikat) frente a × 2,5 (Perseis, [[src-method-class-guides-feral-tank-druid-bis-gear-and-stats]]). Mismo sitio y fecha. Se resuelve probándolo en el juego.
- La build Hybrid de esta guía (R&T 4, Nature's Majesty 2) difiere un poco de la Hybrid de la guía de tanque (R&T 5, Nature's Majesty 1).
- Coincide con [[Druid-Leveling]] en los puntos fijos de Balance (Genesis, Nature's Majesty, Nature's Reach) y en Heart of the Wild.

## Fuentes

| URL | Tipo | Fecha página | Consultada | ¿Pre-parche? |
|---|---|---|---|---|
| https://www.method.gg/wow-forever/class-guides/feral-dps-druid (+ 6 subpáginas) | Guía Method | 2026-11-04 | 2026-11-13 | No |
| https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json | Datos de la calculadora (Method) | 1.60.1 (02-11) | 2026-11-13 | No |
| https://foreverdb.net/class/Druid/talents | Datos de cliente | sin fecha | 2026-11-13 | No |

[Data from ForeverDB.net](https://foreverdb.net)

## Preguntas pendientes
- ¿Multiplicador del daño del arma en la zarpa: ×1 o ×2,5? ¿Cambia según la forma (gato u oso)? Sin confirmar.
- La tabla Hybrid pone "≤53 seconds" para Shifting Power: probable errata por energía.
