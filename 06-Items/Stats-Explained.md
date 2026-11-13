---
type: topic
tags: [forever, stats, items, rogue]
faction: both
status: conflicting
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://foreverdb.net/stats
  - https://foreverdb.net/veterans
  - https://foreverdb.net/faq
  - https://foreverdb.net/bis/rogue/combat
related: ["[[Hit-Chance]]", "[[Itemization]]", "[[Rogue-Gear-and-Stats]]", "[[Rogue-BiS-by-Level]]", "[[Conflicts]]"]
---

# Estadísticas explicadas

> [!warning] Datos en conflicto: ver [[Conflicts]]
> Las conversiones vienen del **cliente** de Forever (build 1.60.1.70938) vía ForeverDB: tablas PlayerExpectedStat y ChrClasses, código de la hoja de personaje y tooltips. El cliente de Classic Era no tiene estos números (los calcula el servidor). El tope de hit con doble arma contra jefes **no coincide** con lo recogido en [[Hit-Chance]].

## Resumen
- **Rogue a nivel 60**: 29,0 Agility = 1 % de crit; cada punto de Strength y de Agility da 1 AP; Agility da 2 AP a distancia.
- **Hit y crit son un solo stat** cada uno (cuerpo a cuerpo, distancia y hechizos comparten valor) y el equipo usa **ratings fijos a cualquier nivel**: 14 crit rating = 1 % crit, 10 hit rating = 1 % hit.
- **14 AP = +1 DPS** del arma; Stamina = 10 de vida por punto (tras los primeros 20); Agility = 2 de armadura por punto.
- Tope de hit para no fallar: jefe de raid 8 % cuerpo a cuerpo con un arma, **27 % con doble arma** (ForeverDB) frente a 29 % (Method, [[Hit-Chance]]).
- No datamineable: crit base, dodge por Agility y regeneración por Spirit.

## Conversiones por clase a nivel 60
| Clase | Agility para 1 % crit | Intellect para 1 % crit de hechizo | AP por Strength | AP por Agility | AP a distancia por Agility | Maná base |
|---|---|---|---|---|---|---|
| **Rogue** | **29,0** | — | 1 | 1 | 2 | — |
| Warrior | 20,0 | — | 2 | — | 2 | — |
| Hunter | 52,9 | 60,6 | 1 | 1 | 2 | 1720 |
| Paladin | 19,8 | 59,9 | 2 | — | — | 1512 |
| Shaman | 19,7 | 59,2 | 2 | — | — | 1520 |
| Druid | 20,0 | 59,9 | 2 | — | — | 1244 |
| Priest | 20,0 | 59,5 | 1 | — | — | 1376 |
| Mage | 19,5 | 59,5 | 1 | — | — | 1213 |
| Warlock | 20,0 | 60,6 | 1 | — | — | 1373 |

Estado: confirmed_forever (cliente). Valores a otros niveles: en la página de cada clase de ForeverDB (no leída).

## Reglas comunes
| Regla | Valor | Estado |
|---|---|---|
| Stamina | 10 de vida por punto tras los primeros 20 | confirmed_forever (cliente) |
| Intellect | 15 de maná por punto tras los primeros 20 | confirmed_forever (cliente) |
| Agility | 2 de armadura por punto | confirmed_forever (cliente) |
| Attack power | 14 AP = 1 DPS de arma | confirmed_forever (cliente) |
| Strength y bloqueo | 1 Block Value por cada 20 Strength (Warrior, Paladin, Shaman) | confirmed_forever (cliente) |
| Ratings | 14 crit = 1 %, 10 hit = 1 %, 12 dodge = 1 %, 15 parry = 1 %, 5 block = 1 %, a todos los niveles | confirmed_forever (cliente) |
| Defense | +0,04 % de dodge, parry y block y −0,04 % de ser golpeado o criticado por punto sobre el máximo de tu nivel; 440 = inmune a críticos de jefe | confirmed_forever (cliente) |
| Armadura | Reducción máxima 75 %; la fórmula de reducción es la de Classic | confirmed_forever (tope) / unknown (fórmula, Speculation) |
| Regeneración sentado | Vida +1/3 | confirmed_forever (cliente) |
| Crit base, dodge por Agility, regeneración por Spirit | No están en el cliente | unknown |

## Tope de hit
| Objetivo | Cuerpo a cuerpo / distancia | Hechizos | Doble arma | Fuente | Estado |
|---|---|---|---|---|---|
| Mismo nivel | 5 % | 4 % | 24 % | ForeverDB (cliente) | confirmed_forever |
| Jefe de raid (+3) | 8 % | 17 % | **27 %** | ForeverDB (cliente) | conflicting |
| Jefe de raid (+3) | 8 % | 17 % | **29 %** | Method, en [[Hit-Chance]] | conflicting |

Coinciden en todo menos en el doble arma contra jefe. Para un Rogue a nivel 11 esto no importa todavía.

## Qué significa para el Orc Rogue
- Agility es el mejor stat por punto (AP + crit + armadura); Strength da la mitad de AP que a un Warrior.
- Hit en el equipo es valioso en mazmorras (los pesos de ForeverDB lo ponen por encima de Agility a 60, ver [[Rogue-BiS-by-Level]]).
- Blood Fury (+10 % AP 15 s) escala con todo el AP que acumules.

## Qué dicen las guías
- [[src-foreverdb-stats]]: todas las conversiones y topes; aclara qué no está en el cliente.
- [[src-foreverdb-veterans]]: hit y crit unificados; ayuda a híbridos.
- [[src-foreverdb-faq]]: AP: Rogue y Hunter reciben 1 por Strength y 1 por Agility.
- [[src-foreverdb-bis-rogue-combat]]: pesos de Combat (DPS de arma 3,5, hit 1,5, expertise 1,1, Agility 1, crit 0,9).
- Discrepancia: doble arma contra jefe 27 % (ForeverDB) frente a 29 % (Method). Ninguno probado en el juego.

## Fuentes
| URL | Tipo | Fecha de la página | Consultada | ¿Antes del 2026-11-02? |
|---|---|---|---|---|
| https://foreverdb.net/stats | Base de datos (cliente) | 2026-11-13 | 2026-11-13 | No |
| https://foreverdb.net/veterans | Guía | 2026-11-13 | 2026-11-13 | No |
| https://foreverdb.net/faq | FAQ | 2026-11-13 | 2026-11-13 | No |
| https://foreverdb.net/bis/rogue/combat | BiS algorítmico | 2026-11-13 | 2026-11-13 | No |

[Data from ForeverDB.net](https://foreverdb.net)

## Preguntas pendientes
- Crit base del Rogue y dodge por Agility medidos en el juego.
- Resolver el tope de hit con doble arma contra jefe (27 % o 29 %).
- Conversión de Agility a crit en niveles 10–30.
