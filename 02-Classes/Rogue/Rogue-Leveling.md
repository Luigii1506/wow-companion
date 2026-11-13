---
type: class
tags: [forever, rogue, leveling, talents]
level_min: 1
level_max: 60
faction: both
status: conflicting
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://www.method.gg/wow-forever/wow-forever-rogue-leveling-guide-and-talents
  - https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json
  - https://www.method.gg/wow-forever/class-guides/combat-rogue/talents
  - https://www.method.gg/wow-forever/class-guides/assassination-rogue/talents
  - https://www.method.gg/wow-forever/class-guides/subtlety-rogue/talents
  - https://foreverdb.net/class/Rogue/talents
  - https://foreverdb.net/class/Rogue/builds
  - https://foreverdb.net/guide/leveling-rogue
  - https://foreverdb.net/trainers
  - https://theforeverera.com/es/guides/classes/rogue/
  - https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696/9
  - "Cliente WoW Forever 1.60.1.70938 vía wago.tools (consulta local, 2026-11-13)"
related: ["[[Rogue]]", "[[Combat-Rogue]]", "[[Assassination-Rogue]]", "[[Subtlety-Rogue]]", "[[Rogue-Poisons]]", "[[Rogue-Gear-and-Stats]]", "[[Rogue-Macros-and-Addons]]", "[[Leveling-Route-Orc]]", "[[Weapons-1-30]]", "[[Conflicts]]"]
---

# Rogue-Leveling

> [!warning] Datos en conflicto: ver [[Conflicts]]
> El orden de talentos ya existe (decodificado del widget de Method, 2026-11-07, árbol del parche del 02-11). Siguen abiertos: cómo se aprenden los venenos, si Dual Wield se entrena, el premio de *Hidden Enemies* y Pick Lock. Nada de esto está comprobado con un export del personaje.

## Resumen
- **Combat para subir en solitario** (Method, ForeverDB y The Forever Era coinciden). Subtlety solo si vas siempre en grupo; Assassination espera a Mutilate al 40 y necesita dos dagas. `confirmed_forever` (medium)
- **Orden Combat de Method** (decodificado): Remorseless Attacks 10–11 → Efficient Strikes 12–13 → Coup de Grace 14–16 → Deflection 17–19 → Precision 20–21 → **Riposte 22** → Precision 23 → Endurance 24–25 → Lightning Reflexes 26 → Flawless Execution 27 → Aggression 28–30 → Weapon Expertise 31 → **Blade Flurry 32** → WE 33 → Dual Wield Spec. 34–35 → Hack and Slash 36–40. `confirmed_forever` (medium)
- Armas: Combat con espada, hacha, maza o puño (Sinister Strike); con dagas, cambiar 1 Lightning Reflexes + 2 Endurance por 3 Puncturing Wounds y usar Backstab. No hay racials de armas en Forever.
- Picos: Slice and Dice y arma secundaria al 10, Garrote 14, Ambush y **Poised** 18, Rupture y venenos 20, **Vanish 22**, **Shank 24**, Cheap Shot 26, Kidney Shot y Blade Flurry 30, Adrenaline Rush 40.
- Rotación base: (Garrote si el mob aguanta) → Sinister Strike → Slice and Dice con 1–2 CP en peleas largas → Sinister Strike a 5 → Eviscerate; desde 24 Shank en CD.
- Para un Orc: Blood Fury (+10 % AP 15 s, 2 min de CD) al empezar peleas duras y Hardiness (−20 % aturdimientos). "Savage" ya no existe.

## Orden de talentos 10–40
Base: build "Combat" de la guía de leveling de Method (Reholy, 2026-11-07), decodificada con el archivo de talentos de Method y los nombres de ForeverDB. Se comprobó que cada punto respeta los requisitos de fila (5 puntos por fila) del árbol del 02-11.

| Nivel | Combat solo (Method) | Variante con dagas | Alternativa ForeverDB a 20/30 | Estado |
|---|---|---|---|---|
| 10 | Remorseless Attacks 1/2 (Assassination) | igual | Coup de Grace | confirmed_forever (medium) |
| 11 | Remorseless Attacks 2/2 | igual | Coup de Grace | confirmed_forever (medium) |
| 12–13 | Efficient Strikes 2/2 | igual | Efficient Strikes / Coup de Grace | confirmed_forever (medium) |
| 14–16 | Coup de Grace 3/3 | igual | Efficient Strikes, Lightning Reflexes 2 | confirmed_forever (medium) |
| 17–19 | Deflection 3/3 | igual | Precision 3/3 | confirmed_forever (medium) |
| 20–21 | Precision 2/3 | igual | Endurance 1/2 (a 20) | confirmed_forever (medium) |
| 22 | **Riposte** | igual | Endurance 2/2 | confirmed_forever (medium) |
| 23 | Precision 3/3 | igual | Deflection | confirmed_forever (medium) |
| 24–25 | Endurance 2/2 | **Puncturing Wounds 2/3** | Deflection, Riposte | confirmed_forever (medium) |
| 26 | Lightning Reflexes 1/5 | **Puncturing Wounds 3/3** | Flawless Execution | confirmed_forever (medium) |
| 27 | Flawless Execution | igual | Aggression | confirmed_forever (medium) |
| 28–30 | Aggression 3/3 | igual | Aggression, **Blade Flurry a 30** | confirmed_forever (medium) |
| 31 | Weapon Expertise 1/2 | igual | — | confirmed_forever (medium) |
| 32 | **Blade Flurry** | igual | — | confirmed_forever (medium) |
| 33 | Weapon Expertise 2/2 | igual | — | confirmed_forever (medium) |
| 34–35 | Dual Wield Specialization 2/2 | igual | Dual Wield Spec. 2/2 | confirmed_forever (medium) |
| 36–40 | Hack and Slash 5/5 | igual (ojo a las combinaciones de armas) | Hack and Slash 2, Flash of Steel 5, **Adrenaline Rush a 40** | confirmed_forever (medium) |
| 41–42 | Flash of Steel 1, Adrenaline Rush | igual | — | confirmed_forever (medium) |

- La alternativa ForeverDB son sus builds publicadas a 20 (Coup de Grace 3, Efficient Strikes 2, Lightning Reflexes 2, Precision 3, Endurance 1) y a 30 (añade Deflection 3, Endurance 2, Riposte, Flawless Execution, Aggression 3, Blade Flurry). No da orden punto a punto; el orden de esa columna es solo para orientarse. Llega antes a Blade Flurry (30 frente a 32) y retrasa Riposte.
- Remorseless Attacks a 10–11 es una elección de Method que ForeverDB no hace en Combat.
- Builds de Assassination y Subtlety por nivel: en [[Assassination-Rogue]] y [[Subtlety-Rogue]].

## Rotación por nivel (Combat, solo)
| Nivel | Qué pulsar | Fuente | Estado |
|---|---|---|---|
| 10–13 | Sinister Strike a 5 CP → Eviscerate. Slice and Dice con 1–2 CP solo si la pelea va a durar. Gouge para recuperar energía o ponerte detrás; Evasion pronto si se suman dos mobs; Kick (12) a curaciones | ForeverDB, Method | confirmed_forever (medium) |
| 14–17 | Abrir con **Garrote** desde sigilo si el mob aguanta todo el sangrado; si no, entrar a golpes | ForeverDB, Method | confirmed_forever (medium) |
| 18–21 | Ambush solo con daga en mano principal. Poised (18): empezar las peleas con la energía llena da −10 energía | ForeverDB, Blizzard | confirmed_forever (high) |
| 20–23 | Rupture flojo en Forever: seguir con Eviscerate. Venenos en cuanto los tengas. Riposte cada vez que se ilumine | ForeverDB, Method | confirmed_forever (medium) |
| 22+ | Vanish como botón de huida o para quitar amenaza | Method, ForeverDB | confirmed_forever (medium) |
| 24+ | **Shank en CD** si llevas arma secundaria (5 de energía, devuelve 15, no falla) | Blizzard, ForeverDB | confirmed_forever (high) |
| 26+ | Cheap Shot en mobs peligrosos o lanzadores (aturde 4 s y da 2 CP) | ForeverDB | confirmed_forever (medium) |
| 30+ | Cheap Shot → SnD → Blade Flurry en mob duro o en parejas → SS → Eviscerate a 5. Kidney Shot a lanzadores y a los que huyen. Blade Flurry rompe Gouge y Sap | ForeverDB | confirmed_forever (medium) |
| 40+ | Adrenaline Rush + Blade Flurry en mob duro o en parejas | ForeverDB | confirmed_forever (medium) |

## Entrenamientos clave
| Nivel | Qué | Nota | Estado |
|---|---|---|---|
| 10 | Sap, Slice and Dice, Sprint; arma secundaria | Method dice "entrenar Dual Wield"; según ForeverDB el cliente da la segunda arma al 10 sin pasar por el entrenador | conflicting |
| 12 | Kick, Backstab r2 | — | confirmed_forever (high) |
| 14 | Garrote, Expose Armor, Sinister Strike r3 | Expose Armor solo en objetivos largos | confirmed_forever (high) |
| 16 | Feint, Eviscerate r3 | Pick Lock en Classic era a 16; en Forever **desconocido** (está en el cliente pero no en la lista del entrenador) | unknown |
| 18 | Ambush, Gouge r2, **Poised** | Poised es nuevo (pasivo) | confirmed_forever (high) |
| 20 | Rupture, Stealth r2, Backstab r3; venenos | Cómo se aprenden los venenos: en conflicto, ver [[Rogue-Poisons]] | conflicting |
| 22 | Vanish, Distract, Garrote r2, SS r4 | — | confirmed_forever (high) |
| 24 | **Shank**, Detect Traps, Eviscerate r4 | Shank nuevo; rango 2 a 44 | confirmed_forever (high) |
| 26 | Cheap Shot, Ambush r2, Kick r2, Expose Armor r2 | — | confirmed_forever (high) |
| 28 | Sap r2, Rupture r2, Backstab r4, Feint r2 | — | confirmed_forever (high) |
| 30 | Kidney Shot, Disarm Trap, Garrote r3, SS r5 | — | confirmed_forever (high) |
| 32 / 34 / 40 | Gouge y Eviscerate / Blind y Sprint / Safe Fall | Especialización dual a 40 (Blizzard) | confirmed_forever (medium) |

### Habilidades de armas (Horde)
| Tipo | Dónde se entrena | Estado |
|---|---|---|
| Hachas 1M (nuevo para Rogue) | Hanashi o Sayoc, Orgrimmar | probable_classic (posición de Classic) |
| Dagas, puños | Sayoc, Orgrimmar | probable_classic |
| Espadas, ballestas | Archibald, **Undercity** | probable_classic |
| Mazas, armas de fuego | Ansekhwa, **Thunder Bluff** | probable_classic |

Method aconseja entrenar la habilidad en el maestro de armas en cuanto tengas un arma mejor de ese tipo. Qué habilidades trae de serie un Orc Rogue: **desconocido** (comprobar con un export).

## Armas por nivel (Horde)
Fuentes: lista de la guía de leveling de Method (solo nombre, nivel y origen) y [[Weapons-1-30]]. Sin stats verificados.

| Nivel | Arma | Tipo | Origen | Para | Estado | Cliente (1.60.1.70938) |
|---|---|---|---|---|---|---|
| 10 | Deathstalker Shortsword | No dado (lista "Swords/Other") | Misión *Escorting Erland* (Silverpine), Horde | Combat | confirmed_forever (medium) | ID 3455 · Common · ilvl 11 · One-Hand · One-Handed Swords · vel. 2.10 · venta 1s 88c · liga al recoger |
| 10 | Blade of Cunning | Daga | "Misión de clase" según Method; la misión Orc de nivel 10 es *Therzok* y su recompensa es desconocida | Daga | conflicting | ID 7298 · Uncommon · ilvl 13 · One-Hand · Daggers · vel. 2.00 · venta 4s 68c · liga al recoger · stats: Agility · AllowableClass 8 (solo Rogue, máscara de ChrClasses ID 4; lectura de la máscara inferida) |
| 11 | Jagged Dagger | Daga | Misión *Skull Rock*, Durotar | Daga | confirmed_forever (medium) | ID 4947 · Uncommon · ilvl 11 · One-Hand · Daggers · vel. 1.50 · venta 3s 25c · liga al recoger · stats: Strength |
| 13 | Cursed Felblade / Bone Knuckles | Espada 1M / puño | RFC (Taragaman / Oggleflint) | Combat | confirmed_forever (medium) | Cursed Felblade: no está en el cliente (posible objeto oculto); Bone Knuckles: no está en el cliente (posible objeto oculto) |
| 14–16 | Hammer of Orgrimmar **o** Kris of Orgrimmar | ? / daga | Misión *Hidden Enemies* (RFC) | — | conflicting | Hammer of Orgrimmar: no está en el cliente (posible objeto oculto); Kris of Orgrimmar: no está en el cliente (posible objeto oculto) |
| 15 | Meathook Slicer | Daga | RoL (The Baron) | Daga | confirmed_forever (medium) | no está en el cliente (posible objeto oculto) |
| 17 | Cell Keeper's Claws | Puño | SFK (Rethilgore) | Combat | confirmed_forever (medium) | no está en el cliente (posible objeto oculto) |
| 18 | Keen Skinning Knife | Daga | Misión *Unwelcome Guests*, Barrens | Daga | confirmed_forever (medium) | ID 269716 · Uncommon · ilvl 18 · Main Hand · Daggers · vel. 1.50 · venta 5s 82c · liga al recoger · stats: Intellect, SkinningSkill |
| 18 | Butcher's Slicer | Espada 1M | SFK (Razorclaw) | Combat | confirmed_forever (medium) | no está en el cliente (posible objeto oculto) |
| 18–20 | Cruel Barb | Espada 1M | Deadmines (VanCleef) | Combat (BiS de nivel 20 en The Forever Era) | confirmed_forever (medium) | no está en el cliente (posible objeto oculto) |
| 20–22 | Wingblade | No dado (lista "Swords/Other" de Method) | Cadena *The Barrens Oases* | Combat | confirmed_forever (medium) | no está en el cliente (posible objeto oculto) |
| 21 | Blade of Silverlaine | Espada 1M | SFK (Silverlaine) | Combat | confirmed_forever (medium) | no está en el cliente (posible objeto oculto) |
| 23–26 | Meteor Shard | Daga | SFK (Arugal) | Daga | confirmed_forever (medium) | no está en el cliente (posible objeto oculto) |
| 24–26 | Outlaw Sabre | Espada 1M | Misión *Baron Aquanis* (BFD), Horde | Combat | confirmed_forever (medium) | no está en el cliente (posible objeto oculto) |
| 29–30 | Bloody Brass Knuckles | Puño | SM Graveyard (Vishas) | Combat (BiS de nivel 30 en The Forever Era) | confirmed_forever (medium) | no está en el cliente (posible objeto oculto) |
| 30 | Swinetusk Shank | Daga | RFK (Agathelos) | Daga | confirmed_forever (medium) | no está en el cliente (posible objeto oculto) |
| 30 | Ruby-Adorned Blade | ? | Misión de clase | — | unknown | ID 277246 · Rare · ilvl 36 · One-Hand · One-Handed Swords · vel. 2.30 · venta 0 · liga al recoger · stats: Stamina, Agility · AllowableClass 8 (solo Rogue, máscara de ChrClasses ID 4; lectura de la máscara inferida) |

> [!info] Datos del cliente (cliente 1.60.1.70938)
> Columna "Cliente": tablas DB2 del cliente WoW Forever build 1.60.1.70938 (wago.tools, extraídas 2026-11-13; ItemSparse, Item, ItemSubClass). Son datos de los archivos del juego, no del servidor: un objeto puede cambiar por hotfix. Calidad y ranura: etiquetas de enums públicos de Blizzard; nombres de stats: `Enum.BonusStatIndex` del propio cliente (solo el nombre, sin cantidad); "req" solo si el cliente da nivel requerido distinto de 0; "vel." = ItemDelay en segundos; "venta" = SellPrice para vendedor, no subasta. Blizzard oculta en el cliente ~40 % de los objetos de Forever hasta que se descubren: "no está en el cliente" no prueba que no exista.

Contraste con el cliente (cliente 1.60.1.70938):
- Rellena tipos que faltaban: **Deathstalker Shortsword** = espada 1M (ID 3455, ilvl 11, sin stats); **Ruby-Adorned Blade** = espada 1M Rare (ID 277246, ilvl 36, Stamina + Agility).
- **Blade of Cunning** (ID 7298) y **Ruby-Adorned Blade** tienen `AllowableClass` = 8 (solo Rogue): encaja con "misión de clase" de Method. La misión Orc de nivel 10 (*Therzok*) sigue sin relacionarse con el objeto desde el cliente: el conflicto se mantiene.
- Blade of Cunning: Method lo pone a nivel 10; el cliente da ilvl 13 y req 0. Ruby-Adorned Blade: Method 30, cliente ilvl 36, req 0. Se conservan ambos.
- **Jagged Dagger** trae Strength, no Agility, como stat (cliente).
- No están en el cliente (posibles objetos ocultos): Cursed Felblade, Bone Knuckles, Hammer of Orgrimmar, Kris of Orgrimmar, Meathook Slicer, Cell Keeper's Claws, Butcher's Slicer, Cruel Barb, Wingblade, Blade of Silverlaine, Meteor Shard, Outlaw Sabre, Bloody Brass Knuckles, Swinetusk Shank.

Combinaciones a evitar con Hack and Slash (Method): maza + maza, daga en mano principal + hacha o espada en secundaria, daga en mano principal + puño en secundaria.

## Builds
| Build | Claves | Estado |
|---|---|---|
| Combat (solo) | Sinister Strike, Riposte, Blade Flurry, Flawless Execution, Aggression; Adrenaline Rush a 40 | confirmed_forever (medium) |
| Combat dagas | Igual con Puncturing Wounds y Backstab | confirmed_forever (medium) |
| Subtlety (grupo) | Opportunity, Imp. Ambush, Initiative, Premeditation, Ghostly Strike, Hemorrhage | confirmed_forever (medium) |
| Assassination | Malice, Ruthlessness, Lethality, Cold Blood, Venom; Mutilate a 40 (dos dagas) | confirmed_forever (medium) |

## Qué dicen las guías
- Consenso: Combat para subir solo; Eviscerate como remate principal; Slice and Dice en peleas largas; Shank en CD desde 24; Leatherworking + Skinning. [[src-method-wow-forever-rogue-leveling-guide-and-talents]], [[src-foreverdb-guide-leveling-rogue]], [[src-foreverdb-class-rogue-builds]], [[src-theforeverera-es-guides-classes-rogue]].
- Orden punto a punto: solo Method lo da (en el widget). ForeverDB da builds por nivel con motivos; The Forever Era, solo una orientación general.
- Discrepancias: Remorseless Attacks a 10 (Method) frente a Coup de Grace primero (ForeverDB); Riposte a 22 (Method) frente a 30 (ForeverDB); Dual Wield entrenado o automático; cómo se aprenden los venenos ([[Rogue-Poisons]]).
- Valores y niveles de habilidades: [[src-foreverdb-class-rogue-talents]] (cliente 1.60.1.70938) y [[src-blizzard-forum-beta-development-notes-november-2-2360696]].
- Habilidades de armas: [[src-foreverdb-trainers]].

## Fuentes
- [Data from ForeverDB.net](https://foreverdb.net)
| URL | Tipo | Fecha página | Consultada | ¿Pre-parche? |
|---|---|---|---|---|
| https://www.method.gg/wow-forever/wow-forever-rogue-leveling-guide-and-talents | Guía Method (Reholy) | 2026-11-07 | 2026-11-13 | No |
| https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json | Datos de talentos de Method | build 1.60.1, 02-11 | 2026-11-13 | No |
| https://www.method.gg/wow-forever/class-guides/combat-rogue/talents | Guía Method | 2026-11-04 | 2026-11-13 | No |
| https://www.method.gg/wow-forever/class-guides/assassination-rogue/talents | Guía Method | 2026-11-04 | 2026-11-13 | No |
| https://www.method.gg/wow-forever/class-guides/subtlety-rogue/talents | Guía Method | 2026-11-04 | 2026-11-13 | No |
| https://foreverdb.net/class/Rogue/talents | Datos de cliente | 2026-11-13 | 2026-11-13 | No |
| https://foreverdb.net/class/Rogue/builds | Builds ForeverDB | sin fecha | 2026-11-13 | No |
| https://foreverdb.net/guide/leveling-rogue | Guía ForeverDB | 2026-11-05 | 2026-11-13 | No |
| https://foreverdb.net/trainers | Datos (posiciones de Classic) | sin fecha | 2026-11-13 | Desconocido |
| https://theforeverera.com/es/guides/classes/rogue/ | Guía fan (es) | 2026-10-25 | 2026-11-13 | Sí (cuerpo) |
| https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696/9 | Notas oficiales | 2026-11-03 | 2026-11-13 | Es el parche |

## Preguntas pendientes
- ¿Cuántos puntos ha gastado ya el personaje y dónde? Desconocido hasta el próximo export.
- ¿Qué misión enseña los venenos a la Horde en Forever?
- ¿Cuándo se aprende Pick Lock?
- Recompensa real de *Therzok* y de *Hidden Enemies* para un Rogue.
- ¿Dual Wield se entrena o viene solo al 10?
