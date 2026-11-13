# WoW Companion — Especificación funcional y técnica
**Versión:** 0.1  
**Estado:** Documento base para implementación; addons y compatibilidad pendientes de validación  
**Juego:** WoW Forever  
**Personaje inicial:** Undead Priest, nivel 9  
**Profesiones:** Herbalism + Skinning  
**Stack:** Claude Code + Obsidian + Python + SQLite

---

## 1. Visión y objetivo

Construir un **WoW Companion personal** que convierta el estado real del personaje y el conocimiento investigado de WoW Forever en recomendaciones concretas, verificables y contextualizadas.

No debe ser únicamente una guía de leveling ni un repositorio de información. Debe ayudar a optimizar simultáneamente:

1. Progresión: experiencia, misiones, zonas, equipo, talentos y hechizos.
2. Economía: oro, compras, ventas, materiales, Auction House y ahorro para objetivos futuros.
3. Profesiones: rutas, nodos, materiales, niveles de habilidad y oportunidades de mercado.
4. Eficiencia: XP/h, oro/h, desplazamientos, uso de maná, espacio de bolsas y coste de oportunidad.
5. Conocimiento del servidor: separar mecánicas confirmadas de WoW Forever de datos heredados de WoW Classic u otros servidores.

Preguntas que debe poder responder:
- ¿Qué debería hacer ahora mismo y por qué?
- ¿Qué misión conviene completar primero?
- ¿Qué ruta combina misiones, hierbas y bestias para skinning?
- ¿Este objeto lo equipo, vendo, guardo o envío al banco?
- ¿Qué materiales debo conservar y cuáles conviene vender?
- ¿Me conviene comprar esta varita o esperar?
- ¿Qué mejora de equipo ofrece más valor por oro?
- ¿Cómo estoy progresando respecto a sesiones anteriores?

Toda recomendación debe explicar **acción, motivo, datos utilizados, vigencia, confianza y dudas**.

## 2. Principios no negociables

### 2.1 Datos reales primero
No asumir nivel, inventario, oro, equipo, misiones, precios, coordenadas ni disponibilidad. Consultar la última captura válida. Si falta un dato, decirlo.

### 2.2 WoW Forever es la autoridad
No asumir que una guía de Classic, Vanilla, Turtle WoW u otro servidor aplica. Clasificar cada mecánica como:
- `confirmed_forever`: confirmada específicamente en WoW Forever.
- `probable_classic`: compatible con Classic, pero pendiente de confirmar.
- `unknown`: sin evidencia suficiente.
- `conflicting`: fuentes contradictorias.

### 2.3 Trazabilidad
Toda afirmación específica debe tener fuente, fecha de verificación, versión/build si existe y confianza. No inventar URLs, precios, drop rates, NPCs, coordenadas ni requisitos.

### 2.4 Seguridad y cumplimiento
Usar APIs permitidas del juego, addons y archivos SavedVariables. No leer ni modificar memoria del proceso, inyectar código, automatizar acciones del cliente, enviar paquetes ni eludir protecciones. El Companion recomienda; el jugador decide y ejecuta.

### 2.5 No destruir valor
Ante incertidumbre, recomendar conservar antes que vender/destruir. No vender objetos raros, de misión, únicos, recetas, materiales difíciles de recuperar o equipo potencialmente útil sin comprobarlos.

### 2.6 Modularidad
Separar captura, normalización, almacenamiento, conocimiento, motor de decisiones y presentación. Wowdee y Dossier deben ser adaptadores sustituibles, no dependencias inseparables.

### 2.7 Evidencia antes de automatizar
Primero probar addons y observar sus archivos reales. Después diseñar parsers. No inventar esquemas de SavedVariables.

## 3. Perfil y objetivos iniciales

| Campo | Valor conocido |
|---|---|
| Raza | Undead |
| Clase | Priest |
| Nivel | 9, comunicado por el usuario; confirmar en captura |
| Profesiones | Herbalism + Skinning |
| Servidor | WoW Forever |
| Objetivo | Optimizar leveling, oro, equipo y profesiones a la vez |

Aún no conocemos nombre del personaje, reino, oro, inventario, equipo, misiones activas, skill de profesiones ni ubicación. No inventar esos valores.

El sistema no debe optimizar solo XP/h. Debe equilibrar experiencia, oro neto, progreso de profesiones, poder de combate, tiempo de viaje, riesgo, maná, espacio de bolsas y objetivos futuros. La montura puede ser un objetivo económico, pero su coste, nivel y requisitos deben verificarse para WoW Forever.

### 3.1 Investigación Priest
Investigar específicamente para Forever:
- Builds y talentos de leveling.
- Eficiencia de hechizos y gestión de maná.
- Varitas y progresión de varitas.
- Spirit Tap y Wand Specialization, si aplican.
- Comparación Discipline/Shadow durante leveling.
- Hechizos, rangos, entrenadores y costes.
- Equipo por nivel, estadísticas prioritarias y mejoras realistas.

Se mencionaron como hipótesis Lesser Magic Wand (nivel requerido 5, ~11.3 DPS) y Greater Magic Wand (nivel 13, ~17.5 DPS). **Verificar antes de recomendar o comprar.**

### 3.2 Investigación de profesiones
Herbalism + Skinning parece una combinación práctica: recolectar hierbas durante rutas y desollar bestias que ya se mataron. Verificar en Forever requisitos y zonas de Peacebloom, Silverleaf y Earthroot (se mencionó Earthroot desde skill 15, pendiente de confirmar). Evaluar cada desvío por valor incremental frente a tiempo, distancia, peligro y coste de oportunidad. Nunca asumir precios de AH sin datos actuales del reino.

## 4. Addons elegidos

El plan acordado es **probar Wowdee y Dossier juntos** porque sus funciones esperadas son complementarias. La compatibilidad con WoW Forever todavía debe comprobarse.

### 4.1 Wowdee — asistente in-game
Rol esperado: herramientas y orientación dentro del cliente. Investigar y probar si ofrece guía de leveling, misiones, equipo, mapas, profesiones, inventario y economía/Auction House. No asumir que todas las funciones existen o funcionan en Forever.

### 4.2 Dossier — historial/telemetría
Rol esperado: registrar actividad y progreso para análisis fuera del juego. Comprobar si captura nivel, sesiones, zonas, misiones, kills, oro, XP/h, profesiones, recolección y si exporta datos. No asumir que genera JSON ni que todos esos campos están disponibles.

### 4.3 División de responsabilidades
- **Wowdee:** ayuda operativa durante la partida.
- **Dossier:** registro e historial.
- **Obsidian:** conocimiento organizado y estado legible.
- **Claude Code:** investigación, análisis, desarrollo y recomendaciones.
- **Python + SQLite:** integración y memoria estructurada.

Si ambos registran el mismo campo, elegir fuente primaria y documentar cómo resolver discrepancias.

### 4.4 Addons complementarios — solo candidatos
Evaluar únicamente si resuelven una carencia real:
- Auctionator: escaneo/información de Auction House.
- GatherMate2: registro de nodos.
- Questie: ayuda de misiones.
- TomTom: navegación por coordenadas.
- Baganator: gestión de bolsas.
- InfiniteSync: se mencionó como posible vía de sincronización SavedVariables; verificar existencia, mantenimiento, compatibilidad y seguridad antes de adoptarlo.

No instalar todos por defecto. Empezar con Wowdee y Dossier.

### 4.5 Matriz obligatoria de validación
Crear `07-Research/Addons.md`:

| Addon | Fuente oficial | Versión/build | Instala | Carga sin errores | Funciona en Forever | Datos exportables | Formato/ruta | Decisión |
|---|---|---|---|---|---|---|---|---|
| Wowdee | Pendiente | Pendiente | No probado | No probado | No probado | Pendiente | Pendiente | Candidato |
| Dossier | Pendiente | Pendiente | No probado | No probado | No probado | Pendiente | Pendiente | Candidato |
| Auctionator | Pendiente | Pendiente | No probado | No probado | No probado | Pendiente | Pendiente | Evaluar |
| GatherMate2 | Pendiente | Pendiente | No probado | No probado | No probado | Pendiente | Pendiente | Evaluar |
| Questie | Pendiente | Pendiente | No probado | No probado | No probado | Pendiente | Pendiente | Evaluar |
| TomTom | Pendiente | Pendiente | No probado | No probado | No probado | Pendiente | Pendiente | Evaluar |
| Baganator | Pendiente | Pendiente | No probado | No probado | No probado | Pendiente | Pendiente | Evaluar |
| InfiniteSync | Pendiente | Pendiente | No probado | No probado | No probado | Pendiente | Pendiente | Evaluar |

Para cada addon: localizar página/repositorio oficial y releases; confirmar cliente/API objetivo; revisar mantenimiento/dependencias; instalar desde fuente confiable; comprobar errores; probar funciones; ejecutar `/reload` y logout; inspeccionar archivos y esquemas reales; documentar frecuencia y límites; decidir mantener/sustituir/descartar.

## 5. Arquitectura propuesta

```text
WoW Forever
   │ APIs permitidas de addons
   ├───────────────┐
   ▼               ▼
 Wowdee          Dossier
 (asistencia)    (historial)
   └───────┬───────┘
           ▼
 SavedVariables / exports
           ▼
 Python Collector
 detect → wait stable → raw snapshot → parse → validate
           ▼
 Normalization → SQLite
           ▼
 Markdown generator → Obsidian vault
           ▼
 Claude Code (consultas + investigación + análisis)
           ▼
 Recomendaciones explicables para el jugador
```

### 5.1 Componentes
**Juego/addons:** fuente del estado del personaje y herramientas in-game.

**SavedVariables/export:** los addons suelen persistir variables al `/reload`, logout o cierre correcto; no asumir escritura inmediata por evento. Verificar comportamiento real. El sistema debe decir “última sincronización” y no afirmar tiempo real si solo tiene snapshots guardados.

**Python Collector:** detectar cambios; esperar a que termine la escritura; copiar snapshot original; parsear Lua/JSON/u otro formato real; validar tipos/esquema; normalizar IDs/timestamps; detectar duplicados/cambios; insertar en SQLite transaccionalmente; generar Markdown; registrar errores y antigüedad.

**SQLite:** base estructurada e histórica. Markdown no será la única base de datos.

**Obsidian:** conocimiento, guías, estado actual, sesiones y decisiones. Separar archivos generados de notas manuales.

**Claude Code:** investiga, consulta estado normalizado, analiza y recomienda. No modifica raw ni inventa datos.

### 5.2 Estructura sugerida

```text
WoW-Companion/
├── CLAUDE.md
├── README.md
├── IMPLEMENTATION_PLAN.md
├── DECISIONS.md
├── pyproject.toml
├── config/
│   ├── settings.example.yaml
│   ├── addon_sources.yaml
│   └── schema_version.txt
├── 00-Dashboard/
│   ├── HOME.md
│   ├── Current-Character.md
│   ├── Next-Actions.md
│   └── Data-Health.md
├── 01-Character/
│   ├── Profile.md
│   ├── Equipment.md
│   ├── Inventory.md
│   ├── Bank.md
│   ├── Talents.md
│   ├── Spells.md
│   └── Progress.md
├── 02-Classes/Priest/
│   ├── Leveling-1-60.md
│   ├── Builds.md
│   ├── Rotations.md
│   ├── Wand-Progression.md
│   └── Gear-Progression.md
├── 03-Professions/
│   ├── Herbalism/{Leveling.md,Herbs.md,Routes.md,Market.md}
│   └── Skinning/{Leveling.md,Materials.md,Routes.md,Market.md}
├── 04-Economy/
│   ├── Auction-House.md
│   ├── Gold-History.md
│   ├── Keep-Sell-Buy.md
│   ├── Mount-Fund.md
│   └── Market-Analysis.md
├── 05-World/{Zones/,NPCs/,Quests/,Dungeons/,Routes/}
├── 06-Items/{Wands/,Materials/,Consumables/,Important-Items/}
├── 07-Research/
│   ├── Sources.md
│   ├── Research-Queue.md
│   ├── Addons.md
│   ├── Conflicts.md
│   └── Patch-Changes.md
├── 08-Sessions/YYYY-MM-DD.md
├── data/{raw/,normalized/,exports/,companion.sqlite}
├── src/wow_companion/{collectors/,parsers/,normalization/,storage/,markdown/,analytics/,cli/}
└── tests/{fixtures/,parsers/,normalization/,analytics/}
```

Es una propuesta, no una obligación de crear todas las carpetas vacías. Ajustar a evidencia y simplicidad.

## 6. Captura y sincronización

### 6.1 MVP fiable
1. Usuario juega.
2. Addons acumulan datos.
3. Usuario hace `/reload` o cierra correctamente.
4. WoW persiste SavedVariables.
5. Collector detecta el cambio.
6. Guarda snapshot raw inmutable.
7. Parser normaliza.
8. SQLite actualiza estado e historial.
9. Markdown se regenera.
10. Claude consulta el estado actualizado.

No prometer tiempo real hasta demostrar escritura durante la sesión o una exportación permitida. Un comando/botón de addon para exportar podría evaluarse si existe.

### 6.2 Datos deseados

| Dominio | Campos | Prioridad |
|---|---|---|
| Personaje | nombre, clase, raza, nivel, XP | Alta |
| Ubicación | zona, subzona, coordenadas si existen | Alta |
| Economía | oro/plata/cobre y cambios | Alta |
| Equipo | slot, item ID, nombre, estadísticas disponibles | Alta |
| Inventario | bolsa/slot, item ID, cantidad, calidad, binding | Alta |
| Banco | items/cantidades si observables | Media |
| Misiones | activas, completadas, objetivos/progreso | Alta |
| Profesiones | skill actual/máxima, recetas | Alta |
| Recolección | nodos, materiales, ubicación, timestamp | Media |
| Talentos | árbol y puntos | Media |
| Hechizos | spells/rangos conocidos | Media |
| Sesiones | inicio/fin, duración, zona, XP/oro ganados | Alta |
| Actividad | kills, muertes, quests, loot si exportable | Media |
| Auction House | escaneos, precio, cantidad, fecha y reino | Alta para economía |

Cada campo tendrá estado `available`, `not_supported`, `not_collected` o `unknown`.

### 6.3 Metadatos y frescura
Cada snapshot debe incluir `captured_at`, `source_addon`, `source_file`, `source_version`, `game_version`, `schema_version`, `parse_status` y `content_hash` cuando estén disponibles. Mostrar antigüedad y advertir si está obsoleto.

### 6.4 Raw y consistencia
Guardar originales sin alterarlos, por ejemplo:
`data/raw/<addon>/<character>/<date>/<timestamp>_<hash>.<ext>`.

No procesar archivos mientras cambian. Si falla el parser, conservar el último estado válido. Procesamiento idempotente. Registrar cambios, errores y procedencia. Versionar esquema y migraciones.

## 7. Modelo de datos inicial

Definir el esquema final después de inspeccionar los archivos reales. Entidades candidatas:
- `characters`, `character_snapshots`
- `inventory_snapshots`, `inventory_items`
- `equipment_snapshots`
- `quests`, `character_quests`
- `professions`, `profession_events`
- `sessions`, `activity_events`
- `gold_transactions`
- `auction_scans`, `auction_prices`
- `gathering_nodes`
- `item_catalog`, `spell_catalog`, `talent_builds`
- `addon_sources`, `raw_files`
- `recommendations`, `recommendation_feedback`
- `research_sources`

Usar IDs estables del juego cuando existan; no depender solo de nombres traducidos. Separar catálogo estático de observaciones. Guardar timestamps en UTC internamente y mostrar hora local.

**Snapshot** = fotografía del estado. **Evento** = cambio observado explícitamente o inferido. No presentar como hecho un evento inferido únicamente comparando snapshots; etiquetarlo `inferred`.

## 8. Motor de recomendaciones

### 8.1 Formato estándar
Cada recomendación debe contener:
- acción sugerida y prioridad;
- beneficio esperado;
- tiempo/coste estimado, solo si hay datos;
- requisitos;
- datos usados y timestamp;
- evidencia/fuentes;
- confianza;
- riesgos/incertidumbres;
- alternativa.

Ejemplo de esquema:

```yaml
id: recommendation-id
action: "..."
priority: high
reason: "..."
expected_benefit: "..."
estimated_time_minutes: null
requirements: []
data_as_of: "..."
evidence: []
confidence: medium
uncertainties: []
```

### 8.2 Categorías
`next_action`, `quest_route`, `gear_upgrade`, `inventory_decision`, `buy_sell`, `profession_route`, `spell_talent`, `gold_goal`, `session_review`, `data_warning`.

### 8.3 Optimización multiobjetivo
No reducir todo a XP/h. Factores posibles: XP/min, oro neto/min, utilidad futura de materiales, progreso de profesión, mejora de equipo, distancia, riesgo, maná/recuperación, espacio de bolsas, sinergia de misiones y confianza. Empezar con reglas transparentes y pesos configurables. No inventar pesos “óptimos”; calibrar con sesiones reales.

### 8.4 Decisiones de inventario
Clasificaciones:
- `KEEP`: conservar.
- `USE`: usar/equipar.
- `SELL_VENDOR`: vender a NPC.
- `AUCTION`: considerar AH.
- `BANK`: guardar.
- `DESTROY`: destruir solo si es seguro y autorizado.
- `UNKNOWN`: evidencia insuficiente.

Antes de recomendar venta: comprobar misión, receta/profesión, rareza, binding, mejora actual/futura, precio vendor vs mercado y coste de recuperar. Si falta información, `KEEP` o `UNKNOWN`.

### 8.5 Economía/Auction House
Registrar fecha, reino, precio, cantidad, stack y precio vendor. Distinguir precio listado de precio vendido. Calcular neto después de comisiones solo si se conocen. Evitar conclusiones con una observación aislada. Mantener historial cuando sea posible. No asumir demanda ni rentabilidad. Validar costes/requisitos de montura en Forever.

### 8.6 Rutas combinadas
Combinar misiones, objetivos, enemigos, bestias para skinning, nodos herbales, vendedores, entrenadores, buzón, banco y AH. Considerar nivel/dificultad, bolsas y capacidad. No desviarse por un nodo sin comparar beneficio incremental con tiempo/coste. Registrar rutas planeadas vs resultados reales.

## 9. Investigación y base de conocimiento

### 9.1 Prioridad de fuentes
1. Sitio/wiki/documentación oficial de WoW Forever.
2. Comunicaciones del equipo del servidor.
3. Datos observados dentro del juego.
4. Repositorios y documentación de addons.
5. Comunidades/guías específicas de Forever.
6. Classic/Vanilla solo como hipótesis comparativa.

No usar snippets de buscador como única prueba de mecánicas importantes.

### 9.2 Plantilla por tema

```markdown
# Nombre de la mecánica
## Resumen
## Cómo funciona
## Datos específicos de WoW Forever
## Diferencias frente a Classic
## Recomendaciones prácticas
## Tablas / niveles / requisitos
## Fuentes
- URL:
- Tipo:
- Fecha consultada:
- Evidencia:
## Estado de verificación
- Estado: confirmed_forever | probable_classic | unknown | conflicting
- Confianza: high | medium | low
- Última verificación:
- Build/versión:
## Preguntas pendientes
```

Mantener `07-Research/Conflicts.md`: conservar fuentes contradictorias, describir diferencias y no resolver por intuición. Cola inicial: compatibilidad/exportación de addons; API/build y SavedVariables; Priest 1–20; varitas; spells/talentos; Herbalism y Skinning; rutas de zonas Undead; economía y AH; objetivos de oro/montura.

## 10. Claude Code y experiencia de uso

Claude Code debe leer `CLAUDE.md` antes de trabajar. Debe:
- no modificar raw;
- no inventar estado ni mecánicas;
- citar fuentes y timestamps;
- distinguir observado, inferido y conocimiento externo;
- revisar `Data-Health.md` antes de tratar Markdown como estado actual;
- pedir confirmación para operaciones destructivas;
- no instalar addons ni manipular el proceso del juego sin autorización.

Workflows deseados (pueden ser prompts o comandos CLI al inicio):

| Comando conceptual | Función |
|---|---|
| `/status` | Estado actual, frescura y salud |
| `/next` | Tres mejores acciones y razones |
| `/character` | Resumen del personaje |
| `/inventory` | KEEP/USE/SELL/AUCTION/BANK/UNKNOWN |
| `/gear` | Comparar equipo y mejoras |
| `/gold` | Oro, ingresos/gastos y objetivos |
| `/route` | Ruta combinada de quests/gathering/skinning |
| `/professions` | Skills y próximos materiales/zonas |
| `/priest` | Talentos, hechizos, rotación y equipo |
| `/session` | XP/h, oro/h y actividad de última sesión |
| `/research <tema>` | Investigación con fuentes |
| `/sync` | Collector, parser y vistas |
| `/data-health` | Validación de archivos, timestamps y DB |

Respuesta de `/next` debe incluir acción concreta, por qué, beneficio, coste/tiempo si se conoce, datos utilizados, confianza, alternativas y advertencias.

## 11. Fases de implementación

### Fase 0 — Descubrimiento y validación de addons
1. Identificar cliente y build de WoW Forever.
2. Localizar carpeta de addons y SavedVariables.
3. Encontrar fuentes oficiales/releases de Wowdee y Dossier.
4. Validar compatibilidad e instalar manualmente con autorización.
5. Probar funciones.
6. Hacer `/reload` y logout; inspeccionar archivos.
7. Guardar fixtures de prueba, evitando credenciales/datos sensibles.
8. Documentar esquemas, frecuencia y límites.
9. Decidir si hace falta addon adicional o propio.

**Entregable:** `07-Research/Addons.md` con evidencia y fixtures reales. Salida: snapshot reproducible de cada addon viable o razón documentada de incompatibilidad.

### Fase 1 — Captura y estado actual
Implementar collector, parsers sobre fixtures reales, normalización, SQLite/migraciones, snapshots idempotentes, generación de `Current-Character.md`, `Inventory.md`, `Equipment.md`, `Progress.md`, `Data-Health.md`, CLI y tests.

**Salida:** `/reload` o logout actualiza Obsidian correctamente sin duplicados.

### Fase 2 — Knowledge Base
Documentar Priest 1–20 y profesiones iniciales primero. Añadir fuentes, confianza, conflictos y fecha de revisión. No documentar todo Azeroth antes de validar el pipeline.

### Fase 3 — Motor de decisiones
Implementar `/next`, `/inventory`, `/gear`, `/gold`, `/professions`, `/route`. Reglas transparentes primero; no introducir ML sin datos suficientes.

### Fase 4 — Historial y optimización
XP/h, oro/h, progreso de profesiones, rutas planeadas vs reales, valor de materiales y feedback del usuario.

### Fase 5 — Sincronización avanzada
Investigar exportación durante sesión, comandos de addon, sincronización periódica permitida y watcher. No prometer tiempo real ni usar métodos no permitidos.

## 12. Pruebas y calidad

### Técnicas
- Parsers con fixtures reales.
- Archivos truncados/parcialmente escritos.
- Cambios de versión de addon.
- Campos faltantes/tipos inesperados.
- Idempotencia.
- Más de un personaje/reino.
- Timestamps/zonas horarias.
- Migraciones SQLite.
- Markdown determinista.
- Recuperación tras fallo y preservación del último snapshot válido.

### Funcionales
- Nivel/oro/equipo/inventario coinciden con captura.
- Misiones/profesiones solo aparecen si la fuente las exporta.
- Datos vencidos siempre se advierten.
- No recomendar venta si es item de misión o su uso no está resuelto.
- Precios incluyen fecha y reino.
- Mecánicas no confirmadas están etiquetadas.

### Observabilidad
`Data-Health.md` debe mostrar último archivo, último parseo exitoso, versión de parser, cantidad de registros, errores, snapshot actual y antigüedad.

## 13. Decisiones iniciales

| Tema | Decisión | Condición |
|---|---|---|
| Conocimiento | Obsidian + Markdown | Portable y legible |
| Agente | Claude Code | Investigación/desarrollo/análisis |
| Captura | Addons + SavedVariables | Vía permitida y auditable |
| Integración | Python | Parsing, watcher, normalización, CLI |
| Historial | SQLite | Consultas, snapshots y eventos |
| Raw | Originales inmutables | Reprocesamiento/auditoría |
| Sync MVP | Post `/reload`/logout | Verificar en práctica |
| Addons | Wowdee + Dossier | Complementarios, compatibilidad pendiente |
| Extras | Solo por necesidad demostrada | Evitar complejidad |
| Recomendaciones | Reglas explicables | Calibrar con datos reales |
| Seguridad | Sin memory reading/injection | Integración legítima |

## 14. Riesgos y preguntas abiertas

1. ¿Qué build exacto de WoW Forever está instalado?
2. ¿Qué cliente/plataforma y ruta utiliza?
3. ¿Wowdee y Dossier tienen versiones compatibles?
4. ¿Qué datos exporta realmente cada uno?
5. ¿Se puede observar AH/transacciones o solo inventario?
6. ¿El juego corre en macOS, Windows o capa de compatibilidad? Determina rutas y watcher.
7. ¿Qué se guarda con `/reload` y qué solo al logout?
8. ¿Cómo identificar personaje/reino/sesión inequívocamente?
9. ¿Qué datos de mercado existen y con qué frecuencia?
10. ¿Qué mecánicas difieren de Classic?

Resolver por inspección cuando sea posible. Preguntar al usuario solo lo que no pueda descubrirse de forma segura y sea necesario.

## 15. Instrucciones de arranque para Claude Code

**No construir todo de golpe.** Al recibir este documento:
1. Leerlo completo.
2. Crear `IMPLEMENTATION_PLAN.md` y `DECISIONS.md`.
3. Inspeccionar el entorno sin modificar nada.
4. Investigar fuentes oficiales/versiones de Wowdee y Dossier.
5. Presentar matriz de compatibilidad con enlaces y evidencia.
6. Solicitar al usuario instalar/probar addons manualmente si hace falta.
7. Inspeccionar SavedVariables reales y generar fixtures.
8. Proponer esquema definitivo y arquitectura del collector.
9. Implementar Fase 1 solo después de validar diseño.
10. Ejecutar tests y demostrar pipeline con snapshot real.

**Primera entrega de Claude:**
- `IMPLEMENTATION_PLAN.md`
- `07-Research/Addons.md`
- `DECISIONS.md`
- inventario de rutas/archivos relevantes encontrados;
- preguntas bloqueantes;
- recomendación sustentada sobre viabilidad de Wowdee + Dossier en WoW Forever.

No declarar que un addon funciona hasta probarlo. No crear datos ficticios para aparentar integración terminada.

## 16. Definición de éxito

El MVP está logrado cuando:
1. Wowdee y Dossier se evaluaron con evidencia y se conoce su aporte real.
2. El usuario juega y sincroniza datos con un paso sencillo.
3. Obsidian muestra estado fiable del personaje.
4. Existe historial de sesiones y cambios.
5. Claude responde sobre inventario, equipo, oro, profesiones y progreso con datos reales.
6. Separa hechos, inferencias y mecánicas no verificadas.
7. Las recomendaciones son accionables, explicables y prudentes.
8. Los parsers son adaptadores sustituibles, sin dependencia irreversible de un addon.

**Principio final:** construir primero una tubería pequeña, real y verificable; después convertirla en un Companion inteligente. La prioridad no es acumular addons ni cientos de páginas: es que cada dato sea confiable y cada recomendación ayude a tomar una mejor decisión en WoW Forever.
