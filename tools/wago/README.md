# Adaptador de wago.tools (datos del cliente de WoW Forever)

Descarga tablas DB2 del cliente de WoW Forever (producto `wowf`) como CSV desde
[wago.tools](https://wago.tools), las guarda en local, las carga en SQLite y permite
consultar objetos y hechizos desde la terminal. Solo biblioteca estándar de Python 3.

## Política de la fuente

wago.tools pide a los agentes de IA que usen sus rutas de API y las exportaciones CSV,
nunca las páginas web (`/llms.txt`, `/robots.txt`, consultados el 2026-11-13). Este
adaptador:

- Solo usa `GET /api/builds/wowf/latest` y `GET /db2/{tabla}/csv?version={versión}`.
  Nunca visita `/db2`, `/db2/{tabla}`, páginas de diff ni el navegador HTML.
- Fija la versión completa (p. ej. `1.60.1.70938`) sin selector de producto, como
  recomienda `llms.txt` para resultados reproducibles, y guarda producto y versión.
- Espera al menos 1 s entre peticiones (1,5 s por defecto), en serie, sin paralelismo.
- Se identifica con un User-Agent descriptivo sin datos personales.
- Reutiliza lo descargado: no repite una tabla ya en caché si su sha256 coincide.
- Si una tabla no existe, wago responde `HTTP 400 {"errors":"Table not found."}`; se
  anota en `manifest.json` (`missing`) y no se intenta otra vía.

Los datos son de Blizzard: quedan solo en local (`data/wago/` está en `.gitignore`).

## Comandos

Desde la raíz del repositorio:

```bash
python3 -m tools.wago.fetch                          # última build de wowf, tablas por defecto
python3 -m tools.wago.fetch --version 1.60.1.70938 --tables ItemSparse SpellName
python3 -m tools.wago.build_db                       # carga la versión más reciente en caché
python3 -m tools.wago.query item "Jagged Dagger"
python3 -m tools.wago.query item --id 4947
python3 -m tools.wago.query spell "Shank"
python3 -m unittest                                  # pruebas (sin red)
```

Tablas por defecto: ItemSparse, Item, ItemClass, ItemSubClass, Spell, SpellName,
SpellMisc, SkillLine, SkillLineAbility, ItemSet, Faction, AreaTable, ChrClasses,
ChrRaces, TalentTab, Talent. Las 16 existían en `wowf 1.60.1.70938`.

## Archivos generados

| Ruta | Contenido |
|---|---|
| `data/wago/<versión>/<tabla>.csv` | CSV tal cual lo sirve wago.tools |
| `data/wago/<versión>/manifest.json` | Por tabla: producto, versión, URL, `fetched_at` (UTC), sha256, filas, columnas; y tablas no disponibles |
| `data/wago/forever.sqlite` | Una tabla SQLite por tabla DB2 con sus columnas originales, más `meta` (producto, versión, fecha, sha256, advertencia) |

La base guarda **una sola versión**: reconstruir borra y sustituye todo en una
transacción, así que es idempotente.

## Qué decodifica `query`

- **Verificado en las tablas:** nombre, clase y subclase (ItemClass, ItemSubClass), nivel
  de objeto, línea de habilidad de un hechizo (SkillLineAbility → SkillLine), rango
  (`NameSubtext_lang`) y descripción.
- **Etiqueta externa (marcada con `*`):** calidad e `InventoryType` se muestran con su
  valor bruto y una etiqueta de los enums públicos de la API de Blizzard, que no están
  en estas tablas.
- **Nombres de estadística (verificado en el cliente):** `StatModifier_bonusStat_N` se traduce con
  `Enum.BonusStatIndex` del archivo de Blizzard
  `Interface/AddOns/Blizzard_APIDocumentationGenerated/ItemConstantsDocumentation.lua`
  (FileDataID 4637111) del propio cliente `wowf 1.60.1.70938`, obtenido el 2026-11-13 con la ruta
  permitida `GET /api/casc/4637111?version=1.60.1.70938` (sha256 `ae3b654c…092e`). 142 valores,
  copiados en `BONUS_STAT_NAMES` de `query.py`. Del mismo archivo sale `Enum.ItemBind` para
  `Bonding` (`BIND_NAMES`: 1 = OnAcquire, 2 = OnEquip, 4 = Quest…). Si una build futura cambia el enum, hay que
  volver a comprobarlo.
- **En bruto, sin decodificar:** la **cantidad** de cada estadística (`StatPercentEditor_N` es el
  reparto del presupuesto; el valor final depende de tablas por nivel de objeto que no se
  descargan) y el daño del arma. `ItemDelay`, `SellPrice`, `SchoolMask`, etc. se
  imprimen en bruto.
- Las descripciones de hechizos son plantillas (`$s1`) sin resolver.

## Advertencias

- **Solo datos del cliente.** No hay misiones, botín, tasas de caída, vendedores,
  entrenadores, precios de subasta ni ubicaciones: son datos del servidor.
- **Objetos ocultos.** Blizzard oculta en el cliente una parte de los objetos de Forever
  (~40 % según la comunidad) hasta que se descubren. En `1.60.1.70938`, 12 683 de los
  32 008 IDs de `Item` no tienen fila en `ItemSparse` (sin nombre en el cliente). Que un
  objeto no aparezca no prueba que no exista.
- `RequiredLevel` vale 0 en muchos objetos de nivel bajo (p. ej. Jagged Dagger); puede que
  el requisito esté en otra tabla. No se interpreta.
- Hay varios hechizos con el mismo nombre (p. ej. cuatro «Shank»: dos antiguos sin línea
  de habilidad y dos rangos de Combat). Los datos no dicen cuál está activo en juego.
- El estado nunca es en tiempo real: toda salida indica la build y la fecha de extracción.
