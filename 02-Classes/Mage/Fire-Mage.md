---
type: spec
tags: [forever, mage, fire, endgame]
level_min: 60
level_max: 60
faction: both
status: confirmed_forever
confidence: medium
last_verified: 2026-11-15
game_version: "Forever 1.60.1"
sources:
  - https://www.method.gg/wow-forever/class-guides/fire-mage
  - https://www.method.gg/wow-forever/class-guides/fire-mage/talents
  - https://www.method.gg/wow-forever/class-guides/fire-mage/rotation-and-playstyle
  - https://www.method.gg/wow-forever/class-guides/fire-mage/bis-gear-and-stats
  - https://www.method.gg/wow-forever/class-guides/fire-mage/enchants-and-consumables
  - https://www.method.gg/wow-forever/class-guides/fire-mage/races-professions-and-other
  - https://www.method.gg/wow-forever/class-guides/fire-mage/interface-addons-and-macros
  - https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json
  - https://foreverdb.net/class/Mage/talents
  - https://foreverdb.net/guide/leveling-mage
  - https://foreverdb.net/class/Mage
related: ["[[Mage]]", "[[Mage-Leveling]]", "[[Frost-Mage]]", "[[Arcane-Mage]]"]
---

# Fire Mage

> [!success] Confirmado en Forever
> Guía de endgame de Method (Celz, 2026-11-09, parche 1.60.1). Builds decodificadas del widget. BiS, encantamientos y consumibles: "Work in Progress". Una sola fuente: confianza media.

## Resumen
- Spec de **crit**: Heating Up acorta Pyroblast un 25 % por cada crítico no periódico (hasta 3 cargas) e **Ignite es ahora personal** (un debuff por Mage). `confirmed_forever`
- Builds de 60: **Fireball / Arcane 16/32/3** (con Combustion) y **Frostfire + Shatter 0/29/22**.
- Mantener **5 cargas de Fire Vulnerability** (Improved Scorch: +3 % de daño Fire por carga, 30 s).
- Stats: **Hit (17 %) > Spell Damage > Crit > Haste > Spell Piercing > Intellect > Spirit > Stamina**. Necesita mucho crit en el equipo.
- Razas: S Gnome; A Human, Troll y Undead; B Orc y Skyborne.
- Débil cambiando de objetivo (sus debuffs son gran parte del daño) y con menos utilidad defensiva.

## Talentos

Decodificadas del widget de Method (datos 1.60.1-2nov; nombres de ForeverDB). Estado `confirmed_forever`.

| Talento | Fireball / Arcane (16/32/3) | Frostfire + Shatter (0/29/22) | Efecto (ForeverDB / Method) |
|---|---|---|---|
| Incineration | 5 | 5 | +10 % crit de Fire Blast, Scorch, Arcane Blast, Ice Lance |
| Accelerant | 5 | 5 | −0,5 s a Fireball y Frostfire Bolt |
| Ignite | 5 | 5 | DoT en los críticos Fire (personal) |
| Pyroblast / Heating Up | 1 / 1 | 1 / 1 | Heating Up: −25 % lanzamiento de Pyroblast por crítico, 3 cargas; Fire Blast da una extra |
| Improved Fire Blast | 2 | 2 | −2 s de CD y +15 m de alcance (Method) |
| Improved Scorch | 3 | 3 | Fire Vulnerability |
| Critical Mass | 3 | 3 | Crit Fire; requisito de Combustion |
| Fire Power | 3 | 3 | +3 % por efecto Fire en el objetivo, máx. 12 % (no cuentan escuelas mixtas) |
| Master of Elements | 3 | 1 | Devuelve maná en críticos Fire y Frost |
| Combustion | 1 | — | Críticos garantizados en la ventana de burst |
| Arcane (Imp. Channeling 5, Subtlety 2, Concentration 5, Missile Barrage 2, Arcane Blast 1, Meditation 1) | ✓ | — | Mantener 1 carga de Arcane Blast por el spell damage |
| Precision (Frost) | 3 | 3 | Hit |
| Frost Warding 2, Ice Shards 5, Frostbite 2, Frost Channeling 3, Ice Lance, Ice Block, Shatter 3, Fingers of Frost 2 | — | ✓ | Frostfire Bolt cuenta como Fire y Frost; Ice Lance es el requisito para llegar a FoF |

Orden del widget:
- **Fireball / Arcane**: Precision 10–12 → Incineration 13–17 → Accelerant 18–22 → Ignite 23–27 → Pyroblast 28 → Imp. Fire Blast 29–30 → Master of Elements 31–32 → Heating Up 33 → Critical Mass 34–36 → Imp. Scorch 37–39 → Fire Power 40–42 → Combustion 43 → Imp. Channeling 44–48 → Arcane Subtlety 49–50 → Arcane Concentration 51–55 → Missile Barrage 56–57 → Arcane Blast 58 → Arcane Meditation 59 → Master of Elements 60.
- **Frostfire + Shatter**: Incineration 10–14 → Accelerant 15–19 → Ignite 20–24 → Pyroblast 25 → Imp. Fire Blast 26–27 → Heating Up 28 → Master of Elements 29 → Imp. Scorch 30–32 → Critical Mass 33–35 → Fire Power 36–38 → Frost Warding 39–40 → Precision 41–43 → Ice Shards 44–48 → Frostbite 49–50 → Frost Channeling 51–53 → Ice Lance 54 → Ice Block 55 → Shatter 56–58 → FoF 59–60.

## Rotación

| Build | Prioridad (Method, simple) | Estado |
|---|---|---|
| Fireball / Arcane | Maná → Combustion → Scorch hasta 5 de Fire Vulnerability → Arcane Blast para mantener 1 carga → Pyroblast con 3 de Heating Up → Fire Blast → Arcane Missiles con Missile Barrage → Fireball | confirmed_forever |
| Frostfire + Shatter | Maná → Scorch (5 cargas) → Pyroblast con 3 de Heating Up → Fire Blast con FoF → Frostfire Bolt con FoF → Fire Blast → Frostfire Bolt | confirmed_forever |

- Avanzado: Mana Ruby bajo 80 %, Evocation bajo 10 %; Combustion con 5 de Fire Vulnerability junto a raciales, pociones y lust; Scorch rango 1 con poco maná.
- Method no da rotación AoE para Fire. Blast Wave sirve de daze en mazmorras.

## Stats y equipo
- **Hit > Spell Damage > Crit > Haste > Spell Piercing > Intellect > Spirit > Stamina**. Hit cap contra jefes: **17 %**. Spirit vale algo más en Fireball / Arcane (Arcane Meditation). Spell Piercing también contra resistencia Frost en la build Frostfire.
- Pre-raid BiS, BiS, tier y abalorios: **desconocido** ("Work in Progress").

## Encantamientos y consumibles
- **Desconocido** ("Work in Progress").

## Razas y profesiones

| Tier | Razas | Motivo |
|---|---|---|
| S | Gnome | Eureka!, Expansive Mind |
| A | Human, Troll, Undead | Human: Ruthless (+1 % crit con todo) y The Human Spirit (+10 % Spirit) |
| B | Orc, Skyborne | — |

- Recomendadas: Human o Gnome (Alliance), Undead o Troll (Horde). Profesiones (WIP): Tailoring + Enchanting; alternativas Alchemy + Herbalism o Engineering + Mining.

## Interfaz, addons y macros
- Mismos addons que Frost/Arcane (EllesmereUI, DBM, Method Raid Tools, Nova Raid Companion; sin probar). Macros: Polymorph al focus y **Combustion + abalorios** en un botón (`/use Combustion`, `/use 13`, `/use 14`).

## En grupo con un Rogue
- Fire hace mucho daño a un objetivo pero tarda en montar sus debuffs. Rinde más si el grupo se queda en un objetivo y no cambia constantemente. *Inferido de la debilidad que cita Method.*

## Qué dicen las guías
- [[src-method-class-guides-fire-mage]], [[src-method-class-guides-fire-mage-talents]], [[src-method-class-guides-fire-mage-rotation-and-playstyle]], [[src-method-class-guides-fire-mage-bis-gear-and-stats]], [[src-method-class-guides-fire-mage-enchants-and-consumables]], [[src-method-class-guides-fire-mage-races-professions-and-other]], [[src-method-class-guides-fire-mage-interface-addons-and-macros]].
- Skyborne queda en B para Fire pero en S para Frost y Arcane (misma guía y autor; el motivo no se explica en la página de Fire).

## Fuentes

| URL | Tipo | Fecha página | Consultada | ¿Pre-parche? |
|---|---|---|---|---|
| https://www.method.gg/wow-forever/class-guides/fire-mage (+ 6 subpáginas) | Guía Method | 2026-11-09 | 2026-11-13 | No |
| https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json | Datos de la calculadora (Method) | 1.60.1 (02-11) | 2026-11-13 | No |
| https://foreverdb.net/class/Mage/talents | Datos de cliente | sin fecha | 2026-11-13 | No |
| https://foreverdb.net/guide/leveling-mage, https://foreverdb.net/class/Mage | Guía y simulador ForeverDB | 2026-11-05 / 2026-11-13 | 2026-11-15 | No |

[Data from ForeverDB.net](https://foreverdb.net)

## Preguntas pendientes
- ¿Cuánto crit hace falta para que Fire supere a Arcane/Frost? Method no da cifra.
- Rotación AoE de Fire: no publicada.

## Datos de ForeverDB (leveling y simulador)
Añadido el 2026-11-15 de [[src-foreverdb-guide-leveling-mage]] y [[src-foreverdb-class-mage]]. `confirmed_forever` (talentos del cliente; simulador propio)
- Build leveling 20 "Fireball leveling": Accelerant 5, Incineration 2, Ignite 3, Pyroblast 1. A 30 "Heating Up leveling": Accelerant 5, Improved Fire Blast 2, Incineration 3, Ignite 5, Pyroblast 1, Heating Up 1, Master of Elements 3, Blast Wave 1.
- Fire Blast solo llega a 20 yd (26 con Flame Throwing); Improved Fire Blast 2/2 le suma 15 yd y −2 s de CD (desde el 31-10 está en la fila 3, nivel 20).
- Heating Up (antes Hot Streak): cada crítico de Fireball, Fire Blast o Scorch acelera un 25 % el siguiente Pyroblast (3 cargas, 20 s), y cada Fire Blast que impacta añade una carga.
- Simulador: a 20–29 el daño es ≈ Fireball 78 % y Fire Blast 19 %; a 60 Scorch vale un 11 % del DPS. Pyroblast R1 hace menos daño que en Classic (95–125 + 44).
