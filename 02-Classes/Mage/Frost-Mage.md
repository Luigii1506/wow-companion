---
type: spec
tags: [forever, mage, frost, endgame]
level_min: 60
level_max: 60
faction: both
status: confirmed_forever
confidence: medium
last_verified: 2026-11-15
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
  - https://foreverdb.net/class/Mage/builds
  - https://foreverdb.net/class/Mage
  - https://foreverdb.net/class/Mage/pve
  - https://foreverdb.net/class/Mage/pvp
  - https://foreverdb.net/bis/mage/frost
  - https://foreverdb.net/buffs-and-nerfs/mage
related: ["[[Mage]]", "[[Mage-Leveling]]", "[[Arcane-Mage]]", "[[Fire-Mage]]", "[[Mage-Comprehension]]", "[[Playbook-Mage-1-20]]", "[[Playbook-Mage-20-30]]"]
---

# Frost Mage

> [!success] Confirmado en Forever
> Guía de endgame de Method (Celz, 2026-11-09, parche 1.60.1). Builds decodificadas del widget con los datos de talentos 1.60.1 de Method y nombres de ForeverDB. BiS, encantamientos y consumibles de Method siguen "Work in Progress"; desde 2026-11-15 se añaden las builds, el BiS, el simulador y la guía PvP de ForeverDB (datos de cliente y ranking propio).

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
- Method: [[src-method-class-guides-frost-mage]], [[src-method-class-guides-frost-mage-talents]], [[src-method-class-guides-frost-mage-rotation-and-playstyle]], [[src-method-class-guides-frost-mage-bis-gear-and-stats]], [[src-method-class-guides-frost-mage-enchants-and-consumables]], [[src-method-class-guides-frost-mage-races-professions-and-other]], [[src-method-class-guides-frost-mage-interface-addons-and-macros]].
- ForeverDB: [[src-foreverdb-class-mage-builds]] (builds por nivel), [[src-foreverdb-bis-mage-frost]] (BiS 60), [[src-foreverdb-class-mage]] (simulador), [[src-foreverdb-class-mage-pve]], [[src-foreverdb-class-mage-pvp]], [[src-foreverdb-buffs-and-nerfs-mage]].
- Discrepancia de builds de 60: Method mezcla Arcane (18/0/33) o Fire (14/5/32, 9/5/37); ForeverDB propone Frost casi puro (48 en Frost + 3 Incineration) para leveling a 60 y otra build de mazmorra con Arcane Concentration.
- Discrepancia de stats: Method pone Haste por encima de Intellect; los pesos de BiS de ForeverDB ponen hit 1,1 y **mp5 1,1** por encima del spell power, y su simulador valora Spirit casi como el hit a 60.
- Discrepancia con la guía de leveling de Method ([[src-method-wow-forever-mage-leveling-guide-and-talents]], en [[Mage]]): allí se recomiendan Human, Gnome, Orc y Troll; en endgame Orc y Human quedan en B y Skyborne sube a S. Son contextos distintos.

## Fuentes

| URL | Tipo | Fecha página | Consultada | ¿Pre-parche? |
|---|---|---|---|---|
| https://www.method.gg/wow-forever/class-guides/frost-mage (+ 6 subpáginas) | Guía Method | 2026-11-09 | 2026-11-13 | No |
| https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json | Datos de la calculadora (Method) | 1.60.1 (02-11) | 2026-11-13 | No |
| https://foreverdb.net/class/Mage/talents | Datos de cliente (nombres y efectos) | sin fecha | 2026-11-13 | No |
| https://foreverdb.net/class/Mage/builds, /pve, /pvp, /class/Mage | ForeverDB (cliente y simulador) | 2026-11-13 | 2026-11-15 | No |
| https://foreverdb.net/bis/mage/frost | BiS ForeverDB (orígenes de Classic salvo vendedores) | 2026-11-13 | 2026-11-15 | No |
| https://foreverdb.net/buffs-and-nerfs/mage | Cambios por build | 2026-11-04 | 2026-11-15 | Incluye beta |

[Data from ForeverDB.net](https://foreverdb.net)

## Preguntas pendientes
- ¿Lleva la build Dungeon Arcane Concentration (texto) o no (widget)?
- Pre-raid BiS, encantamientos y consumibles: pendientes de Method. ForeverDB ya publica un BiS de 60 (abajo) con orígenes casi todos de Classic.
- Si el slow de Frostbolt cuenta como Chill para Frostbite y Fingers of Frost (ForeverDB lo deja abierto).

## Builds de ForeverDB por nivel
De [[src-foreverdb-class-mage-builds]]. Los niveles 40–60 no se jugaron en la beta. `confirmed_forever` (talentos del cliente)

| Nivel | Leveling | Mazmorra | PvP |
|---|---|---|---|
| 20 | Imp. Frostbolt 5, Imp. Frost Nova 2, Frostbite 3, Ice Lance | Imp. Frostbolt 5, Precision 3, Ice Shards 2, Ice Lance | Imp. Frostbolt 3, Frost Warding 2, Imp. Frost Nova 2, Frostbite 3, Ice Lance |
| 30 | + Frost Channeling 3, Imp. Blizzard 1, Shatter 3, Ice Block, Arctic Reach 1, Fingers of Frost 1 | (Frost Channeling para la amenaza) | + Ice Block, Shatter, Cold Snap |
| 40 | + Ice Shards 5, Imp. Cone of Cold 2, Cold Snap, Fingers of Frost 2, Ice Barrier | con Ice Barrier | con Ice Barrier |
| 50 | + Precision 3, Permafrost 3, Imp. Blizzard 3, Arctic Reach 2, Imp. Cone of Cold 3, Frost Warding 2 | — | con Winter's Chill |
| 60 | 48 en Frost + Incineration 3 | con Arcane Concentration | — |

## Simulador de ForeverDB (Frost)
Patrones del simulador, no una rotación probada ([[src-foreverdb-class-mage]]):
- Evocation bajo 15 % de maná; Ice Lance cuando salta Fingers of Frost (≈2 veces por minuto a 30–59); Frostbolt de relleno.
- Reparto de daño: 20–29 ≈ Frostbolt 87 % y Fire Blast 13 %; 60 ≈ Frostbolt 66 %, Fire Blast 15 %, Ice Lance 10 %; la wand vale un 7,5 % del DPS a 60.
- A 60 y a 40–49 hace más daño **sin** Fire Blast a un objetivo; a 20–39 también, aunque la guía de clase lo usa (lo marcan como especulación).
- Pesos por punto a 60 (1 SP = 1): hit 1,63, Spirit 1,61, Intellect 1,31. Mejor consumible: Greater Arcane Elixir (+2,7 %), luego Elixir of Greater Intellect.

## BiS de 60 según ForeverDB (PvE)
De [[src-foreverdb-bis-mage-frost]]; ranking propio de ForeverDB, orígenes de Classic salvo vendedores vistos en Forever. `probable_classic`

| Ranura | Objeto | Origen |
|---|---|---|
| Cabeza | Spellweaver's Turban | General Drakkisath, UBRS (25 %, Classic) |
| Cuello | Charm of the Shifting Sands | *The Fall of Ossirian* (Classic) |
| Hombros | Mantle of the Timbermaw | Tailoring 290 |
| Espalda | Arcanoweave Cloak | Pix Xizzix, Stranglethorn (28.5, 75.8), visto en Forever |
| Pecho / Cintura | Robe of the Archmage / Belt of the Archmage | Tailoring 295 |
| Muñecas | Dryad's Wrist Bindings | Illiyana Moonblaze, Ashenvale (61.5, 83.8), 8g 75s 49c, visto en Forever |
| Manos | General's Silk Gauntlets (Horde) | Origen desconocido |
| Piernas / Pies | Bloodvine Leggings / Bloodvine Boots | Tailoring 300 |
| Anillos | Ring of the Fallen God; Seal of the Damned | Misión AQ (Classic); Naxxramas (Classic) |
| Abalorios | Weakness Analyzer; Warmth of Forgiveness | Pix Xizzix (visto en Forever); Naxxramas |
| Arma | Atiesh (alternativa: Elemental Mage Staff) | Classic |
| Wand | Wand of Biting Cold | *The Legend of Korrak* (Horde, Classic) |

Encantamientos que propone: Enchant Bracer – Greater Spellpower, Enchant Gloves – Frost Power, Enchant 2H Weapon – Spellblasting, Enchant Necklace – Spell Power (Enchanting 210, nuevo en Forever); Mystic Rugged Armor Kit en pecho, piernas y pies.

## PvP Frost (ForeverDB)
- Frost Nova (hasta 8 s) → 2–3 Ice Lance antes de que se rompa → salir; Frostbolt entre congelaciones; Fire Blast en movimiento. Desde 30, Cold Snap da una segunda Frost Nova.
- Frost Warding 2/2 sube un 30 % la armadura de Frost Armor (útil contra Rogue y Warrior).
- En campos de batalla: defensor de banderas y puntos; Polymorph al sanador al empezar la pelea. Ver [[src-foreverdb-class-mage-pvp]].
