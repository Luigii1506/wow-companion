---
type: spec
tags: [forever, mage, frost, endgame]
level_min: 60
level_max: 60
faction: both
status: confirmed_forever
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://www.method.gg/wow-forever/class-guides/frost-mage
  - https://www.method.gg/wow-forever/class-guides/frost-mage/talents
  - https://www.method.gg/wow-forever/class-guides/frost-mage/rotation-and-playstyle
  - https://www.method.gg/wow-forever/class-guides/frost-mage/bis-gear-and-stats
  - https://www.method.gg/wow-forever/class-guides/frost-mage/enchants-and-consumables
  - https://www.method.gg/wow-forever/class-guides/frost-mage/races-professions-and-other
  - https://www.method.gg/wow-forever/class-guides/frost-mage/interface-addons-and-macros
  - https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json
  - https://foreverdb.net/class/Mage/talents
related: ["[[Mage]]", "[[Mage-Leveling]]", "[[Arcane-Mage]]", "[[Fire-Mage]]", "[[Mage-Comprehension]]"]
---

# Frost Mage

> [!success] Confirmado en Forever
> Guía de endgame de Method (Celz, 2026-11-09, parche 1.60.1). Builds decodificadas del widget con los datos de talentos 1.60.1 de Method y nombres de ForeverDB. BiS, encantamientos y consumibles siguen "Work in Progress". Una sola fuente: confianza media.

## Resumen
- Spec de **congelar o pescar procs de Fingers of Frost y gastar Ice Lance** (+300 % contra congelados, CD 8 s según Method). `confirmed_forever`
- Tres builds de 60: **CoC + Meditation (raid) 18/0/33**, **Incineration ST 14/5/32** y **Dungeon AoE + ST 9/5/37**.
- Winter's Chill cambia: lo aplican Frostbolt e Ice Lance potenciado y **potencia el siguiente Cone of Cold**, que por eso entra en la rotación a un objetivo.
- Stats: **Hit (17 % contra jefes) > Spell Damage > Crit > Haste > Intellect > Spell Piercing > Spirit > Stamina**.
- Razas: S Skyborne y Troll; A Gnome y Undead; B Human y Orc. Profesiones: Tailoring + Enchanting.
- El mejor defensivo de los Mage (Ice Block, Ice Barrier, Cold Snap), pero menos daño bruto que Arcane o Fire.

## Talentos

Builds de Method decodificadas del widget (ForeverTalentsData-1.60.1-2nov.json; nombres de ForeverDB). Estado: `confirmed_forever` (guía posterior al parche). Son de nivel 60: Method avisa que rinden peor subiendo; para leveling ver [[Mage-Leveling]].

| Talento | Raid (18/0/33) | ST (14/5/32) | Dungeon (9/5/37) | Efecto (ForeverDB / Method) |
|---|---|---|---|---|
| Improved Frostbolt | 5 | 5 | 5 | Frostbolt más rápido |
| Precision | 3 | 3 | 3 | Hit para todas las escuelas |
| Ice Shards | 5 | 5 | 5 | +100 % bonus de crítico Frost |
| Ice Lance | 1 | 1 | 1 | +300 % daño a congelados |
| Shatter | 3 | 3 | 3 | +50 % crit contra congelados |
| Fingers of Frost | 2 | 2 | 2 | 15 % de los Chill: los 2 siguientes hechizos tratan al objetivo como congelado |
| Winter's Chill | 5 | 5 | 5 | Sube el siguiente Cone of Cold (+20 % y +7 % spell damage por carga, Method) |
| Ice Block / Cold Snap | 1 / 1 | 1 / 1 | 1 / 1 | Defensivos |
| Ice Barrier | 1 | 1 | 1 | Escudo, +15 % daño Frost 1 min y +5 % mientras dura |
| Improved Cone of Cold | 3 | — | 3 | +35 % daño de Cone of Cold |
| Improved Blizzard | 1 | — | 3 | |
| Arctic Reach | 2 | — | — | +20 % alcance/radio Frost |
| Frost Channeling | — | 3 | 3 | |
| Improved Frost Nova | — | 2 | 1 | |
| Arcane Concentration | 5 | 5 | — | Clearcasting |
| Arcane Meditation | 3 | — | — | Regeneración de maná lanzando |
| Wand Spec. / Arcane Resilience / Magic Absorption / Arcane Geometry | 2 / 3 / 2 / 1 | — | — | Relleno del árbol Arcane |
| Improved Channeling / Arcane Subtlety | — / 2 | 5 / 2 | 5 / 2 | Subtlety reduce amenaza |
| Missile Barrage | — | 2 | 2 | Arcane Missiles rápido y gratis |
| Incineration (Fire) | — | 5 | 5 | +crit de Ice Lance |

Orden del widget (empieza en el 10):
- **Raid**: Imp. Frostbolt 10–14 → Precision 15–17 → Ice Shards 18–22 → Ice Lance 23 → Imp. Blizzard 24 → Arctic Reach 25–26 → Ice Block 27 → Shatter 28–30 → Imp. CoC 31–33 → Cold Snap 34 → FoF 35–36 → Winter's Chill 37–41 → Ice Barrier 42 → Wand Spec 43–44 → Arcane Resilience 45–47 → Arcane Subtlety 48–49 → Magic Absorption 50–51 → Arcane Concentration 52–56 → Arcane Geometry 57 → Arcane Meditation 58–60.
- **ST**: Imp. Channeling 10–14 → Arcane Subtlety 15–16 → Arcane Concentration 17–18 → Missile Barrage 19–20 → Arcane Concentration 21–23 → Incineration 24–28 → Imp. Frostbolt 29–33 → Precision 34–36 → Ice Shards 37–41 → Ice Lance 42 → Frost Channeling 43–45 → Ice Block 46 → Shatter 47–49 → Cold Snap 50 → FoF 51–52 → Imp. Frost Nova 53–54 → Winter's Chill 55–59 → Ice Barrier 60.
- **Dungeon**: Imp. Channeling 10–14 → Arcane Subtlety 15–16 → Missile Barrage 17–18 → Precision 19–21 → Imp. Frostbolt 22–26 → Ice Shards 27–31 → Frost Channeling 32–34 → Imp. Blizzard 35–37 → Ice Lance 38 → Ice Block 39 → Shatter 40–42 → Imp. Frost Nova 43 → Imp. CoC 44–46 → Cold Snap 47 → FoF 48–49 → Winter's Chill 50–54 → Ice Barrier 55 → Incineration 56–60.

> [!warning] Incoherencia en la guía
> El texto dice que Arcane Concentration va 5/5 en las tres builds, pero la build Dungeon decodificada no la lleva. Se muestra el widget tal cual.

## Rotación

| Build | Prioridad (Method, versión simple) | Estado |
|---|---|---|
| CoC + Meditation | Ice Barrier → maná (Mana Ruby, Evocation) → Ice Lance con FoF o congelado → Cone of Cold con 5 de Winter's Chill → Frostbolt | confirmed_forever |
| Incineration ST | Ice Barrier → maná → Ice Lance con FoF o congelado → Arcane Missiles con Missile Barrage → Frostbolt | confirmed_forever |
| Dungeon blend | La de raid + Arcane Missiles con Missile Barrage antes de Frostbolt | confirmed_forever |
| AoE (todas) | Flamestrike si es seguro (mucha amenaza) → Blizzard → Cone of Cold (con Winter's Chill) → Arcane Explosion; Frost Nova para posicionar | confirmed_forever |

- Avanzado: Ice Barrier si quedan >25 s; Mana Ruby bajo 80 % de maná; Evocation bajo 20 % con >25 s de combate; Ice Lance con 2 cargas de FoF (o 1 si hay un Frostbolt en vuelo); Fire Blast o Ice Lance si el combate acaba antes de un Frostbolt.
- Utilidad: Blink, Slow Fall (Light Feather), Polymorph, Counterspell, Frostbite, Ice Block + Cold Snap, Mage Armor (maná) o Ice Armor (defensa), Fire Ward, Mana Shield, Arcane Intellect, comida y agua, portales.

## Stats y equipo
- **Hit > Spell Damage > Crit > Haste > Intellect > Spell Piercing > Spirit > Stamina** (Method). Hit cap contra jefes de raid: **17 %**, igual que en [[src-method-how-does-hit-chance-work-in-wow-forever]].
- Spell Piercing sustituye a Spell Penetration en Forever. Spirit vale un poco más con Arcane Meditation.
- Pre-raid BiS, BiS, tier y abalorios: **desconocido** ("Work in Progress").

## Encantamientos y consumibles
- **Desconocido**: las dos secciones están en "Work in Progress". Como referencia de caster, ver [[Arcane-Mage]] (también vacío) o la lista general de Method en [[src-method-list-of-all-consumables-and-enchants-in-wow-forever]].

## Razas y profesiones

| Tier | Razas | Motivo (Method) |
|---|---|---|
| S | Skyborne, Troll | Wind Blessed (2 % haste), Read Leyline (no funciona en raid); Berserking (+10 % velocidad de lanzamiento) |
| A | Gnome, Undead | Eureka! (+10 % daño y −10 % coste en hechizos no periódicos 8 s); Touch of the Grave, Will of the Forsaken |
| B | Human, Orc | — |

- Profesiones (WIP): 1) **Tailoring + Enchanting**; 2) Alchemy + Herbalism; 3) Engineering + Mining.

## Interfaz, addons y macros
- Addons: EllesmereUI; DBM; Method Raid Tools + Nova Raid Companion para raid. Sin probar en el cliente.
- Macros: Polymorph al focus (`/cast [@focus,harm,nodead][] Polymorph`) y abalorios `/use 13`, `/use 14`.

## En grupo con un Rogue
- Frost Nova, Blizzard y Cone of Cold frenan a los enemigos mientras el Rogue pega, y Polymorph se suma a Sap como control. *Inferido de las herramientas que cita Method; no es una recomendación de la guía.*

## Qué dicen las guías
- Method es la única fuente por spec: [[src-method-class-guides-frost-mage]], [[src-method-class-guides-frost-mage-talents]], [[src-method-class-guides-frost-mage-rotation-and-playstyle]], [[src-method-class-guides-frost-mage-bis-gear-and-stats]], [[src-method-class-guides-frost-mage-enchants-and-consumables]], [[src-method-class-guides-frost-mage-races-professions-and-other]], [[src-method-class-guides-frost-mage-interface-addons-and-macros]].
- Discrepancia con la guía de leveling de Method ([[src-method-wow-forever-mage-leveling-guide-and-talents]], en [[Mage]]): allí se recomiendan Human, Gnome, Orc y Troll; en endgame Orc y Human quedan en B y Skyborne sube a S. Son contextos distintos.

## Fuentes

| URL | Tipo | Fecha página | Consultada | ¿Pre-parche? |
|---|---|---|---|---|
| https://www.method.gg/wow-forever/class-guides/frost-mage (+ 6 subpáginas) | Guía Method | 2026-11-09 | 2026-11-13 | No |
| https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json | Datos de la calculadora (Method) | 1.60.1 (02-11) | 2026-11-13 | No |
| https://foreverdb.net/class/Mage/talents | Datos de cliente (nombres y efectos) | sin fecha | 2026-11-13 | No |

[Data from ForeverDB.net](https://foreverdb.net)

## Preguntas pendientes
- ¿Lleva la build Dungeon Arcane Concentration (texto) o no (widget)?
- Pre-raid BiS, encantamientos y consumibles: pendientes de Method.
