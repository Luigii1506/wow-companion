---
type: playbook
tags: [forever, playbook, mage, troll, frost, leveling]
level_min: 20
level_max: 30
faction: horde
status: confirmed_forever
confidence: medium
last_verified: 2026-11-15
game_version: "Forever 1.60.1"
sources:
  - https://foreverdb.net/guide/leveling-mage
  - https://foreverdb.net/class/Mage
  - https://foreverdb.net/class/Mage/talents
  - https://foreverdb.net/class/Mage/builds
  - https://foreverdb.net/class/Mage/changes
  - https://foreverdb.net/class/Mage/pve
  - https://foreverdb.net/quests/mage
  - https://www.method.gg/wow-forever/wow-forever-mage-leveling-guide-and-talents
  - "Azeroth DB (MCP wowdb): costes de maná y CD de hechizos de Mage (cliente Forever)"
  - "Addon ForeverDB, datos 2026-11-13.ea2bb422 (build 1.60.1.70938): misiones, recompensas, entrenadores, recetas"
related: ["[[Playbook-Mage-1-20]]", "[[Mage-Leveling]]", "[[Frost-Mage]]", "[[Mage-Quest-Rewards-1-30]]", "[[Leveling-Route-Orc]]", "[[Dungeons-1-30]]", "[[Quests-Stonetalon-Mountains]]", "[[Quests-Hillsbrad-Foothills]]", "[[Quests-Silverpine-Forest]]"]
---

# Playbook: Troll Mage Frost 20–30 (y esbozo 30–60)

> [!abstract] Para quién
> Troll Mage Frost (Horde). Sin export: basado en guías y datos (ForeverDB web y addon, Method, cliente vía Azeroth DB) a 2026-11-15, no en el estado real del personaje. La guía de ForeverDB cubre hasta 30 (tope de la beta); lo de 30–60 es un esbozo.

> [!success] Confirmado en Forever
> Hechizos, costes y talentos: cliente (build 1.60.1.70938). Misiones: vistas por jugadores en Forever salvo las marcadas. Builds de 40–60: ForeverDB avisa de que esos niveles **nunca se jugaron en la beta**.

## Resumen
- **20 es el gran nivel**: Blink, Blizzard, Evocation, Mana Shield, Frostbolt R4, Polymorph R2, Teleport: Orgrimmar y Undercity. Con 11 puntos tienes **Ice Lance**. `confirmed_forever`
- **Rotación**: Frostbolt → Frost Nova al llegar → 2–3 Ice Lance (CD 8 s) → salir. Cone of Cold (26) cuando Frost Nova está en CD. Blizzard solo en grupos (320 de maná en R1, 520 en R2). `confirmed_forever`
- **Talentos 21–30 (ForeverDB)**: Frost Channeling 3 → Improved Blizzard 1 → Ice Block (25) → Shatter 3 → Arctic Reach 1 → **Fingers of Frost** (30). Method: Ice Shards, Ice Block a 25, Shatter, Fingers of Frost. `confirmed_forever` (talentos) / orden inferido
- **Premios clave**: High Robe of the Adjudicator (SP +8, *Assault on Fenris Isle*, 24), **Warsong Sash** (azul, SP +11, 27), Jutebraid Gloves (SP +6, Int +5, 29), Witch's Finger (azul, Int +8, BFD, 30), wands Sizzle Stick → Branding Rod / Charred Wand. Ver [[Mage-Quest-Rewards-1-30]].
- **Ruta**: terminar Barrens y WC → Stonetalon y Ashenvale (BFD) → Silverpine (SFK) y Hillsbrad → Thousand Needles; cadena de clase a 26 en Orgrimmar y Crossroads. `probable_classic` (orden de zonas)

## Hechizos 20–30 y coste
| Nivel | Entrenar | Maná / CD (cliente) | Estado |
|---|---|---|---|
| 20 | Blink; Blizzard R1; Evocation; Mana Shield R1; Frostbolt R4; Polymorph R2 (oveja hasta 30 s); Fire Ward R1; Frost Armor R3; Conjure Water R3; **Teleport: Orgrimmar** y **Teleport: Undercity** | Blink CD 15 s (coste en % de maná base); Blizzard 320; Evocation CD 8 min; Mana Shield 40 (2 de maná por punto absorbido); Frostbolt R4 65 / 2,6 s | confirmed_forever |
| 22 | Scorch R1, Frost Ward R1, Fire Blast R3, Arcane Explosion R2, Conjure Food R3 (Conjured Rye, 552 de vida) | — | confirmed_forever |
| 24 | **Counterspell** (silencia la escuela 10 s), Fireball R5, Arcane Missiles R3 (5 s), Flamestrike R2, Dampen Magic R2 | Counterspell 100, CD 30 s | confirmed_forever |
| 25 | **Ice Block** (talento) | 15 de maná, CD 5 min, 10 s inmune sin poder actuar | confirmed_forever |
| 26 | **Cone of Cold R1** (instantáneo, ralentiza 40 % **6 s**, 8 s en Classic), Frost Nova R2, **Frostbolt R5** | Cone of Cold 210, CD 10 s; Frost Nova R2 85; Frostbolt R5 100 / 3 s | confirmed_forever |
| 28 | Blizzard R2, **Ice Lance R2** (33–39, 55 de maná), **Conjure Mana Agate** (375–425 de maná instantáneo), Mana Shield R2, Scorch R2, Arcane Intellect R3 | Blizzard R2 520 | confirmed_forever |
| 30 | **Ice Armor** (sustituye a Frost Armor: +290 armadura, +6 resistencia Frost), Conjure Water R4 (Spring Water ~1295 de maná), Fireball R6, Fire Blast R4, Arcane Explosion R3, Fire Ward R2, Amplify Magic R2, **Teleport: Thunder Bluff** | — | confirmed_forever |

Ice Lance R1 (20): 26–30 de daño, 45 de maná, instantáneo, +300 % contra congelados, **CD 8 s** (lo añadió la build del 31-10). Precio de entrenador: desconocido.

## Talentos 21–30
Con Ice Lance a 20 llevas 11 puntos. La fila 4 pide 15 puntos (nivel 24 como pronto); la fila 5, 20 (nivel 29).

| Nivel | ForeverDB "Frost leveling with Shatter" (orden inferido) | Method (prioridad de la guía) |
|---|---|---|
| 21–23 | **Frost Channeling 3/3** (−15 % maná y −30 % amenaza Frost) | Ice Lance (21), Ice Shards (22–24) |
| 24 | Improved Blizzard 1/3 (Blizzard pasa a ser Chill: activa Frostbite y Fingers of Frost) | Ice Shards |
| 25 | **Ice Block** | **Ice Block** |
| 26–28 | **Shatter 3/3** (+50 % crit contra congelados) | Shatter |
| 29 | Arctic Reach 1/2 (+10 % alcance de Frostbolt/Ice Lance/Blizzard y radio de Frost Nova/CoC) | Fingers of Frost (la guía no cuadra aquí: hacen falta 20 puntos) |
| 30 | **Fingers of Frost 1/2** (15 % de los Chill: el siguiente hechizo trata al objetivo como congelado) | Improved Cone of Cold… |

- Build final de ForeverDB a 30: Improved Frostbolt 5, Improved Frost Nova 2, Frostbite 3, Ice Lance 1, Frost Channeling 3, Improved Blizzard 1, Shatter 3, Ice Block 1, Arctic Reach 1, Fingers of Frost 1 (21 puntos). `confirmed_forever`
- Method (10–25): Improved Frostbolt → Precision → Frostbite → Ice Lance → Ice Shards (3) → Ice Block; (26–42): Shatter → Fingers of Frost → Improved Cone of Cold → Winter's Chill → Cold Snap → Ice Barrier. Su orden a 29 no es posible con las reglas de filas del cliente (inferido).
- **Diferencia práctica**: ForeverDB gasta en ahorro de maná y Frost Nova; Method en hit (Precision) y daño crítico (Ice Shards). Para solo, ForeverDB; para mazmorras con jefes por encima de tu nivel, el propio ForeverDB usa Precision en su build de dungeon. *Inferido*.

## Rotación 20–30
| Situación | Qué pulsar | Estado |
|---|---|---|
| Un mob | Frostbolt desde 30 yd → Frostbolt → **Frost Nova** al llegar → **Ice Lance** ×2–3 → salir → Frostbolt. Con Shatter (26–28) el Ice Lance sobre congelado casi siempre critea | confirmed_forever |
| Proc de Fingers of Frost (30) | Ice Lance aunque no haya congelación | confirmed_forever |
| Frost Nova en CD | Cone of Cold (26) y retroceder; Blink si te alcanza; Fire Blast o wand para rematar | confirmed_forever |
| Varios mobs | Polymorph al que sobra; si llegan todos, Frost Nova → salir → Blizzard o Ice Lance a los congelados | confirmed_forever |
| Pull perdido | Ice Block (25), y Frost Nova al salir; Mana Shield si te queda maná | confirmed_forever |
| Pelea larga | Mana Agate (28) a mitad; Evocation solo en emergencias (CD 8 min) | confirmed_forever |

- En grupo: deja que el tanque pegue primero (sin reducción de amenaza hasta Frost Channeling), Counterspell a curas y hechizos grandes de casters, Frost Nova al mob que vaya al sanador. Ver [[src-foreverdb-class-mage-pve]].
- Berserking al empezar pulls grandes o jefes.

## Ruta 20–30
| Nivel | Dónde | Qué hacer | Premio clave para un caster | Estado |
|---|---|---|---|---|
| 20–22 | The Barrens | *Chol'aruk the Ravener* (21, nueva, Gur'ak en Crossroads: 4.100 XP, 50s), *Egg Hunt* (22), *Weapons of Choice* (24) | Quilboar Toothpick (daga Int +2 Spi +2); Harlequin Robes (Int +2 Spi +6); Everglow Lantern (mano izq., Spi +3) | confirmed_forever |
| 20–24 | **Wailing Caverns** | *Deviate Eradication*, *Leaders of the Fang* (Nara Wildmane, Thunder Bluff) | **Sizzle Stick** (wand SP +2); **Crescent Staff** (azul, Int/Agi/Sta +7, 20.3 dps) | confirmed_forever |
| 20–22 | Stonetalon (Sun Rock Retreat) | *Earthen Arise* (20), *Arachnophobia* (21, cartel de Besseleth) | Owlbeard Bracers (Int +2, Sta +1, SP +1); **Clear Crystal Rod** (bastón Int +5, Sta +4) | confirmed_forever |
| 21–25 | Silverpine (zepelín a Undercity) y **Shadowfang Keep** | *Beren's Peril* (21), **Assault on Fenris Isle** (24), *Deathstalkers in Shadowfang* (25, SFK), *The Book of Ur* (26, SFK) | Wand of Decay (Int +2); **High Robe of the Adjudicator** (Int +2, **SP +8**); Ghostly Mantle (Spi +6, healing/SpellDmg); Tattered Mittens | confirmed_forever |
| 23–27 | Ashenvale (Splintertree, Zoram'gar) y **Blackfathom Deeps** | *Torek's Assault* (24), **Warsong Supplies** (27), *Je'neu of the Earthen Ring* (27), *Allegiance to the Old Gods* (26, BFD), *Blackfathom Villainy* (27, BFD), *Baron Aquanis* (30, BFD) | Polished Walking Staff (Int +7, Sta +3); **Warsong Sash** (azul, **SP +11**, Sta +4); Soft Willow Cape (Int +5); Chestnut Mantle (SP +5); **Gravestone Scepter** (wand azul); **Witch's Finger** (mano izq. azul, Int +8, Sta +4) | confirmed_forever |
| 24–28 | Hillsbrad (Tarren Mill) | *Elixir of Pain* (24), *Souvenirs of Death* (25), *Dangerous!* (28), *Humbert's Sword* (30) | Firewalker Boots (SP +2, Spi +5); Skull Ring (Sta/Int +3); **Charred Wand** (Int +2, SP +2, 22.2 dps); Ethereal Mantle (Int/Spi +5) | confirmed_forever |
| 25–29 | Barrens sur y Stonetalon (segunda visita) | *In Nightmares* (25), *New Life* (25), *Bloodfury Bloodline* (26), *Revenge of Gann* (26), *Isha Awak* (27), *Horde Presence* (29), *The Den* (29) | Talbar Mantle (Int +4, mp5 +1); Harpy Bangles (Int +4); Totemic Clan Ring (Int/Spi +3); **Branding Rod** (wand SP +2, Int +2, 21.6 dps); **Jutebraid Gloves** (SP +6, Int +5); Sacred Band (SP +2, Spi +4) | confirmed_forever |
| 26 | Orgrimmar → Crossroads | Cadena de clase: Anastasia Hartwell (Undercity) → *Speak with Deino* (Orgrimmar 38.4, 86.1) → *Waters of Xavian* → *Laughing Sisters* (12 Laughing Sister's Hairs) → *Nether-lace Garment* (Kil'hala, Crossroads 52.2, 31.7) | Nether-lace Robe (Int/Sta/Spi +6) o **Nether-lace Tunic** (Sta +6, Int +9) | probable_classic (nadie la ha registrado aún; XP del addon) |
| 28–30 | Thousand Needles (Freewind Post) | *Arikara* (28), *Grimtotem Spying* (28), *Protect Kanati Greycloud* (28), *Free at Last* (29) | Stingshot Wand (Sta/Int +2); Desert Shoulders (Int/Spi +5); Lightheel Boots (Int/Spi +4); Windsong Drape (Spi +4, SP +5) | confirmed_forever |
| 24–30 | Mazmorras opcionales | [[Razorfen-Kraul]] (24+), [[Excavation-Site-Wetlands]] (26), [[City-of-Dalaran]] (28), [[Scarlet-Monastery-Graveyard]] (30) | Botín de caster de Classic: Death Speaker Mantle (RFK), Gaze Dreamer Pants (BFD), Belt of Arugal y Mindthrust Bracers (SFK) | probable_classic (drops) |

Zonas: [[Quests-The-Barrens]], [[Quests-Stonetalon-Mountains]], [[Quests-Silverpine-Forest]], [[Quests-Hillsbrad-Foothills]]. Mazmorras: [[Wailing-Caverns]], [[Shadowfang-Keep]], [[Blackfathom-Deeps]], [[Dungeons-1-30]]. Desde el 1-10 las misiones de mazmorra dan un 50 % menos de XP extra; las muertes dentro dan más XP desde el 8-10 y el hotfix del 9-11 ([[Dungeon-XP]]).

## Teleports y portales
| Nivel | Qué | Estado |
|---|---|---|
| 20 | Teleport: Orgrimmar, Teleport: Undercity | confirmed_forever |
| 30 | Teleport: Thunder Bluff | confirmed_forever |
| 40 | Portal: Orgrimmar, Portal: Undercity | confirmed_forever |
| 50 | Portal: Thunder Bluff; **Teleport: Dalaran** (nuevo en Forever) | confirmed_forever |

Quién los enseña: en Classic el Portal Trainer (Thuul, Orgrimmar 38.7, 85.6); ForeverDB solo dice "trainer". Reagente (Rune of Teleportation en Classic): desconocido en Forever. `probable_classic`

Uso práctico (inferido): Teleport: Undercity a 20 acorta las idas a Silverpine/SFK y Hillsbrad; Teleport: Orgrimmar sustituye a la piedra de hogar, que puedes dejar en la posada de la zona donde estés.

## Profesiones 20–30
- **Expert** (150–225) a nivel 20: Magar (Expert Tailor, Orgrimmar 63.4, 50.0); Godan (Expert Enchanter según el addon, Orgrimmar 53.7, 38.3). `confirmed_forever` (NPCs)
- Tailoring Silky (patrones de Jim'bek, Crossroads 49.6, 29.5): **Silky Gown** (skill 110, req 22: Int +7, Sta +6, Spi +4, Frost +13*), **Silky Leggings** (125, req 25), **Filigreed Silky Circlet** (125, req 25, patrón de Aku'mai en BFD). `confirmed_forever`
- ForeverDB cita Spidersilk Boots (req 20: SP +7, Int +4, Sta +4) en todas las listas de Mage a 20 y Frothing Slippers, Azure Silk Gloves y Azure Silk Cloak a 30.
- Enchanting a skill 140: **Glimmering Staff** (Int +11, Sta +11, 24.5 dps) y **Orb of Mystic Insight** (mano izq., Int +6, SP +7), ambas nuevas en Forever (receta por objeto). `confirmed_forever` (recetas)

\* Frost = daño de Frost (stat87; confirmado con datos del cliente en azeroth.wiki el 2026-11-17).

## Esbozo 30–60
| Tramo | Talentos (ForeverDB) | Hechizos | Zonas y misiones de clase | Estado |
|---|---|---|---|---|
| 30–40 | 40: + Ice Shards 5, Improved Cone of Cold 2, Cold Snap, Fingers of Frost 2/2, **Ice Barrier** (+15 % daño Frost 1 min) | Mage Armor 34 (50 % de regeneración lanzando), Ice Lance R3 34, Conjure Mana Jade 38, **Frostfire Bolt 40**, portales 40 | Thousand Needles, Stranglethorn, Desolace, Arathi; Magus Tirth (30, Shimmering Flats); Tabetha (38–40, Dustwallow; *Mage's Wand*). Montura y Dual Spec a 40 ([[Mount-and-Costs]]) | confirmed_forever (hechizos); probable_classic (misiones) |
| 40–50 | 50: + Precision 3, Permafrost 3, Improved Blizzard 3, Arctic Reach 2, Improved Cone of Cold 3, Frost Warding 2 | Conjure Mana Citrine 48, Teleport: Dalaran 50 | Riverglades, Tanaris, Feralas, Hinterlands | confirmed_forever (cliente); teoría (ForeverDB no lo probó) |
| 50–60 | 60: 48 puntos en Frost (Winter's Chill 5) + Incineration 3 | Arcane Brilliance 56, Conjure Mana Ruby 58, Felfire y Polymorph: Cow 60 | Un'Goro, Felwood, Azshara (Archmage Xylem 52–60), Plaguelands | igual |

- **Method es distinto en 43–60**: 18 puntos en Arcane (Improved Channeling, Arcane Concentration, Missile Barrage, Arcane Subtlety, Arcane Blast a 57, Arcane Meditation). ForeverDB se queda en Frost puro. Ver [[Mage-Leveling]].
- Ruta de zonas compartida con Orc: [[Leveling-Route-Orc]].

## Pendiente de verificar en el juego
- Si el slow de Frostbolt cuenta como Chill (Frostbite y Fingers of Frost).
- Quién enseña los teleports y si necesitan reagente.
- Que la cadena de clase de 26 exista y dé las mismas recompensas (solo datos de Classic).
- Fire Blast en la rotación a un objetivo: el simulador de ForeverDB hace más daño sin él a 20–39; la guía lo usa.
- Coste de Blink y precio de entrenador por nivel.

## Qué dicen las guías
- ForeverDB: builds a 20/30/40/50/60 en [[src-foreverdb-class-mage-builds]] y rotación en [[src-foreverdb-guide-leveling-mage]]; cambios de hechizos en [[src-foreverdb-class-mage-changes]]; buffs y nerfs en [[src-foreverdb-buffs-and-nerfs-mage]]; misiones de clase en [[src-foreverdb-quests-mage]].
- Method: [[src-method-wow-forever-mage-leveling-guide-and-talents]] (Frost hasta 42 y Arcane después).
- Discrepancia: orden de talentos 21–30 (ForeverDB ahorro de maná y Frost Nova; Method Precision e Ice Shards) y 43–60 (Frost puro frente a 18 en Arcane).

## Fuentes
| URL | Tipo | Fecha página | Consultada | ¿Pre-parche 2026-11-02? |
|---|---|---|---|---|
| https://foreverdb.net/guide/leveling-mage | Guía ForeverDB | 2026-11-05 | 2026-11-15 | No |
| https://foreverdb.net/class/Mage/builds, /talents, /changes, /pve | Datos de cliente ForeverDB | 2026-11-13 | 2026-11-15 | No |
| https://foreverdb.net/quests/mage | Misiones ForeverDB | 2026-11-13 | 2026-11-15 | No |
| https://www.method.gg/wow-forever/wow-forever-mage-leveling-guide-and-talents | Guía Method | 2026-11-10 | 2026-11-13 | No |
| Azeroth DB (azeroth.wiki, MCP) | Datos de cliente: maná, CD | — | 2026-11-15 | No |
| Addon ForeverDB (datos 2026-11-13) | Misiones, recompensas, NPCs, recetas | 2026-11-13 | 2026-11-15 | No |

[Data from ForeverDB.net](https://foreverdb.net)

## Preguntas pendientes
- Botín de caster de las mazmorras 20–30 medido en Forever (hoy solo hay datos de Classic para las piezas de tela).
- Facción del vendedor Illiyana Moonblaze (Ashenvale), que vende Lorekeeper's Ring y Dryad's Wrist Bindings según el addon.
