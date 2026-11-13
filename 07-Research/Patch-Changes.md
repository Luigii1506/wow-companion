---
type: topic
tags: [research, forever]
status: confirmed_forever
confidence: medium
last_verified: 2026-11-10
game_version: "Forever 1.60.1 (launch)"
sources:
  - https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696
  - https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696/9
  - https://news.blizzard.com/en-us/article/24315281
  - https://news.blizzard.com/en-us/article/24302093/
  - https://worldofwarcraft.blizzard.com/en-gb/news/24303313
  - https://kami-labs.fr/en/wow-forever/patch-notes-2-novembre-notes-de-lancement/
  - https://www.warcrafttavern.com/forever/news/wow-forever-pre-launch-class-changes-bug-fixes/
  - https://www.gamerfuzion.com/world-of-warcraft-forever-launch-patch-notes-class-damage-buffs-mob-health-training-costs/
  - https://www.warcrafttavern.com/forever/guides/experience/
  - https://www.warcrafttavern.com/forever/news/camping-profession-buffs-in-world-of-warcraft-forever
  - https://www.warcrafttavern.com/forever/news/legacy-tree-rewards-in-world-of-warcraft-forever
  - https://www.gamerfuzion.com/world-of-warcraft-forever-rule-sets-separate-layering-realmless-world-refresh/
  - https://www.gfinityesports.com/article/world-of-warcraft-forever-skinning-guide-leveling-1300-trainers
  - https://foreverdb.net/veterans
  - https://foreverdb.net/datamine
  - https://foreverdb.net/datamine/world
  - https://foreverdb.net/datamine/removed
  - https://foreverdb.net/changelog
  - https://foreverdb.net/class/Rogue/changes
  - https://foreverdb.net/stats
  - https://foreverdb.net/mounts
  - https://foreverdb.net/reputation
  - https://foreverdb.net/legacy
  - https://foreverdb.net/guide/getting-started
  - https://foreverdb.net/guide/making-money
  - https://foreverdb.net/guide/pvp-guide
  - https://foreverdb.net/faq
  - https://foreverdb.net/llms-full.txt
---

# Cambios de WoW Forever frente a Classic

## Resumen
Forever no es Classic con otro nombre. Las diferencias que más afectan a un **Undead Priest de nivel ~9 con Herbalism + Skinning** son estas:
1. **Coste de entrenamiento** de clase: 206–207 g en total (1–60), igual para todas las clases (`confirmed_forever`).
2. **XP de mazmorras +50 %** (hotfix del 2026-11-09), sumado a un +20 % anterior de la beta (`confirmed_forever`).
3. **Respawns más rápidos** en zonas de nivel bajo, de forma temporal (`confirmed_forever`).
4. **Montura incluida en el entrenamiento de riding** (modelo TBC) (`confirmed_forever`; las cifras están en [[Mount-and-Costs]]).
5. **Sistemas nuevos**: Camping (rested XP y buffs junto a la hoguera), Legacy (talentos de cuenta: Well Rested, Bountiful Harvest, Bartering) y rulesets "sin reinos" (`confirmed_forever`).
6. **Priest/Undead**: Touch of the Grave con ICD de 15 s; Shadow Word: Death y Power Word: Shield cambiados; Binding Heal reemplazado por Holy Binding (`confirmed_forever`).

Relacionado: [[Sources]] · [[Conflicts]] · [[Mount-and-Costs]] · [[Auction-House]]

## Cómo funciona (lectura de este documento)
- **Fuente primaria**: notas de Kaivax en el foro oficial ("Beta Development Notes – Updated November 2", post #9 del 2026-11-03) y la página oficial de hotfixes. Kami-Labs, Warcraft Tavern y GamerFuzion coinciden con el original en todo lo que se comparó.
- Las notas oficiales casi nunca dan la cifra de Classic ("was X" se refiere a la build anterior de la beta, **no** a Classic). Por eso, la columna "frente a Classic" dice "desconocido" salvo que una fuente lo indique.
- Abreviaturas de fuente: **DN** = notas de desarrollo (hilo raíz, por fecha de build); **DN#9** = post del 2-nov; **HF** = hotfixes oficiales; **DD** = Deep Dive oficial (2026-09-13); **WT** = Warcraft Tavern; **KL** = Kami-Labs.

## Datos específicos de WoW Forever (por sistema)

### XP y nivelación
| Cambio | Estado | Fuente | Fecha |
|---|---|---|---|
| Nivel máximo 60 (en la beta estaba limitado a 30) | confirmed_forever | Anuncio oficial 24302093; DN 1-oct (cap 30 en beta) | 2026-09 / 2026-10-01 |
| Sin cambio general de la tasa de XP en las notas de lanzamiento; solo ajustes de XP en algunas misiones (p. ej. "Holy Diver" ahora da XP) | confirmed_forever | DN#9; KL | 2026-11-02 |
| XP de criaturas de mazmorra +~20 % | confirmed_forever | DN 8-oct | 2026-10-08 |
| **XP de todas las muertes en mazmorra +50 %** | confirmed_forever | HF 9-nov | 2026-11-09 |
| Las misiones de mazmorra dan un 50 % menos de XP extra (más allá del valor normal de una misión) | confirmed_forever | DN 1-oct | 2026-10-01 |
| La XP de grupo usa el nivel de cada jugador "como en Classic Era" | confirmed_forever | DN 8-oct | 2026-10-08 |
| Las misiones de mazmorra de Ruins of Lordaeron piden nivel 15 (antes una mezcla de 15 y 16) | confirmed_forever | DN#9 | 2026-11-02 |
| Tabla de XP: 400 (nv 1) → 209 800 (nv 59); 4 084 700 en total | unknown (solo guía sin fecha) | WT experience | sin fecha |
| Rested: dobla la XP de muertes (no la de misiones); +5 % del nivel cada 8 h; tope 150 % | probable_classic (lo dice una guía y coincide con Classic) | WT experience | sin fecha |

### Camping (sistema nuevo)
| Cambio | Estado | Fuente | Fecha |
|---|---|---|---|
| La Basic Campfire crea un campamento con vendedores, reparación, estaciones de profesión y buffs de 1 h; sentarse a descansar activa los buffs | confirmed_forever | DD | 2026-09-13 |
| Hasta 3 objetos por campamento (5 o 10 si un cocinero mejora la hoguera); los objetos iniciales se aprenden con skill 20 de la profesión; los avanzados vienen de Blueprints que sueltan jefes de mazmorra | confirmed_forever | DD | 2026-09-13 |
| Herbalism tiene un objeto de camp: **Incense Candle (+Intellect)**. Útil para un Priest | confirmed_forever | DD | 2026-09-13 |
| Skinning: ningún objeto de camp nombrado | unknown | DD; WT | 2026-09-13 |
| Las hogueras ya no dañan a jugadores de nivel <5; existe un debuff "Boosted Rest" | confirmed_forever | DN 1-oct | 2026-10-01 |
| Camp Tent (Leatherworking) da un buff de XP tipo rested; Cozy Sleeping Bag da hasta +3 % de XP | unknown (solo guía) | WT experience | sin fecha |

### Legacy (sistema de cuenta, nuevo)
| Cambio | Estado | Fuente | Fecha |
|---|---|---|---|
| Los puntos se ganan con Legacy Challenges y se comparten entre personajes; cada personaje los gasta en tres árboles (Professions, Adventure, Resourcefulness); máximo 16 por personaje al lanzamiento | confirmed_forever | DD | 2026-09-13 |
| **Well Rested**: más rested XP y tope más alto | confirmed_forever (nombre y efecto); cifras unknown | DD; WT (4 % por rango, 5 rangos) | 2026-09-13 |
| **Bountiful Harvest**: más materiales de Mining/Herbalism/Skinning | confirmed_forever (efecto); cifras unknown | DD; WT ("20 % more Scarce materials", 5 rangos) | 2026-09-13 |
| **Bartering**: −5 % en precios de vendedor (2 rangos) | unknown (solo WT) | WT legacy | 2026-09-13 |
| **Frequent Flier**: −50 % en vuelos y vuelos un 20 % más rápidos | unknown (solo WT) | WT legacy | 2026-09-13 |
| Reagent Economy (Resourcefulness): elimina los reagentes de habilidades de clase | confirmed_forever | DD | 2026-09-13 |
| Respec más barato de puntos Legacy: 1 s (beta) | confirmed_forever (beta) | DN 8-oct | 2026-10-08 |

### Respawns
| Cambio | Estado | Fuente | Fecha |
|---|---|---|---|
| Respawns más rápidos en zonas bajas (sobre todo las iniciales) y más lentos a medida que se sube; volverán a "more typical rates" cuando pase la ola del lanzamiento. Sin temporizadores publicados | confirmed_forever | DN#9 | 2026-11-02 |
| Ajustes puntuales de respawn (Yarrog en Durotar; Ivar the Foul en Silverpine; Deathstalker Erland más rápido para "Escorting Erland", etc.) | confirmed_forever | HF 5/6/9-nov | 2026-11-05/09 |

### Entrenamiento de clase
| Cambio | Estado | Fuente | Fecha |
|---|---|---|---|
| Entrenar todas las habilidades de clase del 1 al 60 cuesta **entre 206 y 207 g** para todas las clases; las habilidades del mismo nivel cuestan lo mismo, **salvo las habilidades raciales de Priest**; Warlock con descuento por los Grimoires | confirmed_forever | DN#9; KL; WT; GamerFuzion | 2026-11-02 |
| Coste por nivel/habilidad | unknown | — | — |
| Comparación con el total de Classic | unknown (no investigado) | — | — |

### Monturas y viaje
| Cambio | Estado | Fuente | Fecha |
|---|---|---|---|
| El coste de la montura pasa al entrenamiento de riding (modelo TBC); recibes una montura al aprender riding | confirmed_forever | DD | 2026-09-13 |
| Nivel y coste: ver [[Mount-and-Costs]] (nivel 40 / 100 g según guías de beta) | unknown | Method; WT; KL | 2026-10 |
| Las monturas de la tienda (Cerulean Prideclaw) exigen comprar el riding skill en el juego | confirmed_forever | Anuncio 24302093 | 2026-09 |
| La misión de Warlock "Summon Felsteed" otorga **apprentice riding skill** (confirma el nombre de la habilidad en vivo) | confirmed_forever | HF 9-nov | 2026-11-09 |
| Gamepad: se puede terminar un vuelo antes de tiempo (te desmonta en el siguiente punto de vuelo) | confirmed_forever | DN#9 | 2026-11-02 |
| No se puede montar dentro de Stratholme | confirmed_forever | HF 9-nov | 2026-11-09 |

### Bolsas, interfaz y gamepad
| Cambio | Estado | Fuente | Fecha |
|---|---|---|---|
| Las bolsas **ya no se equipan solas** en un hueco libre; hay que equiparlas a mano | confirmed_forever | DN#9 | 2026-11-02 |
| Los hechizos aprendidos ya no se añaden solos a las barras de acción | confirmed_forever | DN#9 | 2026-11-02 |
| Las placas de nombre muestran si un enemigo es élite; las bolsas combinadas muestran la bolsa de origen | confirmed_forever | DN#9 | 2026-11-02 |
| Soporte de gamepad (todavía en beta) | confirmed_forever | DN#9 | 2026-11-02 |
| Los vendedores de Zephras Isle venden bolsas de profesión de aprendiz | confirmed_forever | HF 5-nov | 2026-11-05 |

### Mazmorras y Group Finder
| Cambio | Estado | Fuente | Fecha |
|---|---|---|---|
| Existe un Group Finder/LFG en el juego (postings, modo de voz, filtro por nivel) | confirmed_forever | DN 1/8/16-oct | 2026-10 |
| Mazmorras nuevas (p. ej. Excavation Site: Wetlands, City of Dalaran, The Drowned City, Shaper's Terrace) | confirmed_forever | DN; HF | 2026-09/11 |
| La facción y el ruleset limitan los grupos (no hay grupos cruzados entre rulesets) | confirmed_forever | DD | 2026-09-13 |

### Reinos, AH y correo
| Cambio | Estado | Fuente | Fecha |
|---|---|---|---|
| Los reinos se sustituyen por **rulesets** (Normal, PvP, Roleplaying; Hardcore después del lanzamiento); nombres en dos partes, únicos por región | confirmed_forever | DD | 2026-09-13 |
| AH: columna de nivel equipable y sufijos mostrados correctamente | confirmed_forever | DN 1/16-oct | 2026-10 |
| AH separada por ruleset; sin comercio entre rulesets al lanzamiento | unknown (de segunda mano, podcast vía PCGamesN) | GamerFuzion rulesets | ~2026-11-01 |
| Comisión y depósito de la AH | unknown | — | — |
| Correo: arreglo de apellidos (surnames) en el correo | confirmed_forever | DN 24-sep | 2026-09-24 |

### Recolección y profesiones
| Cambio | Estado | Fuente | Fecha |
|---|---|---|---|
| **Skinning**: cada criatura solo se puede despellejar una vez antes de desaparecer ("once again") | confirmed_forever | DN 1-oct | 2026-10-01 |
| Skinning: "Rough Wolf Pelts" se cancela si desaprendes Skinning | confirmed_forever | HF 6-nov | 2026-11-06 |
| Skinning en Undead: entrenadores Rand Rhobart (Brill) y Killian Sanatha (Undercity) | unknown (solo guía) | Gfinity | 2026-11-02 |
| Rangos: Apprentice/Journeyman 1–150; Expert 150–225 (nv 20+); Artisan 225–300 (nv 35+) | unknown (guía con errores) | Gfinity | 2026-11-02 |
| Herbalism: sin cambios propios en las notas de lanzamiento ni en los hotfixes | confirmed_forever (no hay cambios publicados) | DN#9; HF | 2026-11-02/09 |
| "Cultivation" (racial de Tauren) pide un nivel de jugador por cada hierba y tiene 15 min de cooldown. **No afecta a Undead** | confirmed_forever | DN 24-sep, 16-oct | 2026-09/10 |
| Menos vetas Poor Copper en zonas iniciales | confirmed_forever | DN 1-oct | 2026-10-01 |
| Se bajó el precio de venta a vendedor de muchos objetos creados con profesiones; las varitas encantadas se venden a 1 c | confirmed_forever | DN 1/16-oct | 2026-10 |
| Mild Spices se venden a 1 c (antes 2 c) | confirmed_forever | HF 5-nov | 2026-11-05 |
| Tanning Rack: requisito de skill bajado de 140 a 125 | confirmed_forever | HF 6-nov | 2026-11-06 |
| Más de 600 recetas nuevas | confirmed_forever | DD | 2026-09-13 |

### Razas
| Cambio | Estado | Fuente | Fecha |
|---|---|---|---|
| **Undead – Touch of the Grave**: ICD de 15 s (antes 25 s); se activa más a menudo; visual arreglado | confirmed_forever | DN#9 | 2026-11-02 |
| Undead – Touch of the Grave (build anterior): 30 % de probabilidad para casters, ICD de 25 s | confirmed_forever (sustituido) | DN 16-oct | 2026-10-16 |
| Undead – Cannibalize: vuelve a poder usarse siendo inmune al daño físico | confirmed_forever | DN#9 | 2026-11-02 |
| Undead – Will of the Forsaken: se puede usar dormido o charmeado | confirmed_forever | DN 8-oct | 2026-10-08 |
| Corrección de las estadísticas base de todas las razas | confirmed_forever | DN#9 | 2026-11-02 |
| Raza nueva **Skyborne** (High Order / Windshaper): Wind-Blessed Haste 2 %, Read Leyline, Skysight, etc. Requiere un pack de pago | confirmed_forever | DN#9; anuncio 24302093 | 2026-11-02 |
| Otras: Troll Berserking 15 s; Orc Blood Fury 2 min; Human Spirit +10 %; Dwarf Artisan's Precision; Tauren Plainsrunning ya no afecta a la velocidad montado | confirmed_forever | DN#9 | 2026-11-02 |

### Priest
| Cambio | Estado | Fuente | Fecha |
|---|---|---|---|
| Daño subido en todas las clases y más salud para las criaturas de nivel alto (sin porcentajes globales publicados) | confirmed_forever | DN#9; GamerFuzion | 2026-11-02 |
| Power Word: Shield se puede reemplazar por un rango igual o mayor | confirmed_forever | DN#9 | 2026-11-02 |
| Shadow Word: Death: si falla al matar, el Priest recibe el 30 % de su vida máxima (antes 10 %); ya no hace daño al Priest si falla el golpe (miss) | confirmed_forever | DN#9 | 2026-11-02 |
| Holy: Binding Heal eliminado → **Holy Binding** (el 50 % del Flash Heal a otros también cura al Priest, sin amenaza) | conflicting (ver [[Conflicts]]) | DN#9 vs datamining de KL | 2026-11-02/03 |
| Undead Priest – Dark Sacrifice ya no rompe el control de masas | confirmed_forever | DN#9 | 2026-11-02 |
| Shadow: Cure/Abolish Disease ya no sacan de Shadowform; Vampiric Embrace no hace críticos; Devouring Contagion no se propaga desde critters | confirmed_forever | DN#9 | 2026-11-02 |
| Cooldowns (build 16-oct): Devouring Plague 24 s, SW:Death 18 s, Vampiric Embrace 30 s; Devouring Plague puede hacer crítico (1-oct) | confirmed_forever (beta; no revertido en lo leído) | DN 1/16-oct | 2026-10 |
| Penance rediseñado; rango 1 con +50 % de coste de maná | confirmed_forever (beta) | DN 8-oct | 2026-10-08 |
| Fear Ward ya no rompe Shadowform; Power Infusion persiste en aliados | confirmed_forever | HF 9-nov | 2026-11-09 |
| Dual spec a nivel 40 (precio desconocido) | confirmed_forever (según KL, que cita deep dives oficiales; el original no se consultó) | KL nivel 40 | 2026-10-31 |

## Diferencias frente a Classic
- **Sistemas que no existen en Classic**: Camping, Legacy, rulesets sin reinos, Group Finder, Skyborne, más de 600 recetas, mazmorras nuevas, gamepad.
- **Sistemas cambiados**: montura incluida en riding (modelo TBC); entrenamiento uniforme de 206–207 g; XP de mazmorra aumentada; respawns dinámicos; las bolsas no se equipan solas.
- **Igual o muy probablemente igual a Classic**: reglas básicas de rested XP y del reparto de XP en grupo (`probable_classic`, según guía).

## Diferencias frente a Classic según ForeverDB
> [!info] Añadido el 2026-11-13 desde ForeverDB
> Datos del cliente de Forever (build **1.60.1.70938**, extraída el 2026-11-13) comparados con el cliente de Classic Era, más posts de Blizzard que cita ForeverDB. Que algo esté en el cliente es `confirmed_forever` en cuanto a su existencia; lo que ForeverDB marca "Classic data" (CMaNGOS) es `probable_classic` y lo que marca "Speculation" es `unknown`. Fichas: [[src-foreverdb-veterans]], [[src-foreverdb-datamine]], [[src-foreverdb-datamine-world]], [[src-foreverdb-datamine-removed]], [[src-foreverdb-changelog]], [[src-foreverdb-class-rogue-changes]].

### Por sistema
| Sistema | En Forever | Frente a Classic | Estado | Ficha |
|---|---|---|---|---|
| Reglas del mundo | Sin monturas voladoras ni escalado de nivel; tope 60; raids nuevas el 9-dic (Hyjal Summit 20 jugadores, Barrow Deeps 10) | Igual que Classic en vuelo y escalado | confirmed_forever | veterans |
| Reinos | Rulesets (Normal, PvP, Roleplaying; Hardcore más tarde), cada uno un mundo único | Lista de reinos en Classic | confirmed_forever | veterans |
| Raciales | 26 de los 32 raciales de Classic cambian. **Orc**: Blood Fury (+10 % AP y poder con hechizos, 15 s), Shatter Curse (quita maldiciones, −5 % daño mágico 8 s), Command, Hardiness (aturdimientos −20 %) | Cambiados | confirmed_forever | veterans; guide-getting-started |
| Combinaciones raza/clase | 6 nuevas (Human Hunter, Orc Mage, Dwarf Shaman, Undead Paladin, Gnome Priest, Troll Warlock); raza Skyborne (packs de pago) | Nuevas | confirmed_forever | guide-getting-started |
| Estadísticas | Hit y crit son **un solo stat** cada uno (cuerpo a cuerpo, distancia y hechizos). Ratings en el equipo: 14 crit rating = 1 % crit, 10 hit rating = 1 % hit, a cualquier nivel | Classic separa hit/crit de hechizo y no usa ratings | confirmed_forever | stats; veterans |
| Habilidades de clase | 39 nuevas (Rogue 2: **Poised** nv 18, **Shank** nv 24); 1257 hechizos de clase distintos | Nuevas o cambiadas | confirmed_forever | datamine |
| Rogue: armas | Hachas de una mano desde nivel 1 | Classic: no | confirmed_forever | class-rogue-changes |
| Rogue: Sap | No exige sigilo ni lo rompe; 1 objetivo (2 con Quick Getaway) | Classic: exige sigilo | confirmed_forever | class-rogue-changes |
| Rogue: Rupture | Base mucho menor (rango 6: 105 frente a 180) | Menos daño | confirmed_forever | class-rogue-changes |
| Rogue: Expose Armor | −450 armadura por punto (rango 5) frente a −340 | Más fuerte | confirmed_forever | class-rogue-changes |
| Rogue: talentos | Eliminados Murder, Mace Spec, Fist Weapon Spec, Sleight of Hand, Improved Sap. Nuevos: Dirty Tricks, Blood Splatter, Composure, Quick Getaway, Venom, Flash of Steel, Death Mark, **Mutilate (nv 40)** | Árboles rehechos | confirmed_forever | datamine-removed; class-rogue-changes |
| Objetos | 6009 nuevos y 3592 cambiados. Objetos únicos de jefe de mazmorra en azul (Blizzard). 65 objetos "horizontales" (mejores en una zona o contra un tipo de enemigo). 36 sets nuevos y 76 con bonus nuevos | El botín de Classic no sirve de guía | confirmed_forever | veterans |
| Transmog | Opcional, en transmogrificadores de algunas ciudades; se puede apagar entero | Nuevo | confirmed_forever | veterans |
| Reputaciones | 14 facciones nuevas (Horda: Darkspear Raiders, Bolder'ok Clan, Earthen Ring, Windshapers; para todos: Powderfuse, The Watchers, Nightclaw Druids, Guardians of Hyjal...) | Nuevas | confirmed_forever | reputation |
| Profesiones | 928 de 2493 recetas nuevas y 737 cambiadas. Las pociones de curación normales y los antídotos pasan a **First Aid**. Skinning tiene **Tanning**; Mining funde barras nuevas. Elementos de camp mejores a skill 140 y 300 | Rehechas | confirmed_forever | veterans |
| Consumibles | 401 nuevos | Nuevos | confirmed_forever | veterans; consumables |
| Monturas | Pagas el riding y recibes montura. Apprentice Riding (75) = 60 %, Journeyman (150) = 100 %. Cada objeto **enseña** la montura. Precios del cliente: lobos 20 g (Classic 80 g), lobos rápidos 200 g (Classic 1000 g) | Más baratas; modelo TBC | confirmed_forever | mounts |
| Viaje | 20 rutas de vuelo, 7 maestros de vuelo y 5 rutas de barco/zepelín nuevas (p. ej. Tanaris ↔ Riverglades) | Nuevas | confirmed_forever | veterans |
| PvP | Honor como moneda + Rank Points con tope semanal; temporadas; honor igualado entre BG; Darkspear Islands (nuevo, 30–60); BG mezclan rulesets salvo Hardcore | Sistema de honor de Classic simplificado | confirmed_forever | guide-pvp-guide |
| PvP sin anunciar | Battle for Gilneas, Battle for Blackrock, Mak'gora Arena y un WSG de invierno están en el cliente | — | unknown | datamine-world |
| Casa de subastas | Tasas del cliente: facción depósito 5 % y comisión 5 %; neutral (Blackwater) 25 % y 15 % | Fórmula del depósito: la de Classic (Speculation) | confirmed_forever (tasas) / unknown (fórmula) | guide-making-money |
| Legacy | 65 retos = 65 puntos de cuenta; 16 por personaje; Bartering −5/10 % en todos los vendedores (tooltip) | Nuevo | confirmed_forever | legacy |
| Mazmorras nuevas | Hall of Thanes 13+, Ruins of Lordaeron 15+, Excavation Site: Wetlands 26+, City of Dalaran 28+, Manor Mistmantle | Nuevas | confirmed_forever | veterans; guide-first-dungeon |
| Interfaz y macros | Focus y mouseover existen; sintaxis de macros moderna; Cooldown Manager (desactivado por defecto) | Classic Era oculta el focus | confirmed_forever | macros; guide-getting-started |
| Ritmo de combate | Un monstruo normal debe morir en unos 10–15 s (Blizzard) | Igual que Classic | confirmed_forever | veterans |
| Cazador | 2 familias nuevas (Core Hound, Fox) | Nuevas | confirmed_forever | veterans |

### Builds del cliente desde el lanzamiento
| Build | Fecha | Cambios (ForeverDB) |
|---|---|---|
| 1.60.1.70790 | 2026-11-04 | 25 habilidades de clase, 74 talentos, 66 hechizos |
| 1.60.1.70862 | 2026-11-07 | 621 objetos, 24 hechizos |
| 1.60.1.70888 | 2026-11-11 | 539 objetos, 52 hechizos; monturas pasan a ligarse al recogerlas (llms-full) |
| 1.60.1.70938 | 2026-11-13 | 135 objetos, 4 talentos, 2 habilidades |

### Lo que más afecta a un Orc Rogue de nivel 11 (Mining + Skinning)
- **Sap a partir del nivel 10 sin necesidad de sigilo** y sin romperlo: más control al subir (`confirmed_forever`, cliente).
- **Hachas de una mano** disponibles: más armas útiles en Combat (`confirmed_forever`).
- **Shank** a nivel 24 y **Poised** a 18: habilidades nuevas que alimentan talentos nuevos (Venom, Flash of Steel, Boot Knife, Composure).
- **Rupture** pega mucho menos que en Classic: no planificar el daño como en guías de Classic.
- Blood Fury +10 % AP 15 s y Hardiness: útil en PvP y para matar más rápido.
- Skinning tiene recetas propias (**Tanning**) y Mining funde barras nuevas. **Mining y Skinning no dan puntos Legacy** (solo las 6 de producción) ni título de profesión.
- Lobo normal a 20 g en el cliente; el coste del Apprentice Riding sigue sin dato oficial (ver [[Mount-and-Costs]]).

### Discrepancias encontradas en ForeverDB
- **Comida y XP**: /veterans dice que Blizzard menciona un pequeño bonus de experiencia por comida crafteada; /faq afirma que **ninguna comida** da XP en Forever. → `conflicting`.
- **Lista de mazmorras**: llms-full.txt no incluye Drowned City, Krol'dok, Alcaz Prison, Blackmaw Hold ni Shaper's Terrace, pero los retos de Legacy (/legacy) sí los nombran como mazmorras.
- **Hit con doble arma contra jefe**: ForeverDB 27 %; [[Hit-Chance]] recoge 29 % de Method.

## Recomendaciones prácticas (para el Undead Priest nv ~9)
- Llevar el control de los gastos de entrenamiento: 206–207 g en total hasta el 60; el reparto por nivel es desconocido.
- Aprovechar los respawns rápidos de las zonas bajas mientras duren (Blizzard ya avisó que los bajará).
- Con Herbalism a skill 20, investigar en el juego el objeto de camp **Incense Candle** (+Intellect).
- Considerar las mazmorras para subir: +50 % de XP desde el 2026-11-09.
- Equipar a mano cada bolsa nueva.
- Las habilidades nuevas no aparecen solas en la barra: hay que arrastrarlas desde el spellbook.

## Lista cronológica de parches y hotfixes encontrados
| Fecha | Qué | Fuente | Estado |
|---|---|---|---|
| 2026-09-13 | Panel Deep Dive (BlizzCon): Camping, Legacy, rulesets, montura en riding | https://worldofwarcraft.blizzard.com/en-gb/news/24303313 | Oficial |
| 2026-09-17 | Empieza la beta | https://news.blizzard.com/en-us/article/24302093/ | Oficial |
| 2026-09-24 | Build de beta (Cultivation, camping, Skinning con Helene Peltskinner, PW:S) | DN | Oficial |
| 2026-10-01 | Build de beta (cap 30, XP de misiones de mazmorra, "skin once", AH con sufijos, precios de vendedor) | DN | Oficial |
| 2026-10-08 | Build de beta (XP de mazmorra +20 %, XP de grupo, Legacy, Penance) | DN | Oficial |
| 2026-10-15/16 | Build de beta (raciales, cooldowns de Priest, columna de AH, precios de vendedor de profesiones) | DN | Oficial |
| 2026-10-26/27 | Repaso de raciales | DN | Oficial |
| 2026-11-02 (publicado el 2026-11-03) | **Notas de lanzamiento** (~223 cambios según KL) | DN#9 | Oficial |
| 2026-11-04 | Sección de UI y accesibilidad añadida; **lanzamiento** (15:00 PST) | DN; anuncio | Oficial |
| 2026-11-05 | Hotfixes (respawns, bolsas de profesión en Zephras, Mild Spices) | HF | Oficial |
| 2026-11-06 | Hotfixes (Tanning Rack 125, Voidwalker +40 de vida, misiones) | HF | Oficial |
| 2026-11-09 | Hotfixes (XP de mazmorra +50 %, Priest, riding del Warlock, población de zonas) | HF | Oficial |
| 2026-11-10 | Cambios de clase previstos según una guía de terceros (accountshark), **no verificados** | — | unknown |

## Fuentes
- URL: https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696/9 — Tipo: oficial (foro, Kaivax) — Consultada: 2026-11-10 — Fecha de página: 2026-11-03 — Pre-11-02: no — Evidencia: entrenamiento, respawns, bolsas, raciales, Priest.
- URL: https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696 — Oficial — 2026-11-10 — builds 2026-09-24 → 2026-11-04 — mixto — XP de mazmorra, Skinning, AH, camping, Legacy.
- URL: https://news.blizzard.com/en-us/article/24315281 — Oficial (hotfixes) — 2026-11-10 — 2026-11-05/06/09 — no — XP de mazmorra +50 %, Tanning Rack, Priest.
- URL: https://worldofwarcraft.blizzard.com/en-gb/news/24303313 — Oficial (Deep Dive) — 2026-11-10 — 2026-09-13 — sí — Camping, Legacy, rulesets, montura.
- URL: https://news.blizzard.com/en-us/article/24302093/ — Oficial (anuncio) — 2026-11-10 — 2026-09 — sí — fechas, ediciones, montura de tienda.
- URL: https://kami-labs.fr/en/wow-forever/patch-notes-2-novembre-notes-de-lancement/ — Prensa — 2026-11-10 — 2026-11-03 — no — resumen y datamining.
- URL: https://www.warcrafttavern.com/forever/news/wow-forever-pre-launch-class-changes-bug-fixes/ — Prensa — 2026-11-10 — 2026-11-04 — no.
- URL: https://www.gamerfuzion.com/world-of-warcraft-forever-launch-patch-notes-class-damage-buffs-mob-health-training-costs/ — Prensa — 2026-11-10 — ~2026-11-03 — no.
- URL: https://www.warcrafttavern.com/forever/guides/experience/ — Guía — 2026-11-10 — sin fecha — desconocido.
- URL: https://www.warcrafttavern.com/forever/news/camping-profession-buffs-in-world-of-warcraft-forever — Prensa — 2026-11-10 — 2026-09-13 — sí.
- URL: https://www.warcrafttavern.com/forever/news/legacy-tree-rewards-in-world-of-warcraft-forever — Prensa — 2026-11-10 — 2026-09-13 — sí.
- URL: https://www.gamerfuzion.com/world-of-warcraft-forever-rule-sets-separate-layering-realmless-world-refresh/ — Prensa de segunda mano — 2026-11-10 — ~2026-11-01 — sí.
- URL: https://www.gfinityesports.com/article/world-of-warcraft-forever-skinning-guide-leveling-1300-trainers — Guía — 2026-11-10 — 2026-11-02 — mismo día.

- [Data from ForeverDB.net](https://foreverdb.net) — ForeverDB (fan, datos de cliente build 1.60.1.70938) — Consultadas: 2026-11-13 — Pre-11-02: no. URLs: https://foreverdb.net/veterans, https://foreverdb.net/datamine, https://foreverdb.net/datamine/world, https://foreverdb.net/datamine/removed, https://foreverdb.net/changelog, https://foreverdb.net/class/Rogue/changes, https://foreverdb.net/stats, https://foreverdb.net/mounts, https://foreverdb.net/reputation, https://foreverdb.net/legacy, https://foreverdb.net/guide/getting-started, https://foreverdb.net/guide/making-money, https://foreverdb.net/guide/pvp-guide, https://foreverdb.net/faq, https://foreverdb.net/llms-full.txt.

## Estado de verificación
- Estado: confirmed_forever (cada cambio lleva su propio estado)
- Confianza: medium (alta para lo que viene del foro/hotfixes; baja para lo que solo aparece en guías)
- Última verificación: 2026-11-10
- Build/versión: Forever 1.60.1 (lanzamiento) + hotfixes hasta el 2026-11-09

## Preguntas pendientes
- ¿Qué incluyen los cambios de clase del 2026-11-10 (si existen)? Revisar la página oficial de hotfixes.
- Coste de entrenamiento por nivel de Priest y coste de las habilidades raciales de Undead Priest (la excepción mencionada).
- Cifras exactas de respawn y fecha en que se normalizarán.
- Rangos y costes reales de Legacy (Well Rested, Bountiful Harvest, Bartering) en vivo.
- ¿Skinning tiene objeto de camp? ¿Cuándo se aprende la Incense Candle de Herbalism y qué materiales pide?
- Ganancia real de rested XP en la hoguera (sin cifras oficiales).
- ¿Existe Known Issues oficial?
- El ~223 de cambios es una cifra de KL; no se contó en el original.
