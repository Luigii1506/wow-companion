---
type: system
tags: [system]
last_updated: 2026-11-13
---

# Guía de la bóveda

Reglas para que la bóveda sea navegable en Obsidian y barata de consultar con Claude Code. Todo el que escriba notas (personas o agentes) las sigue.

## Tres capas

| Capa | Dónde | Qué contiene |
|---|---|---|
| 1. Fuente | `07-Research/Guides/<sitio>/` | Una **ficha por página de guía**: qué dice esa fuente, con fecha y autor. Resumen con palabras propias, nunca copia. |
| 2. Conocimiento | carpetas `02`–`10` | Una **nota por tema** que fusiona todas las fuentes: consenso, discrepancias, estado de verificación. Es lo que se consulta. |
| 3. Acción | `00-Dashboard/` | Portada y **playbooks por tramo de nivel** para el personaje. Lo primero que lee Claude para "¿qué hago ahora?". |

Recortes completos de páginas (Web Clipper) van a `07-Research/inbox/`, que **no se sube a git** (derechos de autor).

## Carpetas

| Carpeta | Contenido | Índice |
|---|---|---|
| `00-Dashboard/` | HOME, playbooks | [[HOME]] |
| `01-Character/` | Estado real del personaje, solo desde exports | — |
| `02-Classes/<Clase>/` | Clases, especializaciones, talentos, hechizos, razas | [[Classes]] |
| `03-Professions/` | Profesiones, materiales, recetas, rutas de recolección | [[Professions]] |
| `04-Economy/` | Oro, subasta, montura, costes, reputaciones con valor económico | [[Economy]] |
| `05-World/` | Zonas, mazmorras, raids, misiones, enemigos y raros, viajes | [[World]] |
| `06-Items/` | Armas, wands, bolsas, consumibles, encantamientos, objetos notables | [[Items]] |
| `07-Research/` | Fuentes, catálogo de guías, fichas, conflictos, cambios de parche | [[Sources]] |
| `08-Sessions/` | Sesiones de juego, desde exports | — |
| `09-Systems/` | Sistemas de Forever: camping, Legacy, libros, transmog, PvP, eventos, buffs | [[Systems]] |
| `10-Tips/` | Consejos y trucos | [[Tips]] |
| `_System/` | Esta guía, plantillas y tablas Bases | — |

## Nombres de archivo

- **Únicos en toda la bóveda**, porque Obsidian enlaza por nombre: `Shadowfang-Keep.md`, `Herbalism.md`, `Priest-Talents.md`.
- Palabras con mayúscula inicial separadas por guiones. Nombres del juego en inglés.
- Si el nombre puede repetirse en otra clase o tema, se antepone la entidad: `Mage-Leveling.md`, `Shadow-Priest-Rotation.md`.
- Fichas de fuente: `src-<sitio>-<slug>.md`. El slug es la ruta de la URL tras `/wow-forever/`, con `/` cambiada por `-`. Ejemplo: `https://www.method.gg/wow-forever/class-guides/shadow-priest/talents` → `src-method-class-guides-shadow-priest-talents.md`.

## Propiedades (frontmatter)

Todas las notas de conocimiento llevan estas propiedades. Las tablas Bases dependen de ellas, así que usa exactamente estos nombres y valores.

```yaml
---
type: class | spec | race | profession | material | recipe | dungeon | raid | zone | quest | mob | item | system | gold-method | tip | playbook | topic | source-digest | moc
tags: [forever, ...]
level_min: 15        # número o se omite
level_max: 20        # número o se omite
faction: horde | alliance | both   # si aplica
status: confirmed_forever | probable_classic | unknown | conflicting
confidence: high | medium | low
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources: [URLs leídas de verdad]
related: ["[[Otra-Nota]]"]
---
```

Fichas de fuente (`type: source-digest`) añaden: `site`, `url`, `author`, `published`, `updated`, `ingested`, `feeds` (lista de notas de conocimiento que alimentó).

## Cuerpo de las notas de conocimiento

1. `# Título`
2. Callout de estado al principio:
   - `> [!success] Confirmado en Forever` si `status: confirmed_forever`
   - `> [!warning] Datos en conflicto: ver [[Conflicts]]` si `conflicting`
   - `> [!info] Hipótesis basada en Classic` si `probable_classic`
   - `> [!question] Sin evidencia suficiente` si `unknown`
3. `## Resumen`: 3–6 viñetas con lo que hay que saber. Claude responde desde aquí siempre que puede.
4. Secciones del tema (tablas antes que párrafos).
5. `## Qué dicen las guías`: consenso y discrepancias, citando la ficha de cada fuente con `[[src-...]]`.
6. `## Fuentes`: URL, tipo, fecha de la página, fecha consultada, si es anterior al parche del 2026-11-02.
7. `## Preguntas pendientes`.

Cada afirmación concreta de una tabla lleva su estado. Usa `[[wikilinks]]` hacia notas relacionadas; un enlace a una nota que aún no existe está bien: marca algo pendiente.

## Fichas de fuente

Breves (15–40 líneas): propiedades, `## Puntos clave` (viñetas con datos concretos), `## Fiabilidad` (fecha, si es de beta o de lanzamiento, huecos), `## Alimenta` (enlaces a las notas de conocimiento que usan esta ficha). Nunca copiar párrafos ni listas completas de la fuente: datos concretos con palabras propias.

## Prioridad de fuentes

1. Blizzard: notas de parche, hotfixes, desarrolladores.
2. Datos observados en el juego (exports).
3. Azeroth DB (vía MCP) para datos de objetos, misiones, recetas y talentos. Wowhead bloquea a los bots de Anthropic en su robots.txt: no se usa en ingestas automáticas.
4. Method.
5. Mobalytics guías verificadas.
6. Guías de creadores.
7. Guías de comunidad y foros.
8. Classic: solo hipótesis.

## Créditos obligatorios

- **ForeverDB:** toda nota que use datos de ForeverDB (web o API) incluye en `## Fuentes` el enlace visible `[Data from ForeverDB.net](https://foreverdb.net)`, además de la URL concreta. Es condición del plan gratuito de su API.
- La clave de la API va en `.env` (`FOREVERDB_API_KEY`), nunca en notas ni en git.

## Conflictos

Las contradicciones se registran en [[Conflicts]] con un identificador `C<n>`. La nota de conocimiento enlaza el conflicto y muestra ambas versiones; no se elige por intuición.

## Cómo consulta Claude

1. Lee [[HOME]] y el playbook del tramo de nivel.
2. Si no basta, el índice del área y después la nota concreta: leer el `## Resumen` primero.
3. Solo busca en internet si la nota falta, está desactualizada o la pregunta es sobre algo nuevo. Lo que encuentre lo guarda en la bóveda.
