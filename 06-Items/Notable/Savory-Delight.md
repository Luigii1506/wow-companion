---
type: item
tags: [forever, item, cooking, cosmetic]
item_slot: consumable
source_type: crafted
status: confirmed_forever
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources: ["https://www.method.gg/wow-forever/savory-whimsyfin-delight-and-savory-deviate-delight-how-to-turn-into-a-pirate-or-ninja-in-wow-forever", "Cliente WoW Forever 1.60.1.70938 vía wago.tools (consulta local, 2026-11-13)"]
related: ["[[Cooking]]", "[[Fishing]]", "[[The-Barrens]]", "[[Redridge-Mountains]]"]
wago_item_id: [6657, 251525]
---

# Savory Deviate Delight y Savory Whimsyfin Delight

> [!success] Confirmado en Forever
> Guía escrita en beta (2026-10-12).

## Resumen
- Qué es y para quién: comidas de Cocina que transforman en pirata o ninja durante 60 min (cosmético). Deviate → humano; **Whimsyfin (nueva en Forever) → orco**. Pirata o ninja al azar.
- Se mantiene en combate; se pierde al morir o al cambiar de forma (**Shadowform del Shadow Priest la rompe**).
- Cómo se consigue: receta por drop raro en una zona + pescado de bancos de esa zona; recetas, pescado y comida se venden en subasta.
- Stats (Wowhead Forever): sin stats; IDs abajo.

## Detalle
| Objeto | ID | Receta (drop) | Pescado | Estado |
|---|---|---|---|---|
| Savory Deviate Delight | 6657 | Receta 6661: cualquier mob de The Barrens | Deviate Fish (6522): bancos del interior de Barrens, también fuera de bancos y en la entrada de Wailing Caverns | confirmed_forever |
| Savory Whimsyfin Delight | 251525 | Receta 251526: cualquier mob de Redridge Mountains | Whimsyfin (251524): solo bancos de Redridge, sobre todo el lago pequeño del este junto al poblado murloc | confirmed_forever |

Nivel de Cocina y precios: desconocidos. En beta Whimsyfin convertía en murloc u ogro (placeholder retirado).

## Datos del cliente (cliente 1.60.1.70938)
- Savory Deviate Delight: ID 6657 · Common · ilvl 10 · req 1 · Food & Drink · venta 5c.
- Savory Whimsyfin Delight: ID 251525 · Common · ilvl 10 · req 1 · Other · venta 5c.
- Recipe: Savory Deviate Delight: ID 6661 · Uncommon · ilvl 18 · Cooking · venta 1s 15c.
- Recipe: Savory Whimsyfin Delight: ID 251526 · Uncommon · ilvl 18 · Cooking · venta 1s 15c.
- Deviate Fish: ID 6522 · Common · ilvl 15 · Food & Drink · venta 4c. Whimsyfin: ID 251524 · Common · ilvl 15 · Other · venta 4c.
- Los seis IDs de la tabla de la nota coinciden con el cliente. Las dos recetas piden **Cooking 85** según el cliente (`RequiredSkill` 185 = SkillLine "Cooking", `RequiredSkillRank` 85). Es el requisito para aprender la receta; la nota lo tenía como desconocido. Las comidas no piden skill para usarse (0).
- Fuente: tablas DB2 del cliente WoW Forever 1.60.1.70938 (wago.tools, extraídas 2026-11-13). Datos de los archivos del juego, no del servidor. Calidad y ranura: etiquetas de enums públicos de Blizzard; nombres de stats y de ligado: `Enum.BonusStatIndex` / `Enum.ItemBind` del propio cliente (sin cantidades). "venta" = SellPrice de vendedor, no subasta.

## Fuentes
- https://www.method.gg/wow-forever/savory-whimsyfin-delight-and-savory-deviate-delight-how-to-turn-into-a-pirate-or-ninja-in-wow-forever (Guía Method, 2026-10-12, consultada 2026-11-13, anterior al parche). Ficha: [[src-method-savory-whimsyfin-delight-and-savory-deviate-delight-how-to-turn-into-a-pirate-or-ninja-in-wow-forever]].

## Preguntas pendientes
- Nivel de Cocina requerido.
