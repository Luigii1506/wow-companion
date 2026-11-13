---
type: topic
tags: [forever, professions, engineering, rogue, pvp, gadgets]
level_min: 11
level_max: 60
faction: horde
status: conflicting
confidence: low
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://theforeverera.com/en/guides/professions/engineering/
  - https://theforeverera.com/en/camping/
  - https://theforeverera.com/en/guides/choose-professions/
  - https://foreverdb.net/guide/professions
  - https://foreverdb.net/item/4390
  - https://foreverdb.net/item/4366
  - https://foreverdb.net/item/10720
  - https://foreverdb.net/item/4397
  - https://kami-labs.fr/en/guide-ingenierie-wow-forever/
  - https://www.warcrafttavern.com/forever/guides/engineering/
  - "Cliente WoW Forever 1.60.1.70938 vía wago.tools (consulta local, 2026-11-13)"
  - "Addon ForeverDB 0.60.3, datos 2026-11-13.ea2bb422 (Recipes)"
related: ["[[Engineering]]", "[[Mining]]", "[[Profession-Switch-Plan]]", "[[Rogue]]", "[[Combat-Rogue]]", "[[Rogue-Gear-and-Stats]]", "[[Camping]]", "[[Rogue-Quest-Rewards-10-30]]"]
---

# Engineering para un Rogue

> [!warning] Datos en conflicto: ver [[Conflicts]]
> Recetas, materiales y colores: cliente de Forever (`confirmed_forever`). **Efectos**: solo se leyeron en Forever los de Iron Grenade, Target Dummy, Net-o-Matic, Cloaking Device, Rough Copper Bomb, Rough Dynamite y Satchel of Copper Bombs; el resto es `unknown`. El skill de aprendizaje varía entre fuentes (Kami da el nivel naranja; TFE suele dar solo amarillo). Personaje: Orc Rogue 11 (dato del usuario, sin export).

## Resumen
- Engineering casi no da **equipo** de leveo: 0 piezas BiS a nivel 20 y 30 y 9 a nivel 40 para todas las especializaciones (TFE). Su valor para un Rogue es **utilidad**: aturdir, enraizar, desviar mobs y PvP. `confirmed_forever` (recuento de TFE)
- Primeros útiles realistas (skill ~60–200): **Rough Copper Bomb** (aturde 1 s en área), **Target Dummy** (15 s de distracción), **Iron Grenade** (132–218 de fuego y **3 s** de aturdimiento en 3 m), Goblin Jumper Cables, Flash Bomb. `confirmed_forever` (efectos leídos donde se indica)
- Gnomish: **Net-o-Matic** (red de 10 s, puede fallar sobre ti), Cloaking Device (10 s de invisibilidad), Battle Chicken, Mind Control Cap. Goblin: explosivos (Sapper Charge, The Big One). Que cada receta sea exclusiva de una especialización en Forever: desconocido salvo las que nombra WT. `probable_classic`
- Novedad útil al subir: **Satchel of Copper Bombs** (skill 85) va en la ranura de arma arrojadiza, daño de área bajo sin munición, sirve para atraer de lejos (WT). Que el Rogue pueda equiparlo: inferido (usa arrojadizas), sin comprobar.
- **Addon ForeverDB** (2026-11-13.ea2bb422): skill de aprendizaje y coste de cada útil (Rough Copper Bomb 30 / 1s 30c, Target Dummy 85 / 3s —ambos costes vistos en Forever—, Iron Grenade 175 / 9s, Net-o-Matic 210 / 18s). Ver la sección de datos del addon. `confirmed_forever` (costes vistos) / `probable_classic` (skill)
- Objeto de campamento de Engineering: Reagent Bot (20) y Repair Bot (140). No dan buff; la Lodestone de [[Mining]] sí (AP cuerpo a cuerpo) y es la que conviene colocar.

## Objetos por tramo de skill
Columnas de skill: naranja (aprendizaje) / amarillo según TFE; "?" = el cliente no trae el nivel de aprendizaje. Kami da otro skill entre paréntesis cuando difiere.

| Objeto | Skill | Materiales | Uso para un Rogue | Efecto en Forever | Estado | Cliente (1.60.1.70938) |
|---|---|---|---|---|---|---|
| Rough Copper Bomb | ? / 60 (ForeverDB: Engineering 30) | 1 Copper Bar, 1 Handful of Copper Bolts, 2 Rough Blasting Powder, 1 Linen Cloth | Aturdir 2–3 mobs para escapar o rematar | Daño de fuego + aturdimiento de 1 s en 3 m; cualquier daño lo rompe (ForeverDB) | confirmed_forever | ID 4360 · Common · ilvl 14 · Explosives · venta 60c |
| Rough Dynamite / SAF-T Dynamite | 1 / 30; SAF-T 25 / 25 | 1 Rough Blasting Powder + 1 Linen Cloth (SAF-T: 2 RBP + 1 Linen) | Daño de área barato | 26–34 de fuego en 5 m; la SAF-T no pide skill (ForeverDB) | confirmed_forever | Rough Dynamite: ID 4358 · Common · ilvl 10 · Explosives · venta 30c; SAF-T Dynamite: ID 260792 · Common · ilvl 25 · req 1 · Explosives · venta 75c |
| Satchel of Copper Bombs (nuevo) | 85 / 90 | 20 Rough Copper Bomb, 6 Light Leather, 4 Handful of Copper Bolts | Atraer de lejos sin munición | Arrojadiza de área, poco daño (WT) | confirmed_forever (receta); unknown (cifras) | ID 285275 · Uncommon · ilvl 18 · req 13 · Thrown · Thrown · vel. 2.00 · venta 8s 21c · liga al recoger · stats: Stamina |
| Target Dummy | ? / 115 (Kami 85; Method 145) | 1 Copper Modulator, 2 Handful of Copper Bolts, 1 Bronze Bar, 1 Wool Cloth | Desviar un add, escapar | Atrae a los monstruos cercanos 15 s o hasta morir (ForeverDB) | confirmed_forever (efecto); conflicting (skill) | ID 4366 · Common · ilvl 17 · Devices · venta 75c |
| Goblin Rocket Boots | 130 / 245 (Kami 130) | 1 Black Mageweave Boots, 2 Mithril Tube, 4 Heavy Leather, 2 Goblin Rocket Fuel, 1 Unstable Trigger | Velocidad para huir o viajar | desconocido | unknown | ID 7189 · Uncommon · ilvl 45 · Feet · Cloth · venta 47s 12c · liga al equipar |
| Discombobulator Ray | 160 / 180 | 3 Whirring Bronze Gizmo, 2 Silk Cloth, 1 Jade, 1 Bronze Tube | Control en PvP | desconocido | unknown | ID 4388 · Common · ilvl 32 · Devices · venta 10s |
| Goblin Jumper Cables | 165 / 160 | 6 Iron Bar, 2 Whirring Bronze Gizmo, 2 Flask of Oil, 2 Silk Cloth, 2 Shadowgem, 1 Fused Wiring | Revivir a un compañero (mazmorras) | desconocido | unknown | ID 7148 · Common · ilvl 33 · Trinket · Miscellaneous · venta 21c |
| Iron Grenade | ? / 175 | 1 Iron Bar, 1 Heavy Blasting Powder, 1 Silk Cloth | **El mejor aturdimiento barato** para PvE y PvP | 132–218 de fuego y aturdimiento de 3 s en 3 m; el daño lo rompe (ForeverDB) | confirmed_forever | ID 4390 · Common · ilvl 35 · Explosives · venta 1s 25c |
| Explosive Sheep | ? / 175 | 1 Bronze Framework, 1 Whirring Bronze Gizmo, 2 Heavy Blasting Powder, 2 Wool Cloth | Daño a distancia / distracción | desconocido | unknown | ID 4384 · Common · ilvl 30 · Explosives · venta 10s |
| Flash Bomb | 185 / 185 | 1 Blue Pearl, 1 Heavy Blasting Powder, 1 Silk Cloth; receta de misión | Control (en Classic, miedo a bestias: hipótesis) | desconocido | probable_classic | ID 4852 · Common · ilvl 37 · req 27 · Explosives · venta 3s |
| Advanced Target Dummy | ? / 185 | 1 Iron Strut, 1 Bronze Framework, 1 Gyrochronatom, 4 Heavy Leather | Distracción más duradera | desconocido | unknown | ID 4392 · Common · ilvl 37 · Devices · venta 25s |
| Big Iron Bomb | ? / 190 | 3 Iron Bar, 3 Heavy Blasting Powder, 1 Silver Contact | Daño de área | desconocido | unknown | ID 4394 · Common · ilvl 43 · Explosives · venta 7s 50c |
| Goblin Land Mine | 195 / 215 | 3 Heavy Blasting Powder, 2 Iron Bar, 1 Gyrochronatom | Cubrir una huida | desconocido | unknown | ID 4395 · Common · ilvl 39 · Explosives · venta 16s |
| Gnomish Cloaking Device | 200 / 220 | 4 Gyrochronatom, 2 Jade, 2 Lesser Moonstone, 2 Citrine, 1 Fused Wiring | Abalorio; otra "Vanish" | Invisibilidad 10 s (ForeverDB) | confirmed_forever (efecto) | ID 4397 · Common · ilvl 40 · Trinket · Miscellaneous · venta 50s · liga al equipar |
| Gizmo Girdle / Serrated Strap / Clanking Cord (nuevos) | 175 / 180 | p. ej. Serrated Strap: 2 Copper Modulator, 1 Bronze Tube, 1 Iron Bar; Clanking Cord: 2 Bronze Tube, 1 Copper Modulator, 4 Medium Leather | Cinturón (Clanking Cord tiene versión de cuero, WT) | stats desconocidos; **requieren Anarchist's Workbench** | unknown | Gizmo Girdle: ID 280307 · Uncommon · ilvl 35 · req 30 · Waist · Leather · venta 17s 16c · liga al recoger; Serrated Strap: no está en el cliente (posible objeto oculto); Clanking Cord: ID 280308 · Uncommon · ilvl 35 · req 30 · Waist · Mail · venta 10s 33c · liga al recoger |
| Bent Goggles (nuevo, cuero) | 200 / 205 | 1 Ornate Spyglass, 1 Gyrochronatom, 8 Heavy Leather | Casco de cuero | stats desconocidos; requiere Anarchist's Workbench | unknown | ID 280311 · Uncommon · ilvl 45 · req 40 · Head · Leather · venta 37s 64c · liga al recoger |
| Goblin Sapper Charge | ? / 205 | 1 Mageweave Cloth, 3 Solid Blasting Powder, 1 Unstable Trigger | Daño de área alto (te daña también, en Classic) | desconocido | unknown | ID 10646 · Common · ilvl 41 · Explosives · venta 5s |
| Gnomish Net-o-Matic Projector | ? / 230 (Kami 210) | 1 Mithril Tube, 2 Shadow Silk, 4 Thick Spider's Silk, 2 Solid Blasting Powder, 4 Mithril Bar | Enraizar a un perseguidor o a un caster | Red de 10 s; a veces se engancha en tu propia ropa (ForeverDB) | confirmed_forever (efecto) | ID 10720 · Common · ilvl 42 · Trinket · Miscellaneous · venta 7s 50c · liga al equipar |
| Gnomish Rocket Boots | ? / 245 (Kami 225) | 1 Black Mageweave Boots, 2 Mithril Tube, 4 Heavy Leather, 8 Solid Blasting Powder, 4 Gyrochronatom | Velocidad | desconocido | unknown | ID 10724 · Uncommon · ilvl 45 · Feet · Cloth · venta 46s 97c · liga al equipar |
| Parachute Cloak | 225 / 245 | 4 Bolt of Mageweave, 2 Shadow Silk, 1 Unstable Trigger, 4 Solid Blasting Powder | Caída lenta | desconocido | unknown | ID 10518 · Uncommon · ilvl 45 · Back · Cloth · venta 46s 96c · liga al equipar · stats: Agility |
| Gnomish Battle Chicken | ? / 250 | 1 Mithril Casing, 6 Truesilver Bar, 6 Mithril Bar, 2 Inlaid Mithril Cylinder, 1 Gold Power Core, 2 Jade | Mascota de combate | desconocido | unknown | ID 10725 · Common · ilvl 46 · Trinket · Miscellaneous · venta 15s · liga al recoger |
| Thorium Grenade / Dense Dynamite | 260 / 280; ? / 250 | Thorium Widget, 3 Thorium Bar, 3 Dense BP, 3 Runecloth / 2 Dense BP, 3 Runecloth | Explosivos de nivel 60 (Method los cita para Rogue) | desconocido | unknown | Thorium Grenade: ID 15993 · Common · ilvl 52 · Explosives · venta 15s; Dense Dynamite: ID 18641 · Common · ilvl 45 · Explosives · venta 5s |
| Masterwork Target Dummy | 275 / 295 | Mithril Casing, Thorium Tube, 2 Thorium Widget, Truesilver Bar, 2 Rugged Leather, 4 Runecloth | Distracción de nivel 60 | desconocido | unknown | ID 16023 · Common · ilvl 55 · Devices · venta 1g |
| Stealthman 52 (nuevo) | 300 / 320 | 6 Essence of Air, 6 Illusion Dust, 2 Torbernite, 2 Legionite Bar, 4 Marefoil | El nombre sugiere sigilo; nada confirmado | desconocido | unknown | ID 260827 · Uncommon · ilvl 60 · req 55 · Devices · venta 50s |
| Field Repair Bot 74A | 300 / 320 | 12 Thorium Bar, 4 Rugged Leather, 1 Fused Wiring, 2 Elemental Earth, 1 Elemental Fire | Reparar en mazmorra/raid | desconocido | unknown | ID 18232 · Common · ilvl 60 · Devices · venta 1g |

No para un Rogue (o poco útil): scopes (Crude, Standard, Accurate, Deadly, Sniper) añaden daño a arcos y armas de fuego, la ranura a distancia del Rogue es secundaria; gafas de tela/Spellpower; armas de fuego crafteadas (Rough Boomstick, nivel 5, solo como arma de pull).

> [!info] Datos del cliente (cliente 1.60.1.70938)
> Columna "Cliente": tablas DB2 del cliente WoW Forever build 1.60.1.70938 (wago.tools, extraídas 2026-11-13; ItemSparse, Item, ItemSubClass). Son datos de los archivos del juego, no del servidor: un objeto puede cambiar por hotfix. Calidad y ranura: etiquetas de enums públicos de Blizzard; nombres de stats: `Enum.BonusStatIndex` del propio cliente (solo el nombre, sin cantidad); "req" solo si el cliente da nivel requerido distinto de 0; "vel." = ItemDelay en segundos; "venta" = SellPrice para vendedor, no subasta. Blizzard oculta en el cliente ~40 % de los objetos de Forever hasta que se descubren: "no está en el cliente" no prueba que no exista.

### Contraste con el cliente (cliente 1.60.1.70938)
- **Conflicto:** la nota dice que Clanking Cord "tiene versión de cuero" (WT); en el cliente hay un solo Clanking Cord (ID 280308) y es de **malla**, req 30. El cinturón de cuero es **Gizmo Girdle** (ID 280307, req 30). Se conservan ambas lecturas.
- **Serrated Strap** no está en el cliente (posible objeto oculto).
- Bent Goggles: cuero, req 40 (ID 280311), coincide con "nuevo, cuero".
- Satchel of Copper Bombs: arrojadiza (Thrown), req 13, Stamina, `AllowableClass` -1 (sin restricción de clase en el cliente). Que el Rogue pueda equiparlo sigue sin probar en el juego, pero el cliente no lo impide.
- Flash Bomb pide nivel 27 y Stealthman 52 nivel 55 para usarse (cliente). El resto de consumibles no trae nivel requerido.
- Precios de vendedor de ForeverDB = SellPrice del cliente: Target Dummy 75c, Iron Grenade 1s 25c, Net-o-Matic 7s 50c, Cloaking Device 50s.
- Objetos de campamento: Reagent Bot ID 279950, Repair Bot ID 279949, Anarchist's Workbench ID 279989 (sin precio de venta).

## Datos del addon ForeverDB (2026-11-13.ea2bb422)
Skill para aprender con `(C)` = dato de instructor de Classic; colores del cliente; coste con ✓ = visto en un instructor de Forever. Los efectos siguen como arriba (el addon no trae efectos de objeto).

| Objeto | Skill para aprender | Amarillo / verde / gris | Cómo se aprende | Coste | Forever |
|---|---|---|---|---|---|
| Rough Dynamite | 1 | 30 / 45 / 60 | con la profesión | — | cambiada (reagents) |
| SAF-T Dynamite | 25 | 25 / 30 / 35 | Schematic: SAF-T Dynamite (264202) | — | nueva |
| Rough Copper Bomb | 30 (C) | 60 / 75 / 90 | instructor | 1s 30c ✓ |  |
| Satchel of Copper Bombs | 85 | 90 / 92 / 95 | Schematic: Satchel of Copper Bombs (285285) | — | nueva |
| Target Dummy | 85 (C) | 115 / 130 / 145 | instructor | 3s ✓ |  |
| Large Copper Bomb | 105 (C) | 105 / 130 / 155 | instructor | 4s 50c ✓ |  |
| Small Bronze Bomb | 120 (C) | 120 / 145 / 170 | instructor | 5s ✓ |  |
| Goblin Rocket Boots | 130 | 245 / 255 / 265 | Schematic: Goblin Rocket Boots (7192) | 22s |  |
| Big Bronze Bomb | 140 (C) | 140 / 165 / 190 | instructor | 6s ✓ |  |
| Explosive Sheep | 150 (C) | 175 / 187 / 200 | instructor | 7s 50c ✓ |  |
| Discombobulator Ray | 160 | 180 / 190 / 200 | Schematic: Discombobulator Ray (4413); cae de: Mekgineer Thermaplugg 2% (Classic) | — |  |
| Goblin Jumper Cables | 165 | 160 / 180 / 200 | Schematic: Goblin Jumper Cables (7561); vendedores: 3 | — |  |
| Iron Grenade | 175 (C) | 175 / 195 / 215 | instructor | 9s |  |
| Clanking Cord | 175 | 180 / 182 / 185 | Schematic: Clanking Cord (280323) | — | nueva |
| Gizmo Girdle | 175 | 180 / 182 / 185 | Schematic: Gizmo Girdle (280322) | — | nueva |
| Advanced Target Dummy | 185 (C) | 185 / 205 / 225 | instructor | 10s 80c |  |
| Flash Bomb | 185 | 185 / 205 / 225 | Schematic: Flash Bomb (6672); misión: Flash Bomb Recipe | — |  |
| Big Iron Bomb | 190 (C) | 190 / 210 / 230 | instructor | 12s 60c |  |
| Goblin Land Mine | 195 | 215 / 225 / 235 | Schematic: Goblin Land Mine (4416); cae de: world drop (level 19-50 creatures), Obsidian Sentinel 0.02%, Theka the Martyr 0.02% (Classic) | — |  |
| Bent Goggles | 200 | 205 / 207 / 210 | Schematic: Bent Goggles (280326) | — | nueva |
| Gnomish Cloaking Device | 200 | 220 / 230 / 240 | Schematic: Gnomish Cloaking Device (7742); cae de: Mekgineer Thermaplugg 2% (Classic); vendedores: 1 | — |  |
| Goblin Sapper Charge | 205 (C) | 205 / 225 / 245 | instructor | 15s |  |
| Gnomish Net-o-Matic Projector | 210 (C) | 230 / 240 / 250 | instructor | 18s |  |
| Gnomish Rocket Boots | 225 (C) | 245 / 255 / 265 | instructor | 22s |  |
| Parachute Cloak | 225 | 245 / 255 / 265 | Schematic: Parachute Cloak (10606); cae de: world drop (level 33-55 creatures), Shade of Eranikus 0.01%, Jammal'an the Prophet 0.01% (Classic) | — |  |
| Gnomish Battle Chicken | 230 (C) | 250 / 260 / 270 | instructor | 24s |  |
| Dense Dynamite | 250 (C) | 250 / 260 / 270 | instructor | 50s |  |
| Thorium Grenade | 260 | 280 / 290 / 300 | Schematic: Thorium Grenade (16041); vendedores: 2 | 90s |  |
| Masterwork Target Dummy | 275 | 295 / 305 / 315 | Schematic: Masterwork Target Dummy (16046); vendedores: 1 | — |  |
| Field Repair Bot 74A | 300 | 320 / 330 / 340 | Schematic: Field Repair Bot 74A (18235) | — |  |
| Stealthman 52 | 300 | 320 / 330 / 340 | Schematic: Stealthman 52 (264237) | — | nueva |

- El addon resuelve la discrepancia de skill de **Target Dummy** a favor de Kami: se aprende a **85** (dato de Classic) y es amarilla a 115; coste 3s visto en Forever. Method (145) queda aislado. `probable_classic` (skill) / `confirmed_forever` (coste, colores)
- **Rough Copper Bomb**: aprender a 30, amarilla a 60, 1s 30c visto en Forever. **Iron Grenade**: 175, 9s (coste de Classic, no visto aún).
- **Satchel of Copper Bombs** se aprende con *Schematic: Satchel of Copper Bombs* (285285); de dónde sale el esquema: desconocido en los datos.
- **Gizmo Girdle** (cuero) y **Clanking Cord** (malla) tienen esquemas propios (280322 y 280323), los dos nuevos de Forever, aprender a 175. Encaja con el cliente: el cinturón de cuero es Gizmo Girdle.
- *Gnomish Cloaking Device* y *Discombobulator Ray*: esquemas que caen de Mekgineer Thermaplugg (Gnomeregan, 2 % en Classic). *Goblin Jumper Cables*: esquema de vendedor (el addon cuenta 3 vendedores; no dice cuáles ni si se vieron en Forever). *Flash Bomb*: misión *Flash Bomb Recipe*.
- Recompensas de misión útiles para un Rogue (armas, cuero, anillos) por tramo de nivel: [[Rogue-Quest-Rewards-10-30]].

## Prioridad recomendada (inferido)
| Momento | Fabricar / guardar | Por qué |
|---|---|---|
| Skill 30–75 | Rough Copper Bomb ×10–20 | Aturdimiento de área barato con Copper propio |
| Skill 115–150 | Target Dummy ×3–5 | Seguro de vida en grupos de mobs |
| Skill 175+ | **Iron Grenade** en cantidad | 3 s de aturdimiento: lo más útil para un Rogue en solitario y PvP |
| 200 (decidir especialización) | Gnomish si buscas PvP/solo (Net-o-Matic, Cloaking, Battle Chicken); Goblin si buscas explosivos y daño | Depende de lo que hagas a 60; requisitos de Forever en conflicto (ver [[Engineering]]) |

## Precios observados (ForeverDB, otros reinos, 2026-11-12/13)
| Objeto | Vendedor | Subasta (rango) | Estado |
|---|---|---|---|
| Target Dummy | 75c | 2s40c–6s99c | confirmed_forever |
| Iron Grenade | 1s25c | 1s89c–14s95c (en un reino bajó de 14s88c a 2s39c en 5 días) | confirmed_forever |
| Gnomish Net-o-Matic Projector | 7s50c | 2g–9g99s | confirmed_forever |
| Gnomish Cloaking Device | 50s | 2g90s–6g | confirmed_forever |

## Qué dicen las guías
- Recetas y colores: [[src-theforeverera-en-guides-professions-engineering]]; nivel de aprendizaje alternativo: [[src-kamilabs-guide-ingenierie-wow-forever]].
- Efectos leídos: [[src-foreverdb-item-4390]] (Iron Grenade), [[src-foreverdb-item-4366]] (Target Dummy), [[src-foreverdb-item-10720]] (Net-o-Matic), [[src-foreverdb-item-4397]] (Cloaking Device), [[src-foreverdb-guide-professions]] (Rough Copper Bomb, Rough Dynamite, SAF-T Dynamite).
- Satchels, SAF-T y exclusivas de especialización: [[src-warcrafttavern-guides-engineering]]. Workbench: [[src-theforeverera-en-camping]]. BiS por profesión: [[src-theforeverera-en-guides-choose-professions]].
- Method (Combat Rogue) recomienda Field Repair Bot 74A, Goblin Jumper Cables, Target Dummy, Arcane Bomb / Sapper / Thorium Grenade / Dense Dynamite y Rocket Boots ([[src-method-class-guides-combat-rogue-races-professions-and-other]], ingesta anterior). Sus skills (Target Dummy 145, Jumper Cables 200, Rocket Boots 265) no coinciden con TFE ni Kami.

## Fuentes
- [Data from ForeverDB.net](https://foreverdb.net)
| URL | Tipo | Fecha | Consultada | ¿Antes del parche 2026-11-02? |
|---|---|---|---|---|
| https://theforeverera.com/en/guides/professions/engineering/ | cliente | build 70888 | 2026-11-13 | No |
| https://theforeverera.com/en/camping/ | cliente | 2026-10-17 | 2026-11-13 | Sí |
| https://theforeverera.com/en/guides/choose-professions/ | guía | 2026-11-13 | 2026-11-13 | No |
| https://foreverdb.net/guide/professions | guía | 2026-11-05 | 2026-11-13 | No |
| https://foreverdb.net/item/4390, /4366, /10720, /4397 | cliente + subasta | build 70938; precios 2026-11-12/13 | 2026-11-13 | No |
| https://kami-labs.fr/en/guide-ingenierie-wow-forever/ | guía | 2026-11-10 | 2026-11-13 | No |
| https://www.warcrafttavern.com/forever/guides/engineering/ | guía | sin fecha | 2026-11-13 | Probablemente sí |
| Addon ForeverDB 0.60.3, `Data/Meta.lua` versión 2026-11-13.ea2bb422 (Recipes.lua) | cliente + vistos en Forever + CMaNGOS | 2026-11-13 | 2026-11-13 | No |

## Preguntas pendientes
- Efectos y cooldowns en Forever de Jumper Cables, Discombobulator, Flash Bomb, Rocket Boots, Sapper Charge y los gadgets nuevos (Stealthman 52, Loot-A-Rang).
- Stats de Bent Goggles y de los cinturones de 175; si el Rogue puede usar el Workbench de otro jugador.
- Qué recetas son exclusivas de Gnomish o Goblin en Forever.
- ¿Los objetos de Engineering piden skill para usarse (como Rough Dynamite) y fallan como en Classic?
