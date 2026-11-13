# Matriz de addons

**Última verificación web:** 2026-11-13 (páginas de proyecto de CurseForge; ver matriz ampliada)
**Regla:** ningún addon cuenta como funcional hasta probarlo en el juego. «Funciona en Forever» solo se completa con una prueba propia.

| Addon | Fuente | Versión/build | Instala | Carga sin errores | Funciona en Forever | Datos exportables | Formato/ruta | Decisión |
|---|---|---|---|---|---|---|---|---|
| Dossier: Your Character, Ready for AI | [CurseForge](https://www.curseforge.com/wow/addons/dossier-your-character-ready-for-ai), [GitHub](https://github.com/cyork95/wow-forever-command-center) | 2.2.18 (2026-10-05), cliente 1.60.1, solo flavor Forever | No probado | No probado | No probado | Declarados: nivel, zona, oro, equipo, bolsas, banco, profesiones, misiones, talentos, hechizos, kills, correo, lockouts, tareas, notas, lista de compra, sesiones, biografía | Texto para copiar con `/dossier`; según el repo, SavedVariables por personaje `Dossier.lua` (antes de 2.0.0 `AIExport.lua`). Formato interno por observar | Recomendado (export principal) |
| Wowdee | [CurseForge](https://www.curseforge.com/wow/addons/wowdee), [sitio](https://wowdee.com) | Beta 1.1.7 (2026-11-13), cliente 1.60.1 | No probado | No probado | No probado | Sin exportación documentada (solo importa barras desde la web) | Por observar | Recomendado (asistente in-game, alfa) |
| Auctionator | [CurseForge](https://www.curseforge.com/wow/addons/auctionator) | 12.1.5 (2026-11-12), Forever listado | No probado | No probado | No probado | Dossier lo admite como complemento para precios de bolsas | Por observar | Recomendado |
| Questie | [CurseForge](https://www.curseforge.com/wow/addons/questie) | v12.8.0 (2026-11-12), Forever y 1.60.1 listados | No probado | No probado | No probado | Pendiente | Pendiente | Recomendado; solapa en parte con Wowdee |
| Baganator | [CurseForge](https://www.curseforge.com/wow/addons/baganator) | 12.1.5 (2026-11-13), Forever listado; requiere Syndicator | No probado | No probado | No probado | Syndicator (dependencia) es complemento opcional de Dossier | Pendiente | Recomendado |
| GatherMate2 | [CurseForge](https://www.curseforge.com/wow/addons/gathermate2) | 1.52.6 (2026-11-12), Forever listado | No probado | No probado | No probado | Pendiente | Pendiente | Recomendado (Mining) |
| TomTom | [CurseForge](https://www.curseforge.com/wow/addons/tomtom) | v4.4.1 (2026-11-07), Forever listado | No probado | No probado | No probado | Pendiente | Pendiente | Opcional |
| InfiniteSync | Pendiente | Pendiente | No probado | No probado | No probado | Pendiente | Pendiente | Aplazado: git cubre el transporte |

## No confundir: otros addons llamados Dossier

No instalar estos; registran a otros jugadores, no tu personaje.

| Addon | Autor | Función |
|---|---|---|
| [Dossier Forever](https://www.curseforge.com/wow/addons/dossier-forever) | Roger_Deth | Notas y valoraciones de jugadores |
| [Dossier: Your Personal Player Archive](https://www.curseforge.com/wow/addons/dossier-your-personal-player-archive) | Roger_Deth | Archivo de perfiles de jugadores |
| [PlayerDossier](https://www.curseforge.com/wow/addons/playerdossier) | NiGhTwAlKeR559 | Notas y lista de ignorados |

## Evidencia del entorno

| Dato | Valor | Fuente | Confianza |
|---|---|---|---|
| Base del cliente | UI y API de la era Midnight | [Warcraft Tavern](https://www.warcrafttavern.com/forever/news/wow-forever-loads-your-retail-addons-keybinds/), [Wowdee](https://wowdee.com/articles/wow-forever-addons) | Media: falta fuente de Blizzard |
| Versión e interface | 1.60.1 / 16001 | [Wowdee](https://wowdee.com/articles/wow-forever-addons), CurseForge | Media |
| Carpeta de addons | `_forever_/Interface/AddOns` (`_classic_beta_` en la beta) | [Wowdee: descarga](https://wowdee.com/download) | Media: confirmar en el PC |
| Fallo de carga de ajustes | Reportado desde ~2026-09-18; corrección sin confirmar | [Wowdee](https://wowdee.com/articles/wow-forever-addons) | Baja: confirmar en el PC |

## Notas por addon

### Dossier

- MIT, sin dependencias obligatorias. Descargas: 169 (2026-11-09) → 216 (2026-11-13).
- Complementos opcionales declarados (cada uno con interruptor): Journalator, Altoholic, Syndicator, AllTheThings, Nova Instance Tracker, Profession Master, Auctionator, Talents Forever, KillDex, Memento.
- La ventana muestra un recuento aproximado de tokens; `/dossier off` apaga funciones.
- El repo de GitHub (295 commits, 15 issues abiertos, sin releases, licencia no visible en la portada) describe además un escaneo que produce JSON para una hoja de cálculo; eso es parte del proyecto del autor, no del addon. No verificado.
- Conserva las últimas 20 sesiones.
- Banco y profesiones solo se actualizan al abrir esas ventanas.
- El export detallado añade IDs de objetos, hechizos y misiones.
- Su última versión es anterior al lanzamiento reportado del 2026-11-04: comprobar que funcione.

### Wowdee

- MIT. 103 437 descargas (2026-11-13). En alfa; tras actualizar con archivos nuevos exige reiniciar el juego (no basta `/reload`). Comando `/wowdee`.
- Funciones declaradas: guía 1–60 con tracker, diario de misiones, 20+ mazmorras, recomendaciones de equipo, precios de subasta e historial, beneficio de crafteo, inventario entre personajes, automatizaciones opcionales (misiones, vender basura, reparar, entrenar). Su página dice que todo se queda en el juego y que no usa internet.
- Declara seguimiento de oro, bolsas, bancos, subastas, misiones, sesiones y kills. Son funciones declaradas por el desarrollador.
- Su base de objetos podría servir como catálogo si su contenido es aprovechable; por inspeccionar.

## Matriz ampliada (2026-11-13)

Verificado en la página de proyecto de CurseForge el 2026-11-13. «Forever listado» = el flavor Forever aparece en CurseForge; **no** significa que funcione. Nada probado en el juego. «1.60.1 visible» indica si la página muestra esa versión del juego (muchas lo ocultan tras "+N versiones").

| Addon | Fuente | Versión (fecha) | Forever listado | 1.60.1 visible | Autor | Descargas | Licencia | Dependencias | Propósito | Decisión |
|---|---|---|---|---|---|---|---|---|---|---|
| Dossier: Your Character, Ready for AI | [CF](https://www.curseforge.com/wow/addons/dossier-your-character-ready-for-ai) | 2.2.18 (2026-10-05) | Sí (solo Forever) | Sí | coyos | 216 | MIT | Ninguna | Export del personaje para IA | Recomendado |
| Wowdee | [CF](https://www.curseforge.com/wow/addons/wowdee) | Beta 1.1.7 (2026-11-13) | Sí (solo Forever) | Sí | wowdee | 103 437 | MIT | Ninguna listada | Asistente in-game todo en uno | Recomendado |
| Questie | [CF](https://www.curseforge.com/wow/addons/questie) | v12.8.0 (2026-11-12) | Sí | Sí | TheCrux_BB y equipo | 221,7 M | GPLv3 | No visible | Misiones en mapa y NPC útiles | Recomendado |
| Leatrix Plus | [CF](https://www.curseforge.com/wow/addons/leatrix-plus) | 1.60.30-forever (2026-11-11) | Sí | No (archivo propio de Forever) | Leatrix | 77,4 M | All Rights Reserved | No visible | Calidad de vida (vender grises, reparar, zoom…) | Recomendado |
| BugSack + BugGrabber | [CF](https://www.curseforge.com/wow/addons/bugsack) | v12.1.9 (2026-10-26) | Sí | No | Funkeh | 18,1 M | All Rights Reserved | BugGrabber (obligatoria) | Capturar errores Lua (diagnóstico) | Recomendado |
| Baganator | [CF](https://www.curseforge.com/wow/addons/baganator) | 12.1.5 (2026-11-13) | Sí | No | plusmouse | 42,9 M | All Rights Reserved | Syndicator | Bolsas por categorías | Recomendado |
| Syndicator | [CF](https://www.curseforge.com/wow/addons/syndicator) | 12.1.5 (2026-11-08) | Sí | No | plusmouse | 30,9 M | All Rights Reserved | No visible | Inventario entre personajes; backend de Baganator | Recomendado (dependencia) |
| Auctionator | [CF](https://www.curseforge.com/wow/addons/auctionator) | 12.1.5 (2026-11-12) | Sí | No | plusmouse | 211,4 M | All Rights Reserved | No visible | Subasta: escaneo y precios | Recomendado |
| GatherMate2 | [CF](https://www.curseforge.com/wow/addons/gathermate2) | 1.52.6 (2026-11-12) | Sí | No | moonfann, nevcairiel, Xinhuan | 36,0 M | All Rights Reserved | No visible (opcionales: Routes, GatherMate2_Data) | Registrar nodos de minería | Recomendado |
| Leatrix Maps | [CF](https://www.curseforge.com/wow/addons/leatrix-maps) | 1.60.31-forever (2026-11-12) | Sí | No | Leatrix | 44,1 M | All Rights Reserved | No visible | Coordenadas de jugador y cursor en el mapa | Recomendado |
| What's Training? | [CF](https://www.curseforge.com/wow/addons/whats-training) | 2.5.6 (2026-11-13) | Sí | Sí | Fusionpit | 13,96 M | MIT | No visible | Hechizos y recetas por entrenar en el libro | Recomendado |
| Forever Quest Tint | [CF](https://www.curseforge.com/wow/addons/forever-quest-tint) | 0.7.3 (2026-11-10) | Sí (solo Forever) | Sí | xanastar | 512 379 | GPLv3 | Ninguna | Marca misiones nuevas de Forever | Opcional |
| DungeonJournal | [CF](https://www.curseforge.com/wow/addons/dungeonjournal) | DungeonJournal 2.0.5 (2026-11-13) | Sí | Sí | ExehnTV | 10,1 M | All Rights Reserved | No visible | Misiones y botín por mazmorra | Opcional (útil desde RFC/WC) |
| TomTom | [CF](https://www.curseforge.com/wow/addons/tomtom) | v4.4.1 (2026-11-07) | Sí | No | jnwhiteh | 93,1 M | All Rights Reserved | No visible | Flecha a coordenadas | Opcional |
| Details! | [CF](https://www.curseforge.com/wow/addons/details) | 12.1.5 (2026-11-09) | Sí | No | Terciob | 376,4 M | All Rights Reserved | No visible | Medidor de daño y amenaza | Opcional (medidor integrado basta en solitario) |
| DBM | [CF](https://www.curseforge.com/wow/addons/deadly-boss-mods) | 12.1.23 (2026-11-13) | Sí | No | MysticalOS | 642,8 M | All Rights Reserved | Paquete aparte "Forever and Vanilla Raid Mods" para raids | Avisos de jefes | Opcional (mazmorras) |
| Platynator | [CF](https://www.curseforge.com/wow/addons/platynator) | 12.1.5 (2026-11-12) | Sí | No | plusmouse | 19,2 M | All Rights Reserved | No visible | Nameplates | Opcional |
| Plater | [CF](https://www.curseforge.com/wow/addons/plater-nameplates) | Plater-v663 (2026-11-04) | Sí | No | Terciob / cont1nuity | 105,2 M | All Rights Reserved | No visible | Nameplates muy configurables | Opcional (elegir uno: Plater o Platynator) |
| AtlasLoot Classic Forever | [CF](https://www.curseforge.com/wow/addons/atlasloot-forever) | 1.3.8 (2026-11-13) | Sí | Sí | Sliccer | 9,4 M | GPLv2 | No visible | Tablas de botín y BiS | Opcional |
| Better Vendor Price | [CF](https://www.curseforge.com/wow/addons/better-vendor-price) | v2.1.3 (2026-10-25) | Sí | No | MooreaTV | 4,9 M | LGPLv3 | Ninguna (opcional AHDB) | Precio de vendedor; señala el objeto más barato para tirar sin destruir nada | Opcional |
| MinimapButtonButton | [CF](https://www.curseforge.com/wow/addons/minimapbuttonbutton) | 1.24.17 (2026-11-06) | Sí | No | syndenbock | 18,4 M | All Rights Reserved | No visible | Agrupa botones del minimapa | Opcional |
| ForeverAuras | [CF](https://www.curseforge.com/wow/addons/foreverauras) | 1.3.9 (2026-11-11) | Sí (solo Forever) | Sí | Neroxrw | 1,09 M | GPLv2 | No visible | Fork de WeakAuras para Forever | Opcional (en desarrollo) |
| Rogue HUD | [CF](https://www.curseforge.com/wow/addons/rogue-hud) | 0.1.2 (2026-11-10) | Sí (solo Forever) | Sí | JamesLahey | 379 | All Rights Reserved (uso libre) | No visible | Energía, combos, venenos con aviso | Opcional (poco historial) |
| Cutthroat | [CF](https://www.curseforge.com/wow/addons/cutthroat) | 1.0.0 (2026-10-01) | Sí (solo Forever) | Sí | Hexx98 | 763 | All Rights Reserved | No visible | Combos y temporizadores SnD/Rupture/Expose | Opcional (poco historial) |
| Wick's Poisons and Things | [CF](https://www.curseforge.com/wow/addons/wicks-poisons-and-things) | v0.9.1 (2026-09-27) | Sí (solo Forever) | Sí | Wicksmods | 272 | MIT | WickCore | Venenos por arma, teclas para aplicarlos, combos | Opcional (poco historial) |
| Journey | [CF](https://www.curseforge.com/wow/addons/journey) | 4.00.07 (2026-11-12) | Sí | Sí | journeyaddon / TomCat | 96 293 | All Rights Reserved | No visible | Guía de subida 1–20 con flecha | Opcional (solapa con Wowdee) |
| ForeverCodex | [CF](https://www.curseforge.com/wow/addons/forevercodex) | v1.0.32 (2026-10-16) | Sí (solo Forever) | Sí | Loyftwa | ~1650 | All Rights Reserved | Ninguna (librerías incluidas) | Base de recetas compartida por hermandad | Opcional (sin hermandad no aporta) |
| EllesmereUI | [CF](https://www.curseforge.com/wow/addons/ellesmereui) | v9.8.4 (2026-11-10) | Sí | No | Ellesmere | 10,9 M | Licencia propia | No visible | Reemplazo completo de UI | Opcional (no en la primera instalación) |
| TradeSkillMaster | [CF](https://www.curseforge.com/wow/addons/tradeskill-master) | v4.15.7 (2026-11-13) | Sí ("WoW Forever" en archivos recientes) | No | Sapu94 y equipo | desconocido | All Rights Reserved | desconocido | Subasta avanzada | Pendiente (guías dicen que no hay versión Forever: conflicto) |
| Forever Data Protect | [CF](https://www.curseforge.com/wow/addons/forever-data-protect) | 1.0.1 (2026-10-02) | Sí | Sí | Uggezen | 286 | MIT | Script PowerShell externo | Workaround del fallo de SavedVariables | Evitar salvo que se reproduzca el fallo |
| ForeverSVBridge | [CF](https://www.curseforge.com/wow/addons/foreversvbridge) | sin número (2026-09-24) | Beta de Forever (sin build) | No | Konigtx | 0 | MIT | `setup.bat` + junction | Workaround del fallo de SavedVariables | Evitar |
| ForeverSVFix | — (404 en CurseForge) | desconocido | desconocido | — | desconocido | — | — | — | Citado por Wowdee | Pendiente (no localizado) |
| WeakAuras | [CF](https://www.curseforge.com/wow/addons/weakauras-2) | Retail 5.21.1; Classic 5.22.1 | **No** (sin build Forever) | No | Stanzilla | — | — | — | Auras | Evitar |
| Azeroth Forever: World Recorder | [azeroth-db](https://azeroth-db.github.io/world-recorder.html) | desconocido (no localizado en CurseForge) | Se describe como addon de Forever | — | org `azeroth-db` | — | No declarada | Subida manual o uploader de Windows | Crowdsourcing de drops, misiones, vendedores | Evitar por ahora (sube nombre, reino, hermandad, equipo) |

### Sin verificar en su página de proyecto (solo citados por guías)

Titan Panel, ClassicUI Forever, Bartender4, RestedXP Guides (Kami-Labs declara acuerdo comercial), Guidelime, QuestieTrace, BetterBags, ForeverMail, Threat Plates, Cooldown Manager Centered, Musca Auras, Talents Forever, OpenMap, Parrot 3. Decisión: Pendiente.

### Evitar según Kami-Labs (no verificado por nosotros)

OmniCC, OmniBar, OmniCD, Hekili, Skada/Recount originales, Quartz, Auctioneer, AdiBags, Postal, Kui Nameplates, PitBull4, ForeverCompat (riesgo de taint). Fuente: [[src-kamilabs-addons-wow-forever]].

## Restricciones de la API en Forever

| Afirmación | Estado | Fuente |
|---|---|---|
| Forever comparte la arquitectura de UI de Mainline (12.1.5) con secret values y cambios de auras | unknown (segunda mano: Discord de UI, 2026-09-16) | [[src-wowdee-articles-wow-forever-addons]] |
| Combos y buffs son "secret" en combate; los addons no pueden leerlos ni calcular con ellos | unknown (declarado por el autor de Cutthroat) | [Cutthroat](https://www.curseforge.com/wow/addons/cutthroat) |
| Vida, amenaza, auras y hechizos enemigos secretos en combate; combat log cerrado | unknown | [[src-kamilabs-addons-wow-forever]] |
| Medidor de daño y Cooldown Manager integrados | probable (Method + Wowdee) | [[src-method-understanding-wow-forevers-ui]], [[src-wowdee-articles-wow-forever-addons]] |
| No se encontró ninguna declaración pública de Blizzard en foros sobre addons en Forever | — | búsqueda del 2026-11-13 |

## Fallo de SavedVariables

- Reportado en la beta desde el 2026-09-18 ([[src-blizzard-forum-ui-addon-settings-wiped-2353992]]).
- Jugadores dicen que quedó arreglado en la build 1.60.1.70009 (2026-09-23) ([[src-blizzard-forum-savedvariables-not-restored-2356559]]); el autor de Forever Data Protect también cree que ya no hace falta, sin confirmarlo. Wowdee (2026-10-06) lo daba por no confirmado. Sin palabra de Blizzard.
- Decisión: no instalar workarounds. Copia de seguridad de `WTF` antes de instalar addons. Si tras reiniciar se pierden ajustes, documentarlo y reevaluar.

## Conflictos detectados (no registrados aún en [[Conflicts]])

1. **TSM**: Kami-Labs y otras guías dicen que no hay versión Forever; CurseForge lista el flavor Forever (v4.15.7, 2026-11-13). Sin probar si su servicio de precios cubre Forever.
2. **GatherMate2**: la guía de oro de Mein-MMO (2026-11-03) dice que no hay versión Forever; CurseForge lista Forever (1.52.6, 2026-11-12).
3. **Amenaza en Details!**: Mein-MMO lo recomienda por la amenaza; Kami-Labs dice que la amenaza es secreta en combate.
4. **SavedVariables**: arreglado según jugadores (build 70009) frente a "sin confirmar" (Wowdee, 2026-10-06).
5. **Carpeta de addons tras el lanzamiento**: Mein-MMO indica `_forever_/Interface/AddOns`; Wowdee (octubre) no la tenía confirmada.

## Fallos de acceso (2026-11-13)

- Icy Veins, "Set Up Your WoW Forever UI Before Launch With These 9 Addons": 403. No citado.
- `curseforge.com/wow/addons/foreversvfix`: 404.
- Mein-MMO: URL alemana inicial redirigida; se usó la edición inglesa.

## Fuentes (2026-11-13)

Páginas de proyecto de CurseForge enlazadas en la matriz; [[src-wowdee-articles-wow-forever-addons]], [[src-meinmmo-wow-forever-the-10-most-important-addons]], [[src-kamilabs-addons-wow-forever]], [[src-warcrafttavern-news-wow-forever-loads-your-retail-addons-keybinds]], [[src-blizzard-forum-savedvariables-not-restored-2356559]], [[src-blizzard-forum-ui-addon-settings-wiped-2353992]], [[src-method-class-guides-combat-rogue-interface-addons-and-macros]], [[src-method-understanding-wow-forevers-ui]]; [Azeroth DB World Recorder](https://azeroth-db.github.io/world-recorder.html); [GitHub de Dossier](https://github.com/cyork95/wow-forever-command-center).

Recomendación de instalación para el personaje: [[Recommended-Addons]].
