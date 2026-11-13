---
type: tip
tags: [forever, tips, xp, leveling, rested, camping, food]
level_min: 1
level_max: 60
faction: horde
status: confirmed_forever
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://www.warcrafttavern.com/forever/news/cooked-food-provides-an-xp-buff-in-world-of-warcraft-forever/
  - https://kami-labs.fr/en/guide-cuisine-wow-forever/
  - https://foreverdb.net/quests/durotar
  - "Cliente WoW Forever 1.60.1.70938 vía wago.tools (tablas Spell, SpellEffect, SpellDuration, ItemEffect; consulta local)"
related: ["[[Leveling-Tips]]", "[[Camping]]", "[[Cozy-Sleeping-Bag]]", "[[Legacy]]", "[[Dungeon-XP]]", "[[Food-and-Cooking-for-Leveling]]", "[[Buffs-Guide]]", "[[Beginner-Guide]]", "[[Conflicts]]"]
---

# Bonus de XP en Forever

> [!success] Confirmado en Forever
> Las cifras de comida, Camp Tent, Cozy Sleeping Bag y Legacy *Well Rested* se han leído en el **cliente de Forever 1.60.1.70938** (wago.tools, consulta local del 2026-11-13). Eso dice lo que el juego tiene programado, no lo que el servidor aplica: falta probarlo en el juego. Personaje: Orc Rogue 11 dicho por el usuario, **sin export**.

## Resumen
- **Hay solo tres bonus de XP reales a tu alcance ahora**: descanso (dobla la XP de muertes), **comida nutritiva** (+5 % XP de muertes durante los 15 min del Well Fed) y, más adelante, el **Cozy Sleeping Bag** (hasta +3 % a toda la XP, 2 h).
- **Camp Tent** no es un buff de 1 h: rellena tu descanso hasta el **5 % de un nivel** si tienes menos, una vez por hora. Lo pone alguien con Leatherworking; tú no lo tienes.
- **La mayor fuente de XP siguen siendo las misiones**, sobre todo las de mazmorra (las muertes en mazmorra dan +50 % desde el hotfix del 9-nov). Ver [[Dungeon-XP]].
- No todo lo cocinado da XP: **Charred Wolf Meat, Scorpid Surprise, Dig Rat Stew y Boiled Clams no dan Well Fed** (cliente). Come algo de la tabla de [[Food-and-Cooking-for-Leveling]].
- Warchief's Blessing, Sayge y Blood Shards **no dan XP**; solo matan más rápido. Están en [[Buffs-Guide]].

## Tabla de bonus
"Cliente" = leído en las tablas del cliente 1.60.1.70938. Cómo se combinan entre sí (suma o multiplicación): **desconocido**.

| Bonus | Efecto | Duración | Cómo conseguirlo (Horde) | Nivel | ¿Se suma con...? | Estado |
|---|---|---|---|---|---|---|
| **Descanso (rested)** | Dobla la XP de muertes, no la de misiones | Hasta gastarlo | Desconectar en posada o capital (Razor Hill, Crossroads, Orgrimmar). +5 % de un nivel cada 8 h; tope 150 % (~10 días) | 1+ | Sí, con comida y saco | confirmed_forever (medium, WT); reglas `probable_classic` ([[Patch-Changes]]) |
| **Well Fed XP Boost** (comida nutritiva) | **+5 % XP de muertes** (aura 1243969, cliente) | Lo que dure el Well Fed: **15 min** (cliente); se pierde al morir (WT) | Comer 10 s sentado una comida "Nutritious Food/Drink": Roasted Boar Meat, Spiced Wolf Meat, Herb Baked Egg… ([[Food-and-Cooking-for-Leveling]]) | Comida desde nivel 1 | Sí | confirmed_forever (cliente + WT). El texto depende de una condición de jugador (pc142418) sin decodificar: quizá se apague a 60 (`unknown`) |
| **Camp Tent** (Leatherworking 20) | Sube tu descanso hasta el **5 % de un nivel**; si ya tienes más, nada | La tienda dura 15 min; hay que estar sentado 30 s cerca; luego *Boosted Rest* te bloquea **1 h** | Un jugador con Leatherworking la pone junto a una hoguera; tú solo te sientas | Cualquiera | Es descanso, así que dobla la XP de muertes | confirmed_forever (cliente). Corrige a WT ("buff de 1 h"): ver C36 en [[Conflicts]] |
| Adventurer's Tent | Igual, pero hasta el **20 % de un nivel** para el grupo | 15 min | **Origen desconocido** (está en el cliente, sin fuente) | ? | — | unknown |
| **Cozy Sleeping Bag** | +1 % de XP por acumulación (a XP de muertes **y** de misiones, cliente), máx. 3 | 2 h; el saco desplegado dura 20 min; 1 min dentro por acumulación | Cadena de 6 misiones desde Burned-Out Remains, Barrens (46.12, 74.32). Method recomienda 30+ a la Horde | 14 (requisito) / 30+ (práctico) | Sí; además es zona de descanso | confirmed_forever ([[Cozy-Sleeping-Bag]], cliente) |
| **Legacy: Well Rested** | Descanso un **20 % más rápido y tope +20 %** (valor del hechizo en el cliente; WT: 4 % por rango, 5 rangos) | Pasivo | Puntos Legacy de cuenta (tecla Y). No tienes ninguno conocido: Mining y Skinning no dan puntos | Cuando haya puntos | Sí | confirmed_forever (cifra del cliente); rangos `unknown` ([[Legacy]]) |
| Misiones de mazmorra | Mucha más XP que en Classic (p. ej. *Deviate Hides* 3.100 en beta) | — | RFC (13–18), WC (17–24): todas las misiones, una vez | 13+ | — | confirmed_forever (medium) ([[Dungeon-XP]]) |
| Muertes en mazmorra | +50 % de XP (hotfix 9-nov) | Permanente | Cualquier mazmorra | 13+ | — | confirmed_forever (high) |
| Libros de biblioteca | Algo de XP y plata por libro | — | Entregar a Owen Thadd, **Undercity** (74.0, 32.5). Cerca de ti: *The Lessons of Ta'zo* (Orgrimmar 38.6, 78.4) y 3 en The Barrens | 1+ | — | confirmed_forever ([[Library-Books]]); cantidad `unknown` |
| Fortunas de Sayge #23–27 | Misión de 660 XP + 50 rep + Mysterious Lockbox | — | Darkmoon Faire (Mulgore o Elwynn) | ? | — | confirmed_forever ([[Darkmoon-Faire]]) |

### En el cliente, pero no cuentes con ellos
| Hechizo u objeto | Qué dice el cliente | Por qué no | Estado |
|---|---|---|---|
| Elixir of Endless Experience (objeto 289334, req. nivel 1) | Aura de XP con valor 200 durante 1 h | Sin ninguna fuente sobre cómo se consigue; valor sospechoso | unknown |
| Archmagister's Wisdom / Perception | +10 % XP al matar no-muertos, 5 min | Origen desconocido; en Barrens casi no hay no-muertos | unknown |
| Winds of Wisdom, Adventure Awaits, Discoverer's Delight | +50 % / +100 % XP | El propio cliente los marca de China, Season of Mastery y Season of Discovery: restos de otras versiones | unknown (no aplicar) |

### Lo que no da XP (aunque ayuda a subir)
- **Thrill of Adventure** (Legacy): recupera vida y maná al matar (5 % a rango máximo según el cliente); menos tiempo comiendo. `confirmed_forever` (cifra del cliente).
- **Warchief's Blessing**, **Blood Shards**, **Sayge**, objetos de campamento: matan más rápido. [[Buffs-Guide]].

## Rutina antes de jugar (Orc Rogue, Durotar/Barrens)
1. **Al desconectar la vez anterior**: en posada o capital, para acumular descanso. Ver la barra de XP: la parte azul es descanso.
2. **Comprueba si hay Warchief's Blessing** activo en Orgrimmar, Razor Hill o Crossroads: si alguien entrega la cabeza de Rend mientras estás allí, lo recibes (1 h, sobrevive a la muerte). No se puede planificar.
3. **Hoguera**: si tienes Cooking, pon una Basic Campfire (Simple Wood + Flint and Tinder; materiales en conflicto, ver [[Camping]]), siéntate 1 min y coloca tu objeto (Lodestone con Mining 20). Si hay un Leatherworker cerca con Camp Tent, siéntate 30 s: rellena el descanso hasta el 5 % de un nivel.
4. **Come una comida nutritiva** (10 s sentado) justo antes de salir a matar. Repite cada 15 min mientras hagas muertes, y tras morir.
5. **Agrupa muertes** cuando tengas descanso y Well Fed: es cuando la XP de muertes vale doble +5 %. Las entregas de misiones guárdalas para cuando se acabe (no les afecta ninguno de los dos).
6. Desde 14, si vas a matar quillboars cerca de Camp Taurajo: Agamaggan's Agility (4 Blood Shards, 30 min). Ver [[Buffs-Guide]].

## Qué dicen las guías
- Consenso: comida +5 % XP de muertes ([[src-warcrafttavern-news-cooked-food-provides-an-xp-buff-in-world-of-warcraft-forever]], [[src-warcrafttavern-guides-experience]], [[src-meinmmo-wow-forever-level-guide-tricks]]); Camp Tent +5 % de un nivel ([[src-meinmmo-wow-forever-level-guide-tricks]]; Method, citado en [[Priest-Leveling]]).
- Discrepancias:
  - WT describe el Camp Tent como "descanso de 1 h que sobrevive a la muerte"; el cliente dice que rellena el descanso al 5 % de un nivel con 1 h de bloqueo (C36).
  - [[src-kamilabs-guide-cuisine-wow-forever]] dice que el bonus de XP de la comida no está datamineado; el cliente sí lo tiene.
  - [[Leveling-Tips]] dudaba si el Cozy Sleeping Bag afecta solo a muertes: el cliente aplica el +1 % a XP de muertes y de misiones.

## Fuentes
- [Data from ForeverDB.net](https://foreverdb.net)
| Fuente | Tipo | Fecha de la página | Consultada | ¿Antes del parche 2026-11-02? |
|---|---|---|---|---|
| Cliente 1.60.1.70938 vía wago.tools (Spell, SpellEffect, SpellDuration, ItemEffect, ItemSparse) | datos del cliente | build de lanzamiento | 2026-11-13 | No |
| https://www.warcrafttavern.com/forever/news/cooked-food-provides-an-xp-buff-in-world-of-warcraft-forever/ | noticia (Deep Dive) | 2026-09-13 | 2026-11-13 | Sí |
| https://kami-labs.fr/en/guide-cuisine-wow-forever/ | guía | 2026-11-10 | 2026-11-13 | No |
| https://foreverdb.net/quests/durotar | base de datos | 2026-11-13 | 2026-11-13 | No |
| Notas de la bóveda: [[Leveling-Tips]], [[Camping]], [[Cozy-Sleeping-Bag]], [[Legacy]], [[Dungeon-XP]], [[World-Buffs]], [[Library-Books]], [[Darkmoon-Faire]] | conocimiento | 2026-11-13 | 2026-11-13 | mezcla |

## Preguntas pendientes
- ¿Qué es la condición pc142418 del bonus de comida? ¿Se apaga a 60 o en algún contenido?
- ¿Los bonus se suman o se multiplican? Medir con el log de XP de un export.
- Origen de Adventurer's Tent y Elixir of Endless Experience.
- ¿El Well Fed se pierde al morir también en vivo (dato de WT)?
