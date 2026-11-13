---
type: spec
tags: [forever, mage, arcane, endgame]
level_min: 60
level_max: 60
faction: both
status: confirmed_forever
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://www.method.gg/wow-forever/class-guides/arcane-mage
  - https://www.method.gg/wow-forever/class-guides/arcane-mage/talents
  - https://www.method.gg/wow-forever/class-guides/arcane-mage/rotation-and-playstyle
  - https://www.method.gg/wow-forever/class-guides/arcane-mage/bis-gear-and-stats
  - https://www.method.gg/wow-forever/class-guides/arcane-mage/enchants-and-consumables
  - https://www.method.gg/wow-forever/class-guides/arcane-mage/races-professions-and-other
  - https://www.method.gg/wow-forever/class-guides/arcane-mage/interface-addons-and-macros
  - https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json
  - https://foreverdb.net/class/Mage/talents
related: ["[[Mage]]", "[[Mage-Leveling]]", "[[Frost-Mage]]", "[[Fire-Mage]]"]
---

# Arcane Mage

> [!success] Confirmado en Forever
> Guía de endgame de Method (Celz, 2026-11-09, parche 1.60.1). Builds decodificadas del widget. BiS, encantamientos y consumibles: "Work in Progress". Una sola fuente: confianza media.

## Resumen
- En Forever Arcane es una spec de daño completa: **Arcane Blast se acumula** (cada lanzamiento da 12 % del Intellect como spell damage y dobla su coste, según ForeverDB) y se gasta en un hechizo fuerte. `confirmed_forever`
- Builds de 60: **Arcane / Pyroblast 32/16/3** y **Pure Arcane 38/10/3**.
- Burst dentro de **Arcane Power** con 4 cargas de Arcane Blast; Missile Barrage da Arcane Missiles rápidos y gratis.
- Stats: **Hit (17 %) > Spell Damage > Crit > Spell Piercing > Haste > Intellect > Spirit > Stamina**.
- Razas: S Gnome y Skyborne; A Human, Undead y Troll; B Orc.
- Muy exigente en maná y estática (casi todo con tiempo de lanzamiento); defensivos peores que Frost.

## Talentos

Decodificadas del widget de Method (datos 1.60.1-2nov; nombres de ForeverDB). Estado `confirmed_forever`. Para leveling ver [[Mage-Leveling]].

| Talento | Arcane / Pyro (32/16/3) | Pure Arcane (38/10/3) | Efecto (ForeverDB / Method) |
|---|---|---|---|
| Improved Channeling | 5 | 5 | Arcane Missiles, Arcane Blast y Arcane Wrath resisten el retroceso |
| Arcane Subtlety | 2 | 2 | −resistencias y −30 % amenaza Arcane |
| Arcane Concentration | 5 | 5 | Clearcasting |
| Missile Barrage | 2 | 2 | Arcane Missiles rápido y gratis |
| Arcane Impact | 3 | 3 | +6 % crit Arcane |
| Arcane Blast | 1 | 1 | Filler acumulable |
| Arcane Meditation | 3 | 3 | Regeneración lanzando |
| Arcane Wrath | 1 | 1 | Nuke con +5 % del maná máximo como spell damage |
| Presence of Mind | 1 | 1 | |
| Arcane Mind | 5 | 5 | +10 % Intellect y +100 % bonus de crítico Arcane |
| Arcane Instability | 3 | 3 | +3 % daño y +3 % crit |
| Arcane Power | 1 | 1 | Ventana de burst |
| Wand Spec. / Arcane Geometry / Imp. Counterspell | — | 2 / 2 / 2 | Puntos flexibles (Method: mejor Improved Flamestrike si se busca AoE) |
| Incineration (Fire) | 5 | 5 | +10 % crit de Arcane Blast, entre otros |
| Accelerant (Fire) | 2 | 5 | −0,5 s a Arcane Wrath en máx. |
| Ignite / Pyroblast / Imp. Fire Blast / Heating Up | 5 / 1 / 2 / 1 | — | Pyroblast potenciado por Heating Up y Arcane Blast |
| Precision (Frost) | 3 | 3 | Hit |

Orden del widget:
- **Arcane / Pyro**: Imp. Channeling 10–14 → Arcane Subtlety 15–16 → Arcane Concentration 17–21 → Missile Barrage 22–23 → Arcane Blast 24 → Arcane Wrath 25 → Arcane Meditation 26–28 → Arcane Impact 29–31 → PoM 32 → Arcane Mind 33–37 → Arcane Instability 38–40 → Arcane Power 41 → Accelerant 42 → Incineration 43–47 → Accelerant 48 → Ignite 49–53 → Pyroblast 54 → Imp. Fire Blast 55–56 → Heating Up 57 → Precision 58–60.
- **Pure Arcane**: Precision 10–12 → Imp. Channeling 13–17 → Incineration 18–22 → Accelerant 23–27 → Arcane Subtlety 28–29 → Arcane Concentration 30–34 → Missile Barrage 35–36 → Arcane Geometry 37–38 → Arcane Impact 39–41 → Arcane Blast 42 → Arcane Meditation 43–45 → Arcane Wrath 46 → PoM 47 → Arcane Mind 48–52 → Arcane Instability 53–55 → Arcane Power 56 → Wand Spec 57–58 → Imp. Counterspell 59–60.

## Rotación

| Build | Prioridad (Method) | Estado |
|---|---|---|
| Arcane / Pyro (simple) | Arcane Power → Pyroblast con 3 de Heating Up y 4 de Arcane Blast → Fire Blast → Arcane Missiles con Missile Barrage → PoM para Arcane Wrath o Pyroblast → Arcane Wrath con 4 cargas → Arcane Blast si hay maná → maná (Mana Ruby, Evocation) → varita | confirmed_forever |
| Pure Arcane | Arcane Power (con maná y hechizos listos) → PoM + Arcane Wrath con 4 cargas → Arcane Wrath con 4 cargas → Arcane Missiles con Missile Barrage → Arcane Blast si hay maná → varita | confirmed_forever |
| AoE | Arcane Explosion en bucle; Flamestrike previo si compensa la amenaza | confirmed_forever |

- La versión avanzada de Arcane / Pyro añade condiciones de tiempo sobre Heating Up (lanzar Pyroblast si va a caducar o si Fire Blast vuelve en <1,5 s) y Evocation bajo 15 % de maná con >20 s.
- Mage Armor casi siempre. Ice Block, Fire Ward y Mana Shield como defensivos.

## Stats y equipo
- **Hit > Spell Damage > Crit > Spell Piercing > Haste > Intellect > Spirit > Stamina**. Hit cap contra jefes: **17 %** ([[src-method-how-does-hit-chance-work-in-wow-forever]]). Haste sirve para meter más hechizos en Arcane Power.
- Pre-raid BiS, BiS, tier y abalorios: **desconocido** ("Work in Progress").

## Encantamientos y consumibles
- **Desconocido** ("Work in Progress" en las dos secciones).

## Razas y profesiones

| Tier | Razas |
|---|---|
| S | Gnome, Skyborne |
| A | Human, Undead, Troll |
| B | Orc |

- Recomendadas: Skyborne o Gnome (Alliance), Undead o Troll (Horde). Raciales descritas en [[Frost-Mage]].
- Profesiones (WIP): Tailoring + Enchanting; alternativas Alchemy + Herbalism o Engineering + Mining.

## Interfaz, addons y macros
- EllesmereUI, DBM, Method Raid Tools + Nova Raid Companion (sin probar). Macros de Polymorph al focus y de abalorios 13/14.

## En grupo con un Rogue
- Arcane hace burst a un objetivo y su AoE es Arcane Explosion a melee, así que comparte zona con el Rogue. Polymorph se suma a Sap. *Inferido; Method no habla de composiciones.*

## Qué dicen las guías
- [[src-method-class-guides-arcane-mage]], [[src-method-class-guides-arcane-mage-talents]], [[src-method-class-guides-arcane-mage-rotation-and-playstyle]], [[src-method-class-guides-arcane-mage-bis-gear-and-stats]], [[src-method-class-guides-arcane-mage-enchants-and-consumables]], [[src-method-class-guides-arcane-mage-races-professions-and-other]], [[src-method-class-guides-arcane-mage-interface-addons-and-macros]].
- La guía de leveling ([[src-method-wow-forever-mage-leveling-guide-and-talents]]) termina con 18 puntos en Arcane; las builds de endgame van mucho más hondo (32–38).

## Fuentes

| URL | Tipo | Fecha página | Consultada | ¿Pre-parche? |
|---|---|---|---|---|
| https://www.method.gg/wow-forever/class-guides/arcane-mage (+ 6 subpáginas) | Guía Method | 2026-11-09 | 2026-11-13 | No |
| https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json | Datos de la calculadora (Method) | 1.60.1 (02-11) | 2026-11-13 | No |
| https://foreverdb.net/class/Mage/talents | Datos de cliente | sin fecha | 2026-11-13 | No |

[Data from ForeverDB.net](https://foreverdb.net)

## Preguntas pendientes
- BiS, encantamientos y consumibles: pendientes de Method.
- ¿Cuánto maná cuesta la cuarta carga de Arcane Blast? No hay cifra base en las fuentes leídas.
