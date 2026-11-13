---
type: spec
tags: [forever, priest, holy, healer, endgame]
level_min: 40
level_max: 60
faction: both
status: confirmed_forever
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://www.method.gg/wow-forever/class-guides/holy-priest
  - https://www.method.gg/wow-forever/class-guides/holy-priest/talents
  - https://www.method.gg/wow-forever/class-guides/holy-priest/rotation-and-playstyle
  - https://www.method.gg/wow-forever/class-guides/holy-priest/bis-gear-and-stats
  - https://www.method.gg/wow-forever/class-guides/holy-priest/enchants-and-consumables
  - https://www.method.gg/wow-forever/class-guides/holy-priest/races-professions-and-other
  - https://www.method.gg/wow-forever/class-guides/holy-priest/interface-addons-and-macros
  - https://www.method.gg/dfc/ForeverTalentsData-1.60.1.json
  - https://nether.wowhead.com/forever/tooltip/spell/401859
  - https://nether.wowhead.com/forever/tooltip/spell/1317006
  - https://nether.wowhead.com/forever/tooltip/spell/1328569
  - https://timesaver.gg/tools/wow-forever/talent-calculator/priest
related: ["[[Priest]]", "[[Priest-Talents]]", "[[Discipline-Priest]]", "[[Shadow-Priest]]", "[[Priest-Macros-and-Addons]]", "[[Priest-Gear-and-Stats]]"]
---

# Holy Priest

> [!success] Confirmado en Forever
> Guía de endgame de Method (Shive, 2026-11-10, parche 1.60.1). BiS, tier y profesiones siguen "Work In Progress".

## Resumen
- Healer de raid y mazmorra. Núcleo: **Prayer of Mending en CD**, alternar curas para **Litany of Light** y cancelar casts para no romper la regla de 5 s (Method).
- Dos builds de Method: **Deep Holy Raid 16/35/0** y **Disc/Holy Penance & Soul Warding 21/30/0** para mazmorras y raids de 10 (ver [[Discipline-Priest]]).
- Stats: **Healing Power ≥ Spirit > MP5 > Intellect > Stamina > Crit**. Spiritual Guidance convierte el 25 % del Spirit en curación.
- **Undead es tier A** para Holy (Human es S). Profesiones: Tailoring (Truefaith Vestments) y Alchemy + Herbalism para consumibles. El personaje ya tiene Herbalism.
- No es spec de leveling en solitario (Warcraft Tavern: "slow kill times"). Sí sirve curar mazmorras durante el leveling (Method lo hace incluso en Shadow).

## Talentos

### Deep Holy Raid (16/35/0), Method
| Árbol | Talento | Rangos | Efecto (tooltip Wowhead Forever) |
|---|---|---|---|
| Holy | Improved Renew | 3/3 | +5 % a Renew (valor mostrado) |
| Holy | Holy Specialization | 5/5 | Crit de hechizos Holy |
| Holy | Divine Fury | 5/5 | −1 s a Smite, Holy Fire, Heal, Greater Heal |
| Holy | Holy Nova | 1/1 | |
| Holy | Inspiration | 3/3 | Crit de cura: +armadura al objetivo 15 s (Method: +25 %) |
| Holy | Holy Reach | 2/2 | +10 % alcance/radio |
| Holy | Improved Healing | 3/3 | −15 % coste de Lesser Heal, Heal, Greater Heal, Penance y PoM |
| Holy | Holy Binding | 1/1 | Flash Heal a otro te cura el 50 %, sin amenaza |
| Holy | Litany of Light | 2/2 | Si la cura anterior era otra, recuperas el 20 % del coste base |
| Holy | Spirit of Redemption | 1/1 | |
| Holy | Spiritual Guidance | 5/5 | +25 % del Spirit a curación, +8 % a daño |
| Holy | Spiritual Healing | 3/3 | |
| Holy | Prayer of Mending | 1/1 | Talento de 31 puntos; CD 10 s, 5 saltos |
| Disc | Twin Disciplines | 5/5 | Mejora PoM y Renew |
| Disc | Silent Resolve | 3/3 | −30 % amenaza (evita agro al aparecer adds) |
| Disc | Mental Strength | 4/5 | Resto de puntos al maná |
| Disc | Inner Focus | 1/1 | |
| Disc | Meditation | 3/3 | 50 % de regeneración al castear |

- Variantes: −2 Mental Strength → Twilight Focus en combates con mucho AoE; −1 Holy Reach → Mental Strength 5/5 si no hace falta radio.
- Fuera a propósito: Improved PW:S y Soul Warding (los escudos quitan ira a los tanques) y Mental Agility (en raid casi todo es casteado).

### Disc/Holy Penance & Soul Warding (21/30/0), Method
Ver detalle en [[Discipline-Priest]]. Resumen: Disc hasta Penance con Improved PW:S 3/3 y Soul Warding; Holy hasta Spiritual Guidance 5/5 y Litany of Light 2/2.

### Elecciones por objetivo (Method)
| Objetivo | Talentos |
|---|---|
| Spirit y maná | Meditation, Spiritual Guidance |
| Eficiencia al alternar | Litany of Light, Improved Healing |
| Autocuración | Holy Binding + Flash Heal |
| Mitigación del tanque y velocidad | Holy Specialization, Divine Fury, Inspiration |
| Ráfaga de grupo gratis | Inner Focus + Prayer of Healing |

Legacy al 60: árbol Resourcefulness (Reagent Economy, Permanence y Gourmand para ahorrar Sacred Candles; The Quick and the Dead y Reinforce para rebufar gratis tras un wipe; Diplomat para reputación). Ver [[Legacy]].

## Rotación y prioridades

| Contexto | Prioridad (Method) |
|---|---|
| Pre-pull raid | Prayer of Fortitude/Spirit/Shadow Protection, Inner Fire, Fear Ward al MT, PoM al MT 2 s antes. **Sin** Renew ni PW:S antes del pull |
| Raid | PoM cada 10 s → PW:S en picos → Inner Focus + PoH → Flash Heal + Holy Binding → Greater Heal r1 / Heal r2–r4 alternando con Renew y PoM |
| Mazmorra | PW:F, Divine Spirit, Shadow Protection; Fear Ward antes de packs con miedo (Stratholme, Scholomance, Ruins of Lordaeron); esperar al agro del tanque → PoM → Holy Binding → Greater Heal → PW:S a DPS → Dispel Magic ofensivo |

- Regla de 5 s: Meditation mantiene el 50 % de regeneración; cancelar un cast cuesta 0 de maná y no rompe la regla; Inner Focus hace gratis el siguiente hechizo.
- Downranking: Greater Heal r1 al tanque; Heal r2/r4 para curas puntuales con poco maná.
- CDs: Fade (amenaza, 10 s), Fear Ward, Spirit of Redemption (al morir, PoH/PoM/Greater Heal a rango máximo).
- Estado: `confirmed_forever` (guía post-parche).

## Stats y equipo
- **+Healing Power ≥ Spirit > MP5 > Intellect > Stamina > Spell Crit** (Method, WIP).
- Intellect: 15 de maná por punto y ~59,5 Int por 1 % de crit al 60. Stamina: 10 de vida por punto. Crit: cura al 150 % y activa Inspiration. Haste: rara, útil para Greater Heal y PoH.
- BiS, pre-raid, tier y trinkets: **desconocido** (WIP).

## Encantamientos y consumibles

| Slot | Encantamiento (Method) | Alternativas |
|---|---|---|
| Arma | Healing Power | Mighty Spirit; 2H Major Intellect |
| Cabeza / piernas | Prophetic Aura | Arcanum of Focus |
| Hombros | Zandalar Signet of Serenity | Chromatic Mantle of the Dawn |
| Capa | Subtlety | Greater Resistance; Greater Fire Resistance |
| Pecho | Greater Stats | Major Intellect; Major Stamina |
| Muñecas | Healing Power | Mana Regeneration; Superior Spirit |
| Guantes | Healing Power | Riding Skill; Core Armor Kit |
| Pies | Minor Speed | Spirit; Greater Stamina |

- Flask of Distilled Wisdom; Mageblood Potion y Elixir of the Sages (se acumulan); Major Mana Potion (primera hacia 2 200 de maná); protecciones Fire/Nature/Shadow; Nightfin Soup o Runn Tum Tuber Surprise; Brilliant Mana Oil; Demonic/Dark Rune (CD aparte); Kreeg's Stout Beatdown; Gordok Green Grog.

## Razas y profesiones
- Tier Method: S Human · **A Undead** · B Troll · C Night Elf/Gnome.
- Undead: Dark Sacrifice (maná en combates largos), Will of the Forsaken (curar durante Fear/Charm), Cannibalize (menos tiempo bebiendo). Ver [[Priest]] para las raciales en Forever.
- **Tailoring** como primera profesión: Truefaith Vestments (BoP, +73 Healing Power, +14 Spirit según Method; sin verificar en DB), bolsas, Mooncloth. **Alchemy + Herbalism**: Major Mana Potion, Mageblood Potion, Flask of Distilled Wisdom.

## Interfaz y macros
- Sin addons; marcos de raid centrados, atenuación a 40 m, curas entrantes, borde rojo para quien tiene agro. Seis macros mouseover en [[Priest-Macros-and-Addons]].

## Qué dicen las guías
- Method es la única guía Holy de endgame leída: [[src-method-class-guides-holy-priest]], [[src-method-class-guides-holy-priest-talents]], [[src-method-class-guides-holy-priest-rotation-and-playstyle]], [[src-method-class-guides-holy-priest-bis-gear-and-stats]], [[src-method-class-guides-holy-priest-enchants-and-consumables]], [[src-method-class-guides-holy-priest-races-professions-and-other]], [[src-method-class-guides-holy-priest-interface-addons-and-macros]].
- La build Holy de leveling de Icy Veins (vía Timesaver, 14/32/5, en [[Priest-Talents]]) es otra cosa: pensada para subir, con Spirit Tap.
- Discrepancias: razas (Holy: Undead A; Shadow: Undead S); consumible Mageblood (cheat sheet ID 250341 frente a Mageblood Potion 20007 en la subpágina).

## Fuentes

| URL | Tipo | Fecha de la página | Consultada | ¿Anterior al parche del 02-11? |
|---|---|---|---|---|
| https://www.method.gg/wow-forever/class-guides/holy-priest (+ 6 subpáginas) | guide | 2026-11-10 | 2026-11-13 | No |
| https://www.method.gg/dfc/ForeverTalentsData-1.60.1.json | datos de la calculadora | 1.60.1 | 2026-11-13 | No |
| https://nether.wowhead.com/forever/tooltip/spell/<id> | community DB | sin fecha | 2026-11-13 | Desconocido |
| https://timesaver.gg/tools/wow-forever/talent-calculator/priest | community tool | 04-11 | 2026-11-10 (nota previa) | No |

## Preguntas pendientes
- ¿Stats reales de Truefaith Vestments en Forever?
- ¿Es Mageblood Potion (20007) o Greater Mageblood Elixir (250341) lo que recomienda Method?
- ¿BiS pre-raid Holy? Pendiente de Method.
- ¿Qué % de armadura da Inspiration? El tooltip muestra "0%"; Method dice +25 %.
