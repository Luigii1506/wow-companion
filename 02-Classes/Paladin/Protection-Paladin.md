---
type: spec
tags: [forever, paladin, protection, tank, endgame]
level_min: 10
level_max: 60
faction: both
status: confirmed_forever
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://www.method.gg/wow-forever/class-guides/protection-paladin
  - https://www.method.gg/wow-forever/class-guides/protection-paladin/talents
  - https://www.method.gg/wow-forever/class-guides/protection-paladin/rotation-and-playstyle
  - https://www.method.gg/wow-forever/class-guides/protection-paladin/bis-gear-and-stats
  - https://www.method.gg/wow-forever/class-guides/protection-paladin/enchants-and-consumables
  - https://www.method.gg/wow-forever/class-guides/protection-paladin/races-professions-and-other
  - https://www.method.gg/wow-forever/class-guides/protection-paladin/interface-addons-and-macros
  - https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json
  - https://foreverdb.net/class/Paladin/talents
related: ["[[Paladin]]", "[[Paladin-Leveling]]", "[[Holy-Paladin]]", "[[Retribution-Paladin]]", "[[Hit-Chance]]"]
---

# Protection Paladin

> [!success] Confirmado en Forever
> Guía de endgame de Method (Jurdi, 2026-11-09, parche 1.60.1). Cuatro builds decodificadas. Pre-raid BiS publicado como WIP, con objetos de Classic sin confirmar. Un valor de talento discrepa con el cliente (ver Talentos).

## Resumen
- Tanque de **daño pasivo y reactivo**: sellos, Retribution Aura, Reckoning, Holy Shield. Mezcla de Vanilla y TBC. `confirmed_forever`
- Novedades: **Seal of Fury** (su Judgement es el taunt), Holy Strike, sellos no consumidos al juzgar, Consecration completa solo en 4 objetivos, capstone **Shieldsworn**.
- Build estándar **0/35/16** (Sacred Arbiter); variantes Improved Seals y **Shock Prot 22/21/8**.
- Stats: **Defense 440 > Stamina > Hit 8 % > Expertise > Spell Power > Block chance > Crit > Block value**.
- Trucos únicos: reck bomb, bubble taunt con Swift Judgement, Divine Shield para limpiar debuffs.

## Talentos

### Build "Standard Prot: Sacred Arbiter" (Method) — 0/35/16
| Nivel | Talento | Árbol |
|---|---|---|
| 10–14 | Redoubt 5/5 | Prot |
| 15–16 | Sacred Duty 2/2 | Prot |
| 17–19 | Precision 3/3 | Prot |
| 20 | Templar's Bulwark | Prot |
| 21–22, 60 | Toughness 3/5 | Prot |
| 23–24 | Shield Specialization 2/2 | Prot |
| 25–29 | Anticipation 5/5 | Prot |
| 30–32 | Improved Righteous Fury 3/3 | Prot |
| 33 | Swift Judgement | Prot |
| 34 | Holy Shield | Prot |
| 35–39 | Reckoning 5/5 | Prot |
| 40–42 | Iron Creed 3/3 | Prot |
| 43 | Shieldsworn | Prot |
| 44–48 | Deflection 5/5 | Ret |
| 49–51 | Sanctified Judgement 3/3 | Ret |
| 52–54 | Conviction 3/3 | Ret |
| 55–56 | Improved Judgement 2/2 | Ret |
| 57–58 | Pursuit of Justice 2/2 | Ret |
| 59 | Sacred Arbiter | Ret |

### Variantes (Method)
| Build | Reparto | Diferencias | Estado |
|---|---|---|---|
| Improved Seals | 10/31/10 | Shieldsworn al 40 con Anticipation 2/5 y Toughness 2/5; luego Divine Strength 5, Improved Seals 5, Deflection 5, Sanct. Judgement 3, Imp. Judgement 2. Por si Sacred Arbiter no escala con daño Sagrado | confirmed_forever |
| Improved Seals + Pursuit of Justice | 8/31/12 | Igual, con Improved Seals 3/5 y Pursuit of Justice 2/2 | confirmed_forever |
| Shock Prot | 22/21/8 | Holy hasta Holy Shock (30) + Consecrated Ground 2, Benediction 5, Sanct. Judgement 3; Prot hasta Holy Shield (60). Más AoE, menos mitigación y maná | confirmed_forever |

- Sin Warrior para Demoralizing Shout: pasar 3 puntos de Conviction a Vindication.
- Innegociables: Precision, Swift Judgement, Improved Righteous Fury. Anticipation 5/5 para el tope de 440 de Defense (revisable con mejor equipo).
- Al principio, mejor talentos de maná y Pursuit of Justice en Ret.

### Talentos clave (texto del cliente, ForeverDB)
| Talento | Efecto | Estado |
|---|---|---|
| Improved Righteous Fury | Con Righteous Fury: −9 % de daño recibido (3/3). **Method dice 6 %** | conflicting |
| Redoubt | Golpes recibidos: 10 % de +30 % bloqueo (10 s o 5 bloqueos) | confirmed_forever |
| Reckoning | 40 % tras bloquear (100 % tras recibir crítico) de ataque extra; guarda hasta 4 | confirmed_forever |
| Holy Shield | +30 % bloqueo 10 s, 75 de daño Sagrado por bloqueo, 4 cargas | confirmed_forever |
| Templar's Bulwark (nuevo) | Escudo de absorción del 100 % de tu vida 8 s; aplica Forbearance | confirmed_forever |
| Swift Judgement (nuevo) | Judgement extra que no comparte CD con Judgement | confirmed_forever |
| Iron Creed (nuevo) | Holy Strike +30 % amenaza; con Righteous Fury, −6 % daño recibido 6 s | confirmed_forever |
| Shieldsworn (nuevo) | Holy Strike −4 s de CD, golpea con el escudo (activa Holy Shield y Shield Spec. sin gastar cargas) y bloquea hechizos 6 s | confirmed_forever |
| Sacred Arbiter (nuevo, Ret) | Holy Strike +20 % de daño y refresca los Judgements | confirmed_forever |

## Rotación
| Situación | Prioridad (Method) | Estado |
|---|---|---|
| Antes del pull | Righteous Fury (>5 min), aura (normalmente Retribution), buffs | confirmed_forever |
| Apertura | Seal of Fury → Holy Shield → (Holy Shock) → Judgement a 10 m → Swift Judgement si no hará falta taunt en 1 min → Holy Strike → Consecration | confirmed_forever |
| Un objetivo | Holy Shield en CD → Seal of Fury activo → (Holy Shock) → Judgement → Holy Strike → Consecration | confirmed_forever |
| Área | Consecration → Holy Shield → Seal of Fury → Judgement si no molesta el taunt → (Holy Shock) → Holy Strike | confirmed_forever |

- Sin ser tanque activo: Seal of Righteousness para no quitarle el boss al otro tanque. Si no hay otro Paladin: Seal of Wisdom y juzgarlo para el maná del grupo.
- Más de 4 objetivos: Judgement y Holy Strike a los que no reciben el daño completo de Consecration.
- **Reck bomb**: guardar 4 cargas de Reckoning con trash; en Forever cada golpe también aplica el sello.
- **Bubble taunt**: Divine Shield + Judgement of Fury (fijación de 3 s) + Swift Judgement para refrescarla; luego cancelar la burbuja.

## Stats y equipo
- **Defense hasta 440 (inmunidad a críticos) > Stamina > Hit 8 % > Expertise > Spell Power > Block chance > Crit > Block value** (provisional).
- Topes según Method: hit cuerpo a cuerpo 8 % y de hechizo 17 % contra jefe; Expertise 6,5 % (sin esquivas) y 14 % (sin paradas); crush cap 102,4 %. Ver [[Hit-Chance]].
- Judgement usa hit cuerpo a cuerpo (el taunt de Judgement of Fury, hit de hechizo); Hammer of Wrath usa hit a distancia. 60 Intellect = 1 % crit de hechizo.

| Slot | Pre-raid BiS (Method, WIP) | Origen |
|---|---|---|
| Cabeza | Stalwart Helm (amenaza) / Enriched Thorium Helm (supervivencia) | Blacksmithing |
| Collar | Horn of Ve'han | desconocido |
| Hombros, muñecas, manos, cintura, pies | Piezas Warder's | Blacksmithing |
| Capa | Cloak of Warding / Arcanoweave Cloak (75 Real) | Tailoring / vendedor |
| Pecho, piernas | Enriched Thorium Breastplate / Leggings | Blacksmithing |
| Anillos | Initiate's Signet of Vigilance (The Watchers, amistoso); Don Julio's Band | reputación |
| Trinkets | Adaptive Combat Assistant o Defender's Grip Stabilizer (125 Real, solo uno); Cleansed Vilebranch Icon | vendedor / desconocido |
| Arma | Sageblade / Flurry Axe / Hand of Edward the Odd | Blacksmithing / BoE |
| Escudo | Antique Bulwark | desconocido |
| Libram | Libram of Law (50 Real) | vendedor |

- Estado: `probable_classic`. Method incluye objetos de Classic **no vistos en Forever** (Hand of Justice, Draconian Deflector, Libram of Fervor). BiS y tier: **desconocido**.

## Encantamientos y consumibles
| Slot | Encantamiento (predicción) | Alternativa |
|---|---|---|
| Cabeza | Arcanum of Rapidity | — |
| Collar | Deflection | Spell Power |
| Capa | Minor Agility | — |
| Pecho / guantes / piernas / botas | Wild Leather Armor Kit (para 440 de Defense) | Greater Stats / Holy Power / Arcanum of Rapidity / Greater Agility o Stamina |
| Muñecas | Superior Deflection | Greater Spellpower o Stamina |
| Arma | Revelation | — |
| Escudo | Lesser Block | — |

- Subiendo: Mystic Armor Kits (armadura + spell power) de Leatherworking.
- Frasco: Supreme Power o Titans si existen; si no, **Flask of Natural Precision** (+5 % Expertise, +60 Stamina).
- Elixires: Ferocity/Grizzly, Greater Arcane, Holy Power, Mongoose, Owl, Sages, Phalanx, Greater Defense, Gift of Arthas, Juju Might, Greater Mageblood. Sin saber si Mongoose y Owl acumulan.
- Brilliant Wizard Oil (acumula con Windfury Totem); Baked Salmon o Savory Turtle Stew + Dragonbreath Chili (el último); Major Spellblasting, Greater Stoneshield, Free Action; Goblin Sapper Charge, Advanced Target Dummy; Dark/Demonic Rune.

## Razas y profesiones
- Alliance: Dwarf (+1 % hit, Stoneform) o Human (Ruthless, Will to Survive). Horde: solo **Undead** (Touch of the Grave salta a menudo).
- Leveling: **Mining + Blacksmithing** (en beta no había mail con spell power del 1 al 30 salvo BoP de Blacksmithing). Endgame: Blacksmithing y quizá Engineering.

## Interfaz, addons y macros
- UI centrada; Cooldown Manager y marcos de grupo cerca del centro. Ellesmere UI (o ElvUI/ShadowedUI), Details + Tiny Threat, Plater; ForeverAuras en desarrollo. Addons sin probar por nosotros.
- Macros: mouseover para BoP, Blessing of Freedom y Cleanse; `/cast Divine Shield` + `/cancelaura Divine Shield`; `/startattack` en Holy Strike (no en Holy Shield); Advanced Target Dummy + BoP sobre el muñeco.

## En grupo con un Rogue
Tanque con buena amenaza en área (Consecration) para que el Rogue haga cleave tranquilo; da Blessing of Might/Kings, Cleanse contra venenos y BoP de emergencia si el Rogue se lleva un golpe. Taunt más débil que el de un Warrior.

## Qué dicen las guías
- [[src-method-class-guides-protection-paladin]], [[src-method-class-guides-protection-paladin-talents]], [[src-method-class-guides-protection-paladin-rotation-and-playstyle]], [[src-method-class-guides-protection-paladin-bis-gear-and-stats]], [[src-method-class-guides-protection-paladin-enchants-and-consumables]], [[src-method-class-guides-protection-paladin-races-professions-and-other]], [[src-method-class-guides-protection-paladin-interface-addons-and-macros]].
- **Discrepancia**: [[src-method-class-guides-protection-paladin-talents]] da un 6 % de reducción para Improved Righteous Fury; el tooltip de ForeverDB (3/3) dice 9 %. Pendiente de registrar en [[Conflicts]].
- Inconsistencia interna: BoP sobre el muñeco dura 8 s según consumibles y 10 s según macros.
- Topes de hit coherentes con [[src-method-how-does-hit-chance-work-in-wow-forever]].

## Fuentes
| URL | Tipo | Fecha de la página | Consultada | ¿Anterior al parche del 02-11? |
|---|---|---|---|---|
| https://www.method.gg/wow-forever/class-guides/protection-paladin (+ 6 subpáginas) | guide | 2026-11-09 | 2026-11-13 | No |
| https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json | datos de la calculadora (Method) | 2026-11-02 | 2026-11-13 | No |
| https://foreverdb.net/class/Paladin/talents | datos de cliente | sin fecha | 2026-11-13 | No |

[Data from ForeverDB.net](https://foreverdb.net)

## Preguntas pendientes
- Improved Righteous Fury: ¿6 % o 9 %? Comprobar el tooltip en el juego.
- ¿Escala Sacred Arbiter con daño Sagrado o es un bug?
- ¿Se puede llegar al crush cap (102,4 %)?
