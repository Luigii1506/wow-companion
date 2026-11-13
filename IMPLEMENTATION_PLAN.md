# Plan de implementación

**Última revisión:** 2026-11-09
**Especificación base:** [wow.md](wow.md). Si este plan y la especificación difieren, manda este plan; los motivos están en [DECISIONS.md](DECISIONS.md).

## Enfoque

Primero un ciclo manual real, después automatizar lo que duela. Los datos salen de Windows, viajan por git y se analizan en el Mac.

```text
PC Windows (juego)                      Mac (conocimiento y análisis)
Dossier /dossier → texto                git pull
guardar en data/inbox/  → git push  →   Claude lee el export
SavedVariables (copia)                  notas de Obsidian + recomendaciones
```

No hay tiempo real: cada recomendación indica la fecha del último export.

## Fase 0 — Validar addons en Windows

Pasos detallados en [data/inbox/README.md](data/inbox/README.md).

- [ ] Hacer privado el repositorio antes de subir datos (ver D-003).
- [ ] Clonar el repositorio en el PC Windows.
- [ ] Copiar la carpeta `WTF` como respaldo.
- [ ] Instalar Dossier solo y comprobar que carga sin errores de Lua.
- [ ] Generar y subir un primer export detallado.
- [ ] Hacer `/reload`, localizar el archivo de Dossier en SavedVariables y subir una copia.
- [ ] Salir del juego, volver a entrar y comprobar que el historial sigue ahí (fallo reportado de carga de ajustes).
- [ ] Instalar Wowdee y comprobar que convive con Dossier.
- [ ] Completar [07-Research/Addons.md](07-Research/Addons.md) con lo observado.

**Salida:** un export real en el repositorio y una decisión por addon: mantener, sustituir o descartar.

## Fase 1 — Ciclo manual sin código

- Claude lee el export más reciente de `data/inbox/` y actualiza:
  - `00-Dashboard/Current-Character.md`, con fecha del dato y campos ausentes;
  - `00-Dashboard/Next-Actions.md`, con el formato de recomendación de la §8.1 de la especificación;
  - `08-Sessions/YYYY-MM-DD.md`.
- Solo se crean notas que tengan datos reales. Nada de carpetas vacías.
- Este repositorio se abre como bóveda propia de Obsidian (ver D-004).

**Salida:** tras una sesión de juego, un export produce recomendaciones que coinciden con lo que ves en el juego.

## Fase 2 — Base de conocimiento

**Estado (2026-11-10):** primera versión creada en paralelo a la Fase 0 (D-012). Portada en `00-Dashboard/HOME.md`; 22 conflictos registrados en `07-Research/Conflicts.md`. Pendiente: Reddit y comunidad (D-013) y validación en el juego.

Áreas cubiertas, con la plantilla de la §9.2:

1. Priest: talentos, hechizos, varitas y maná.
2. Herbalism y Skinning: hierbas, zonas y rutas para su nivel actual.
3. Economía: montura y valor de materiales, solo con datos del reino.

Cada mecánica lleva estado (`confirmed_forever`, `probable_classic`, `unknown`, `conflicting`), fuente y fecha. El detalle cubre 1–30 y se amplía a medida que el personaje avanza.

**Salida:** `/next` puede citar guías verificadas para el nivel actual.

## Fase 3 — Parser y SQLite

**Se activa solo si ocurre alguna de estas condiciones:**

- Hay suficientes exports como para que leerlos a mano sea lento o caro.
- Se necesita historial más largo que las 20 sesiones que guarda Dossier.
- Se quieren tendencias de XP/h u oro/h entre muchas sesiones.

Alcance inicial: parser sobre fixtures reales, inbox hacia `data/raw/` inmutable, SQLite con unas 5 tablas (`raw_files`, `character_snapshots`, `inventory_items`, `equipment_items`, `sessions`), Markdown generado y `Data-Health.md`. El esquema se define tras inspeccionar los archivos reales.

## Fase 4 — Decisiones e historial

Reglas explicables para inventario, equipo, oro y rutas. Comparar rutas planeadas con resultados reales y calibrar con sesiones reales.

## Plan B — Addon exportador propio

Solo si los datos de Dossier resultan insuficientes o inestables: un addon mínimo con API permitidas y esquema versionado propio.

## Fuera de alcance por ahora

Tiempo real, watcher, sincronización automática entre máquinas y los addons complementarios sin una carencia demostrada.

## Medidas de éxito

- Un export llega del juego a una recomendación en menos de 5 minutos de trabajo manual.
- Cero recomendaciones basadas en un dato que contradiga el export.
- Toda recomendación indica la fecha del dato y su confianza.
- Toda mecánica citada tiene estado de verificación y fuente.

## Preguntas abiertas

1. ¿El Dossier 2.2.18 funciona en el cliente actual tras el lanzamiento?
2. ¿Qué formato exacto tiene el export y es estable entre versiones?
3. ¿Qué guardan Dossier y Wowdee en SavedVariables?
4. ¿El fallo de carga de ajustes sigue activo?
5. ¿Qué datos de subastas se pueden obtener y con qué frecuencia?
