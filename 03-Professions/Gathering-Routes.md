---
type: topic
tags: [forever, professions, routes, gathering]
level_min: 9
level_max: 30
faction: horde
status: unknown
confidence: low
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://www.method.gg/wow-forever/herbalism-in-wow-forever-leveling-guide-herbalism-items-enchants-trainers
  - https://www.method.gg/wow-forever/skinning-in-wow-forever-leveling-guide-skinning-items-enchants-trainers
  - https://www.method.gg/wow-forever/camping-in-wow-forever-how-it-all-works-all-profession-buffs
  - https://www.method.gg/wow-forever/first-aid-in-wow-forever-1-300-leveling-guide-and-trainers
  - https://www.method.gg/wow-forever/wow-forever-cooking-profession-leveling-guide-items-and-trainers
  - https://www.method.gg/wow-forever/fishing-in-wow-forever-leveling-guide-fishing-items-trainers
  - https://www.wow-professions.com/forever/herbalism-leveling-guide
  - https://www.wow-professions.com/forever/herbalism-trainers
  - https://www.wow-professions.com/forever/skinning-leveling-guide
  - https://www.wow-professions.com/forever/skinning-trainers
  - https://www.warcrafttavern.com/forever/guides/herbalism/
  - https://kami-labs.fr/en/guide-depecage-wow-forever/
  - https://www.gfinityesports.com/article/world-of-warcraft-forever-herbalism-guide-1-300-leveling-herb-map
  - https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-%E2%80%93-updated-november-2/2360696/9
related: ["[[Herbalism]]", "[[Herbs]]", "[[Skinning]]", "[[Camping]]", "[[First-Aid]]", "[[Cooking]]", "[[Fishing]]"]
---

# Gathering Routes (Undead, Herbalism + Skinning)

> [!question] Sin evidencia suficiente
> **Propuestas sin validar.** Combinan datos de guías con razonamiento propio. Ninguna guía describe una ruta Undead que combine quests, hierbas y desuelle. Probar en juego y anotar plan frente a resultado (§8.6 de wow.md). No hay coordenadas de nodos ni precios.

## Resumen
- Idea: subir zona a zona con las quests (Tirisfal → Silverpine → Hillsbrad), recoger hierbas del camino y desollar todo lo que ya matas; la fórmula de Skinning sigue al nivel de los mobs.
- En Brill/Tirisfal están juntos (Method): campamento (*The Great Outdoors*, Eleanor Shackleton 57.23 55.46), Cooking (William Pickman 61.8 51.6), First Aid (Nurse Neela 61.82 52.83) y Fishing (Clyde Kellen, Brightwater Lake 67.2 51.0). Una sola parada para aprender las secundarias.
- Hitos a skill 20: Incense Candle (Herbalism) y Camp Chair (Skinning). A 50: Journeyman en Brill (Faruza, Rand Rhobart).
- Method propone otra ruta Horde: Herbalism por Mulgore → Barrens → Hillsbrad, y Skinning por Durotar → Barrens → Thousand Needles. Para un Undead implica viajar a Kalimdor; la ruta por Silverpine evita el viaje pero no la cubre ninguna guía de Skinning.
- Peacebloom tiene ahora uso propio para ti si aprendes First Aid (Minor Healing Potion, 45–75) ([[First-Aid]]).

## Supuestos
- Skill de Skinning según nivel del mob: 1 para 1–10, (nivel−10)×10 para 11–19, nivel×5 desde 20 ([[Skinning]]; `probable_classic`).
- Hierbas por zona: Tirisfal (Peacebloom, Silverleaf, Earthroot), Silverpine (Earthroot, Mageroyal, Briarthorn, Stranglekelp), Hillsbrad (Bruiseweed, Wild Steelbloom, Kingsblood, Liferoot) ([[Herbs]]; `confirmed_forever` según guías).
- Respawn acelerado en zonas bajas desde el 2026-11-02, temporal (oficial). No consta si afecta a nodos.
- Si Forever movió nodos (8 marcados "Changed" por Kami-Labs), las rutas pueden fallar. `unknown`.

## Rutas por tramo (propuestas)
| Tramo | Nivel pj | Zona | Hierbas objetivo | Skinning (skill que piden los mobs) | Entrenadores cercanos | Estado |
|---|---|---|---|---|---|---|
| A | 9–12 | Tirisfal | Peacebloom, Silverleaf, Earthroot | 1 | Death Knell (Junior), Brill (Faruza, Rand Rhobart, Cooking, First Aid, Fishing) | Propuesta |
| B | 12–20 | Silverpine | Earthroot, Mageroyal, Briarthorn, Stranglekelp | ~20–80 (mobs 12–18) | Brill / Undercity | Propuesta |
| B' (Method) | 10–20 | The Barrens | Mageroyal, Briarthorn, Stranglekelp | Plainstriders, Raptors, Hyenas… (75–175) | Dranh (Camp Taurajo, Expert Skinning) | Ruta de guía, no adaptada a Undead |
| C | 20–30 | Hillsbrad (alt. Barrens/Stonetalon) | Bruiseweed, Wild Steelbloom, Kingsblood, Liferoot | ~100–150; yetis de Foothill Caverns para 150–225 | Tarren Mill (herb), Undercity | Propuesta |
| D | 30+ | STV, Arathi, Thousand Needles | Fadeleaf, Goldthorn, Khadgar's Whisker | 150–225 | Grom'gol (herb) | Esbozo |

### Tramo A: Tirisfal (nivel ~9–12)
- Termina las quests recogiendo cada Peacebloom, Silverleaf y Earthroot (laderas). Desuella todas las bestias.
- Si no lo hiciste: *The Great Outdoors* (desde nivel ~5) para desbloquear el campamento; Cooking en Brill para la hoguera básica (Simple Wood + Flint And Tinder) ([[Camping]]).
- Skill 20: Incense Candle y Camp Chair. Skill 50: Journeyman en Brill; si pide nivel 10, vuelve al llegar.
- Guarda Scarce y semillas ([[Herb-Seeds]]).
- Validar: ¿Earthroot y nodos Wilted/Stunted en Tirisfal? ¿Skill por hora?

### Tramo B: Silverpine (nivel ~12–20)
- Quests desde The Sepulcher (hub `probable_classic`). Mageroyal (50), Briarthorn (70), Earthroot, Stranglekelp (85) en la costa.
- Bestias 12–18 piden 20–80 de skill.
- Circuito corto en la parte baja de Silverpine para hierbas (wow-professions, beta).
- Validar: ¿mobs por encima de tu skill? ¿Respawn de nodos rápido?

### Tramo C: Hillsbrad desde Tarren Mill (nivel ~20–30)
- Expert de Herbalism (125 o 150, ver [[Herbalism]]); Expert de Skinning a 125 (Killian Hagey, Rand Rhobart o Dranh).
- Bruiseweed, Wild Steelbloom, Kingsblood (125), Liferoot (150). Method también usa Hillsbrad para 115–170.
- Al final: yetis de Foothill Caverns (30–32) para Skinning 150–225 (wow-professions).

### Tramo D: más allá de 30
- Herbalism 170–205 en STV; Skinning 175–225 en Thousand Needles (Method). Por encima, datos especulativos.

## Registro de resultados en juego
| Fecha | Tramo | Tiempo | Skill herb inicial/final | Skill skin inicial/final | Hierbas/cueros | Scarce/semillas | Observaciones |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## Qué dicen las guías
- [[src-method-herbalism-in-wow-forever-leveling-guide-herbalism-items-enchants-trainers]] y [[src-method-skinning-in-wow-forever-leveling-guide-skinning-items-enchants-trainers]]: rutas Horde por Kalimdor (Mulgore/Durotar/Barrens); Hillsbrad para hierbas 115–170.
- wow-professions (beta): Silverpine 70–115 para hierbas; raptor camp de Barrens y yetis de Hillsbrad para Skinning.
- Entrenadores secundarios de Tirisfal: [[src-method-camping-in-wow-forever-how-it-all-works-all-profession-buffs]], [[src-method-first-aid-in-wow-forever-1-300-leveling-guide-and-trainers]], [[src-method-wow-forever-cooking-profession-leveling-guide-items-and-trainers]], [[src-method-fishing-in-wow-forever-leveling-guide-fishing-items-trainers]].

## Fuentes
| URL | Tipo | Fecha de la página | Consultada | ¿Antes del parche 2026-11-02? |
|---|---|---|---|---|
| method.gg …/herbalism-in-wow-forever-… | guide | 2026-11-05 | 2026-11-13 | No |
| method.gg …/skinning-in-wow-forever-… | guide | 2026-11-06 | 2026-11-13 | No |
| method.gg …/camping-in-wow-forever-… | guide | 2026-10-07 | 2026-11-13 | Sí |
| method.gg …/first-aid-in-wow-forever-… | guide | 2026-11-12 | 2026-11-13 | No |
| method.gg …/wow-forever-cooking-profession-… | guide | 2026-11-12 | 2026-11-13 | No |
| method.gg …/fishing-in-wow-forever-… | guide | 2026-11-03 | 2026-11-13 | No |
| wow-professions.com (herbalism/skinning leveling y trainers) | guide | sin fecha (beta) | 2026-11-10 | Probablemente sí |
| warcrafttavern.com/forever/guides/herbalism/ | guide | sin fecha | 2026-11-10 | Desconocido |
| kami-labs.fr/en/guide-depecage-wow-forever/ | database/guide | sin fecha | 2026-11-10 | Probablemente sí |
| gfinityesports.com …herb-map | guide | 2026-10-21 | 2026-11-10 | Sí |
| us.forums.blizzard.com …development-notes (2 nov) | official | 2026-11-03 | 2026-11-10 | Es el parche |

## Preguntas pendientes
- Nivel real y skill actual de las dos profesiones (falta export en `data/inbox/`).
- ¿Quests de Silverpine o Hillsbrad que pidan hierbas o cuero?
- Tiempo y skill por hora reales; competencia por nodos.
- ¿Sigue activo el respawn acelerado?
- ¿Compensa viajar a The Barrens (ruta Method) frente a Silverpine?
- Huecos de bolsa disponibles; las semillas van en bolsa de hierbas (ranura Reagent).
