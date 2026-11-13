---
type: topic
tags: [forever, professions, mining, nodes, gathering, horde, foreverdb-addon]
level_min: 1
level_max: 50
faction: horde
status: probable_classic
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - "Addon ForeverDB 0.60.3, datos 2026-11-13.ea2bb422 (build 1.60.1.70938): Gather.lua"
  - https://foreverdb.net
related: ["[[Mining]]", "[[Ores]]", "[[Gathering-Routes]]", "[[Engineering]]", "[[Quests-Durotar]]", "[[Quests-The-Barrens]]", "[[Quests-Stonetalon-Mountains]]", "[[Leveling-Route-Orc]]", "[[Conflicts]]"]
---

# Vetas de Mining por zona (Horde)

> [!info] Hipótesis basada en Classic
> Casi todos los puntos son **posiciones de spawn de Classic** (CMaNGOS classic-db, vía el addon ForeverDB). Solo una parte la han **visto jugadores en Forever** (columna en negrita): esa sí es `confirmed_forever`. En todo el addon hay 6906 puntos de Classic y 166 vistos en Forever para las 10 vetas de Mining. Un punto es un lugar posible, no una veta simultánea, y varios minerales comparten puntos.

## Resumen
- Copper (1–65): **Durotar** es la mejor zona Horde: 159 puntos de Classic y **15 vistos en Forever**, todos en la mitad sur (x 39–53, y 52–73). Le siguen Silverpine (105) y Mulgore (67). `probable_classic` (Durotar: 15 puntos `confirmed_forever`)
- Tin y Silver (65–125): en Forever se han visto **19 Tin y 8 Silver en The Barrens** (más que en ninguna otra zona Horde de Kalimdor) y 12 Tin / 5 Silver en Silverpine. Silver solo aparece donde hay Tin: en los datos de Classic los dos comparten casi los mismos puntos. `confirmed_forever` (puntos vistos)
- **Iron en Stonetalon**: jugadores vieron 3 Iron Deposit (35.4, 9.4 · 37.4, 69.8 · 38.8, 20.9) donde los datos de Classic del addon no tienen ninguno. También 2 Silver frente a 1 de Classic. `confirmed_forever`
- Iron/Gold (125–175): Thousand Needles (Iron 110, Gold 35), Desolace (Iron 92), Ashenvale (Iron 55), Arathi y Stranglethorn (~130–260 puntos compartidos). Ninguno visto aún en Forever salvo Hillsbrad (4 Iron). `probable_classic`
- No hay "Poor Copper Vein" entre los tipos de veta del addon (10 tipos: Copper, Tin, Silver, Iron, Gold, Mithril, Dark Iron, Truesilver, Small y Rich Thorium). `unknown`
- Fuera de las zonas de esta tabla: Alterac Mountains Silver Vein 1 vistos (Classic 175); Dun Morogh Copper Vein 9 vistos (Classic 90); Elwynn Forest Copper Vein 19 vistos (Classic 110); Redridge Mountains Tin Vein 2 vistos (Classic 103); Teldrassil Copper Vein 3 vistos (Classic 0); Westfall Copper Vein 2 vistos (Classic 143); Westfall Tin Vein 5 vistos (Classic 23); Zephras Isle Copper Vein 25 vistos (Classic 0).

## Cómo leer las tablas
- Celda `Classic / Forever`: número de puntos de spawn de Classic (CMaNGOS) / número de puntos donde jugadores de ForeverDB vieron la veta en Forever. "—" = la zona no tiene esa veta en los datos.
- Coordenadas: x, y en % del mapa de la zona, tal como las da el addon (décimas de %).
- El addon trae otra cifra por zona (`w`) sin documentar; no se usa aquí.
- Skill entre paréntesis: skill mínimo de la veta (cliente).

## Vetas de 1 a 175 por zona
| Zona (nivel orientativo) | Copper Vein (1) | Tin Vein (65) | Silver Vein (75) | Iron Deposit (125) | Gold Vein (155) | Mithril Deposit (175) |
|---|---|---|---|---|---|---|
| Durotar (1–10) | 159 / **15** | — | — | — | — | — |
| Orgrimmar (ciudad) | 4 / 0 | — | — | — | — | — |
| Mulgore (1–10) | 67 / 0 | 1 / 0 | — | — | — | — |
| The Barrens (10–25) | 38 / **11** | 23 / **19** | 20 / **8** | 10 / 0 | 2 / 0 | — |
| Stonetalon Mountains (15–27) | 47 / **3** | 19 / **6** | 1 / **2** | 0 / **3** | — | — |
| Ashenvale (18–30) | 55 / 0 | 33 / 0 | 57 / 0 | 55 / 0 | 3 / 0 | — |
| Thousand Needles (25–35) | 45 / 0 | 24 / 0 | 7 / **1** | 110 / 0 | 35 / 0 | — |
| Desolace (30–40) | 9 / 0 | 20 / 0 | 4 / 0 | 92 / 0 | 5 / 0 | 30 / 0 |
| Tirisfal Glades (1–10) | 64 / **2** | 6 / 0 | 6 / 0 | — | — | — |
| Silverpine Forest (10–20) | 105 / **2** | 105 / **12** | 105 / **5** | — | — | — |
| Hillsbrad Foothills (20–30) | 55 / 0 | 65 / **4** | 68 / **3** | 18 / **4** | 18 / 0 | — |
| Arathi Highlands (30–40) | 2 / 0 | 2 / 0 | 259 / 0 | 244 / 0 | 258 / 0 | — |
| Stranglethorn Vale (30–45) | 4 / 0 | 4 / 0 | 130 / 0 | 130 / 0 | 130 / 0 | — |
| Badlands (35–45) | 1 / 0 | 1 / 0 | 1 / 0 | — | 109 / 0 | 109 / 0 |
| Swamp of Sorrows (35–45) | — | — | — | — | 9 / 0 | 9 / 0 |
| Dustwallow Marsh (35–45) | — | — | 1 / 0 | 14 / 0 | 1 / 0 | — |
| Feralas (40–50) | 3 / 0 | 1 / 0 | — | 1 / 0 | 2 / 0 | 20 / 0 |

## Vetas de 175+ (Mithril y superiores) en estas zonas
| Zona | Dark Iron Deposit (230) | Truesilver Deposit (230) | Small Thorium Vein (245) | Rich Thorium Vein (275) |
|---|---|---|---|---|
| Desolace | — | 8 / 0 | — | — |
| Badlands | — | 109 / 0 | — | — |
| Swamp of Sorrows | — | 9 / 0 | 9 / 0 | — |
| Feralas | — | 8 / 0 | — | — |

## Puntos vistos en Forever (todas las coordenadas)
| Zona | Veta | Puntos | Coordenadas vistas en Forever (x, y) |
|---|---|---|---|
| Durotar | Copper Vein | 15 | 39.3, 61.0 · 40.0, 64.2 · 40.0, 66.4 · 40.4, 70.7 · 42.9, 63.0 · 43.0, 52.3 · 43.4, 58.2 · 44.7, 69.6 · 44.8, 55.0 · 45.2, 72.5 · 46.1, 61.7 · 46.2, 59.5 · 47.0, 67.1 · 47.6, 64.5 · 52.5, 59.3 |
| Hillsbrad Foothills | Tin Vein | 4 | 64.7, 11.5 · 65.1, 47.8 · 68.4, 37.6 · 70.4, 40.6 |
| Hillsbrad Foothills | Silver Vein | 3 | 57.0, 61.3 · 59.6, 13.5 · 64.1, 55.3 |
| Hillsbrad Foothills | Iron Deposit | 4 | 37.6, 25.9 · 44.0, 31.4 · 45.3, 27.1 · 46.3, 31.8 |
| Silverpine Forest | Copper Vein | 2 | 49.3, 13.4 · 54.0, 23.3 |
| Silverpine Forest | Tin Vein | 12 | 41.0, 15.8 · 55.3, 46.0 · 56.0, 50.4 · 56.6, 75.5 · 57.1, 71.0 · 57.7, 44.5 · 58.0, 79.1 · 59.1, 70.6 · 59.7, 40.2 · 61.7, 21.0 · 61.8, 71.1 · 66.2, 77.2 |
| Silverpine Forest | Silver Vein | 5 | 56.0, 50.3 · 58.3, 44.7 · 59.6, 40.2 · 59.6, 72.1 · 65.9, 61.4 |
| Stonetalon Mountains | Copper Vein | 3 | 45.5, 25.3 · 66.1, 89.8 · 68.2, 44.7 |
| Stonetalon Mountains | Tin Vein | 6 | 35.1, 17.3 · 40.2, 17.7 · 45.4, 25.1 · 57.4, 90.4 · 60.1, 91.8 · 72.6, 87.3 |
| Stonetalon Mountains | Silver Vein | 2 | 32.6, 62.1 · 35.4, 75.2 |
| Stonetalon Mountains | Iron Deposit | 3 | 35.4, 9.4 · 37.4, 69.8 · 38.8, 20.9 |
| The Barrens | Copper Vein | 11 | 41.9, 13.6 · 44.4, 83.0 · 44.9, 23.1 · 45.2, 51.2 · 46.7, 39.7 · 50.9, 57.7 · 53.5, 54.6 · 55.3, 27.2 · 55.7, 43.0 · 57.4, 25.6 · 58.9, 27.7 |
| The Barrens | Tin Vein | 19 | 37.1, 16.9 · 38.3, 11.8 · 40.0, 20.6 · 43.5, 13.6 · 44.0, 26.6 · 45.2, 22.7 · 46.4, 12.9 · 46.4, 39.9 · 47.1, 30.5 · 47.4, 68.7 · 47.9, 15.9 · 48.5, 49.5 · 50.5, 58.1 · 51.7, 48.3 · 55.4, 42.9 · 57.0, 25.5 · 57.8, 18.6 · 60.0, 3.9 · 62.1, 55.1 |
| The Barrens | Silver Vein | 8 | 40.0, 20.6 · 44.9, 25.1 · 46.1, 45.0 · 46.4, 12.9 · 48.6, 14.8 · 55.3, 42.1 · 57.0, 25.5 · 59.6, 3.7 |
| Thousand Needles | Silver Vein | 1 | 50.6, 46.5 |
| Tirisfal Glades | Copper Vein | 2 | 24.4, 60.6 · 28.7, 60.7 |

Puntos de Classic completos de una zona: `python3 -m tools.fdb_addon.query nodes "Copper Vein" --zone Durotar --points` (`--source classic` o `--source forever` para filtrar).

## Observado, inferido y externo
- Observado (Forever): solo los puntos en negrita y la tabla de coordenadas.
- Externo (Classic, CMaNGOS): el resto de conteos. Hipótesis hasta verlo en el juego.
- Inferido: "mejor zona" = más puntos en los datos; no tiene en cuenta la reaparición dinámica de Forever ni la competencia de jugadores.

## Qué dicen las guías
- [[Ores]] y [[Mining]] usan conteos de The Forever Era y de la guía de ForeverDB, también de CMaNGOS. **Las cifras no coinciden** con las de este addon (p. ej. Durotar Copper 156 en TFE / 162 en la guía de ForeverDB / 159 aquí; Stonetalon Iron 12 en TFE / 0 aquí; Thousand Needles Mithril 17 en TFE / ninguno aquí; Hillsbrad Tin 81 en TFE / 65 aquí). Misma raíz, distinto recuento: pendiente de registrar en [[Conflicts]].

## Fuentes
- [Data from ForeverDB.net](https://foreverdb.net)

| Fuente | Tipo | Fecha de los datos | Consultada | ¿Antes del parche 2026-11-02? |
|---|---|---|---|---|
| Addon ForeverDB 0.60.3, `Data/Meta.lua` versión 2026-11-13.ea2bb422, `Data/Gather.lua` | puntos de Classic (CMaNGOS classic-db, GPL-3.0) + puntos vistos por jugadores en Forever | 2026-11-13 | 2026-11-13 | No |

## Preguntas pendientes
- Densidad real en Forever de Ashenvale, Thousand Needles y Desolace (nadie ha registrado vetas allí todavía).
- ¿Existen las vetas Poor Copper de las que habla Warcraft Tavern? El addon no las tiene.
- ¿Dónde salen Pyrite, Bauxite y Pitchblende? No son tipos de veta en el addon (inferido: salen de vetas existentes).
