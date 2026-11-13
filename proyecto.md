# WOW FOREVER — KNOWLEDGE SYSTEM
## Especificación maestra de investigación, recopilación, organización y recuperación de conocimiento mediante IA + Obsidian

**Proyecto:** WoW Forever Knowledge Base & AI Game Assistant  
**Formato principal:** Markdown + Obsidian  
**Ingestión:** Python, scraping, APIs y extracción estructurada con LLM  
**Objetivo:** Construir una base de conocimiento exhaustiva, interconectada, verificable y actualizada de World of Warcraft Forever.

---

# 1. VISIÓN DEL PROYECTO

Construir una enciclopedia inteligente de WoW Forever que recopile, normalice, clasifique, relacione y mantenga actualizada la mayor cantidad posible de información relevante del juego.

La base de conocimiento debe permitir que una LLM responda preguntas complejas utilizando información documentada, fuentes verificables y datos específicos de WoW Forever.

No queremos simplemente descargar guías y almacenarlas en Obsidian.

Queremos desarrollar un sistema de inteligencia de juego capaz de:

- Conocer clases, especializaciones, talentos y habilidades.
- Conocer items, estadísticas, requisitos y fuentes de obtención.
- Conocer quests, cadenas, NPCs y ubicaciones.
- Conocer dungeons, raids, bosses, mecánicas y loot.
- Conocer profesiones, materiales, recetas y rutas de optimización.
- Conocer economía, farming, Auction House y generación de oro.
- Conocer zonas, mapas, rutas y puntos de interés.
- Conocer sistemas exclusivos de WoW Forever.
- Conocer addons y herramientas disponibles.
- Detectar cambios en hotfixes y actualizaciones.
- Identificar información contradictoria entre fuentes.
- Recomendar estrategias basadas en el estado real del personaje.
- Detectar información faltante y generar investigaciones automáticamente.

## 1.1 Filosofía fundamental

La información debe ser:

1. Exhaustiva: recopilar todo lo relevante que sea posible.
2. Estructurada: cada entidad debe tener un formato consistente.
3. Interconectada: los elementos deben relacionarse entre sí.
4. Verificable: cada dato importante debe tener procedencia.
5. Versionada: conservar el historial de cambios.
6. Específica: diferenciar WoW Forever de WoW Classic y otras versiones.
7. Consultable: optimizada para recuperación mediante LLM y RAG.
8. Mantenible: permitir actualizaciones incrementales.
9. Escalable: admitir nuevas fuentes y dominios.
10. Práctica: priorizar conocimiento que permita tomar mejores decisiones dentro del juego.

---

# 2. FUENTES DE INFORMACIÓN

Las fuentes deben registrarse individualmente, evaluarse y clasificarse.

No se debe asumir que dos sitios representan verificaciones independientes: algunos pueden compartir los mismos datos de origen.

## 2.1 Fuentes prioritarias

### 1. Azeroth DB

URL: https://azeroth-db.github.io/

Prioridad: CRÍTICA.

Investigar y extraer:

- Talent calculator.
- Legacy planner.
- Spellbook.
- Habilidades por nivel.
- Items.
- Estadísticas de objetos.
- Dungeon loot.
- Bosses.
- Quests.
- NPCs.
- Monstruos.
- Mapas.
- Zonas.
- Profesiones.
- Recetas.
- Materiales.
- Trainers.
- Addons.
- Herramientas de planificación.

Investigar especialmente sus estructuras de datos, APIs, archivos públicos y posibilidades de exportación.

### 2. WoW Forever Wiki

URL: https://wowfwiki.com/

Prioridad: CRÍTICA.

Investigar:

- Base de datos del juego.
- Items.
- Quests.
- NPCs.
- Enemigos.
- Zonas.
- Dungeons.
- Raids.
- Clases.
- Profesiones.
- Talentos.
- Cambios específicos del servidor.
- Referencias y fuentes de los datos.

Investigar su cobertura, formatos y métodos de extracción.

### 3. Forever Helper

URL: https://wowforeverhelper.com/

Prioridad: CRÍTICA.

Investigar:

- Datos del cliente.
- Items.
- Spells.
- Zonas.
- Dungeons.
- Raids.
- Profesiones.
- Diferencias respecto a Classic.
- Herramientas de consulta.

### 4. ForeverDB

URL: https://foreverdb.net/

Prioridad: ALTA.

Investigar:

- Rutas de leveling.
- Guías.
- Clases.
- Profesiones.
- Dungeons.
- Economía.
- Farming.
- Correcciones y cambios del servidor.

### 5. Eternadex

URL: https://eternadex.com/en/

Prioridad: ALTA.

Investigar:

- Item database.
- Gear planner.
- Best in Slot.
- Item stats.
- Loot sources.
- Quests.
- NPCs.
- Profesiones.
- Recetas.
- Materiales.
- Dungeon loot.

### 6. Wowhead Forever

URL: https://www.wowhead.com/forever/guides

Prioridad: ALTA.

Investigar:

- Class guides.
- Quest guides.
- Dungeon guides.
- Reputación.
- Armas.
- Objetos.
- Mecánicas.
- Experiencias de jugadores.

No limitarse a las guías principales: investigar contenido complementario y community guides.

### 7. WoW Forever Path

URL: https://www.wowforeverpath.com/guides/

Prioridad: ALTA.

Investigar:

- Atlas de regiones.
- Zonas.
- Quests.
- Coordenadas.
- Rutas.
- BiS.
- Census.
- Herramientas de profesiones.
- Planificación del personaje.

### 8. ForeverGuide

URL: https://foreverguide.app/guides

Prioridad: MEDIA-ALTA.

Investigar:

- Guías de clases.
- Builds.
- Especializaciones.
- Legacy.
- Leveling 1–60.
- Reglas del servidor.

### 9. The Forever Era

URL: https://theforeverera.com/en/guides/

Prioridad: MEDIA-ALTA.

Investigar:

- Guías de profesiones 1–300.
- Leveling.
- Rutas por zonas.
- Legacy.
- BiS.
- Sistemas particulares del servidor.

### 10. Mobalytics

URLs:

- https://mobalytics.gg/wow-forever/leveling-guides
- https://mobalytics.gg/wow-forever/community-guides

Prioridad: ALTA.

Investigar:

- Leveling.
- Builds.
- Clases.
- Profesiones.
- Guías de comunidad.
- Trucos.
- Estrategias.
- Experiencias de jugadores.

### 11. Method

URL: https://www.method.gg/wow-forever

Prioridad: ALTA.

Investigar:

- Guías de clases.
- Dungeons.
- Raids.
- Builds.
- Estrategias.
- Contenido endgame.

---

## 2.2 Fuentes oficiales

### Blizzard

Noticias:
https://worldofwarcraft.blizzard.com/en-us/news

Hotfixes:
https://worldofwarcraft.blizzard.com/en-us/news/24315281/wow-forever-hotfixes-november-6-2026

Roadmap:
https://worldofwarcraft.blizzard.com/en-us/news/24303862/world-of-warcraft-forever-whats-next

Prioridad: CRÍTICA.

Registrar:

- Patch notes.
- Hotfixes.
- Cambios de clases.
- Cambios de habilidades.
- Modificaciones de experiencia.
- Cambios de items.
- Cambios de quests.
- Cambios de dungeons.
- Modificaciones de economía.
- Cambios de profesiones.
- Sistemas nuevos.
- Correcciones de bugs.

Cada actualización debe generar un registro histórico.

No sobrescribir datos antiguos sin conservar la versión anterior.

---

## 2.3 Fuentes comunitarias adicionales

Investigar e incorporar cuando aporten información original:

- Reddit: https://www.reddit.com/
- Discord oficial y comunidades de WoW Forever.
- Foros oficiales.
- YouTube.
- Twitch.
- GitHub.
- Repositorios de addons.
- Bases de datos comunitarias.
- Publicaciones de jugadores experimentados.

Objetivo:

Obtener información que no necesariamente está documentada en las bases de datos:

- Rutas de farming eficientes.
- Trucos de leveling.
- Mecánicas poco conocidas.
- Secretos.
- Estrategias alternativas.
- Errores conocidos.
- Experiencias reales.
- Rentabilidad de profesiones.
- Comparaciones de builds.

Para cada aportación comunitaria, identificar si es experiencia personal, observación reproducible o afirmación sin verificar.

---

# 3. TAXONOMÍA COMPLETA DE CONOCIMIENTO

El conocimiento se dividirá en dominios independientes pero interconectados.

## 3.1 Classes & Builds

Documentar todas las clases y sus posibilidades.

Por cada clase:

- Descripción.
- Roles.
- Fortalezas.
- Debilidades.
- Habilidades.
- Talentos.
- Árboles de talentos.
- Builds de leveling.
- Builds PvE.
- Builds PvP.
- Builds endgame.
- Rotaciones.
- Prioridad de habilidades.
- Estadísticas prioritarias.
- Equipamiento recomendado.
- Consumibles.
- Enchants.
- Macros.
- Sinergias.
- Variaciones según nivel.
- Cambios específicos de Forever.

Clases:

- Warrior.
- Paladin.
- Hunter.
- Rogue.
- Priest.
- Shaman.
- Mage.
- Warlock.
- Druid.

## 3.2 Leveling & World

Documentar:

- Rutas 1–60.
- Rutas por facción.
- Rutas por raza.
- Rutas por clase.
- Zonas recomendadas.
- Rangos de nivel.
- XP necesaria.
- XP por enemigo.
- XP por quest.
- XP por dungeon.
- Tiempo estimado.
- Quests recomendadas.
- Quests que conviene evitar.
- Flight paths.
- Puntos de transporte.
- Vendedores.
- Trainers.
- Lugares de descanso.
- Rutas alternativas.

Cada ruta debe explicar:

1. Nivel inicial.
2. Nivel final.
3. Zona.
4. Orden de quests.
5. Enemigos relevantes.
6. Coordenadas.
7. Requisitos.
8. Tiempo estimado.
9. Experiencia esperada.
10. Equipo recomendado.
11. Alternativas.

## 3.3 Quests

Por cada quest:

- ID.
- Nombre.
- Descripción.
- NPC inicial.
- NPC final.
- Ubicación.
- Coordenadas.
- Nivel requerido.
- Nivel recomendado.
- Facción.
- Requisitos.
- Objetivos.
- Enemigos.
- Items necesarios.
- Rewards.
- XP.
- Oro.
- Reputación.
- Quest chains.
- Quests posteriores.
- Dificultad.
- Consejos.
- Cambios por versión.

## 3.4 Dungeons

Por cada dungeon:

- Nombre.
- Ubicación.
- Coordenadas.
- Nivel mínimo.
- Nivel recomendado.
- Nivel máximo.
- Facción.
- Número de jugadores.
- Entrada.
- Requisitos.
- Quests disponibles.
- Bosses.
- Enemigos.
- Mecánicas.
- Loot.
- Drops.
- Estrategias.
- Composición recomendada.
- Roles.
- Resistencias.
- Atajos.
- Rutas internas.
- Consejos para principiantes.
- Consejos de optimización.

Por cada boss:

- Nombre.
- Ubicación.
- Nivel.
- Habilidades.
- Mecánicas.
- Adds.
- Posicionamiento.
- Prioridades.
- Estrategia para tank.
- Estrategia para healer.
- Estrategia para DPS.
- Loot.
- Errores frecuentes.

## 3.5 Raids

Documentar:

- Raids disponibles.
- Requisitos de acceso.
- Tamaño de grupo.
- Bosses.
- Encuentros.
- Mecánicas.
- Fases.
- Roles.
- Composiciones.
- Resistencias.
- Preparación.
- Consumibles.
- Loot.
- BiS.
- Estrategias.
- Dificultad.
- Cambios específicos de Forever.

## 3.6 Items & Equipment

Por cada item:

- ID.
- Nombre.
- Tipo.
- Slot.
- Calidad.
- Nivel requerido.
- Item level.
- Estadísticas.
- Atributos.
- Efectos.
- Proc.
- Restricciones.
- Clases compatibles.
- Facciones.
- Profesión requerida.
- Fuente de obtención.
- Boss.
- Quest.
- Vendor.
- Drop rate, si está documentado.
- Precio.
- Alternativas.
- Mejoras posteriores.
- Builds compatibles.

Clasificación:

- Weapons.
- Armor.
- Shields.
- Wands.
- Trinkets.
- Rings.
- Necklaces.
- Cloaks.
- Consumables.
- Enchants.
- Quest items.
- Crafting materials.

## 3.7 Best in Slot & Gear Optimization

Documentar:

- BiS por clase.
- BiS por especialización.
- BiS por slot.
- BiS por etapa de progresión.
- Pre-raid BiS.
- Dungeon BiS.
- Raid BiS.
- Alternativas económicas.
- Equipamiento accesible.
- Mejoras marginales.
- Comparaciones de estadísticas.
- Requisitos de obtención.

No confundir BiS teórico con mejor opción práctica para un personaje determinado.

## 3.8 Professions

Documentar las diez profesiones principales:

- Alchemy.
- Blacksmithing.
- Enchanting.
- Engineering.
- Herbalism.
- Leatherworking.
- Mining.
- Skinning.
- Tailoring.
- Cooking.
- Fishing.

Para cada profesión:

- Descripción.
- Trainers.
- Ubicaciones.
- Requisitos.
- Recetas.
- Materiales.
- Costos.
- Rangos.
- Rutas de leveling.
- Productos.
- Utilidad por clase.
- Rentabilidad.
- Sinergias.
- Consejos.
- Cambios específicos de Forever.

Para cada receta:

- ID.
- Nombre.
- Profesión.
- Skill requerido.
- Trainer o fuente.
- Materiales.
- Cantidades.
- Resultado.
- Probabilidad de skill-up.
- Utilidad.
- Precio estimado.
- Alternativas.

## 3.9 Economy & Gold Making

Documentar:

- Auction House.
- Precios de materiales.
- Farming.
- Gold per hour.
- Recursos demandados.
- Items comerciables.
- Items vinculados.
- Consumibles.
- Fluctuaciones.
- Rutas rentables.
- Estrategias de compra.
- Estrategias de venta.
- Riesgos.
- Capital necesario.

Diferenciar siempre precios observados, estimaciones y datos históricos.

## 3.10 NPCs & Factions

Por cada NPC:

- ID.
- Nombre.
- Tipo.
- Zona.
- Coordenadas.
- Facción.
- Función.
- Quests.
- Productos.
- Servicios.
- Trainer.
- Reputación.
- Requisitos.
- Relaciones.

Categorías:

- Trainers.
- Vendors.
- Quest givers.
- Flight masters.
- Guards.
- Bosses.
- Rare NPCs.
- Faction leaders.

## 3.11 Game Mechanics

Documentar:

- Combat system.
- Threat.
- Aggro.
- Armor.
- Resistance.
- Critical strike.
- Hit rating.
- Spell power.
- Attack power.
- Weapon skill.
- Mana regeneration.
- Healing.
- Damage formulas.
- Stat scaling.
- Diminishing returns.
- Crowd control.
- Buffs.
- Debuffs.
- Proc mechanics.
- XP calculations.
- Loot mechanics.

Cada fórmula debe incluir su fuente, versión y nivel de confianza.

## 3.12 Legacy & Forever Systems

Este dominio debe ser independiente de las guías genéricas de Classic.

Investigar exhaustivamente:

- Legacy progression.
- Legacy points.
- Perks.
- Desafíos.
- Requisitos.
- Recompensas.
- Beneficios permanentes.
- Restricciones.
- Sistemas exclusivos.
- Interacciones con personajes.
- Estrategias de progresión.

## 3.13 Camping

Investigar:

- Sistema de camping.
- Beneficios.
- Mejoras.
- Objetos.
- Materiales.
- Requisitos.
- Ubicaciones.
- Estrategias.
- Interacciones con profesiones.
- Beneficios económicos.

## 3.14 Addons & Tools

Por cada addon:

- Nombre.
- Descripción.
- URL.
- Repositorio.
- Compatibilidad.
- Versión.
- Instalación.
- Configuración.
- Dependencias.
- Comandos.
- Limitaciones.
- Datos que puede exportar.

Investigar especialmente addons para:

- Inventory management.
- Quest tracking.
- Maps.
- Coordinates.
- Loot.
- Professions.
- Auction House.
- Character inspection.
- Talent tracking.
- Combat logging.
- Gathering routes.

## 3.15 Secrets & Community Knowledge

Documentar:

- Easter eggs.
- Secret quests.
- Rare spawns.
- Objetos ocultos.
- Rutas desconocidas.
- Trucos.
- Atajos.
- Estrategias poco conocidas.
- Experiencias de jugadores.
- Bugs conocidos.

Diferenciar información confirmada de rumores.

---

# 4. ARQUITECTURA DE OBSIDIAN

Estructura propuesta:

```text
wow-forever/
│
├── 00-Home/
│   ├── Dashboard.md
│   ├── Knowledge-Index.md
│   ├── Source-Registry.md
│   └── Game-Version.md
│
├── 01-Game-Systems/
│   ├── Classes/
│   ├── Talents/
│   ├── Legacy/
│   ├── Camping/
│   └── Combat-Mechanics/
│
├── 02-World/
│   ├── Continents/
│   ├── Zones/
│   ├── Flight-Paths/
│   ├── Maps/
│   └── Leveling-Routes/
│
├── 03-Quests/
│   ├── Quest-Database/
│   ├── Quest-Chains/
│   ├── Class-Quests/
│   └── Hidden-Quests/
│
├── 04-Dungeons/
│   ├── Dungeon-Index.md
│   ├── Bosses/
│   ├── Mechanics/
│   ├── Loot/
│   └── Strategies/
│
├── 05-Raids/
│   ├── Encounters/
│   ├── Bosses/
│   ├── Loot/
│   └── Compositions/
│
├── 06-Items/
│   ├── Weapons/
│   ├── Armor/
│   ├── Consumables/
│   ├── Enchants/
│   └── Item-Sources/
│
├── 07-Professions/
│   ├── Herbalism/
│   ├── Skinning/
│   ├── Mining/
│   ├── Alchemy/
│   ├── Blacksmithing/
│   ├── Cooking/
│   ├── Engineering/
│   ├── Enchanting/
│   ├── Fishing/
│   ├── Leatherworking/
│   └── Tailoring/
│
├── 08-Economy/
│   ├── Auction-House/
│   ├── Gold-Farming/
│   ├── Material-Prices/
│   └── Gold-Making-Strategies/
│
├── 09-NPCs/
│   ├── Trainers/
│   ├── Vendors/
│   ├── Quest-Givers/
│   └── Rare-NPCs/
│
├── 10-Addons/
│   ├── Addon-Registry.md
│   ├── Installation/
│   └── Configurations/
│
├── 11-Community-Knowledge/
│   ├── Tips/
│   ├── Secrets/
│   ├── Farming-Routes/
│   └── Player-Experiences/
│
├── 12-Character/
│   ├── Character-Profile.md
│   ├── Progression.md
│   ├── Equipment.md
│   ├── Talent-Build.md
│   ├── Inventory.md
│   ├── Professions.md
│   └── Goals.md
│
├── 13-Patches/
│   ├── Patch-History.md
│   ├── Hotfixes/
│   └── Deprecated-Information/
│
├── 14-Sources/
│   ├── Official/
│   ├── Databases/
│   ├── Guides/
│   └── Community/
│
└── 15-AI/
    ├── Retrieval-Index.md
    ├── Knowledge-Rules.md
    ├── Conflicts.md
    └── Research-Backlog.md
```

La estructura debe poder evolucionar sin romper los enlaces existentes.

---

# 5. MODELO DE DATOS Y METADATA

Todas las páginas deben utilizar identificadores estables y metadata consistente.

## 5.1 Campos generales

```yaml
---
id: unique-entity-id
type: item
name: Example Item
game: wow-forever
game_build: unknown
sources: []
source_urls: []
created_at: YYYY-MM-DD
observed_at: YYYY-MM-DD
verified_at: null
last_updated: YYYY-MM-DD
confidence: unknown
status: provisional
tags: []
---
```

Valores permitidos para `status`:

- verified
- provisional
- disputed
- deprecated
- unverified

Valores permitidos para `confidence`:

- high
- medium
- low
- unknown

No marcar automáticamente un dato como verificado solamente porque una LLM lo haya extraído.

## 5.2 Modelo de item

```yaml
---
id: item-unique-id
type: item
name: Item Name
item_type: weapon
slot: main_hand
quality: unknown
required_level: null
item_level: null
classes: []
stats: {}
effects: []
sources: []
game_build: unknown
confidence: unknown
status: provisional
---
```

## 5.3 Modelo de dungeon

```yaml
---
id: dungeon-unique-id
type: dungeon
name: Dungeon Name
faction: both
level_min: null
level_max: null
party_size: 5
zone: null
bosses: []
quests: []
loot: []
game_build: unknown
confidence: unknown
status: provisional
---
```

## 5.4 Modelo de quest

```yaml
---
id: quest-unique-id
type: quest
name: Quest Name
quest_level: null
required_level: null
faction: unknown
start_npc: null
end_npc: null
zone: null
prerequisites: []
follow_up_quests: []
rewards: []
experience: null
game_build: unknown
confidence: unknown
status: provisional
---
```

## 5.5 Modelo de profesión

```yaml
---
id: profession-unique-id
type: profession
name: Herbalism
skill_cap: 300
trainers: []
recipes: []
materials: []
leveling_guides: []
game_build: unknown
confidence: unknown
status: provisional
---
```

## 5.6 Modelo de fuente

```yaml
---
id: source-unique-id
type: source
name: Source Name
url: https://example.com
category: database
owner: unknown
authority: unknown
game_specificity: unknown
access_method: unknown
crawl_policy: unknown
last_checked: null
update_frequency: unknown
independence_group: unknown
status: active
---
```

Estos son esquemas iniciales. Deben ampliarse cuando la investigación confirme los campos y relaciones reales.

---

# 6. RELACIONES ENTRE ENTIDADES

La base no debe limitarse a documentos aislados.

Cada entidad debe relacionarse con otras entidades mediante Obsidian Wikilinks y referencias estructuradas.

Ejemplo:

```markdown
# Shadowfang Keep

## Información general

Dungeon de WoW Forever.

## Relaciones

- Zona: [[Silverpine Forest]]
- Bosses:
  - [[Baron Silverlaine]]
  - [[Commander Springvale]]
- Quests:
  - [[Shadowfang Keep Quest 1]]
- Loot:
  - [[Item Example 1]]
  - [[Item Example 2]]

## Clases relevantes

- [[Priest]]
- [[Warrior]]
- [[Rogue]]

## Estrategias

- [[Shadowfang Keep Beginner Strategy]]
- [[Shadowfang Keep Farming Strategy]]
```

Relaciones mínimas que deben soportarse:

- Class → Talent.
- Class → Spell.
- Class → Item.
- Item → Dungeon.
- Item → Boss.
- Item → Quest.
- Item → Profession.
- Dungeon → Boss.
- Dungeon → Quest.
- Dungeon → Zone.
- Quest → NPC.
- Quest → Zone.
- Quest → Item.
- NPC → Vendor.
- NPC → Trainer.
- Profession → Recipe.
- Recipe → Material.
- Material → Zone.
- Material → Creature.
- Zone → Quest.
- Zone → Dungeon.
- Zone → Gathering Route.
- Patch → Affected Entity.
- Build → Talent.
- Build → Item.
- Build → Rotation.

Las relaciones deben incluir procedencia y, cuando sea necesario, condiciones o restricciones.

---

# 7. PIPELINE DE INGESTIÓN

Implementar un pipeline modular en Python.

## 7.1 Arquitectura

```text
SOURCE DISCOVERY
       |
       v
SOURCE REGISTRY
       |
       v
CRAWLER / API CLIENTS
       |
       v
RAW DOCUMENT STORAGE
       |
       v
CONTENT EXTRACTION
       |
       v
ENTITY RECOGNITION
       |
       v
NORMALIZATION
       |
       v
ENTITY RESOLUTION
       |
       v
LLM STRUCTURED EXTRACTION
       |
       v
VALIDATION
       |
       v
CONFLICT DETECTION
       |
       v
OBSIDIAN MARKDOWN GENERATION
       |
       v
INDEXING / RAG
```

## 7.2 Ingestion adapters

Cada fuente debe tener un adapter independiente.

Ejemplos:

- AzerothDBAdapter.
- ForeverWikiAdapter.
- ForeverHelperAdapter.
- ForeverDBAdapter.
- EternadexAdapter.
- WowheadAdapter.
- MobalyticsAdapter.
- MethodAdapter.
- BlizzardAdapter.
- CommunityAdapter.

Cada adapter debe implementar:

- Discover.
- Fetch.
- Parse.
- Normalize.
- Validate.
- Export.

No utilizar un scraper universal para todas las fuentes.

## 7.3 Métodos de extracción

Prioridad:

1. APIs oficiales o públicas.
2. Archivos de datos estructurados.
3. JSON embebido en páginas.
4. HTML parsing.
5. Scraping tradicional.
6. Extracción mediante navegador.
7. LLM sobre contenido cuando sea necesario.

Evitar scraping innecesario cuando exista una fuente estructurada.

Respetar robots.txt, condiciones de uso, rate limits y restricciones de acceso.

No intentar evadir autenticación ni mecanismos de protección.

## 7.4 Almacenamiento RAW

Conservar el contenido original cuando las condiciones de la fuente lo permitan.

Estructura:

```text
data/
├── raw/
│   ├── blizzard/
│   ├── databases/
│   ├── guides/
│   └── community/
│
├── normalized/
│   ├── items/
│   ├── quests/
│   ├── npcs/
│   ├── dungeons/
│   └── professions/
│
├── exports/
│   └── obsidian/
│
└── logs/
```

Cada registro debe conservar:

- URL original.
- Fecha de captura.
- Hash de contenido.
- Fuente.
- Identificador.
- Versión.
- Estado de procesamiento.

---

# 8. NORMALIZACIÓN Y ENTITY RESOLUTION

Una misma entidad puede aparecer con nombres diferentes.

Ejemplo:

- Lesser Magic Wand.
- Lesser Magic Wand (Item).
- Item ID 11287.

El sistema debe identificar que se trata de la misma entidad cuando exista evidencia suficiente.

Utilizar:

- IDs nativos del juego.
- IDs de fuente.
- Normalización de nombres.
- Alias.
- Exact matching.
- Fuzzy matching.
- Jaro-Winkler.
- Token similarity.
- Context matching.
- Validación mediante atributos.

No fusionar entidades únicamente por similitud de nombre.

Mantener un registro de aliases y fusiones.

Cuando existan dudas, crear un conflicto pendiente de revisión.

---

# 9. LLM EXTRACTION

Utilizar LLM para convertir contenido no estructurado en registros consistentes.

Ejemplo de extracción de una guía de dungeon:

```json
{
  "entity_type": "dungeon",
  "name": "Shadowfang Keep",
  "bosses": [],
  "quests": [],
  "level_range": {
    "min": null,
    "max": null
  },
  "strategies": [],
  "loot": [],
  "source": "",
  "confidence": "unknown",
  "claims": []
}
```

Cada claim importante debe tener:

- Texto extraído.
- Fuente.
- URL.
- Fragmento de evidencia.
- Fecha.
- Entidad relacionada.
- Confianza.
- Estado de verificación.

La LLM no debe inventar valores ausentes.

Si no hay evidencia, usar null o unknown.

---

# 10. CONFLICT DETECTION

Cuando dos fuentes presentan información diferente:

1. Identificar la entidad.
2. Identificar el atributo conflictivo.
3. Recuperar las evidencias.
4. Comparar fechas.
5. Comparar builds.
6. Revisar autoridad de las fuentes.
7. Comprobar si existe un hotfix.
8. Determinar si son diferencias de contexto.
9. Registrar el conflicto.
10. Resolverlo o dejarlo pendiente.

Ejemplo:

```yaml
id: conflict-item-001
entity: item-example
attribute: required_level
claims:
  - value: 20
    source: source-a
    observed_at: 2026-11-01
  - value: 22
    source: source-b
    observed_at: 2026-11-12
status: unresolved
resolution: null
```

No resolver automáticamente todos los conflictos dando prioridad a la fecha más reciente: primero comprobar que las fuentes se refieren a la misma versión y contexto.

---

# 11. PATCH & HOTFIX MONITORING

Sistema de mantenimiento automático.

Monitorear:

- Noticias oficiales.
- Hotfixes.
- Actualizaciones.
- Cambios de balance.
- Cambios de habilidades.
- Cambios de XP.
- Cambios de loot.
- Cambios de quests.
- Cambios de profesiones.

Proceso:

```text
NEW PATCH DETECTED
        |
        v
EXTRACT CHANGES
        |
        v
IDENTIFY AFFECTED ENTITIES
        |
        v
SEARCH OBSIDIAN REFERENCES
        |
        v
MARK OUTDATED INFORMATION
        |
        v
GENERATE UPDATED VERSION
        |
        v
VALIDATE CLAIMS
        |
        v
UPDATE KNOWLEDGE BASE
        |
        v
SAVE CHANGE HISTORY
```

Nunca reemplazar silenciosamente información histórica.

Cada actualización debe tener un registro:

```yaml
id: patch-2026-example
type: patch
published_at: YYYY-MM-DD
source_url: ""
affected_entities: []
changes: []
previous_version: null
status: verified
```

---

# 12. CHARACTER INTELLIGENCE

El personaje debe tener un módulo independiente.

Perfil inicial del proyecto:

- Character: Undead Priest.
- Faction: Horde.
- Professions: Herbalism + Skinning.
- Objetivo: máxima eficiencia de leveling, oro y equipamiento.

El perfil debe actualizarse con información real del juego.

## 12.1 Character Profile

```yaml
---
id: character-main
type: character
name: Main Character
race: Undead
class: Priest
faction: Horde
level: 9
professions:
  - Herbalism
  - Skinning
gold: null
current_zone: unknown
current_build: unknown
current_gear: []
talents: []
goals:
  - efficient_leveling
  - gold_generation
  - gear_optimization
---
```

Los valores de nivel y demás campos deben sincronizarse con el estado real, no permanecer estáticos.

## 12.2 Datos a recopilar

- Level.
- XP.
- Gold.
- Inventory.
- Bank.
- Equipment.
- Stats.
- Talents.
- Spells.
- Professions.
- Profession skills.
- Quests.
- Reputation.
- Current zone.
- Current coordinates.
- Playtime.
- Death count.
- Farming history.

## 12.3 Recomendaciones contextuales

La LLM debe responder considerando:

- Nivel actual.
- Clase.
- Talentos.
- Equipo.
- Inventario.
- Profesiones.
- Oro.
- Ubicación.
- Objetivos.
- Disponibilidad de quests.
- Contenido accesible.

Ejemplo:

Pregunta: ¿Qué debería hacer ahora?

La LLM debe evaluar:

1. Qué nivel tiene el personaje.
2. Qué equipo tiene.
3. Qué upgrades están disponibles.
4. Qué quests convienen.
5. Qué rutas están cerca.
6. Qué materiales puede recolectar.
7. Qué dungeons son apropiadas.
8. Qué actividad produce mejor progreso.

---

# 13. FARMING & ECONOMY INTELLIGENCE

Especial atención a Herbalism y Skinning.

Para cada ruta:

- Zona.
- Coordenadas.
- Materiales.
- Enemigos.
- Nivel requerido.
- Skill requerido.
- Tiempo.
- Rendimiento.
- Competencia.
- Riesgos.
- Oro estimado.
- Alternativas.

Registrar observaciones reales del personaje.

Ejemplo:

```yaml
id: route-herbalism-example
type: gathering_route
profession: Herbalism
zone: unknown
required_skill: null
materials: []
estimated_duration_minutes: null
gold_per_hour: null
observed_at: null
evidence: []
confidence: unknown
status: provisional
```

No presentar estimaciones como resultados reales.

Crear comparativas:

- Mejor ruta por nivel.
- Mejor ruta por skill.
- Mejor material para vender.
- Mejor actividad por hora.
- Mejor combinación de profesiones.
- Materiales que conviene guardar.
- Materiales que conviene vender.

---

# 14. ADDON INTELLIGENCE

Investigar addons compatibles con WoW Forever.

Priorizar:

- Questie o alternativas compatibles.
- Atlas.
- Mapas.
- Coordenadas.
- GatherMate y alternativas.
- Inventory management.
- Auction House.
- Profession tracking.
- Loot tracking.
- Character inspection.
- Combat logging.
- Talent tracking.

No asumir compatibilidad por ser un addon de Classic.

Verificar:

- Versión de interfaz.
- Dependencias.
- Compatibilidad con Forever.
- Funcionalidad real.
- Método de instalación.
- Restricciones del servidor.

Investigar especialmente mecanismos de exportación de datos del personaje para alimentar Character Intelligence.

---

# 15. RAG & AI RETRIEVAL

La base debe ser consultable mediante recuperación híbrida.

No depender exclusivamente de embeddings.

## 15.1 Estrategia

Combinar:

- Full-text search.
- BM25.
- Semantic search.
- Metadata filtering.
- Entity lookup.
- Graph traversal.
- Exact ID matching.

## 15.2 Retrieval pipeline

```text
USER QUESTION
      |
      v
INTENT CLASSIFICATION
      |
      v
ENTITY EXTRACTION
      |
      v
METADATA FILTERING
      |
      v
HYBRID SEARCH
      |
      v
GRAPH RELATIONSHIPS
      |
      v
RERANKING
      |
      v
EVIDENCE COLLECTION
      |
      v
LLM RESPONSE
```

## 15.3 Tipos de preguntas

El sistema debe reconocer:

- Fact lookup.
- Recommendations.
- Comparisons.
- Planning.
- Optimization.
- Troubleshooting.
- Farming.
- Leveling.
- Dungeon preparation.
- Gear upgrades.
- Profession progression.
- Economy analysis.

## 15.4 Respuestas fundamentadas

Cada respuesta debe:

1. Identificar la pregunta.
2. Recuperar entidades relevantes.
3. Consultar las fuentes.
4. Comprobar versión.
5. Identificar contradicciones.
6. Construir una recomendación.
7. Explicar por qué.
8. Citar documentos y fuentes.
9. Indicar incertidumbre.

Si la información no existe, la LLM debe reconocerlo.

No inventar datos para completar respuestas.

---

# 16. KNOWLEDGE QUALITY CONTROL

Crear pruebas automáticas para detectar:

- Páginas sin fuente.
- IDs duplicados.
- Entidades duplicadas.
- Wikilinks rotos.
- Relaciones inválidas.
- Metadata incompleta.
- Datos obsoletos.
- Conflictos sin resolver.
- Entidades sin categoría.
- Documentos sin fecha.
- Información sin versión.
- Registros con campos inconsistentes.

Indicadores del sistema:

- Total de fuentes.
- Total de documentos.
- Total de entidades.
- Total de items.
- Total de quests.
- Total de NPCs.
- Total de dungeons.
- Total de bosses.
- Total de recetas.
- Total de materiales.
- Porcentaje de entidades verificadas.
- Cobertura por dominio.
- Cobertura por versión.
- Conflictos pendientes.
- Documentos obsoletos.

Crear un dashboard en Obsidian.

---

# 17. RESEARCH BACKLOG

El sistema debe mantener una lista de información faltante.

Ejemplos:

- Dungeon sin estrategia documentada.
- Boss sin loot completo.
- Item sin fuente conocida.
- Profesión sin ruta de leveling.
- Zona sin coordenadas.
- Quest sin cadena completa.
- Build sin validación.
- Hotfix sin analizar.

Cada tarea debe incluir:

- Dominio.
- Entidad.
- Información faltante.
- Prioridad.
- Fuentes potenciales.
- Estado.
- Fecha de creación.
- Fecha de resolución.

La LLM debe poder generar investigaciones a partir de huecos detectados.

---

# 18. PLAN DE IMPLEMENTACIÓN

Implementar progresivamente.

## Fase 1 — Research & Source Discovery

Objetivo: conocer todas las fuentes disponibles.

Tareas:

1. Investigar las fuentes enumeradas.
2. Descubrir nuevas fuentes.
3. Verificar URLs y disponibilidad.
4. Identificar APIs.
5. Identificar estructuras de datos.
6. Identificar posibilidades de extracción.
7. Evaluar calidad.
8. Evaluar especificidad de Forever.
9. Registrar licencias y restricciones.
10. Crear Source Registry.

Entregable: inventario de fuentes documentado.

## Fase 2 — Architecture & Schemas

Objetivo: definir la estructura de conocimiento.

Tareas:

1. Diseñar taxonomía.
2. Definir metadata.
3. Definir IDs.
4. Definir relaciones.
5. Diseñar estructura de Obsidian.
6. Crear plantillas.
7. Definir reglas de validación.
8. Definir versionado.

Entregable: arquitectura aprobada.

## Fase 3 — Data Acquisition

Objetivo: recopilar información de manera automatizada.

Tareas:

1. Crear adapters.
2. Implementar crawlers.
3. Integrar APIs.
4. Extraer JSON.
5. Procesar HTML.
6. Guardar RAW.
7. Registrar fuentes.
8. Implementar procesamiento incremental.

Entregable: pipeline de ingestión.

## Fase 4 — Normalization & Entity Resolution

Objetivo: unificar entidades.

Tareas:

1. Normalizar nombres.
2. Identificar IDs.
3. Resolver aliases.
4. Detectar duplicados.
5. Identificar relaciones.
6. Detectar conflictos.
7. Crear registros normalizados.

Entregable: base de entidades consistente.

## Fase 5 — Obsidian Generation

Objetivo: producir documentación navegable.

Tareas:

1. Generar Markdown.
2. Crear Wikilinks.
3. Crear índices.
4. Crear MOCs.
5. Crear dashboards.
6. Añadir metadata.
7. Verificar enlaces.
8. Generar documentación por dominio.

Entregable: vault navegable.

## Fase 6 — Character Intelligence

Objetivo: incorporar el personaje real.

Tareas:

1. Investigar addons.
2. Investigar exportaciones.
3. Capturar equipo.
4. Capturar inventario.
5. Capturar talentos.
6. Capturar profesiones.
7. Capturar quests.
8. Actualizar perfil.
9. Implementar recomendaciones contextuales.

Entregable: Character Intelligence.

## Fase 7 — RAG & AI Assistant

Objetivo: consultar la base con precisión.

Tareas:

1. Indexación.
2. Full-text.
3. BM25.
4. Embeddings.
5. Metadata filtering.
6. Graph traversal.
7. Reranking.
8. Citations.
9. Evaluación de respuestas.
10. Tests de recuperación.

Entregable: WoW AI Assistant.

## Fase 8 — Autonomous Maintenance

Objetivo: mantener el conocimiento actualizado.

Tareas:

1. Monitorizar fuentes.
2. Detectar cambios.
3. Procesar hotfixes.
4. Identificar documentos afectados.
5. Detectar información obsoleta.
6. Actualizar registros.
7. Mantener historial.
8. Generar research backlog.

Entregable: Knowledge Maintenance Engine.

---

# 19. REGLAS PARA CLAUDE CODE

Actuar como arquitecto de software, ingeniero de datos y especialista en sistemas de recuperación de conocimiento.

Reglas obligatorias:

1. No comenzar implementando todo sin investigar las fuentes.
2. No asumir que una fuente existe o funciona sin verificarla.
3. No inventar URLs.
4. No asumir compatibilidad con WoW Forever.
5. No confundir WoW Classic con WoW Forever.
6. No fusionar entidades sin evidencia.
7. No eliminar información histórica.
8. No sobrescribir datos verificados sin conservar versiones.
9. No marcar información como verificada sin evidencia.
10. No crear documentos duplicados innecesariamente.
11. Mantener IDs estables.
12. Utilizar metadata consistente.
13. Crear pruebas automáticas.
14. Documentar decisiones arquitectónicas.
15. Mantener adapters independientes.
16. Respetar las políticas de extracción de cada fuente.
17. Optimizar para recuperación mediante LLM.
18. Mantener la estructura escalable.
19. Registrar errores.
20. Priorizar la precisión sobre la cantidad.

## 19.1 Principio de ejecución

Trabajar por fases.

Al terminar cada fase:

- Mostrar resultados.
- Mostrar cobertura.
- Mostrar errores.
- Mostrar información faltante.
- Presentar decisiones pendientes.
- Esperar aprobación cuando la decisión afecte la arquitectura.

No declarar una fase completada sin pruebas.

---

# 20. DEFINICIÓN DE ÉXITO

El proyecto estará bien implementado cuando:

- Las principales fuentes estén registradas.
- Exista un pipeline reproducible.
- Los datos estén normalizados.
- Las entidades estén relacionadas.
- Obsidian sea navegable.
- Las fuentes puedan verificarse.
- Los cambios del juego puedan rastrearse.
- Los conflictos puedan detectarse.
- El personaje tenga datos propios.
- La LLM pueda responder preguntas complejas.
- Las respuestas incluyan referencias.
- La información obsoleta pueda identificarse.
- El sistema pueda crecer sin rediseñarse por completo.

## Resultado final esperado

Una base de conocimiento de WoW Forever que funcione como una enciclopedia, un buscador semántico, un planificador de personaje, un optimizador de equipo, un experto en profesiones y un asistente de juego.

**La meta no es almacenar la mayor cantidad de archivos posible. La meta es conseguir la mayor cantidad de conocimiento útil, estructurado, relacionado y verificable para tomar las mejores decisiones dentro de WoW Forever.**

---

# 21. PRIMERA TAREA PARA CLAUDE CODE

Antes de implementar cualquier sistema, ejecutar una investigación exhaustiva de las fuentes.

Entregar:

1. Inventario de todas las fuentes conocidas.
2. Nuevas fuentes descubiertas.
3. URLs verificadas.
4. Clasificación por dominio.
5. Métodos de acceso.
6. APIs disponibles.
7. Posibilidades de extracción.
8. Calidad y cobertura.
9. Nivel de especificidad respecto a WoW Forever.
10. Restricciones de uso.
11. Fuentes redundantes.
12. Fuentes prioritarias.
13. Información faltante.
14. Propuesta de arquitectura final.

No comenzar todavía con un scraping masivo.

Primero entender el ecosistema de información de WoW Forever y diseñar la mejor estrategia de adquisición.

**Prioridad absoluta: calidad, exhaustividad, relaciones, trazabilidad y utilidad para la LLM.**

## Fuentes
- [Data from ForeverDB.net](https://foreverdb.net)
