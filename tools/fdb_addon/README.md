# tools/fdb_addon

Convierte los archivos `Data/*.lua` del addon **ForeverDB** (y de **ForeverDB Helper**) en una base SQLite local para consultarla desde la bóveda. Solo biblioteca estándar de Python (3.9+).

> **Crédito obligatorio:** Data from ForeverDB.net (https://foreverdb.net)
>
> En las notas de Obsidian: `[Data from ForeverDB.net](https://foreverdb.net)` en `## Fuentes`.

## Licencia de los datos

- El addon y sus datos se distribuyen con **GPL-3.0 más una cláusula de atribución** (sección 7(b)): se pueden reutilizar si se conservan los avisos y se acredita a ForeverDB.net donde se listen las fuentes. Ver `NOTICE.txt` y `LICENSE.txt` del addon.
- Lo etiquetado como Classic deriva de **CMaNGOS classic-db** (GPL-3.0). Es Classic 1.12: en Forever solo sirve como hipótesis.
- Los nombres y números del cliente son de Blizzard Entertainment.
- `data/` no se sube a git: la base y el addon extraído se quedan en local.

## Uso

```bash
# 1. El addon ya extraído en data/foreverdb/addon_zip/extracted/{ForeverDB,ForeverDB_Helper}/
python3 -m tools.fdb_addon.build            # -> data/foreverdb/addon.sqlite (≈2 s)

# 2. Consultas
python3 -m tools.fdb_addon.query quest "Cutting Teeth"
python3 -m tools.fdb_addon.query nodes "Copper Vein" --zone Durotar --points [--source forever]
python3 -m tools.fdb_addon.query recipe engineering --max-skill 150
python3 -m tools.fdb_addon.query npc "Gornek"
python3 -m tools.fdb_addon.query zone-quests "The Barrens" --side h --min-level 10 --max-level 20 [--confirmed]
python3 -m tools.fdb_addon.query item "Rough Boomstick"
python3 -m tools.fdb_addon.query rares Durotar
python3 -m tools.fdb_addon.query meta        # versión de datos (Data/Meta.lua) y recuentos
```

## Origen de cada dato

| Valor | Significado |
|---|---|
| `forever` | Visto por jugadores de ForeverDB en WoW Forever (capturas del addon) |
| `client` | Tablas del cliente de Forever (títulos, niveles, colores de receta) |
| `classic` | CMaNGOS classic-db: Classic 1.12, puede no coincidir con Forever |
| `curve_estimate` | XP de misión estimada por la curva de nivel del addon (no capturada) |

## Tablas

| Tabla | Origen | Notas |
|---|---|---|
| `quests` | QuestForever, QuestClassic, QuestGuide, QuestXP, Quests, QuestOffers | `confirmed_forever`=1 si jugadores la vieron, es nueva o tiene XP capturada; `xp_src`, `money_src`, `reward_src`, `giver_spot_src` |
| `quest_rewards` | QuestGuide | `kind` get/choose; `class` = recompensas por clase vistas en Forever |
| `gather_kinds`, `gather_zones`, `gather_nodes` | Gather | `source` classic/forever; coordenadas en % del mapa |
| `recipes`, `recipe_reagents` | Recipes | skill, amarillo/verde/gris, aprendizaje (`a` automática, `t` instructor, `i<id>` objeto), nueva/cambiada en Forever |
| `prof_ranks`, `prof_route`, `prof_best_zones` | Helper Professions | rangos, ruta de subida por facción, mejores zonas de recolección |
| `npcs`, `trainers`, `vendor_items` | NPCs, Helper Professions, Supplies, QuestForever, QuestClassic | `seen_forever` |
| `items` | SearchNames, Items, Gear, Helper Items | stats, dps, nivel requerido, nuevo/cambiado en Forever |
| `rares` | Rares | lugares de Classic y vistos en Forever, botín |
| `loot`, `dungeons` | Loot, Dungeons | % medido en Forever o de Classic |
| `level_routes`, `level_route_zones` | LevelRoutes | tiempo por nivel y XP/hora por zona de jugadores de ForeverDB |
| `consumables`, `supplies`, `special_quest_steps` | Consumables, Supplies, SpecialQuests | |

## Seguridad

El parser (`lua_table.py`) solo reconoce literales de datos (tablas, cadenas, números, booleanos). Nunca ejecuta Lua y trata el contenido como datos.

## Pruebas

`python3 -m unittest discover -s tests -t .` (fixtures inline en `tests/fdb_addon/`, sin los archivos reales).
