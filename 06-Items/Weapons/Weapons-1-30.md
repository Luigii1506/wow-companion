---
type: topic
tags: [forever, items, weapons, leveling]
level_min: 1
level_max: 30
faction: both
status: confirmed_forever
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources: ["https://www.method.gg/wow-forever/the-best-weapons-in-wow-forever-from-levels-1-30", "https://www.method.gg/wow-forever/itemization-updates-in-world-of-warcraft-forever-expertise-spell-damage-more", "Cliente WoW Forever 1.60.1.70938 vía wago.tools (consulta local, 2026-11-13)"]
related: ["[[Priest-Wands]]", "[[Itemization]]", "[[Dungeons-1-30]]", "[[Priest-Gear-and-Stats]]", "[[Leveling-Route-Undead]]"]
---

# Armas de leveling 1-30

> [!success] Confirmado en Forever
> Lista de una sola fuente (Method, 2026-11-06, posterior al lanzamiento). Los nombres y orígenes son de Forever; **los stats no están en la fuente ni verificados en Wowhead Forever**.

## Resumen
- En Forever las mejoras de arma durante el leveling pesan más que en Classic, y las armas de nivel ~10 traen bonus de daño y sanación ([[Itemization]]).
- El equipo de sanación en Forever también da poder con hechizos: un Priest puede usar tanto la lista de "poder con hechizos" como la de "sanación".
- **Para un Undead Priest en Tirisfal (nv ~9):** la misión **Leonid's Letter** da a elegir Mug of Muddled Memories (maza 1M de hechizos, nv 10); después **The Family Crypt** da Darkwood Staff (bastón de hechizos, nv 13). Ambas en Tirisfal Glades.
- Wands: ver [[Priest-Wands]]. La primera wand de misión Horde en Tirisfal es Riptear's Spare Arm (Rear Guard Patrol, nv 13).
- Mazmorras nuevas de Forever aparecen como fuente: Hall of Thanes, Ruins of Lordaeron, Excavation Site: Wetlands, Dalaran ([[Dungeons-1-30]]).

## Qué puede usar un Priest
Bastones, mazas de una mano, dagas, sostener en mano izquierda (off-hand) y wands (conocimiento general del juego, no de la fuente). No escudos, espadas, hachas, puños ni armas de fuego/arcos. Columna "Útil para Priest": **Sí** = tipo usable, de hechizos/sanación y accesible para Horde; **Usable** = el Priest puede equiparla pero no aporta stats de lanzador (inferido); **No** = tipo no usable o solo Alliance.

> [!info] Datos del cliente (cliente 1.60.1.70938)
> Columna "Cliente": tablas DB2 del cliente WoW Forever build 1.60.1.70938 (wago.tools, extraídas 2026-11-13; ItemSparse, Item, ItemSubClass). Son datos de los archivos del juego, no del servidor: un objeto puede cambiar por hotfix. Calidad y ranura: etiquetas de enums públicos de Blizzard; nombres de stats: `Enum.BonusStatIndex` del propio cliente (solo el nombre, sin cantidad); "req" solo si el cliente da nivel requerido distinto de 0; "vel." = ItemDelay en segundos; "venta" = SellPrice para vendedor, no subasta. Blizzard oculta en el cliente ~40 % de los objetos de Forever hasta que se descubren: "no está en el cliente" no prueba que no exista. El poder con hechizos implícito de las armas de lanzador puede venir de un flag (ItemConsts `CASTER_WEAPON_*`) y no aparecer como stat.

## Armas de poder con hechizos
Nivel = el que da Method (no aclara si es requerido o de objeto). Estado de todas las filas: `confirmed_forever` (Method).

| Nv | Objeto | Tipo | Facción | Origen | Útil para Priest | Cliente (1.60.1.70938) |
|---|---|---|---|---|---|---|
| 7 | Makeshift Stormcaller | Bastón | Horde | Misión Stormy Potential, Durotar | Sí (Durotar) | ID 281274 · Uncommon · ilvl 11 · Two-Hand · Staves · vel. 3.30 · venta 0 · liga al recoger · stats: Intellect |
| 7 | Apprentice's Spellstaff | Bastón | Alliance | Misión Rare Books, Elwynn Forest | No (Alliance) | ID 248008 · Uncommon · ilvl 12 · Two-Hand · Staves · vel. 2.20 · venta 6s 1c · liga al recoger · stats: Intellect |
| 10 | **Mug of Muddled Memories** | Maza 1M | Horde | Misión Leonid's Letter, Tirisfal Glades | **Sí: siguiente mejora** | ID 277247 · Uncommon · ilvl 12 · Main Hand · One-Handed Maces · vel. 2.80 · venta 0 · liga al recoger · stats: Spirit, Intellect |
| 12 | Thornroot Club | Maza 1M | Alliance | Misión Ursal the Mauler, Teldrassil | No (Alliance) | ID 5587 · Uncommon · ilvl 13 · Main Hand · One-Handed Maces · vel. 2.10 · venta 5s 12c · liga al recoger · stats: Stamina |
| 13 | **Darkwood Staff** | Bastón | Horde | Misión The Family Crypt, Tirisfal Glades | **Sí** | ID 3446 · Uncommon · ilvl 13 · Two-Hand · Staves · vel. 3.20 · venta 5s 92c · liga al recoger · stats: Stamina |
| 13 | Oakthrush Staff | Bastón | Alliance | Misión The Fragments Within, Darkshore | No (Alliance) | ID 15397 · Uncommon · ilvl 14 · Two-Hand · Staves · vel. 2.80 · venta 7s 31c · liga al recoger · stats: Stamina, Intellect |
| 13 | Fang of Magmatus | Daga | Ambas | Mazmorra: Magmatus, Hall of Thanes | Sí | no está en el cliente (posible objeto oculto) |
| 15 | Buckler of the Seas | Escudo | Alliance | Misión The Coastal Menace, Westfall | No | ID 1557 · Uncommon · ilvl 20 · Shield · Shields · venta 9s 18c · liga al recoger · stats: SpellPower, Spirit |
| 16 | Staff of Orgrimmar | Bastón | Horde | Misión de mazmorra Hidden Enemies, Ragefire Chasm | Sí | no está en el cliente (posible objeto oculto) |
| 16 | Buzzer Blade | Daga | Ambas | Mazmorra: Sneed, The Deadmines | Sí | no está en el cliente (posible objeto oculto) |
| 17 | Monastic Hammer | Maza 1M | Alliance | Misión Red Silk Bandanas, Deadmines | No (Alliance) | no está en el cliente (posible objeto oculto) |
| 17 | Scepter of the Abandoned | Maza 1M | Ambas | Mazmorra: The Abandoned, Ruins of Lordaeron | Sí | no está en el cliente (posible objeto oculto) |
| 17 | Emberstone Staff | Bastón | Ambas | Mazmorra: Captain Greenskin, Deadmines | Sí | no está en el cliente (posible objeto oculto) |
| 18 | Keen Skinning Knife | Daga | Horde | Misión Unwelcome Guests, The Barrens | Sí | ID 269716 · Uncommon · ilvl 18 · Main Hand · Daggers · vel. 1.50 · venta 5s 82c · liga al recoger · stats: Intellect, SkinningSkill |
| 18 | Pathfinder's Clearway | Hacha 1M | Horde | Misión Wrongly Blamed, Justly Corrected, The Barrens | No (hacha) | ID 277288 · Uncommon · ilvl 23 · req 1 · Main Hand · One-Handed Axes · vel. 2.30 · venta 0 · liga al recoger · stats: Intellect, Stamina |
| 19 | Seedcloud Buckler | Escudo | Ambas | Mazmorra: Verdan the Everliving, Wailing Caverns | No | no está en el cliente (posible objeto oculto) |
| 21 | Blade of Silverlaine | Espada 1M | Ambas | Mazmorra: Baron Silverlaine, Shadowfang Keep | No (espada) | no está en el cliente (posible objeto oculto) |
| 22 | Gnarled Necromancer's Staff | Bastón | Horde | Misión The Wrath of Rath'mael, Tirisfal Glades (ver dudas) | Sí | no está en el cliente (posible objeto oculto) |
| 23 | Staff of the Purifier | Bastón | Alliance | Misión The Tower of Althalaxx, Ashenvale | No (Alliance) | ID 5613 · Uncommon · ilvl 23 · Two-Hand · Staves · vel. 3.70 · venta 26s 35c · liga al recoger · stats: Spirit |
| 24 | Fallen Dragon's Scepter | Bastón | Alliance | Misión Stopping the Cycle, Wetlands | No (Alliance) | ID 281312 · Rare · ilvl 32 · Two-Hand · Staves · vel. 3.40 · venta 0 · liga al recoger · stats: Intellect, Spirit |
| 24 | Hornbeam Heft | Hacha 1M | Alliance | Misión de mazmorra Horrors in the Highland, Wetlands | No | ID 271664 · Uncommon · ilvl 33 · One-Hand · One-Handed Axes · vel. 2.40 · venta 16c · liga al recoger · stats: Strength |
| 24 | Rod of the Sleepwalker | Bastón | Ambas | Mazmorra: Twilight Lord Kelris, Blackfathom Deeps | Sí | no está en el cliente (posible objeto oculto) |
| 26 | Debt Collector | Espada 1M | Alliance | Mazmorra: Bazil Thredd, Stormwind Stockade | No | no está en el cliente (posible objeto oculto) |
| 26 | Raptor's Gaze | Off-hand | Ambas | Mazmorra: Shadetooth, Excavation Site: Wetlands | Sí | no está en el cliente (posible objeto oculto) |
| 27 | Hydrocane | Bastón | Ambas | Mazmorra: Viscous Fallout, Gnomeregan | Sí | no está en el cliente (posible objeto oculto) |
| 28 | Spine of the Devourer | Bastón | Ambas | Mazmorra: Mana Devourer, Dalaran | Sí | no está en el cliente (posible objeto oculto) |
| 30 | Swinetusk Shank | Daga | Ambas | Mazmorra: Agathelos the Raging, Razorfen Kraul | Sí | no está en el cliente (posible objeto oculto) |

## Armas de sanación

| Nv | Objeto | Tipo | Facción | Origen | Útil para Priest | Cliente (1.60.1.70938) |
|---|---|---|---|---|---|---|
| 10 | Skyseeker's Greatstaff | Bastón | Ambas | BoE del raro Den'dralass, isla Skyborne; también subasta | Sí (subasta) | no está en el cliente (posible objeto oculto) |
| 13 | Trogg Scepter | Maza mano derecha | Horde | Mazmorra: Oggleflint, Ragefire Chasm | Sí | no está en el cliente (posible objeto oculto) |
| 15 | Staff of Nobles | Bastón | Ambas | BoE del raro Brainwashed Noble, Westfall; también subasta | Sí (subasta) | no está en el cliente (posible objeto oculto) |
| 15 | The Stitcher | Maza mano derecha | Horde | Misión de mazmorra Light's Justice (zona no indicada) | Sí | no está en el cliente (posible objeto oculto) |
| 16 | Kris of Orgrimmar | Daga | Horde | Misión de mazmorra Hidden Enemies, Ragefire Chasm | Sí | no está en el cliente (posible objeto oculto) |
| 18 | Taskmaster Axe | Hacha 2M | Ambas | Mazmorra: Sneed, Deadmines | No (hacha) | no está en el cliente (posible objeto oculto) |
| 18 | Living Root | Bastón | Ambas | Mazmorra: Verdan the Everliving, Wailing Caverns | Sí | no está en el cliente (posible objeto oculto) |
| 18 | Staff of Westfall | Bastón | Alliance | Misión de mazmorra The Defias Brotherhood | No (Alliance) | no está en el cliente (posible objeto oculto) |
| 21 | Odo's Ley Staff | Bastón | Ambas | Mazmorra: Odo the Blindwatcher, Shadowfang Keep | Sí | no está en el cliente (posible objeto oculto) |
| 22 | Reef Axe | Hacha 2M | Ambas | Mazmorra: Gelihast, Blackfathom Deeps | No (hacha) | no está en el cliente (posible objeto oculto) |
| 24 | Healer's Staff | Bastón | Ambas | Misión de mazmorra Earthen Echo / Prehistoric Prism, Excavation Site: Wetlands | Sí | ID 271767 · Rare · ilvl 33 · Two-Hand · Staves · vel. 2.60 · venta 16c · liga al recoger · stats: Stamina, ManaRegeneration |
| 28 | Death Speaker Scepter | Maza mano derecha | Ambas | Mazmorra: Death Speaker Jargba, Razorfen Kraul | Sí | no está en el cliente (posible objeto oculto) |

## Wands
Detalle y análisis para Priest en [[Priest-Wands]]. Resumen de lo que lista Method:

| Nv | Objeto | Facción | Origen | Útil para Priest | Cliente (1.60.1.70938) |
|---|---|---|---|---|---|
| 1 | Novice's Practice Wand | Ambas | Encantamiento (fabricada) | Sí (subasta) | ID 247789 · Common · ilvl 6 · req 1 · Ranged (gun/crossbow/wand) · Wands · vel. 1.50 · venta 5c · liga al equipar |
| 13 | Riptear's Spare Arm | Horde | Misión Rear Guard Patrol, Tirisfal Glades | Sí | no está en el cliente (posible objeto oculto) |
| 13 | Elven Wand | Alliance | Misión Bashal'Aran, Darkshore | No (Alliance) | ID 5604 · Uncommon · ilvl 13 · Ranged (gun/crossbow/wand) · Wands · vel. 1.60 · venta 3s 80c · liga al recoger · stats: Intellect |
| 13 | Greater Magic Wand | Ambas | Encantamiento (fabricada) | Sí (subasta) | ID 11288 · Uncommon · ilvl 23 · req 13 · Ranged (gun/crossbow/wand) · Wands · vel. 1.80 · venta 2s · liga al equipar · stats: SpellPower |
| 15 | Cinder Wand | Horde | Misión Arugal's Folly, Silverpine Forest | Sí | ID 5242 · Uncommon · ilvl 16 · Ranged (gun/crossbow/wand) · Wands · vel. 1.40 · venta 6s 23c · liga al recoger · stats: SpellPower |
| 15 | Torchlight Wand | Alliance | Misión The Coastal Menace, Westfall | No (Alliance) | ID 5240 · Uncommon · ilvl 21 · Ranged (gun/crossbow/wand) · Wands · vel. 1.30 · venta 12s 44c · liga al recoger · stats: SpellPower |
| 17 | Cookie's Stirring Rod | Ambas | Mazmorra: Cookie, Deadmines | Sí | no está en el cliente (posible objeto oculto) |
| 27 | Gravestone Scepter | Horde | Misión de mazmorra Blackfathom Villainy | Sí | no está en el cliente (posible objeto oculto) |
| 27 | Wand of Mana Concentration | Ambas | Mazmorra: Arcanic Enigma, Dalaran | Sí | no está en el cliente (posible objeto oculto) |
| 28 | Charred Wand | Horde | Misión Dangerous!, Hillsbrad Foothills | Sí | ID 5250 · Uncommon · ilvl 28 · Ranged (gun/crossbow/wand) · Wands · vel. 1.80 · venta 26s 46c · liga al recoger · stats: Intellect, SpellPower |
| 30 | Necrotic Wand | Ambas | Raro de mazmorra: Azshir the Sleepless, Scarlet Monastery Graveyard | Sí | no está en el cliente (posible objeto oculto) |

## Cuerpo a cuerpo
Armas de daño físico. Para un Priest solo dagas, mazas 1M y bastones son equipables, sin valor de lanzador (inferido).

| Nv | Objeto | Tipo | Facción | Origen | Útil para Priest | Cliente (1.60.1.70938) |
|---|---|---|---|---|---|---|
| 10 | Tim's Lost Rib | Daga | Horde | Misión Leonid's Letter, Tirisfal Glades | Usable (mejor elegir Mug) | ID 282064 · Uncommon · ilvl 12 · Main Hand · Daggers · vel. 1.70 · venta 0 · liga al recoger · stats: Agility, Stamina |
| 10 | Coldridge Hammer | Maza 2M | Alliance | Misión Protecting the Herd, Dun Morogh | No | ID 3103 · Uncommon · ilvl 12 · Two-Hand · Two-Handed Maces · vel. 2.70 · venta 4s 66c · liga al recoger · stats: Strength, Spirit |
| 11 | Jagged Dagger | Daga | Horde | Misión Skull Rock, Durotar | Usable | ID 4947 · Uncommon · ilvl 11 · One-Hand · Daggers · vel. 1.50 · venta 3s 25c · liga al recoger · stats: Strength |
| 11 | Steady Bastard Sword | Espada 2M | Horde | Misión Skull Rock, Durotar | No | ID 4939 · Uncommon · ilvl 11 · Two-Hand · Two-Handed Swords · vel. 2.70 · venta 3s 95c · liga al recoger · stats: Agility |
| 12 | Balanced Fighting Stick | Bastón | Alliance | Misión WANTED: "Hogger", Elwynn Forest | No (Alliance) | ID 6215 · Uncommon · ilvl 13 · Two-Hand · Staves · vel. 2.20 · venta 6s 1c · liga al recoger · stats: Agility, Stamina |
| 13 | Durgen's Crescent Axe | Hacha 1M | Alliance | Mazmorra: Durgen Dirgehammer, Hall of Thanes | No | no está en el cliente (posible objeto oculto) |
| 13 | Cursed Felblade | Espada 1M | Horde | Mazmorra: Taragaman the Hungerer, Ragefire Chasm | No | no está en el cliente (posible objeto oculto) |
| 13 | Bone Knuckles | Puño | Horde | Mazmorra: Oggleflint, Ragefire Chasm | No | no está en el cliente (posible objeto oculto) |
| 15 | Segmented Spider Leg | Bastón | Ambas | Mazmorra: Witherfang, Ruins of Lordaeron | Usable | no está en el cliente (posible objeto oculto) |
| 15 | Meathook Slicer | Daga | Ambas | Mazmorra: The Baron, Ruins of Lordaeron | Usable | no está en el cliente (posible objeto oculto) |
| 15 | Forsaken Greataxe | Hacha 2M | Horde | Misión de mazmorra The Wrath of Rath'mael, Ruins of Lordaeron | No | no está en el cliente (posible objeto oculto) |
| 16 | Ironforge Greathammer | Maza 2M | Alliance | Misión de mazmorra Old Ironforge Incursion, Hall of Thanes | No | no está en el cliente (posible objeto oculto) |
| 16 | Axe of Orgrimmar | Hacha 2M | Horde | Misión de mazmorra Hidden Enemies, Ragefire Chasm | No | no está en el cliente (posible objeto oculto) |
| 17 | Impaling Harpoon | Arma de asta | Ambas | Mazmorra: Captain Greenskin, Deadmines | No | no está en el cliente (posible objeto oculto) |
| 17 | Cell Keeper's Claws | Puño | Ambas | Mazmorra: Rethilgore, Shadowfang Keep | No | no está en el cliente (posible objeto oculto) |
| 18 | Smite's Mighty Hammer | Maza 2M | Ambas | Mazmorra: Mr. Smite, Deadmines | No | no está en el cliente (posible objeto oculto) (solo existe 10756 «Monster - Mace2H, Smite's Mighty Hammer», arma de PNJ, no el objeto) |
| 18 | Butcher's Slicer | Espada 1M | Ambas | Mazmorra: Razorclaw the Butcher, Shadowfang Keep | No | no está en el cliente (posible objeto oculto) |
| 19 | Cruel Barb | Espada 1M | Ambas | Mazmorra: Edwin VanCleef, Deadmines | No | no está en el cliente (posible objeto oculto) |
| 23 | Graverobber's Shovel | Maza 2M | Alliance | Mazmorra: Dextren Ward, Stormwind Stockade | No | no está en el cliente (posible objeto oculto) |
| 23 | Meteor Shard | Daga | Ambas | Mazmorra: Archmage Arugal, Shadowfang Keep | Usable | no está en el cliente (posible objeto oculto) |
| 24 | Outlaw Sabre | Espada 1M | Horde | Misión de mazmorra Baron Aquanis, Blackfathom Deeps | No | no está en el cliente (posible objeto oculto) |
| 24 | Heavehammer | Maza 2M | Ambas | Misión de mazmorra Earthen Echo / Prehistoric Prism, Excavation Site: Wetlands | No | ID 271766 · Rare · ilvl 33 · Two-Hand · Two-Handed Maces · vel. 3.30 · venta 31s 3c · liga al recoger · stats: AttackPower, ExtraArmor |
| 25 | Hamhock's Cleaver | Hacha 1M | Alliance | Mazmorra: Hamhock, Stormwind Stockade | No | no está en el cliente (posible objeto oculto) |
| 29 | Manual Crowd Pummeler | Maza 2M | Ambas | Mazmorra: Crowd Pummeler 9-60, Gnomeregan | No | no está en el cliente (posible objeto oculto) |
| 29 | Corpsemaker | Hacha 2M | Ambas | Mazmorra: Overlord Ramtusk, Razorfen Kraul | No | no está en el cliente (posible objeto oculto) |
| 29 | Felbough Arm | Arma de asta | Ambas | Mazmorra: Fel Ancient, Dalaran | No | no está en el cliente (posible objeto oculto) |
| 30 | Bloody Brass Knuckles | Puño | Ambas | Mazmorra: Interrogator Vishas, Scarlet Monastery Graveyard | No | no está en el cliente (posible objeto oculto) |
| 30 | Pronged Reaver | Hacha 1M | Ambas | Mazmorra: Charlga Razorflank (zona no indicada) | No | no está en el cliente (posible objeto oculto) |

## A distancia
Ningún arma de esta lista es útil para Priest (su ranura de distancia es la wand).

| Nv | Objeto | Tipo | Facción | Origen | Cliente (1.60.1.70938) |
|---|---|---|---|---|---|
| 10 | Footman's Pocketknife | Arrojadiza | Alliance | Misión Riverpaw Gnoll Bounty, Elwynn Forest | no está en el cliente (posible objeto oculto) |
| 10 | Misplaced Shooter | Arma de fuego | Horde | Misión Leonid's Letter, Tirisfal Glades | ID 277255 · Uncommon · ilvl 12 · Ranged (gun/crossbow/wand) · Guns · vel. 2.80 · venta 0 · liga al recoger · stats: Stamina, Strength |
| 13 | Harvester's Pestslayer | Arco | Alliance | Misión The Killing Fields, Westfall | ID 276695 · Uncommon · ilvl 15 · Ranged (bow) · Bows · vel. 2.40 · venta 12s 69c · liga al recoger · stats: Agility, Stamina |
| 13 | Barbaric Crossbow | Ballesta | Horde | Mazmorra: Oggleflint, Ragefire Chasm | no está en el cliente (posible objeto oculto) |
| 16 | Calibrated Blunderbuss | Arma de fuego | Alliance | Misión de mazmorra Old Ironforge Incursion, Hall of Thanes | no está en el cliente (posible objeto oculto) |
| 16 | Dull Sawblade | Arrojadiza | Ambas | Mazmorra: Sneed's Shredder, Deadmines | no está en el cliente (posible objeto oculto) |
| 19 | Venomstrike | Arco | Ambas | Mazmorra: Lord Serpentis (zona no indicada) | no está en el cliente (posible objeto oculto) |
| 22 | Naga Heartpiercer | Arco | Ambas | Mazmorra: Lady Sarevess, Blackfathom Deeps | no está en el cliente (posible objeto oculto) |
| 23 | Fallenroot Longbow | Arco | Ambas | Mazmorra: Lorgus Jett, Blackfathom Deeps | no está en el cliente (posible objeto oculto) |
| 26 | Gravespike Repeater | Ballesta | Ambas | Mazmorra: Atrexis the Grave Knight, Dalaran | no está en el cliente (posible objeto oculto) |
| 26 | Concealed Hand Crossbow | Ballesta | Alliance | Mazmorra: Bazil Thredd, Stormwind Stockade | no está en el cliente (posible objeto oculto) |
| 28 | Golemsight Long Gun | Arma de fuego | Ambas | Drop: Relic Guardian, Excavation Site: Wetlands | no está en el cliente (posible objeto oculto) |
| 30 | Booty Bay Bruiser's Buckshot | Arma de fuego | Ambas | Reputación Booty Bay, Honored | ID 274748 · Rare · ilvl 35 · req 30 · Ranged (gun/crossbow/wand) · Guns · vel. 2.80 · venta 62s 17c · liga al recoger · stats: AttackPower, Stamina |
| 30 | Quilboar Blaster | Arma de fuego | Ambas | Misiones The Crone of the Kraul / A Vengeful Fate | no está en el cliente (posible objeto oculto) |

## Ruta sugerida para Undead Priest (inferido)
Inferencia a partir de la tabla, sin stats que la respalden:
1. Nv 10: Mug of Muddled Memories (Leonid's Letter).
2. Nv 13: Darkwood Staff (The Family Crypt) y wand Riptear's Spare Arm (Rear Guard Patrol), todo en Tirisfal.
3. Nv 13-18 en mazmorras: Trogg Scepter (Ragefire Chasm), Scepter of the Abandoned (Ruins of Lordaeron), Staff of Orgrimmar / Kris of Orgrimmar (Hidden Enemies), Living Root (Wailing Caverns).
4. Comparar stats reales en Wowhead Forever antes de elegir recompensa.

## Contraste con el cliente (cliente 1.60.1.70938)
- **Encontrados:** 28 de 92 nombres; **ocultos o ausentes:** 64 (casi todos los botines de mazmorra). Ninguno con varios IDs.
- **Tipos:** todos los encontrados coinciden con el tipo de Method.
- **Nivel:** el cliente casi nunca trae nivel requerido (0). Donde el "Nv" de Method se aleja del nivel de objeto, se conservan ambos: Hornbeam Heft, Healer's Staff y Heavehammer (Method 24, ilvl 33), Fallen Dragon's Scepter (24, ilvl 32, Rare), Torchlight Wand (15, ilvl 21), Buckler of the Seas (15, ilvl 20), Makeshift Stormcaller (7, ilvl 11). Booty Bay Bruiser's Buckshot sí coincide (Nv 30 = req 30). `unknown` cuál es el requisito real.
- **Charred Wand:** aquí Nv 28 (Method), coincide con su ilvl 28; [[Priest-Wands]] da "Nivel req. 19" (Wowhead). El cliente da req 0. Conflicto abierto.
- **Darkwood Staff** solo trae Stamina como stat y **Thornroot Club** también; Method los lista como armas de poder con hechizos. Puede ser poder con hechizos implícito por flag de arma de lanzador; sin verificar (`unknown`).
- Venta 0 en varias recompensas de misión nuevas (Mug of Muddled Memories, Tim's Lost Rib, Makeshift Stormcaller, Misplaced Shooter, Pathfinder's Clearway, Fallen Dragon's Scepter): no se pueden vender al vendedor según el cliente.

## Qué dicen las guías
- Consenso: solo una fuente leída ([[src-method-the-best-weapons-in-wow-forever-from-levels-1-30]]). Coincide con [[src-method-itemization-updates-in-world-of-warcraft-forever-expertise-spell-damage-more]] en que las armas de ~nv 10 y el equipo de sanación ganan poder con hechizos.
- Discrepancias: The Wrath of Rath'mael aparece como misión de Tirisfal (Gnarled Necromancer's Staff, nv 22) y como misión de mazmorra de Ruins of Lordaeron (Forsaken Greataxe, nv 15) en la misma página.

## Fuentes
| URL | Tipo | Fecha página | Consultada | ¿Antes del parche 2026-11-02? |
|---|---|---|---|---|
| https://www.method.gg/wow-forever/the-best-weapons-in-wow-forever-from-levels-1-30 | Guía Method | 2026-11-06 | 2026-11-13 | No |
| https://www.method.gg/wow-forever/itemization-updates-in-world-of-warcraft-forever-expertise-spell-damage-more | Guía Method | 2026-09-15 | 2026-11-13 | Sí |

## Preguntas pendientes
- Stats reales de Mug of Muddled Memories, Darkwood Staff y Riptear's Spare Arm en Wowhead Forever.
- ¿El nivel de Method es nivel requerido o nivel de objeto?
- ¿Dónde se recoge The Wrath of Rath'mael y es una sola misión?
- Zona de Light's Justice (The Stitcher), Venomstrike y Pronged Reaver.
