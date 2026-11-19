---
type: topic
tags: [research, forever]
status: conflicting
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1 (launch)"
sources:
  - https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696
  - https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696/9
  - https://kami-labs.fr/en/wow-forever/patch-notes-2-novembre-notes-de-lancement/
  - https://worldofwarcraft.blizzard.com/en-gb/news/24303313
  - https://www.warcrafttavern.com/forever/guides/riding/
  - https://www.method.gg/wow-forever/how-to-get-a-mount-in-wow-forever-cost-requirement-and-mount-options
  - https://kami-labs.fr/en/wow-forever/wow-forever-niveau-40-monture-double-specialisation/
  - https://mein-mmo.de/en/wow-forever-gold-guide-how-to-farm-quickly-for-the-mount-and-expensive-purchases,1594663/
  - https://www.warcrafttavern.com/forever/news/camping-profession-buffs-in-world-of-warcraft-forever
  - https://www.warcrafttavern.com/forever/guides/experience/
---

# Conflictos entre fuentes

## Resumen
Este registro guarda las **contradicciones entre fuentes** sin resolverlas por intuición (wow.md §9). Cada conflicto indica qué dice cada fuente, sus fechas, el estado actual y cómo resolverlo, normalmente observándolo en el juego o con una fuente oficial nueva. Los conflictos de otros investigadores se fusionarán aquí más adelante.

No se registran como conflicto los cambios que simplemente **evolucionaron entre builds** de la beta (p. ej. Orc Blood Fury 2→3→2 min, Plainsrunning con o sin velocidad montado, ICD de Touch of the Grave 25→15 s). En esos casos manda la build más reciente → ver [[Patch-Changes]].

Relacionado: [[Sources]] · [[Patch-Changes]] · [[Mount-and-Costs]] · [[Auction-House]]

## Conflictos

### C1 — ¿Hay que comprar aparte la primera montura de nivel 40?
- **Afirmación A**: el Apprentice Riding (nv 40, 100 g) **incluye** la primera montura; los colores extra cuestan 20 g cada uno. — Method (2026-10-21, beta). Coincide con el modelo oficial: "recibes una montura al aprender riding" (Deep Dive de Blizzard, 2026-09-13).
- **Afirmación B**: el riding cuesta 100 g y la montura cuesta 20 g, en columnas separadas, sin decir que la primera sea gratis. — Warcraft Tavern, guía de riding (sin fecha).
- **Impacto**: la meta es de 100 g o de 120 g.
- **Estado**: conflicting. Peso a favor de A (Method + modelo oficial), pero ninguna cifra es oficial.
- **Cómo resolver**: preguntar o mirar en el juego el precio de Velma Warnam (Brill) y de Zachariah Post al acercarse al nivel 40. Si hay un export del addon con precios de vendedor, usarlo.

### C2 — Coste total de la montura rápida de nivel 60
- **Afirmación A**: el Journeyman Riding cuesta 1000 g **y** cada montura épica cuesta 200 g. — Method (2026-10-21); Warcraft Tavern riding (sin fecha).
- **Afirmación B**: "la montura rápida a 60 cuesta 1000 g", sin mencionar los 200 g. — Mein-MMO (2026-11-03).
- **Matiz**: el modelo oficial incluye una montura con el riding. Si eso también vale para el nivel 60, la primera épica podría venir incluida (no confirmado).
- **Estado**: conflicting / unknown.
- **Cómo resolver**: preguntar en el juego al llegar a 60, o esperar a una fuente oficial con precios. Prioridad baja para un nivel 9.

### C3 — Binding Heal: ¿eliminado o todavía entrenable?
- **Afirmación A**: Binding Heal "eliminado" del árbol Holy y reemplazado por el talento Holy Binding. — Kaivax, notas del 2-nov (publicadas el 2026-11-03).
- **Afirmación B**: los datos del juego (datamining) todavía listan Binding Heal como hechizo entrenable, con 6 rangos desde el nivel 25; Renewed Hope ya no lo menciona. — Kami-Labs (2026-11-03).
- **Lectura posible**: puede que solo haya desaparecido del árbol de talentos y no del entrenador. Es una interpretación, no un hecho.
- **Estado**: conflicting.
- **Cómo resolver**: revisar la lista del entrenador de Priest al nivel 25 o un export del addon con los hechizos disponibles.

### C4 — Cooldown de los objetos de camp: ¿por jugador o compartido?
- **Afirmación A**: cada jugador puede poner un objeto con un cooldown de 1 h. — Warcraft Tavern (2026-09-13), resumiendo el panel.
- **Afirmación B**: los objetos comparten ("shared") un cooldown de 1 h. — Recap oficial del Deep Dive (2026-09-13).
- **Estado**: conflicting (manda la fuente oficial, B, pero la redacción es ambigua).
- **Cómo resolver**: probarlo en el juego cuando el jugador tenga Herbalism 20 (Incense Candle).

### C5 — Reparto de XP en grupo
- **Afirmación A**: la XP de grupo usa el nivel de cada jugador, "igual que en Classic Era". — Notas de desarrollo, build del 2026-10-08.
- **Afirmación B**: "Forever aplica penalizaciones de XP mayores" a los miembros de nivel alto. — Warcraft Tavern, guía de experiencia (sin fecha).
- **Estado**: conflicting (puede que sean compatibles; B no da cifras).
- **Cómo resolver**: comparar la XP de una muerte en solitario y en grupo con el log del addon.

### C6 — Fecha del +50 % de XP por muerte en mazmorras
- **Afirmación A**: aplicado el 2026-11-08, según un post de Kaivax en el foro. Lo cita [[Dungeons-1-30]].
- **Afirmación B**: aparece en la edición del 9 de noviembre de la página oficial de hotfixes (news.blizzard.com, artículo 24315281).
- **Impacto**: ninguno práctico; el cambio ya está activo.
- **Estado**: conflicting, menor. Probablemente es la misma entrada: el post del foro sería del 8 y la recopilación del 9. Es una suposición.
- **Cómo resolver**: tomar la fecha de la página oficial de hotfixes.

### C7 — Nivel de Ruins of Lordaeron
- **Afirmación A**: 15–20. **Afirmación B**: 15–22. Ver [[Dungeons-1-30]], que cita las fuentes.
- **Estado**: conflicting.
- **Cómo resolver**: mirar el rango en el buscador de grupos del juego.

### C8 — Nivel de algunas wands de misión
- **Gravestone Scepter**: 18 contra 27, según la fuente.
- **Charred Wand**: 19 contra 28.
- Ver [[Dungeons-1-30]] y [[Priest-Wands]] para fuentes y fechas.
- **Estado**: conflicting. Puede que unas fuentes den el nivel requerido para equiparla y otras el nivel de la misión. Es una suposición.
- **Cómo resolver**: consultar la base de datos de Wowhead Forever o el tooltip en el juego.

### C9 — Ruta de los niveles 20–30
- **Afirmación A**: Hillsbrad. **Afirmación B**: Barrens y Kalimdor. Ver [[Leveling-Route-Undead]].
- **Estado**: conflicting. Puede no ser un error, sino dos rutas válidas.
- **Cómo resolver**: decidir por eficiencia real cuando el personaje llegue a ~20, con datos de sesiones.

### C10 — Nivel de personaje para cada rango de profesión
- **Afirmación A**: Journeyman 10, Expert 20, Artisan 35 (Warcraft Tavern, Gfinity).
- **Afirmación B**: sin requisito de nivel (wow-professions).
- **Afirmación C**: Artisan "25 o más" (Method).
- **Impacto**: inmediato. Con nivel 9, Journeyman podría estar bloqueado hasta el 10.
- **Estado**: conflicting. Ver [[Herbalism]] y [[Skinning]].
- **Cómo resolver**: hablar con el entrenador en Brill al llegar a skill 50.

### C11 — Skill necesaria para entrenar cada rango
- **Afirmación A**: 50 / 125 / 200 (casi todas las guías).
- **Afirmación B**: 75 / 150 / 225 (Rankedboost).
- **Estado**: conflicting; el peso favorece A.
- **Cómo resolver**: el entrenador lo indica en el juego.

### C12 — Skill de Bruiseweed
- **Afirmación A**: 100 (Kami-Labs, Rankedboost). **Afirmación B**: 85 (Gfinity). Ver [[Herbs]].
- **Estado**: conflicting.
- **Cómo resolver**: tooltip del nodo en el juego.

### C13 — Tope de Skinning
- **Afirmación A**: 225 "por ahora" (Method, 2026-11-06). **Afirmación B**: 300 (resto de guías). Ver [[Skinning]].
- **Estado**: conflicting; A es la fuente más reciente.
- **Cómo resolver**: ventana de profesión al aprender Expert.

### C14 — Nombre del objeto que cultiva semillas
- **Afirmación A**: Greenhouse. **Afirmación B**: Fermenter. Ver [[Herbalism]].
- **Estado**: conflicting, prioridad baja.

### C15 — Zona para Herbalism 1–100
- **Afirmación A**: Barrens (Rankedboost). **Afirmación B**: Silverpine (wow-professions). Ver [[Gathering-Routes]].
- **Estado**: conflicting. Pueden ser dos opciones válidas; para un Undead, Silverpine encaja con su ruta de misiones.

### C16 — ¿La wand reemplaza a Smite?
- **Afirmación A**: sí; el Priest sube de nivel con la wand en lugar de Smite. — Kami-Labs (2026-09-23, beta).
- **Afirmación B**: las wands dejan de ganar daño del spell damage del usuario. — Notas oficiales de Blizzard, 2026-09-24.
- **Estado**: resuelto a favor de B (fuente oficial y posterior). A se basaba en el escalado que se quitó. La wand sigue siendo el slot clave por su DPS base. Ver [[Priest-Wands]].

### C17 — Stats de Sizzle Stick y Gravestone Scepter
- **Sizzle Stick**: +5 SP y ~23 DPS (Kami) contra +2 SP y 17,65 DPS (Wowhead Forever).
- **Gravestone Scepter**: +4 Shadow resistance (Kami) contra +6 de daño Shadow (Wowhead Forever).
- **Estado**: conflicting; el peso favorece la base de datos de Wowhead Forever. Relacionado con C8. Ver [[Priest-Wands]].
- **Cómo resolver**: tooltip en el juego.

### C18 — ¿Usar Mind Flay al subir de nivel?
- **Afirmación A**: evitarlo (Kami); los jugadores lo ven flojo a nivel bajo (foro EU, 2026-11-07/08).
- **Afirmación B**: Method y Warcraft Tavern lo incluyen, y Blizzard lo mejoró el 2026-10-16.
- **Estado**: conflicting. Ver [[Priest-Talents]].
- **Cómo resolver**: comparar tiempo por muerte y maná con datos de sesiones.

### C19 — Plan de talentos del 20 al 40
- **Afirmación A**: Discipline hasta el 39 (Method; Maxroll vía Timesaver).
- **Afirmación B**: Shadow temprano (Kami y jugadores del foro).
- **Afirmación C**: tres opciones al nivel 30 (Warcraft Tavern).
- **Estado**: conflicting; no afecta hasta el nivel 20. Ver [[Priest-Talents]].

### C20 — Velocidad de leveling del Priest
- **Afirmación A**: mata ~25 % más lento que en Classic tras el aumento de vida de los enemigos (jugadores, foro EU).
- **Afirmación B**: el Priest está bien y recibió una de las mejores revisiones (otros jugadores, mismo hilo).
- **Estado**: conflicting, opiniones sin datos.
- **Cómo resolver**: medir con los datos de sesión de Dossier.

### C21 — Coste de maná de Devouring Plague
- **Afirmación A**: ~20 % del maná. **Afirmación B**: ~25 %. Ambas de jugadores.
- **Estado**: conflicting.
- **Cómo resolver**: tooltip en el juego.

### C22 — Cooldown de Shadow Word: Death
- **Afirmación A**: 15 s (artículo oficial, 2026-09-30). **Afirmación B**: 18 s (nota oficial, 2026-10-16).
- **Estado**: probablemente cambió entre builds; manda la más reciente (18 s) hasta verlo en el juego. Ver [[Priest-Spells]].

Binding Heal ya figura como C3.

## Resoluciones de la tanda del 2026-11-13
- **C6**: resuelto. Mismo cambio: activo el 2026-11-08 hacia las 11:05 PST según Kaivax, listado en la página oficial del 2026-11-09.
- **C10**: el peso se inclina a Journeyman 10 / Expert 20 / Artisan 35 para profesiones principales (las 5 guías de fabricación de Method). Method Herbalism dice Artisan "25 o más". Secundarias: First Aid 1/1, Fishing 10/20, Cooking 1/1 en tabla y 10/20 en texto. Sigue abierto hasta verlo en el juego.
- **C13**: no era un conflicto. 225 es donde termina la guía de Method, no el tope del juego, que sigue sin confirmar.
- **C14**: resuelto. "Fermenter" es el objeto de campamento de nivel 2 de Alchemy, no de Herbalism.
- **C16**: confirmado de nuevo; "Improved Wands" y "Thrill of Adventure" no existen en el árbol 1.60.1.

## Conflictos de la tanda del 2026-11-13 (Method y otras fuentes)
Formato breve: afirmación A frente a B, y nota afectada. Resolver en el juego o con datos de ForeverDB / Azeroth DB / wago.tools.

### Mazmorras y mundo
- **C23** — Rangos de nivel: las páginas de mazmorras de Method y su artículo de XP no coinciden en 20 mazmorras (Hall of Thanes 13–20 frente a 13–18; Excavation Site 26–33 frente a 24–29; Shadowfang Keep 20–30 frente a 21–26). Amplía C7. [[Dungeon-XP]]
- **C24** — City of Dalaran: 28–35 (cabecera) frente a 26–33 (intro) frente a 28–33 (artículo de XP). [[City-of-Dalaran]]
- **C25** — Hyjal Summit: Method nombra Ancient Guardian como primer encuentro, pero no está entre los 13 jefes listados. [[Hyjal-Summit]]
- **C26** — Nombre del NPC: "Tabitha Heartweaver" (Method) frente a "Tabetha" (nota antigua).
- **C27** — Entrada Horde a Stonetalon: nivel 18 frente a 15. [[Quests-Stonetalon-Mountains]]
- **C28** — *A Righteous Cause*: nivel 12 frente a 13.
- **C29** — Raros nuevos: Coldrasp y Decrepit Harvester marcados como nuevos en una web y no en otra. [[Rares-Horde-1-30]]
- **C30** — "The Wrath of Rath'mael" aparece como misión de Tirisfal y como misión de Ruins of Lordaeron. [[Weapons-1-30]]

### Objetos y mecánicas
- **C31** — Expertise sustituye a Weapon Skill (Method, 2026-09-15) frente a Weapon Skill sigue causando fallos (Method, 2026-10-06). [[Itemization]], [[Hit-Chance]]
- **C32** — Topes de hit incoherentes en la guía de Method (hechizos 4 %/17 %, cuerpo a cuerpo 5 %/8 %, doble arma 24 %/29 %); "Holy Precision +18 %" dudoso. [[Hit-Chance]]
- **C33** — Malignant Root: la página se contradice sobre si es BoE. [[Malignant-Root]]
- **C34** — Old Toolbox: "desde nivel 14" (bolsas) frente a "Horde 30+" (Cozy). [[Bags]]
- **C35** — Cozy Sleeping Bag: ID 211527, el mismo que en Season of Discovery; bolsa Horde Sturdy Lunchbox (Warcraft Tavern) frente a Old Toolbox (Method); buff de 2 h para toda la XP (Method) frente a +1 % por acumulación. [[Cozy-Sleeping-Bag]]
- **C36** — Camp Tent: buff de descanso de 1 h (Warcraft Tavern) frente a "5 % de un nivel por hora" (Mein-MMO). [[Camping]]
- **C37** — Hoguera: Simple Wood + Flint And Tinder (Method Camping, 2026-10-07) frente a 1 Simple Wood (Method recetas, 2026-11-12); Journeyman Campfire con Cooking 140 (Warcraft Tavern) frente a kit con Cooking 90 (hotfix 2026-11-10). [[Camping]]

### Profesiones y consumibles
- **C38** — Rangos de entrenador desplazados en Leatherworking y Alchemy de Method (Cured Medium Hide en 75 como "Expert"; un entrenador "Master" que no existe). [[Leatherworking]], [[Alchemy]]
- **C39** — Tailoring: el texto dice que solo pide nivel de personaje y su tabla pide skill. [[Tailoring]]
- **C40** — Enchant Chest - Greater Intellect: skill 185 en la lista frente a 201–205 en la ruta. [[Enchanting]]
- **C41** — Elixir of Sages listado dos veces con efectos distintos. [[Consumables]]
- **C42** — Vendedor del Expert Cookbook Horde: Durotar (texto) frente a Wulan en Desolace (tabla). [[Cooking]]
- **C43** — ID de *Triage*: 6622 frente a 6624. [[First-Aid]]

### Clases y razas
- **C44** — Skyborne: versión Alliance y Horde con racials distintos; Shaman Alliance solo Dwarf frente a Skyborne Shaman sin facción (página de beta). [[Races]]
- **C45** — "Savage", racial pasivo de crítico de Orc en la guía de Rogue, no aparece en la página de racials. [[Races]]
- **C46** — Racials: cifras de Night Elf Quickness y Skyborne Read Ley Line distintas entre tabla y texto. [[Races]]
- **C47** — Mage Comprehension: primer nivel en 5 (texto) frente a 6 (tabla). [[Mage-Comprehension]]
- **C48** — Rogue: Combat evita dagas frente a otras builds que las piden; venenos a 20 frente a "30-". [[Rogue-Leveling]]
- **C49** — Priest 17–39: Method (Improved SW:Pain, Martyrdom, Penance a 37) frente a Maxroll (Twin Disciplines, Holy Precision, Penance a 35). Amplía C19. [[Priest-Talents]]
- **C50** — Primeros puntos de Shadow: Spirit Tap (respec a 40 de Method) frente a Shadow Focus (41–60 y raid de Method, Maxroll). [[Shadow-Priest]]
- **C51** — Mental Strength: +15 % Intellect (tooltip) frente a 2–10 % (notas oficiales, 2026-10-16). [[Discipline-Priest]]
- **C52** — Vampiric Embrace: requiere nivel 30 (tooltip) frente a tomado a 25 en las builds. [[Shadow-Priest]]
- **C53** — Mageblood: ID 250341 frente a Mageblood Potion (20007). [[Holy-Priest]]

### Sistemas y economía
- **C54** — Coste de reiniciar Legacy: 10 g (Method) frente a 1 s (notas, 2026-10-08). [[Legacy]]
- **C55** — Bartering: materiales y monturas sin riding (Method) frente a −5 % por rango en todo vendedor (Warcraft Tavern). [[Legacy]]
- **C56** — World Buffs: dos IDs de hechizo distintos por buff. [[World-Buffs]]
- **C57** — Libros "Stonewrought Design" y "Magma or Lava?" con las mismas coordenadas. [[Library-Books]]
- **C58** — Waylaid Crates: Apprentice y Journeyman ambos a nivel 10; facción escrita "Supply" y "Supplies". [[Durotar-Supply-and-Logistics]]
- **C59** — Descuento de montura por reputación de Undercity: 5 % en Friendly hasta 20 % en Exalted (Warcraft Tavern) frente a −10 % en Honored (Method). [[Mount-and-Costs]]


### Rogue y Orc (2026-11-13)
- **C60** — "Savage" (racial Orc de crítico): resuelto, **eliminado**. Las notas de Blizzard del 2026-11-02 lo quitan y bajan Blood Fury a 2 min; los datos del cliente (ForeverDB) y The Forever Era (2026-11-13) coinciden. El texto de la guía de Rogue de Method está desfasado. Cierra C45. [[Races]]
- **C61** — Racial Orc de hachas: resuelto, **eliminado**. La guía de clase de The Forever Era (2026-10-25) lo citaba; su guía de razas y ForeverDB no. [[Races]]
- **C62** — Cómo aprende la Horde los venenos: misión *Hinott's Assistance* (ForeverDB) frente a "sin confirmar" (su propia guía) y sin mecanismo en Method; también se cita *Deep Cover* → *Mission: Possible But Not Probable*. [[Rogue-Poisons]]
- **C63** — Venom: remate (artículo de octubre, Method, The Forever Era) frente a pasivo (notas del 2026-11-02). [[Rogue-Poisons]]
- **C64** — Recompensa de *Hidden Enemies*: Hammer of Orgrimmar frente a Kris of Orgrimmar. [[Ragefire-Chasm]]
- **C65** — Dual Wield: se entrena a 10 (Method) frente a automático (ForeverDB, cliente). [[Rogue-Leveling]]
- **C66** — Rangos de nivel de Stonetalon y Thousand Needles distintos entre fuentes. Amplía C27. [[Leveling-Route-Orc]]


## Conflictos de la tanda 3 (2026-11-13)

### Mining y Engineering (2026-11-13)
- **C67** — Rangos de los entrenadores de Engineering en Orgrimmar/Ratchet (Thund, Nogg, Roxxik): Apprentice/Journeyman/Expert (Warcraft Tavern, Gfinity) frente a un rango más alto cada uno (Kami-Labs). [[Engineering]]
- **C68** — Apprentice de Engineering pide nivel 5 (ForeverDB, Gfinity) frente a nivel 1 (Eternadex). [[Engineering]]
- **C69** — Gfinity cita objetos de campamento, un mineral "Elementite" y recetas que no están en los datos del juego: tratar esa guía como poco fiable para Engineering. [[Engineering]], [[Ores]]
- **C70** — Especialización Gnomish/Goblin: skill 200 (Warcraft Tavern, Kami-Labs) frente a skill 200 y nivel 30 (Gfinity). [[Engineering]]
- **C71** — Puntos de aparición de mineral: Iron en Barrens 41 (ForeverDB) frente a 2 (The Forever Era); Ashenvale también difiere. [[Ores]]
- **C72** — Skill para Target Dummy y Rocket Boots distinta entre Method, Kami-Labs y The Forever Era. [[Engineering-for-Rogue]]
### Guías de novato (2026-11-13)
- **C36 actualizado**: los datos del cliente (build 1.60.1.70938) dicen que la Camp Tent rellena el descanso hasta un 5 % de nivel, como máximo una vez por hora. Apoya a Mein-MMO frente al "buff de 1 h" de Warcraft Tavern. Pendiente de verlo en el juego. [[XP-Buffs]]
- **C73** — Bonus de XP de la comida: Kami-Labs dice que no está en los archivos del juego; el cliente lo tiene (+5 %, Well Fed). Warcraft Tavern dice que toda comida cocinada lo da; solo la "Nutritious" lo da. [[Food-and-Cooking-for-Leveling]]
- **C74** — Cozy Sleeping Bag: el +1 % por acumulación se aplica también a la XP de misiones, no solo de muertes (cliente). Amplía C35. [[XP-Buffs]]
- **C75** — Basic Campfire: Cooking 1 frente a 20, en dos partes de la guía de Kami-Labs. [[Camping]]
### Ruta 30–60 (2026-11-13)
- **C76** — Rangos de mazmorras: Scarlet Monastery 34–45 (The Forever Era) frente a 30–38 (ForeverDB) frente a por ala (Method); Sunken Temple 50–56 / 50–60 / 50–55; Dire Maul 55–60 / 54–60 / 56–60. [[Dungeons-30-60]]
- **C77** — Truestrike Shoulders y Royal Seal of Eldre'Thalas: no están en el cliente (The Forever Era) frente a listados (ForeverDB). [[Rogue-BiS-by-Level]]
- **C78** — Reto de Legacy Master Spelunker: el texto dice "Timbermaw Hold" pero cuenta Blackmaw Hold. [[Legacy]]
- **C79** — ForeverDB omite en su lista de mazmorras las 5 nuevas de 35–60 (Drowned City, Krol'dok, Alcaz, Blackmaw, Shaper's Terrace) que su propia guía nombra, e incluye una desconocida "Manor Mistmantle". [[Dungeons-30-60]]
- **C80** — Riverglades (zona nueva, 150+ misiones, punto de vuelo Horde Rog'mar): The Forever Era la recomienda para 36–45; la ruta basada en datos de jugadores de ForeverDB no la incluye. [[Leveling-Route-Orc]]
- **C81** — Las listas de equipo de The Forever Era mezclan objetos solo Alliance y su lista de 60 usa raids no anunciados. [[Rogue-BiS-by-Level]]
- Pendiente de ver en el juego: The Forever Era no muestra punto de vuelo Horde en Western Plaguelands ni en Blasted Lands.
### Notas frente a datos del cliente (2026-11-13)
- **C82** — Charred Wand: nivel requerido 19 (notas) frente a 0 en el cliente, con nivel de objeto 28. Relacionado con C8. [[Priest-Wands]]
- **C83** — Greater Mystic Wand: "28+" (nota) frente a nivel requerido 30 (cliente). [[Priest-Wands]]
- **C84** — Lesser Magic Wand: el cliente la vende por 1 s 10 c frente a la nota oficial de que las varitas fabricadas se venden a 1 c. [[Priest-Wands]]
- **C85** — Clanking Cord: la nota cita versión de cuero; el cliente solo tiene una, de malla. El cinturón de cuero es Gizmo Girdle. [[Engineering-for-Rogue]]
- **C86** — Darkwood Staff y Thornroot Club: Method los da como armas de poder de hechizos; el cliente solo les da Stamina. [[Weapons-1-30]]
- **C87** — Varios niveles de Method lejos del nivel de objeto del cliente (Blade of Cunning, Ruby-Adorned Blade, otros); ambos valores se conservan. [[Weapons-1-30]], [[Rogue-Leveling]]
- **C33 (Malignant Root)**: el cliente dice que se liga al recoger, lo que apoya "no es BoE". Sigue abierto hasta verlo en el juego.
### Especializaciones Mage, Warlock y Druid (2026-11-13)
- **C88** — Daño de arma en formas Feral: ×1 (guía Feral DPS) frente a ×2,5 (guía Feral Tank). [[Feral-DPS-Druid]], [[Feral-Tank-Druid]]
- **C89** — Naturalist (Resto): reduce el enfriamiento de Wild Growth a 2,5 s (Method) frente a reduce el tiempo de lanzamiento 0,5 s (ForeverDB). [[Restoration-Druid]]
- **C90** — Frost: el texto dice Arcane Concentration 5/5 en las tres builds, pero la build de mazmorra no lo lleva. [[Frost-Mage]]
- **C91** — Niveles de raza distintos entre guías de Method de endgame y de leveling (Orc baja a B en Mage, Undead sube a A en Affliction, Orc en S para Destruction). [[Races]]
- Resuelve parte de C44: la guía de Balance muestra Skyborne Druid en ambas facciones.
### Especializaciones Warrior, Paladin, Hunter y Shaman (2026-11-13)
- **C92** — Improved Righteous Fury: 6 % de reducción de daño (guía Protection Paladin de Method) frente a 9 % a 3/3 (tooltip de ForeverDB). [[Protection-Paladin]]
- **C93** — Incoherencias internas de Method: Arms pone Haste tercera en estadísticas pero su página de razas dice que apenas la valora; el truco de muñeco + Blessing of Protection dura 8 s en una página y 10 en otra; las tablas de encantamientos de Hunter ponen uno de brazales en guantes. [[Arms-Warrior]], [[Protection-Paladin]]
- El BiS pre-raid de Protection Paladin incluye objetos de Classic no confirmados en Forever (Hand of Justice, Draconian Deflector). [[Protection-Paladin]]
### ForeverDB público (2026-11-13)
- **C94** — Comida y XP: /faq de ForeverDB dice que ninguna comida da XP; /veterans cita a Blizzard sobre un pequeño bonus de XP de la comida fabricada; el cliente tiene Well Fed +5 % (ver C73). [[XP-Buffs]], [[FAQ]]
- **C95** — Tope de hit con doble arma contra jefes de raid: 27 % (ForeverDB) frente a 29 % (Method). Relacionado con C32. [[Hit-Chance]], [[Stats-Explained]]
- **C96** — Krethis Shadowspinner: Tirisfal (ForeverDB) frente a Silverpine (games.gg). [[Rares-Horde-1-30]]
- **C55 actualizado (Bartering)**: el tooltip del cliente dice −5/10 % en todo vendedor, lo que apoya a Warcraft Tavern frente a Method. [[Legacy]]
- **C97** — Black War Wolf listado a nivel 40, 100 g y 100 % de velocidad: incoherente con el resto de monturas de 40. [[Mounts]]
- **C79 ampliado**: llms-full de ForeverDB también omite las 5 mazmorras nuevas, que su página /legacy sí nombra.
- Nota: Rogue-BiS-by-Level se sobrescribió por accidente el 2026-11-13 y se reconstruyó desde las fichas; sus afirmaciones sobre Bloody Brass Knuckles y Swinetusk Shank deben revisarse contra [[Dungeons-30-60]].

## Conflictos de la tanda 4 (2026-11-13, páginas de ForeverDB)
- **C98** — Skinning y Legacy: Kami-Labs decía que Skinning da puntos de Legacy a 150/225/300; ForeverDB y Blizzard dicen que solo las profesiones de fabricación. Se toma ForeverDB/Blizzard. [[Skinning]], [[Legacy]]
- **C99** — Armas de Rogue "no en el cliente": [[Rogue-Leveling]] las daba como posiblemente ocultas; ForeverDB registra diez de ellas cayendo en Forever (addon de jugadores). Resuelto a favor de ForeverDB para esas diez.
- **C100** — Karazhan Crypts y Demon Fall Canyon: Method las trata como mazmorras de Forever; ForeverDB dice que solo están en los archivos del cliente, sin anuncio de Blizzard. [[Karazhan-Crypts]], [[Demon-Fall-Canyon]]
- **C101** — Niveles de misión: ForeverDB da niveles más altos que Method (misiones de RFC 15–16 frente a 9; Book of Ur 26 frente a 16; Essence of Aku'Mai 22 frente a 17; Rig Wars 35 frente a 25; Going, Going, Guano! 33 frente a 30; A Vengeful Fate 34 frente a 29; Hearts of Zeal 33 frente a 30). ForeverDB pone An Unholy Alliance en RFD, no en RFK. Cómo resolver: en el juego. [[Dungeons-1-30]], [[Dungeons-30-60]]
- **C102** — Número de jefes: Ruins of Lordaeron 7 (ForeverDB) frente a 6 (Method); SFK 8 frente a 9 con raro; Dalaran 9 frente a 8. [[Ruins-of-Lordaeron]], [[Shadowfang-Keep]], [[City-of-Dalaran]]
- **C103** — Nivel de los talentos: la guía de ForeverDB dice que empiezan a nivel 5 y no a 10; su calculadora da 9 a 5. Cómo resolver: en el juego. [[Rogue-Leveling]]
- **C104** — Venenos (relacionado con C62): la página de PvP de ForeverDB dice que se aprenden con la misión de clase de nivel 20; su lista de misiones (datos de Classic) pone *Plundering the Plunderers* a 18. [[Rogue-Poisons]]
- **Nota sobre C7**: los rangos de nivel de mazmorra no chocan. El rango "hub" es el del buscador de grupos del cliente y el inferior viene de posts de Blizzard (Kaivax); ambos son oficiales.

## Conflictos de la tanda 5 (2026-11-13, datos del addon de ForeverDB)
- **C105** — Rangos de los entrenadores de Engineering: los títulos vistos en Forever (Thund Journeyman, Nogg Expert, Roxxik Artisan) coinciden con Kami-Labs, un rango por encima de Warcraft Tavern y Gfinity. Se toma el addon (visto en Forever). [[Engineering]]
- **C106** — Recompensa de *Scramble*: Iron Star (281660) según el addon; "Silver Star" en [[Quests-Stonetalon-Mountains]] y [[Cozy-Sleeping-Bag-Quest-Chain]].
- **C107** — *... and that note you found*: Lesser Troll's Blood **Elixir** (3388) según el addon; "Potion" en [[Quests-The-Barrens]].
- **C108** — Shipping Label: el addon solo la tiene en Stormwind y Undercity (61.0, 48.2) a nivel 60; [[Quests-The-Barrens]] la pone con Dokimi en Crossroads.
- **C109** — Puntos de mineral por zona: el addon, The Forever Era y la guía de ForeverDB dan cifras distintas (p. ej., Iron en los Barrens 10 / 2 / 41; Gold y Mithril en Stonetalon ninguno / 27 y 15). [[Mining-Nodes]]
- **C110** — Objetos "no en el cliente" según wago.tools (Kris of Orgrimmar, Wingblade, Outlaw Sabre): el addon tiene sus estadísticas y los jugadores los vieron como recompensa en Forever. Resuelto: existen. [[Weapons-1-30]], [[Rogue-Leveling]]
- **C111** — Habilidad para aprender Target Dummy: 85 (addon, dato de entrenador de Classic; Kami-Labs), ?/115 (The Forever Era), 145 (Method). [[Engineering]]
- **C112** — *Stepping Stones* (79192): el addon la sitúa en los Barrens (46.4, 73.8); la nota de Stonetalon la pone en Stonetalon. [[Quests-Stonetalon-Mountains]]
- **C113** — Entrenadores: en el addon Norzsh no es entrenador de Mining y Kaylaena Springwhisper no aparece. Añade a Strange Hermit (Zephras Isle) como entrenador de Engineering visto en Forever. [[Mining]], [[Engineering]]
- **C64 (actualización)** — El addon da a elegir en *Hidden Enemies* entre Kris, Hammer, Axe y Staff of Orgrimmar: las dos fuentes tenían razón en parte. Resuelto.

## Conflictos de la tanda 6 (2026-11-15, Troll Frost Mage)
- **C114** — Talentos Frost 10–30: ForeverDB pone Improved Frost Nova y Ice Lance a 20; Method pone Precision antes y Ice Lance a 21, cambia a Arcane a 43 (ForeverDB sigue Frost puro) y su orden a 29 rompe las reglas de filas del cliente. [[Mage-Leveling]], [[Frost-Mage]], [[Playbook-Mage-1-20]], [[Playbook-Mage-20-30]]
- **C115** — Cold Snap: Method lo pone a 34; en el cliente es talento disponible desde 30 y ForeverDB lo toma a 40. [[Mage-Leveling]]
- **C116** — Penalización por rango bajo: la página de downrank de ForeverDB dice que el cliente no la tiene; su guía de leveling cita notas de Blizzard del 1-oct que dicen que sí existe en el servidor. Cómo resolver: en el juego. [[Mage-Leveling]]
- **C117** — Fire Blast en la rotación Frost: el simulador de ForeverDB da más daño sin él a 20–39; su guía de clase lo usa. [[Frost-Mage]]
- **C118** — Objeto de campamento de Tailoring: Intellect según Method ([[Tailoring]]); Faction Banner con Spirit según [[Camping]].
- **C119** — Rangos de los entrenadores de Enchanting: Godan Journeyman y Hgarth Expert (Method) frente a Expert y Artisan en el addon. Los títulos de NPC pueden no coincidir con el rango que enseñan. [[Enchanting]]
- **C120** — Comprehend Scroll: Method dice que se aprende del entrenador a 6; la lista de ForeverDB de nivel 6 no lo incluye. **Resuelto el 2026-11-15:** el usuario lo aprendió en el juego a nivel 6 (observado, sin export). [[Mage-Comprehension]]
- **C121** — Prioridad de estadísticas: Method pone Haste por encima de Intellect; los pesos de ForeverDB ponen hit y regeneración de maná por encima de spell power. [[Frost-Mage]]
- **C122** — Sable Wand: la guía de leveling de ForeverDB la recomienda, pero su misión es solo de la Alliance (Stormwind) según el addon. No sirve para la Horde. [[Mage-Quest-Rewards-1-30]]
- **Errores de datos de ForeverDB** (no son conflictos de mecánica): la guía de Valley of Trials da a Norzsh como vendedor de armas y a Nartok como entrenador de Blacksmithing; la guía de Troll Mage lista *Vile Familiars* como misión de clase (en el addon es general, 792).

## Conflictos de la tanda 7 (2026-11-15, oro y Enchanting)
- **C123** — Frost Nova + Blizzard: [[Mage-Leveling]] y [[Playbook-Mage-20-30]] recomiendan la combinación, pero el hotfix del 2026-11-13 hace que el daño de Blizzard rompa Frost Nova. Ver [[Gold-Making-Mage]]. Falta añadir esa línea a [[src-blizzard-hotfixes-24315281]].
- **C124** — Plano del Arcane Salvager: Charlga Razorflank (RFK) según el addon; Rath'mael (Ruins of Lordaeron) según Warcraft Wiki. [[Enchanting]]
- **C125** — Profession Certification: [[Titles]] da su origen como desconocido; [[Durotar-Supply-and-Logistics]] dice 1000 Merchant's Favor y el addon pone las certificaciones de Enchanting y Tailoring en Beneris y Jim'bek.
- **C126** — Armadura del Enchanted Lute: +28 (Blizzard Watch, beta) frente a 308 (addon y ForeverDB). [[Camping]], [[Enchanting]]
- **C127** — "Ninguna fuente tiene precios": [[Auction-House]] y [[Gold-Making]] lo dicen, pero las páginas de objeto de ForeverDB traen escaneos de subasta con fecha (de otros rulesets). Hay que matizar esas notas.
- **C128** — Rutas para subir Enchanting y Tailoring: ForeverDB (unos 318 Strange Dust para la Horde) frente a Method. [[Enchanting]], [[Tailoring]]
- **C129** — Desencantar blancos: la FAQ de Strange Dust de ForeverDB dice que se puede; Warcraft Tavern dice que solo verde o mejor. Cómo resolver: en el juego. [[Enchanting]]
- **C130** — Cooldown de Ice Lance: Method dice 8 s; los datos del cliente (azeroth.wiki, 2026-11-18) no le dan cooldown propio, solo el global de 1,5 s. R1 (nivel 20): 27–33 de daño, 45 de maná, instantáneo, ×4 contra congelados. Cómo resolver: en el juego (¿se queda gris el botón tras lanzarlo?). [[Frost-Mage]], [[Playbook-Mage-20-30]]
- **C131** — Novice Arcanist's Sash (y Ardent's): warcraft.wiki.gg ("Forever tailoring patterns", editada el 2026-10-28) la da como receta de **entrenador a skill 35**; el cliente (azeroth.wiki y ForeverDB, 2026-11-18) tiene un **Pattern: Novice Arcanist's Sash** azul que pide Tailoring 50, sin fuente registrada, y el addon pone la receta a skill 50. La misma página del wiki pone Pearl-clasped Cloak a 70 frente a 90 en el addon. Cómo resolver: en el juego, mirando la lista de Snang. [[Tailoring]]

## Estado de verificación
- Estado: conflicting
- Confianza: medium
- Última verificación: 2026-11-10
- Build/versión: Forever 1.60.1 (lanzamiento)

## Preguntas pendientes
- Revisar los conflictos marcados "Cómo resolver: en el juego" cuando lleguen los primeros exports.
- El alcance de la AH (¿por ruleset, región o facción?) todavía no es un conflicto documentado porque solo hay una fuente leída (GamerFuzion, de segunda mano). Ver [[Auction-House]].
