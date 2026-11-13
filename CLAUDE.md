# WoW Companion

Compañero personal para WoW Forever. Especificación: `wow.md`. Plan vigente: `IMPLEMENTATION_PLAN.md`. Decisiones: `DECISIONS.md`.

## Flujo

El usuario juega en un PC Windows y sube exports a `data/inbox/` por git. Este Mac aloja la guía en Obsidian y el análisis. Ejecuta `git pull` antes de leer el estado del personaje.

## Cómo responder preguntas del juego (barato primero)

1. Leer `00-Dashboard/HOME.md` y, si aplica, el playbook del tramo de nivel.
2. Ir al índice del área (`Classes`, `Professions`, `Economy`, `World`, `Items`, `Systems`, `Tips`) y abrir solo la nota concreta. Leer su `## Resumen` antes que el resto.
3. Buscar en internet solo si la nota no existe, está desactualizada o la pregunta trata de algo nuevo. Guardar lo encontrado en la bóveda siguiendo `_System/Vault-Guide.md` y citar la fecha.
4. Tras crear o cambiar notas, ejecutar `python3 _System/build_index.py`.

La estructura, los nombres de archivo y las propiedades están en `_System/Vault-Guide.md`.

## Reglas

- No modificar ni borrar archivos de `data/inbox/` ni `data/raw/`.
- No inventar estado del personaje, precios, coordenadas, NPCs, drop rates ni mecánicas. Si falta un dato, decirlo.
- Toda recomendación indica la fecha del export usado, sus fuentes y su confianza. El estado nunca es en tiempo real.
- Distinguir lo observado, lo inferido y el conocimiento externo.
- Etiquetar cada mecánica: `confirmed_forever`, `probable_classic`, `unknown` o `conflicting`, con fuente y fecha.
- Los datos de Classic son solo hipótesis.
- Ante la duda, recomendar conservar un objeto antes que venderlo o destruirlo.
- No declarar que un addon funciona hasta que se haya probado en el juego.
- Solo addons y API permitidas. Nunca lectura de memoria, inyección ni automatización del cliente.
- Crear notas de Obsidian solo cuando tengan datos reales.
- No subir el repositorio ni cambiar su visibilidad sin confirmación del usuario.
