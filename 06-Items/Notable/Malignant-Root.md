---
type: item
tags: [forever, item, ring, rare]
item_slot: finger
level_min: 20
faction: alliance
source_type: rare
status: conflicting
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources: ["https://www.method.gg/wow-forever/how-to-get-malignant-root-powerful-rare-ring-in-wow-forever", "Cliente WoW Forever 1.60.1.70938 vía wago.tools (consulta local, 2026-11-13)"]
related: ["[[Itemization]]", "[[Wetlands]]", "[[Excavation-Site-Wetlands]]"]
wago_item_id: 282283
---

# Malignant Root

> [!warning] Datos en conflicto: ver [[Conflicts]]
> La fuente se contradice sobre si el anillo es BoE. Las Rotheap Innards sí se comercian.

## Resumen
- Qué es y para quién: anillo raro con stats "de nivel 30+" (aguante, poder con hechizos/sanación y poder de ataque), sin nivel mínimo. Method lo destaca para Paladin; por sus stats sirve a cualquier lanzador (inferido).
- Cómo se consigue: matar al élite raro **Nightveiled Rotheap** (nv 31-32, Wetlands), saquear **Rotheap Innards** y entregarlas a **Rethiel the Greenwarden** (Wetlands 56.4, 40.5, diálogo "I found something").
- **Solo Alliance:** Rethiel es hostil a la Horde. Un Undead Priest **no puede conseguir el anillo** por ahora; sí puede matar al raro y vender las Innards.
- Stats (Wowhead Forever): item 282283; cifras no verificadas.

## Detalle
| Dato | Valor | Estado |
|---|---|---|
| Item | Malignant Root (282283) | confirmed_forever |
| Objeto de entrega | Rotheap Innards (279537), comerciable | confirmed_forever |
| Raro | Nightveiled Rotheap, élite nv 31-32, patrulla aguas pantanosas hacia la presa, se puede ralentizar | confirmed_forever |
| Nivel práctico | Solado por jugadores nv 20-25 kiteando (level_min de esta nota = ese dato) | confirmed_forever |
| Botín | Todos los miembros del grupo o raid saquean Innards | confirmed_forever |
| Reaparición | desconocido | unknown |
| ¿BoE el anillo? | La fuente dice que no, pero también habla de "parte BoE" | conflicting |
| Precio Innards | 29s, EU PvE Normal, >40 subastas (fecha ~2026-11-11) | confirmed_forever |

## Datos del cliente (cliente 1.60.1.70938)
- Malignant Root: ID 282283 · Rare · ilvl 32 · req 1 · Finger · Miscellaneous · venta 0 · liga al recoger · stats: Stamina, AttackPower, SpellPower. Coincide con los stats que describe Method (aguante, poder de ataque y poder con hechizos).
- **Ligado:** Bonding = 1 (`OnAcquire`, se liga al recoger) según el cliente. Apoya la versión "no es BoE" del conflicto, pero es dato del cliente, no del servidor: el conflicto se mantiene hasta verlo en el juego.
- Nivel requerido 1 en el cliente: coincide con "sin nivel mínimo" de la fuente.
- Rotheap Innards (279537): existe en la tabla `Item` (ClassID 15, varios) pero **sin fila en ItemSparse**: no está en el cliente con nombre (posible objeto oculto). No se puede confirmar el nombre desde el cliente.
- La facción (solo Alliance) no está en estos datos: AllowableRace no se interpreta.
- Fuente: tablas DB2 del cliente WoW Forever 1.60.1.70938 (wago.tools, extraídas 2026-11-13). Datos de los archivos del juego, no del servidor. Calidad y ranura: etiquetas de enums públicos de Blizzard; nombres de stats y de ligado: `Enum.BonusStatIndex` / `Enum.ItemBind` del propio cliente (sin cantidades). "venta" = SellPrice de vendedor, no subasta.

## Qué dicen las guías
- Solo [[src-method-how-to-get-malignant-root-powerful-rare-ring-in-wow-forever]]. No sabe si se añadirá un NPC Horde.

## Fuentes
- https://www.method.gg/wow-forever/how-to-get-malignant-root-powerful-rare-ring-in-wow-forever (Guía Method, 2026-11-11, consultada 2026-11-13, posterior al parche).

## Preguntas pendientes
- ¿Habrá entrega para la Horde?
- Stats exactos y si el anillo es BoP.
