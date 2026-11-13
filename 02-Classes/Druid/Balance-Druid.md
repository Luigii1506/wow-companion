---
type: spec
tags: [forever, druid, balance, endgame]
level_min: 60
level_max: 60
faction: both
status: confirmed_forever
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://www.method.gg/wow-forever/class-guides/balance-druid
  - https://www.method.gg/wow-forever/class-guides/balance-druid/talents
  - https://www.method.gg/wow-forever/class-guides/balance-druid/rotation-and-playstyle
  - https://www.method.gg/wow-forever/class-guides/balance-druid/bis-gear-and-stats
  - https://www.method.gg/wow-forever/class-guides/balance-druid/enchants-and-consumables
  - https://www.method.gg/wow-forever/class-guides/balance-druid/races-professions-and-other
  - https://www.method.gg/wow-forever/class-guides/balance-druid/interface-addons-and-macros
  - https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json
  - https://foreverdb.net/class/Druid/talents
related: ["[[Druid]]", "[[Druid-Leveling]]", "[[Feral-DPS-Druid]]", "[[Feral-Tank-Druid]]", "[[Restoration-Druid]]"]
---

# Balance Druid

> [!success] Confirmado en Forever
> Guía de endgame de Method (Shantie, 2026-11-04, parche 1.60.1). Build decodificada del widget. La página de equipo no publica BiS. Una sola fuente: confianza media.

## Resumen
- Rotación sencilla: **Moonfire e Insect Swarm activos, Wrath para cargar Eclipse y Starfire con Eclipse**. Eclipse: cada Wrath acelera los 2 siguientes Starfire 0,5 s (hasta 4 cargas, ForeverDB). `confirmed_forever`
- Una build **Core 38/0/13**, con poca flexibilidad.
- Stats (aproximados, simular): **Spell Piercing > Hit (17 %) > Spell Damage > Haste > Crit > Arcane > Nature > Intellect > MP5 > Spirit**.
- Razas: Skyborne algo por delante (2 % haste), Night Elf cerca, Tauren la más débil en PvE; diferencias diminutas.
- Muy poca dependencia del maná; sin interrupción y con poco control.

## Talentos

Decodificada del widget de Method (datos 1.60.1-2nov; nombres de ForeverDB). Estado `confirmed_forever`.

| Árbol | Talento | Rangos | Nota |
|---|---|---|---|
| Balance | Improved Wrath | 5/5 | |
| Balance | Genesis | 2/5 | +periódico; se deja en 2 para coger los talentos de maná |
| Balance | Moonglow | 3/3 | Maná |
| Balance | Improved Moonfire | 2/2 | |
| Balance | Nature's Majesty | 2/2 | +4 % crit |
| Balance | Nature's Reach | 2/2 | |
| Balance | Nature's Splendor | 1/1 | Alarga Moonfire e Insect Swarm |
| Balance | Insect Swarm | 1/1 | |
| Balance | Vengeance | 5/5 | |
| Balance | Improved Starfire | 5/5 | |
| Balance | Nature's Grace | 1/1 | |
| Balance | Eclipse | 3/3 | |
| Balance | Moonfury | 5/5 | +10 % daño Arcane y Nature |
| Balance | Moonkin Form | 1/1 | |
| Restoration | Nature's Focus | 5/5 | Alternativa: Heart of the Wild (~0,5 % de daño) si no hay retroceso |
| Restoration | Naturalist | 5/5 | +10 % a todo el daño |
| Restoration | Reflection | 3/3 | Maná; si sobra maná, Genesis 5/5 en su lugar |

Orden del widget: Imp. Wrath 10–14 → Moonglow 15–17 → Imp. Moonfire 18–19 → Nature's Majesty 20–21 → Nature's Reach 22–23 → Nature's Splendor 24 → Vengeance 25–29 → Insect Swarm 30 → Imp. Starfire 31–35 → Eclipse 36 → Nature's Grace 37 → Eclipse 38–39 → Moonfury 40–44 → Moonkin Form 45 → Nature's Focus 46–50 → Naturalist 51–55 → Genesis 56–57 → Reflection 58–60.

- Overgrowth: mover 2 puntos de Genesis si el combate lo pide.
- Legacy (árbol Resourcefulness): Gourmand, The Quick and the Dead, Reagent Economy (Rebirth sin semilla), Reinforce.

## Rotación

| Objetivos | Prioridad (Method) | Estado |
|---|---|---|
| Pre-pull | Read Leyline 5 s antes (Skyborne Alliance) y 2 Wrath 3 s antes | confirmed_forever |
| 1 | Elune's Light (Night Elf) → Moonfire si falta → Insect Swarm si falta → Starfire con Eclipse → Wrath | confirmed_forever |
| 2–3 | DoTs en todos → Starfire con Eclipse al prioritario → Wrath al prioritario | confirmed_forever |
| 4–5 | DoTs en todos → Hurricane | confirmed_forever |
| 6+ | Hurricane | confirmed_forever |

- Variante con maná positivo: Starfire solo con Omen of Clarity, ~10 % menos daño.
- Para moverte: Cat Form + Dash.

## Stats y equipo
- Spell Piercing > Hit (hasta **17 %**) > Spell Damage > Haste > Crit > Arcane Damage > Nature Damage > Intellect > MP5 > Spirit. Aún no se ha visto haste ni MP5 en el equipo, y Spell Pierce es incierto.
- Crit y hit vienen en pasos de 0,1 % en el equipo: compara 0,1 % de crit o hit con 1 punto de Spell Damage o Intellect.
- BiS: **desconocido**. La página no tiene secciones de equipo.

## Encantamientos y consumibles

| Slot | Encantamiento (Method) | Alternativa |
|---|---|---|
| Arma 2M | Spellblasting | Mighty Spell Power |
| Arma 1M | Spell Power | — |
| Cabeza | Arcanum of Focus | — |
| Collar | Spell Power | — |
| Capa | Subtlety | Greater Resistance |
| Pecho | Mystic Rugged Armor Kit | Greater Stats |
| Muñecas | Greater Spellpower | — |
| Guantes | Arcane Power | — |
| Piernas | Arcanum of Focus | Mystic Rugged Armor Kit |
| Pies | Speed | Mystic Rugged Armor Kit |

- Flask of Supreme Power. Elixires: Owl, Greater Mageblood, Greater Arcane, Nature Power, Sages o Whale (+ defensivos Greater Fortitude, Major Troll's Blood, Greater Defense).
- Pociones: Major Spellblasting, Elemental Purging, Major Mana, Dragonfire (AoE en melee), Caustic Smog (AoE a distancia), Venomous Blood (nicho); protecciones, Free Action, Living Action, Limited Invulnerability.
- Baked Salmon, Brilliant Wizard Oil, Dark o Demonic Rune, Saf-T Clever Dynamite, Goblin Sapper Charge (Engineering, en melee).
- Efectos de los consumibles nuevos: **desconocidos**.

## Razas y profesiones
- **Skyborne** (más daño: 2 % haste, +5 % contra elementales; Alliance con Read Leyline, Horde con Skysight) > **Night Elf** (Elune's Light, Quickness, Shadowmeld; mejor utilidad) > **Tauren** (sin raciales de daño).
- Profesiones: solo Engineering da algo de daño (Goblin Sapper Charge) y utilidad (Ultralight Goblin Glider). Leatherworking sin BoP potentes conocidos.

## Interfaz, addons y macros
- Duración de DoTs en placas (o Cooldown Manager). Boss mod (DBM o BigWigs; sin probar).
- Macros: `/cast [nochanneling:Hurricane] Hurricane`; Moonfire/Insect Swarm por `[@mouseover,exists]`.

## En grupo con un Rogue
- Moonkin Aura da crit al grupo, pero según Method no se acumula con Leader of the Pack (ver [[Feral-DPS-Druid]]). Balance aporta Rebirth, Innervate y curas de reserva. *Composición inferida.*

## Qué dicen las guías
- [[src-method-class-guides-balance-druid]], [[src-method-class-guides-balance-druid-talents]], [[src-method-class-guides-balance-druid-rotation-and-playstyle]], [[src-method-class-guides-balance-druid-bis-gear-and-stats]], [[src-method-class-guides-balance-druid-enchants-and-consumables]], [[src-method-class-guides-balance-druid-races-professions-and-other]], [[src-method-class-guides-balance-druid-interface-addons-and-macros]].
- La guía Balance confirma que hay **Skyborne Druid en ambas facciones** (Read Leyline en Alliance, Skysight en Horde), lo que responde a una pregunta abierta de [[Druid]].
- Profesiones: la guía de leveling ([[Druid]]) propone LW+Skinning, Mining+Engineering o Herbalism+Alchemy; la de Balance endgame solo valora Engineering.

## Fuentes

| URL | Tipo | Fecha página | Consultada | ¿Pre-parche? |
|---|---|---|---|---|
| https://www.method.gg/wow-forever/class-guides/balance-druid (+ 6 subpáginas) | Guía Method | 2026-11-04 | 2026-11-13 | No |
| https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json | Datos de la calculadora (Method) | 1.60.1 (02-11) | 2026-11-13 | No |
| https://foreverdb.net/class/Druid/talents | Datos de cliente | sin fecha | 2026-11-13 | No |

[Data from ForeverDB.net](https://foreverdb.net)

## Preguntas pendientes
- ¿Hay haste o MP5 en el equipo de Forever? La guía aún no lo ha visto.
- Pre-raid BiS de Balance: no publicado.
