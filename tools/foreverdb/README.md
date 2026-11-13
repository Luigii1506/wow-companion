# Adaptador de la API de ForeverDB

Consulta la API de solo lectura de [ForeverDB.net](https://foreverdb.net) (objetos,
hechizos, misiones, vendedores, profesiones, recolección, cambios de Forever…) desde la
terminal, con caché local y límites de uso por debajo de los del plan gratuito. Solo usa la
biblioteca estándar de Python 3.

Datos de la API leídos en <https://foreverdb.net/developers> el 2026-11-13.
**Estado: sin probar contra la API real** (aún no hay clave). Las pruebas usan HTTP simulado.

## Configuración (cuando llegue la clave)

1. Pide la clave personal en <https://foreverdb.net/developers> (empieza por `fdb_`).
2. En la raíz del repositorio: `cp .env.example .env`
3. Edita `.env` y deja `FOREVERDB_API_KEY=fdb_...` (sin espacios). `.env` está en
   `.gitignore`. También vale exportar la variable `FOREVERDB_API_KEY` en la shell, que
   tiene prioridad sobre `.env`.
4. Prueba con una sola petición: `python3 -m tools.foreverdb.query meta`

Si falta la clave, el comando lo dice y no envía nada. La clave nunca se imprime ni se
guarda en la caché, y se oculta de los mensajes de error.

## Comandos

Desde la raíz del repositorio:

```bash
python3 -m tools.foreverdb.query meta
python3 -m tools.foreverdb.query item 4947
python3 -m tools.foreverdb.query item --q "Jagged Dagger"
python3 -m tools.foreverdb.query quests --zone Durotar --side horde --min 10 --max 20
python3 -m tools.foreverdb.query vendor --q "nombre"
python3 -m tools.foreverdb.query gathering mining --zone Durotar
python3 -m tools.foreverdb.query changes --kind quest --verified 1
python3 -m tools.foreverdb.query profession engineering
python3 -m tools.foreverdb.query get /dungeons limit=10      # cualquier otro endpoint
python3 -m tools.foreverdb.export item --q "Jagged Dagger"  # fragmento markdown para una nota
python3 -m unittest discover -s tests -t .                  # pruebas (sin red ni clave)
```

Opciones comunes: `--refresh` (ignora la caché), `--limit 1-100`, `--offset`, `--all N`
(pagina hasta N filas; cada página es una petición), `--json` (respuesta en bruto), `--md`.

Toda salida termina con la URL, la fecha de obtención (UTC), si vino de la caché, la build
del juego que indica `meta` y la línea `Data from ForeverDB.net (https://foreverdb.net)`.
Los datos son conocimiento externo de una base comunitaria: no son estado del personaje
ni en tiempo real.

`export` solo imprime: tabla markdown + `## Fuentes` con el enlace obligatorio y la URL
exacta. No escribe en notas; se copia a mano en la nota correspondiente.

## Límites

| | ForeverDB (plan gratuito) | Este adaptador |
|---|---|---|
| Por minuto | 30 | 25 (espera automática) |
| Por día | 5000 | 4500 (se niega a seguir; día UTC) |

- El recuento diario está en `data/foreverdb/usage.json`. Los reintentos cuentan; las
  respuestas en caché no.
- `429`: espera lo que diga `Retry-After` y reintenta (máximo 2 veces). Si pide más de
  2 minutos, para y avisa.
- `402 subscription_required`: el endpoint o el volumen no entra en el plan gratuito.
- `403`: clave inválida o revocada; con «error 1010», Cloudflare bloqueó el User-Agent.
- Caché en `data/foreverdb/cache/`, un JSON por endpoint + parámetros, con `fetched_at`
  (UTC) y build. Caduca a los 7 días.

## Atribución obligatoria

Condición de los términos de la API: donde se muestren datos de ForeverDB debe aparecer
el crédito «Data from ForeverDB.net» con enlace visible a <https://foreverdb.net>. En la
bóveda va en `## Fuentes` como `[Data from ForeverDB.net](https://foreverdb.net)` junto a
la URL concreta (ver `_System/Vault-Guide.md`, «Créditos obligatorios»).

## Qué NO hacer

- No usar la clave personal en una web ni en nada publicado; es solo para uso personal.
- No poner la clave en código, notas, commits ni capturas. Vive solo en `.env`.
- No subir la caché ni `usage.json`: `data/foreverdb/` está en `.gitignore`. Las respuestas
  llevan marcas invisibles que identifican la clave, así que tampoco se redistribuyen
  volcados en bruto; en las notas, solo resúmenes con crédito.
- No saltarse los límites (varias claves, paralelismo, borrar `usage.json` para seguir).

## Dudas pendientes sobre la API

Por confirmar con la primera respuesta real:

- Nombre exacto del campo de build en `meta` (se prueban `build`, `gameBuild`,
  `game_build`, `version`).
- Forma de la paginación en `meta` (se usa `total` si existe; si no, se para cuando una
  página trae menos filas que `limit`).
- Hora de reinicio del cupo diario (el adaptador asume medianoche UTC).
- Formato de los cuerpos de error (402/403) y si `verified`/`seen` esperan `1` o `true`.
