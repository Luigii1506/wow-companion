---
type: spec
tags: [forever, warlock, affliction, endgame]
level_min: 60
level_max: 60
faction: both
status: confirmed_forever
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://www.method.gg/wow-forever/class-guides/affliction-warlock
  - https://www.method.gg/wow-forever/class-guides/affliction-warlock/talents
  - https://www.method.gg/wow-forever/class-guides/affliction-warlock/rotation-and-playstyle
  - https://www.method.gg/wow-forever/class-guides/affliction-warlock/bis-gear-and-stats
  - https://www.method.gg/wow-forever/class-guides/affliction-warlock/enchants-and-consumables
  - https://www.method.gg/wow-forever/class-guides/affliction-warlock/races-professions-and-other
  - https://www.method.gg/wow-forever/class-guides/affliction-warlock/interface-addons-and-macros
  - https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json
  - https://foreverdb.net/class/Warlock/talents
related: ["[[Warlock]]", "[[Warlock-Leveling]]", "[[Demonology-Warlock]]", "[[Destruction-Warlock]]"]
---

# Affliction Warlock

> [!success] Confirmado en Forever
> Guía de endgame de Method (Roguery, 2026-11-04, parche 1.60.1). Builds decodificadas del widget. BiS "Work In Progress"; encantamientos y consumibles basados en beta y datamining. Una sola fuente: confianza media.

## Resumen
- Spec de DoT: **mantener Bane of Agony, Corruption, Siphon Life e Immolate**, gastar Nightfall en Shadow Bolt y rellenar con Shadow Bolt. Los DoT pueden hacer crítico y Pandemic sube su daño crítico. `confirmed_forever`
- Build principal **Shadow Mastery / Ruin 31/0/20**: potencia Shadow Bolt con talentos de Affliction y Destruction. La build **Wrack 33/11/7** existe porque el capstone es débil hoy y el autor espera un buff.
- **No hay ventana de refresco tipo pandemic de retail**: deja que los DoT terminen antes de reaplicarlos.
- Stats: **Hit 17 % > Spell Damage > Shadow Damage > Spell Piercing (hasta 0 resistencia) > Crit > Intellect > Haste > MP5 > Spirit**. Haste vale poco (no afecta a los DoT).
- Razas: S Human; A Orc y Undead; B Gnome; C Troll. Diferencia "dentro de 10 DPS".
- Al 60, cambiar Enchanting por Engineering (consumibles de daño).

## Talentos

Decodificadas del widget de Method (datos 1.60.1-2nov; nombres de ForeverDB). Estado `confirmed_forever`.

| Talento | SM / Ruin (31/0/20) | Wrack (33/11/7) | Efecto (ForeverDB / Method) |
|---|---|---|---|
| Suppression | 5 | 5 | +5 % hit y −20 % amenaza; no quitarla aunque sobre hit |
| Improved Corruption | 5 | 3 | 5/5 = Corruption instantánea |
| Improved Life Tap | 2 | 2 | |
| Improved Bane of Agony | 2 | 2 | +10 % daño de Bane of Agony |
| Amplify Curse | 1 | 1 | +50 % al siguiente Bane of Agony |
| Pandemic | 3 | 3 | +100 % bonus de crítico de DoTs y drenajes |
| Malevolence | 5 | 5 | +5 % crit Shadow |
| Nightfall | 2 | 2 | 4 % de Shadow Trance (Shadow Bolt rápido) |
| Siphon Life | 1 | 1 | |
| Soul Siphon | — | 3 | +12 % a drenajes y Wrack por DoT activo |
| Shadow Mastery | 5 | 5 | +10 % daño Shadow |
| Wrack | — | 1 | Canalizado de 6 s que acelera tus DoTs (capstone) |
| Demonic Embrace / Demonic Aegis / Fel Vitality / Demonic Sacrifice | — | 5 / 2 / 3 / 1 | Sacrificar el Imp: +15 % Shadow (Method) |
| Improved Shadow Bolt | 5 | 5 | |
| Bane | 5 | 2 | −0,5 s a Shadow Bolt e Immolate |
| Cataclysm | 2 | — | −mana de Destruction |
| Ruin | 5 | — | +100 % bonus de crítico Destruction |
| Agonizing Flames | 3 | — | +10 % daño Destruction |

Orden del widget:
- **SM / Ruin**: Suppression 10–13 → Imp. Corruption 14–16 → Suppression 17 → Imp. Bane of Agony 18–19 → Pandemic 20–22 → Amplify Curse 23 → Malevolence 24–28 → Siphon Life 29 → Nightfall 30–31 → Shadow Mastery 32–36 → Imp. Life Tap 37–38 → Imp. Corruption 39 → Imp. Shadow Bolt 40–44 → Bane 45–49 → Cataclysm 50–51 → Ruin 52–56 → Agonizing Flames 57–59 → Imp. Corruption 60.
- **Wrack**: igual hasta Nightfall 30–31 → Soul Siphon 32–34 → Shadow Mastery 35–39 → Wrack 40 → Demonic Embrace 41–45 → Demonic Aegis 46–47 → Fel Vitality 48–50 → Demonic Sacrifice 51 → Imp. Shadow Bolt 52–56 → Bane 57–58 → Imp. Life Tap 59–60.
- Multiobjetivo (Wrack): pasar 2 puntos de Bane a Improved Corruption.

## Rotación

| Paso | Prioridad (Method) | Estado |
|---|---|---|
| Antes del jefe | Succubus/Incubus, Greater Spellstone en el arma, Soulstone a un healer, Healthstone, repartir curses | confirmed_forever |
| Combate | Mascota atacando → curse asignada → Shadow Bolt con Nightfall → Amplify Curse → Bane of Agony → Corruption → Siphon Life → Immolate → Shadow Bolt o Wrack → Life Tap bajo 30 % de maná | confirmed_forever |

- Siempre Amplify Curse con Bane of Agony. No usar Life Tap si queda <1 min (acabar con poco maná). Drain Life si baja la vida. Vigila a la Succubus: se queda en zonas de daño.

## Stats y equipo
- Hit hasta **17 %** ([[src-method-how-does-hit-chance-work-in-wow-forever]]) > Spell Damage > Shadow Damage > Spell Piercing > Crit > Intellect > Haste > MP5 > Spirit.
- Pre-raid BiS, BiS, tier y abalorios: **desconocido** ("Work In Progress").

## Encantamientos y consumibles

| Slot | Encantamiento (Method) | Alternativa |
|---|---|---|
| Arma | 2M Spellblasting | Spell Power (1M) |
| Cabeza | Hoodoo Hex | — |
| Hombros | Power of the Scourge | — |
| Capa | Subtlety | Greater Resistance |
| Pecho | Major Intellect | Greater Stats |
| Muñecas | Greater Spellpower | Superior Intellect |
| Guantes | Shadow Power | — |
| Piernas | Mystic Thick Armor Kit | — |
| Pies | Minor Speed | Greater Stamina |
| Collar | Spell Power | — |

- Frasco: **Flask of Natural Aggression** en Hyjal Summit y Barrow Deeps; **Flask of Supreme Power** en el resto (según Method).
- Se pueden acumular elixires: Elixir of Shadow Power y Greater Arcane Elixir los importantes.
- Pociones: Major Spellblasting; reserva Living Action y Major Rejuvenation. Comida Baked Salmon o Lobster Stew. Demonic Rune.
- Estado `confirmed_forever` como recomendación de guía, pero la página dice basarse en beta y datamining. No explica cómo se obtienen Hoodoo Hex y Power of the Scourge en Forever.

## Razas y profesiones

| Tier | Razas | Motivo |
|---|---|---|
| S | Human | +1 % crit; The Human Spirit mejora Life Tap |
| A | Orc, Undead | A 1 DPS; Orc más burst, Undead más constante |
| B | Gnome | — |
| C | Troll | — |

- Profesiones: Tailoring + Enchanting subiendo; al 60 Engineering en lugar de Enchanting.

## Interfaz, addons y macros
- DoTs en placas o Cooldown Manager. Boss mod (BigWigs o DBM); sin probar.
- Macros: Pet Attack/Assist (`/petattack` + `/petpassive`), Amplify Curse + Bane of Agony, Drain Life con `[nochanneling:Drain Life]`, DoTs por `[@mouseover,exists]`.

## En grupo con un Rogue
- El Warlock aporta Healthstone, Soulstone y curses; si hay que elegir curse, las de reducción de armadura que cita la guía de Feral Tank (CoR) ayudan al daño físico del Rogue. *Inferido; la guía de Affliction no detalla qué curse poner.*

## Qué dicen las guías
- [[src-method-class-guides-affliction-warlock]], [[src-method-class-guides-affliction-warlock-talents]], [[src-method-class-guides-affliction-warlock-rotation-and-playstyle]], [[src-method-class-guides-affliction-warlock-bis-gear-and-stats]], [[src-method-class-guides-affliction-warlock-enchants-and-consumables]], [[src-method-class-guides-affliction-warlock-races-professions-and-other]], [[src-method-class-guides-affliction-warlock-interface-addons-and-macros]].
- Discrepancia de razas con la guía de leveling ([[src-method-wow-forever-warlock-leveling-guide-and-talents]], en [[Warlock]]): leveling pone a Undead en B; endgame Affliction lo pone en A junto a Orc.

## Fuentes

| URL | Tipo | Fecha página | Consultada | ¿Pre-parche? |
|---|---|---|---|---|
| https://www.method.gg/wow-forever/class-guides/affliction-warlock (+ 6 subpáginas) | Guía Method | 2026-11-04 | 2026-11-13 | No |
| https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json | Datos de la calculadora (Method) | 1.60.1 (02-11) | 2026-11-13 | No |
| https://foreverdb.net/class/Warlock/talents | Datos de cliente | sin fecha | 2026-11-13 | No |

[Data from ForeverDB.net](https://foreverdb.net)

## Preguntas pendientes
- ¿Recibirá Wrack un buff? El autor lo espera.
- ¿Dónde se consiguen Hoodoo Hex y Power of the Scourge en Forever?
