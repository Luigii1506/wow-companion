---
type: item
tags: [forever, item, utility]
item_slot: none
faction: both
source_type: quest
status: confirmed_forever
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources: ["https://www.method.gg/wow-forever/how-to-get-a-torch-in-wow-forever-night-watchmans-torch", "Cliente WoW Forever 1.60.1.70938 vía wago.tools (consulta local, 2026-11-13)"]
related: ["[[Duskwood]]", "[[Cozy-Sleeping-Bag]]"]
wago_item_id: none
---

# Night Watchman's Torch

> [!success] Confirmado en Forever
> Guía escrita en beta (2026-10-07).

## Resumen
- Qué es y para quién: antorcha de uso que da luz 5 min (reutilización 30 s). El nuevo motor de luz de Forever oscurece zonas como **Tirisfal Glades y Silverpine**, Duskwood y Stranglethorn de madrugada.
- Cómo se consigue: misión instantánea ("!" amarillo) sobre un **Night Watch Guard** muerto en Duskwood, solo de noche (desde ~20:00 hora del juego). Posición variable; reproducida en Raven Hill 18.1, 55.2.
- Horde: zepelín Orgrimmar → Grom'gol y a pie al norte hasta Duskwood. Para un nivel 9 el viaje es largo y peligroso (inferido); mejor más adelante.
- Stats (Wowhead Forever): item 280612; sin stats.

## Detalle
| Dato | Valor | Estado |
|---|---|---|
| Duración / reutilización | 5 min / 30 s | confirmed_forever |
| Se apaga | Al hacer acción de combate, en agua, dentro de capitales | confirmed_forever |
| Único | Sí; si se borra se vuelve a por otra | confirmed_forever |
| Nivel mínimo | desconocido | unknown |

## Datos del cliente (cliente 1.60.1.70938)
- Night Watchman's Torch: no está en el cliente por nombre (posible objeto oculto).
- El ID 280612 (Wowhead) existe en la tabla `Item` (ClassID 15, SubclassID 0) pero **sin fila en ItemSparse**: el cliente no tiene su nombre, nivel ni precio. No se puede confirmar que 280612 sea la antorcha. Nivel requerido: sigue `unknown`.
- Fuente: tablas DB2 del cliente WoW Forever 1.60.1.70938 (wago.tools, extraídas 2026-11-13). Datos de los archivos del juego, no del servidor. Calidad y ranura: etiquetas de enums públicos de Blizzard; nombres de stats y de ligado: `Enum.BonusStatIndex` / `Enum.ItemBind` del propio cliente (sin cantidades). "venta" = SellPrice de vendedor, no subasta.

## Fuentes
- https://www.method.gg/wow-forever/how-to-get-a-torch-in-wow-forever-night-watchmans-torch (Guía Method, 2026-10-07, consultada 2026-11-13, anterior al parche). Ficha: [[src-method-how-to-get-a-torch-in-wow-forever-night-watchmans-torch]].

## Preguntas pendientes
- Nivel requerido y nivel de mobs en el camino Grom'gol → Duskwood.
