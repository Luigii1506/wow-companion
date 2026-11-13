# Decisiones

| ID | Fecha | Decisión | Motivo | Estado |
|---|---|---|---|---|
| D-001 | 2026-11-09 | El juego y los exports se hacen en el PC Windows; la guía, Obsidian y el análisis, en el Mac. | Indicado por el usuario. | Vigente |
| D-002 | 2026-11-09 | Git es el transporte: los exports se suben a `data/inbox/` y se leen en el Mac. Reemplaza el watcher local de la §5 de la especificación. | El juego y el análisis están en máquinas distintas. | Vigente |
| D-003 | 2026-11-09 | Los exports se versionan en git, por lo que el repositorio debe ser privado antes de subir el primero. Nunca se sube `Config.wtf` ni la carpeta `WTF` completa. | Los exports incluyen nombre, reino, oro, correo y notas. El repositorio era público el 2026-11-09. | Pendiente de hacer privado el repositorio |
| D-004 | 2026-11-09 | Este repositorio se abre como bóveda propia de Obsidian, separada de `~/Documents/Obsidian Vault`. | Sigue la estructura de la §5.2 y evita mezclar datos del juego con la bóveda personal. | Supuesto; fácil de cambiar |
| D-005 | 2026-11-09 | Dossier «Your Character, Ready for AI» es la fuente principal del estado del personaje, sujeta a validación. | Es el único candidato encontrado que documenta exportar equipo, bolsas, oro, misiones, profesiones y sesiones en Forever. | Candidata |
| D-006 | 2026-11-09 | Wowdee queda como ayuda dentro del juego y no es fuente de datos hasta inspeccionar lo que guarda. | No documenta exportación y publica versiones con mucha frecuencia. | Candidata |
| D-007 | 2026-11-09 | El MVP es un ciclo manual sin código. Parser y SQLite solo cuando se cumplan las condiciones de la Fase 3. | Da valor con datos reales mientras el personaje sube de nivel. | Vigente |
| D-008 | 2026-11-09 | Un addon exportador propio queda como plan B. | Dossier podría cubrir la necesidad sin mantener código en Lua. | Vigente |
| D-009 | 2026-11-09 | Las fuentes de Blizzard encabezan la prioridad de la §9.1. WoW Forever no se trata como servidor privado. | Prensa y guías lo describen como producto oficial con API de la era Midnight. Falta confirmarlo en una página de Blizzard. | Pendiente de fuente primaria |
| D-010 | 2026-11-09 | La guía se investiga para los próximos ~10 niveles del personaje, no del 1 al 60 por adelantado. | Evita documentar niveles que el personaje ya habrá superado. | Sustituida por D-012 |
| D-011 | 2026-11-09 | `.gitattributes` desactiva la conversión de finales de línea en `data/inbox/` y `data/raw/`. | Windows podría alterar los archivos y romper su inmutabilidad y sus hashes. | Vigente |

| D-012 | 2026-11-10 | La base de conocimiento se construye ya y de forma amplia: Priest, profesiones, ruta 1–30, economía y fuentes, sin esperar al primer export. El detalle se concentra en 1–30 y se esboza 30–60. | Pedido por el usuario. Las guías públicas no dependen del estado del personaje. | Vigente |
| D-013 | 2026-11-10 | Reddit no se consulta con las herramientas web, que Reddit bloquea. Solo se lee en el Chrome del usuario, a petición suya, con pocos hilos y sin rastreo masivo. | Respetar el bloqueo del sitio a herramientas automatizadas; el usuario pidió leerlo desde su navegador. | Vigente. El 2026-11-10 la extensión de Chrome también bloqueó Reddit por restricciones de seguridad. Vía disponible: el usuario pega o guarda hilos en `07-Research/inbox/` y Claude los resume |
| D-014 | 2026-11-10 | Las guías de pago (por ejemplo, Journey 30–60) solo se documentan desde sus páginas públicas. No se copia ni se sortea contenido de pago. | Derechos de autor y términos de uso. | Vigente |

| D-015 | 2026-11-13 | El personaje principal pasa a ser un **Orc Rogue nivel 11**. El Undead Priest queda como alt. La bóveda sigue siendo general; playbooks, prioridad del catálogo y portada se centran en el Rogue. | Indicado por el usuario. | Vigente |
| D-016 | 2026-11-13 | Fuentes de datos estructurados: MCP de Azeroth DB para consultas, wago.tools (CSV del cliente, permitido a IA) para datos en bloque, ForeverDB API con clave del usuario para misiones, vendedores y recolección. Wowhead no se usa en ingestas: bloquea a los bots de Anthropic. No se esquivan bloqueos ni antibots. | Registro de fuentes del 2026-11-13. | Vigente; MCP y ForeverDB pendientes |
| D-017 | 2026-11-13 | Los datos del addon de ForeverDB (zip público, GPL-3.0 con atribución) se usan en bloque: se guardan en `data/foreverdb/addon_zip/` (fuera de git), se convierten a `data/foreverdb/addon.sqlite` con `tools/fdb_addon/` y cada nota que los usa cita "Data from ForeverDB.net". Las páginas de ForeverDB se leen según su robots.txt (permitido a ClaudeBot salvo `/api/`). Cada dato conserva su etiqueta de origen: visto en Forever, cliente o Classic (CMaNGOS). | Cubre misiones, recompensas, nodos y recetas sin esperar la clave de la API. El robots.txt invita a herramientas a usar estos archivos. | Vigente |

## Resolución de discrepancias

Sin definir. Si Dossier y Wowdee registran el mismo campo, se elegirá la fuente principal después de comparar datos reales de ambos.
