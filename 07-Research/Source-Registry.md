---
type: topic
tags: [forever, research, sources]
status: confirmed_forever
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://azeroth-db.github.io/
  - https://azeroth-db.github.io/sitemap.xml
  - https://azeroth-db.github.io/why.html
  - https://azeroth-db.github.io/world-recorder.html
  - https://api.github.com/orgs/azeroth-db/repos
  - https://azeroth.wiki/
  - https://azeroth.wiki/robots.txt
  - https://azeroth.wiki/terms
  - https://azeroth.wiki/sitemap.xml
  - https://wowfwiki.com/
  - https://wowfwiki.com/robots.txt
  - https://wowfwiki.com/api.php?action=query&meta=siteinfo&siprop=general|statistics|rightsinfo&format=json
  - https://wowfwiki.com/sitemap.xml
  - https://wowfwiki.com/wiki/Project:Data_policy
  - https://wowfwiki.com/wiki/Project:About
  - https://wowfwiki.com/wiki/Project:Database_coverage
  - https://wowfwiki.com/wiki/Project:General_disclaimer
  - https://wowfwiki.com/wiki/Project:Copyrights
  - https://wowfwiki.com/wiki/Project:Sources
  - https://wowfwiki.com/wiki/Datamined_data
  - https://wowforeverhelper.com/
  - https://wowforeverhelper.com/robots.txt
  - https://wowforeverhelper.com/sitemap-index.xml
  - https://wowforeverhelper.com/sitemap-0.xml
  - https://wowforeverhelper.com/about/data
  - https://wowforeverhelper.com/about/legal
  - https://foreverdb.net/
  - https://foreverdb.net/robots.txt
  - https://foreverdb.net/llms.txt
  - https://foreverdb.net/developers
  - https://foreverdb.net/about
  - https://foreverdb.net/sitemap.xml
  - https://foreverdb.net/sitemap-pages.xml
  - https://foreverdb.net/downloads/addon-manifest.json
  - https://eternadex.com/en/
  - https://eternadex.com/robots.txt
  - https://eternadex.com/sitemap-index.xml
  - https://eternadex.com/en/ueber/
  - https://eternadex.com/en/impressum/
  - https://eternadex.com/en/beitragen/
  - https://www.wowforeverpath.com/guides/
  - https://www.wowforeverpath.com/robots.txt
  - https://wowforeverpath.com/sitemap.xml
  - https://www.wowforeverpath.com/en/about
  - https://www.wowforeverpath.com/en/legal/terms
  - https://foreverguide.app/guides
  - https://foreverguide.app/robots.txt
  - https://foreverguide.app/sitemap.xml
  - https://foreverguide.app/terms
  - https://foreverguide.app/credits
  - https://foreverguide.app/disclaimer
  - https://theforeverera.com/en/guides/
  - https://theforeverera.com/robots.txt
  - https://theforeverera.com/sitemap-index.xml
  - https://theforeverera.com/sitemap-pages-0.xml
  - https://theforeverera.com/en/about/
related: ["[[Sources]]", "[[Conflicts]]", "[[Addons]]", "[[Patch-Changes]]"]
---

# Registro de fuentes de datos — WoW Forever

> [!success] Confirmado en Forever
> Que estas fuentes existen, sus reglas de `robots.txt`, sus términos y sus cifras se observaron el 2026-11-13. Las valoraciones de calidad y la estrategia son **juicio del investigador** (inferido), no un hecho.

## Resumen
- Ningún sitio de la comunidad publica sus **datos** con una licencia libre clara. Las únicas excepciones parciales: la prosa de **wowforeverhelper** (CC BY-SA 4.0), el conjunto de datos de **wowforeverpath** (CC BY-SA 4.0, derivado de warcraft.wiki.gg) y los archivos de datos del addon de **ForeverDB** (GPL-3.0 con atribución, según su `robots.txt`). **wowfwiki** es MediaWiki, pero **no declara licencia**.
- Acceso masivo permitido: los sitemaps de todos los sitios (ninguno los bloquea), `api.php` de wowfwiki (no está bloqueado en robots), `llms.txt` y el manifiesto del addon de ForeverDB, y la API de ForeverDB **con clave**. La clave exige iniciar sesión con Battle.net y la aprobación del operador, así que la decide el usuario, no un agente.
- **Prohibido por términos**: el scraping o las peticiones masivas en **foreverguide.app** y **azeroth.wiki** (salvo sus interfaces publicadas). **Wowhead** bloquea a los bots de Anthropic: no se consulta.
- Casi todas las bases de datos leen el **cliente del juego** (la misma raíz). Cuando les falta un dato del servidor (misiones, drops, NPC), ForeverDB y The Forever Era rellenan con **CMaNGOS classic-db** (Classic 1.12). Eso es `probable_classic`, nunca `confirmed_forever`.
- La más fresca y completa a fecha de hoy es **ForeverDB** (build 1.60.1.70938, extraída el 2026-11-13). **wowforeverhelper** y **wowfwiki** son instantáneas de antes del lanzamiento.

## Tabla resumen

| # | Fuente | Operador (declarado) | Específica de Forever | Origen de los datos | Build / frescura | Licencia de reutilización | Acceso masivo permitido | Mejor uso en la bóveda |
|---|---|---|---|---|---|---|---|---|
| 1 | Azeroth DB (azeroth-db.github.io → azeroth.wiki) | No declarado (org de GitHub `azeroth-db`) | Sí | No declarado para el cliente; datos de jugadores vía el addon World Recorder | Repos actualizados el 2026-11-05 | Código MCP/skill: MIT. Datos: los términos prohíben redistribuirlos | Sitemaps, feeds, JSON públicos y APIs documentadas (según sus términos); `/api/` bloqueado en robots | Profesiones (orden de subida), calculadora de talentos y Legacy, nodos de recolección |
| 2 | wowfwiki.com | No declarado; "independent community wiki" | Sí | Archivo del cliente beta (builds 69913–70374) + "licensed export" de talentos y hechizos + artículos curados con fuente | Base congelada en beta; portada y noticias del 2026-11-13 | **No declarada** (`rightsinfo` vacío; no existen páginas de copyright ni de aviso legal) | `api.php` y sitemap (1418 URL) permitidos por robots | Consulta puntual de IDs y de artículos curados con fuente y estado de revisión |
| 3 | wowforeverhelper.com | No declarado; fan, no comercial | Sí | Tablas del cliente vía exportaciones de wago.tools, con SHA-256 | Build 1.60.1.70532 (prelanzamiento), generado el 2026-10-23 | Prosa propia: CC BY-SA 4.0 (declarada como "intended"); el dataset tiene licencia por anunciar | Sitemap (17 715 objetos); `/search` y `/data/` bloqueados | Stats de objetos con procedencia verificable; cambios de hechizos frente a Classic |
| 4 | foreverdb.net | No declarado; fan, con anuncios | Sí | Cliente (build 1.60.1.70938) + hotfixes + addon de jugadores + CMaNGOS como respaldo etiquetado | Extraído el 2026-11-13 | Sitio: sin licencia; API: crédito obligatorio en el plan gratuito; datos del addon: GPL-3.0 + atribución | Sitemap, `llms.txt`, manifiesto del addon, API con clave (5000 peticiones/día gratis) | **Base principal** para objetos, misiones (con marca de "visto en Forever"), vendedores y entrenadores |
| 5 | eternadex.com | Elemental Gilde (Múnich), según su Impressum | Sí | Cliente (build 1.60.1.70862) + subidas voluntarias del addon | Datos a 2026-11-07; sitemaps a 2026-11-11 | No declarada | Sitemaps (~2000 URL en inglés); `/entwurf/` bloqueado | Segunda opinión independiente en drops, misiones y NPC por crowdsourcing |
| 6 | wowforeverpath.com | Dominio de contacto kolcu.ai | Sí | warcraft.wiki.gg (CC BY-SA) + resúmenes de Blizzard | Guías "1.60.1 BETA", fechadas el 2026-11-08 | **CC BY-SA 4.0** (dataset adaptado) | Sitemap (12 180 URL, 1015 por idioma) | Poco: es un derivado de warcraft.wiki.gg, no una fuente independiente |
| 7 | foreverguide.app | Un operador particular (contacto personal) | Sí | Cobertura de prensa y beta + datasets de comunidad; "nunca lee el cliente" | Sitemap del 2026-10-18 | Guías propiedad del sitio; los términos **prohíben scraping, bots y peticiones masivas** | Ninguno para nosotros (solo lectura manual) | Contraste puntual; sin uso sistemático |
| 8 | theforeverera.com | Un jugador hispanohablante (sin nombre) | Sí | Tablas del cliente + cachés del servidor beta + CMaNGOS etiquetado | Build 1.60.1.70888 (2026-11-10); detecta la 70938 el 2026-11-13 | No declarada | Sitemaps (3061 URL de páginas); `/mv/` bloqueado | Guías escritas a mano con fuente; cambios frente a Classic; está en español |
| 9 | wowhead.com/forever | Wowhead | Sí | — | — | — | **No: su robots.txt bloquea a los bots de Anthropic** | Solo recortes manuales del usuario |
| 10 | mobalytics.gg/wow-forever, reddit | — | — | — | — | — | No consultados | Solo recortes manuales del usuario |

## 1. Azeroth DB (azeroth-db.github.io / azeroth.wiki)

- **Qué es**: azeroth-db.github.io es una página de presentación de 6 URL (sitemap con `lastmod` 2026-10-12). Las herramientas están en **azeroth.wiki**: calculadora de talentos con Legacy, planificador de Legacy, libro de hechizos, razas, profesiones en orden de subida (con el skill al que cada receta pasa a amarillo y gris), lista de materiales, objetos, equipo, botín de mazmorras por jefe, camping, misiones y quest givers, mapa del mundo con nodos de hierbas y minerales recogidos por jugadores, y un índice de addons.
- **Origen de los datos**: las páginas leídas no dicen de dónde salen los datos del cliente. Sí describen el addon **World Recorder**: registra drops por muerte, recolección, misiones (dador, receptor, texto y recompensas), vendedores, entrenadores y vuelos, y los combina con los de todos los jugadores (crowdsourcing).
- **GitHub (org `azeroth-db`)**: `wowdb-mcp` (MIT; busca objetos, recetas, habilidades y misiones con enlaces a Azeroth DB), `wowdb-skill` (MIT; skill de agente), `world-recorder` (sin licencia detectada por GitHub), `wowdb-search` (extensión de Chrome, sin licencia detectada). Último push: 2026-11-05. Otro revisor está auditando el MCP; aquí no se evalúa su código.
- **Robots** (azeroth.wiki): `/account` y `/api/` bloqueados. Sitemap con 12 archivos; no se procesaron, así que **no se contaron las guías de Forever**.
- **Términos** (azeroth.wiki/terms): prohíben el scraping y la descarga masiva **salvo por las interfaces publicadas** (sitemaps, feeds, APIs documentadas, sus JSON públicos y su app de asistente) y dentro de sus límites. También prohíben republicar la base de datos total o sustancialmente. La licencia MIT cubre el **código** del MCP, **no los datos**.
- **Calidad**: es multi-juego (la cabecera enlaza a FFXIV, GW2 y otros), lo que apunta a una plataforma genérica. Las páginas leídas no muestran build ni fecha de los datos.
- **Mejor para**: orden de subida de profesiones, nodos de recolección observados y planificación de talentos y Legacy. Acceso solo por el MCP o las interfaces que nombran sus términos.

## 2. wowfwiki.com

- **¿MediaWiki?** Sí: **MediaWiki 1.43.9** (siteinfo). `wikiid` foreverwiki.
- **Estadísticas** (siteinfo del 2026-11-13): 57 217 páginas, 56 642 artículos, 61 590 ediciones, 484 imágenes, **1 usuario** activo, 2 administradores. Casi una edición por página y un solo editor: apunta a contenido **generado por un único operador o bot** (inferido).
- **Licencia**: `rightsinfo` vacío. `Project:Copyrights` y `Project:General_disclaimer` **no existen**. El pie de página no menciona ninguna licencia. **No es CC BY-SA**, o al menos no lo declara: hay que tratarlo como "todos los derechos reservados".
- **Robots**: `Allow: /`. **`api.php` no está bloqueado.** El sitemap índice apunta a un único archivo de 1418 URL (las páginas curadas, no las 57 000), de las cuales 9 tienen "guide" en la ruta. Último `lastmod`: 2026-11-13.
- **Origen de los datos** (Project:Database_coverage): 55 191 registros congelados del cliente beta, build 1.60.1.69913, revisados el 2026-09-20/23. Desglose: 17 592 objetos, 29 414 habilidades, 2258 recetas, 1578 misiones, 2658 NPC, 303 monstruos, 1340 zonas, 35 mazmorras, 13 raids. Comparaciones de archivo hasta la build 70374 y auditorías de distribución hasta el 2026-11-13, pero **sin reimportar los registros**. Talentos y hechizos vienen de un "licensed export" de origen no identificado. Algunas misiones se importaron de otros sitios (Warcraft Forever, WoW Forever Talents).
- **Señales de calidad**: tiene una política de datos rigurosa (estados Unverified / Source checked / In-game checked / Needs review; prohíbe trasladar datos de Classic), pero las cifras de la base son **de beta**. La portada cuenta 334 objetos, 174 misiones y 122 NPC curados.
- **Mejor para**: comprobar un ID o leer un artículo curado con su fuente. **No** sirve como fuente de valores actuales.

## 3. wowforeverhelper.com

- **Operador**: no declarado. Proyecto de fans no comercial, sin cookies.
- **Cobertura**: 17 715 objetos, 154 conjuntos, 51 zonas, 33 mazmorras, raids, razas, clases (cambios por habilidad), recetas por profesión y rutas de vuelo. **No incluye misiones, NPC ni fuentes de drop**, por decisión propia: son datos del servidor.
- **Origen**: tablas del cliente Forever (build 1.60.1.70532, producto `wowf`, prelanzamiento) leídas vía **exportaciones de wago.tools**, cada tabla con su SHA-256. Calcula los stats con fórmulas validadas (dice reproducir el 99,3 % de los stats de objetos sin cambios frente a Classic). Etiquetas: Official / Confirmed in game / Datamined / Derived / Community reported / Sources conflict / Unknown. Declara no copiar a Wowhead, Questie ni servidores privados.
- **Frescura**: instantánea del 2026-10-23. La portada todavía muestra "Launch in 12 days", así que **no se ha actualizado desde el lanzamiento**.
- **Licencia**: su prosa propia se publicaría bajo **CC BY-SA 4.0** ("intended"); el dataset tiene "licencia por anunciar".
- **Robots**: `/search` y `/data/` bloqueados. El sitemap tiene 18 040 URL (17 715 objetos, 2 guías, 12 páginas de sistemas).
- **Mejor para**: stats de objetos con procedencia comprobable y la tabla de mazmorras por nivel con desacuerdos marcados (±). Siempre indicar que es una build de prelanzamiento.

## 4. foreverdb.net

- **Operador**: no declarado. Proyecto de fans, financiado con anuncios. Tiene un registro público de correcciones.
- **Cobertura** (llms.txt): 23 686 objetos, 32 121 hechizos, 47 mazmorras y raids, guías de clase (PvE y PvP), misiones, profesiones con mapas de hierbas y minerales, raros, reputación, monturas, entrenadores, vendedores, consumibles, Legacy, BiS, simulador, downrank, macros, tier lists, blue tracker y estado del servidor. Disponible en 5 idiomas, español incluido.
- **Origen**: cliente Forever (build **1.60.1.70938, extraída el 2026-11-13**) con los hotfixes aplicados, posts de Blizzard y el addon ForeverDB de los jugadores. Donde falta un dato de Forever (dadores de misiones, drops, vendedores), usa **CMaNGOS classic-db (GPL-3.0)**, etiquetado "Speculation: Classic data". Su API distingue `seen in WoW Forever` (con número de jugadores) de `Classic data (CMaNGOS)`.
- **Robots**: `/api/`, `/auth/`, `/me`, `/admin` bloqueados para crawlers. Los bots de IA están "welcome" con las mismas reglas. El comentario del robots.txt aclara que esas reglas no restringen la API con clave.
- **API** (/developers): JSON de solo lectura en `/api/v1`, con clave en `X-API-Key`. Para conseguir la clave hay que tener una cuenta de ForeverDB, **iniciar sesión con Battle.net** y pedir acceso explicando el uso. Gratis: 5000 peticiones/día y 30/min, con **crédito obligatorio** ("Data from ForeverDB.net" con enlace). De pago: 5,99 $/mes. Endpoints: meta, items, spells, quests, vendors, poisons, disenchant y más.
- **Otros accesos permitidos**: `llms.txt` y `llms-full.txt` (resumen en texto plano), RSS y un manifiesto del addon con los archivos de datos y su SHA-256 (versión de datos 2026-11-13). Según el robots.txt, esos archivos son GPL-3.0 con cláusula de atribución.
- **Guías**: el sitemap de páginas tiene 6053 URL: 93 `/guide/`, 91 `/class/`, 64 `/bis/`, 4261 `/quest/`, 357 `/rare/`, 57 `/maps/`.
- **Mejor para**: fuente principal de datos estructurados actuales. Usar el campo de origen para separar `confirmed_forever` (visto en Forever) de `probable_classic` (CMaNGOS).

## 5. eternadex.com

- **Operador**: **Elemental Gilde**, Múnich (Impressum). Financiado con anuncios. Sitio en 9 idiomas; los textos que no están en alemán se traducen en parte con IA.
- **Cobertura**: 19 383 objetos, 5167 misiones, NPC, 38 listas de BiS, 31 mazmorras, 8 profesiones, 154 conjuntos, rutas de subida por facción, tier list, planificador de equipo y de Legacy, macros, montar, camping, Waylaid Crates y oro. También publica 6 addons propios en CurseForge.
- **Origen**: archivos del cliente (build **1.60.1.70862**, a 2026-11-07) + posts de Blizzard + **subidas voluntarias** de los SavedVariables de sus addons (drops, ubicaciones, vendedores, textos de misiones). Etiqueta cada dato como "according to Blizzard", "according to the game data", "our assessment" o "according to fan sites". Dice mostrar porcentajes de drop solo cuando hay observaciones suficientes.
- **Licencia**: no declarada. Ofrece tooltips embebibles para otros sitios.
- **Robots**: `/entwurf/` bloqueado. Índice de sitemaps con 834 archivos (todos los idiomas). En inglés hay ~2000 URL: 1125 de objetos, 169 de directorio, 47 de noticias y el resto (~650) temáticas o de guía (61 de niveles, 49 de zonas, 45 de cadenas de misiones, 38 de BiS, 27 de builds, 27 de misiones de mazmorra). `lastmod` máximo: 2026-11-11.
- **Mejor para**: contrastar drops, misiones y NPC con un **segundo pool de crowdsourcing**, independiente del de ForeverDB.

## 6. wowforeverpath.com

- **Operador**: el contacto es una dirección del dominio kolcu.ai. App móvil y web con foro, chat, censo "en vivo" y "War Chest" (packs de apoyo de hasta 1000 $ por transacción y un título personalizado por más de 10 000 $).
- **Cobertura**: talentos, BiS, clases, misiones ("1000+ exclusive quests" + base de Classic con coordenadas), mazmorras, razas, profesiones, lore y atlas.
- **Origen**: según su página de fuentes, la estructura de talentos, la disponibilidad raza/clase y los raciales vienen de revisiones citadas de **warcraft.wiki.gg (CC BY-SA 4.0)**; las notas de cambios son resúmenes de Blizzard.
- **Licencia**: el dataset adaptado se publica bajo **CC BY-SA 4.0**. Términos fechados el 2026-11-02.
- **Frescura**: las guías llevan la etiqueta "1.60.1 BETA" y la fecha 2026-11-08; las fuentes se consultaron hasta el 2026-11-12.
- **Robots**: `Allow: /`. Sitemap con 12 180 URL (1015 por idioma × 12). En inglés: 467 de talentos, 228 de misiones, 176 de lore, 35 de mazmorras, 10 de guías y 9 de clases.
- **Calidad**: es un derivado de wiki con fuerte monetización. **No es independiente** de warcraft.wiki.gg.
- **Mejor para**: casi nada directo. Si hace falta lo que cita, ir a warcraft.wiki.gg (no evaluada en este registro).

## 7. foreverguide.app

- **Operador**: un particular (contacto con un correo personal, que no se reproduce aquí). Premium por 7 $/mes, con un "AI companion".
- **Cobertura**: 13 guías gratuitas (lanzamiento, novedades frente a Classic, Legacy, rulesets y una guía de subida por clase), ruta 1-60, calculadora de talentos y una base pequeña (objetos, misiones y jefes "con nombre").
- **Origen** (créditos): **nunca lee el cliente**. Talentos de datasets de comunidad (wowforevertalents.com, wowclassicforever.info y un export de un usuario), Legacy de Zockify, y zonas, mazmorras y profesiones de cobertura de prensa y beta (Warcraft Tavern, Method, Wowhead, Icy Veins, Kotaku, etc.).
- **Términos**: **prohíben expresamente scripts, bots y peticiones masivas** contra el sitio.
- **Robots**: `/api/` y otros bloqueados. El sitemap tiene 297 URL (41 de guías, 37 de talentos, 126 de herramientas), con `lastmod` máximo del **2026-10-18**.
- **Mejor para**: contraste ocasional leído a mano. Es una fuente **secundaria de secundarias**: no añade independencia frente a Method o Wowhead.

## 8. theforeverera.com

- **Operador**: un jugador (sin nombre), sitio en español, inglés, alemán y francés. Anuncios y Ko-fi.
- **Cobertura**: mapa, objetos, BiS, talentos, cambios frente a Classic (844 documentados), clases, zonas, 29 mazmorras, raids, Merchant's Favor, hierbas y minerales, una "Classic database" separada (misiones, raros, NPC y libros de Classic 1.12), blue tracker, hotfixes, calculadora de Legacy, libro de hechizos y un addon propio.
- **Origen** (about): tablas del cliente por build, procesadas automáticamente; lo que envía el servidor (cachés y hotfixes, **por ahora del servidor beta**) marcado con build y fecha; y **CMaNGOS Classic-DB** para misiones y drops de objetos que ya existían en Classic, marcado "Classic data". Los resúmenes en español de los posts de Blizzard los escribe una IA (hoy DeepSeek). Las guías se escriben y corrigen a mano, citando fuentes.
- **Frescura**: datos de la build 1.60.1.70888 (actualizados el 2026-11-10). Banner del 2026-11-13: nueva build 70938 detectada, "updating the data".
- **Licencia**: no declarada.
- **Robots**: `/mv/` bloqueado. 9 sitemaps. El de páginas tiene 3061 URL; en inglés: 55 de guías, 178 de BiS, 196 de mazmorras, 92 de misiones, 46 de zonas y 40 de recolección.
- **Mejor para**: guías en español con fuente y la tabla de cambios frente a Classic. Sus misiones y drops son mayoritariamente **Classic** y deben etiquetarse `probable_classic`.

## 9. Fuentes solo por recorte del usuario

| Fuente | Motivo | Cómo usarla |
|---|---|---|
| Wowhead (`wowhead.com/forever`) | Su robots.txt bloquea a los bots de Anthropic (verificado por el usuario). **No se consultó.** | Solo recortes del Web Clipper que haga el usuario en `07-Research/inbox/`. Nota: [[Sources]] cita fichas de Wowhead de una investigación anterior; a partir de ahora no se vuelven a consultar automáticamente |
| Mobalytics (`mobalytics.gg/wow-forever`) | No evaluada | Recorte manual del usuario |
| Reddit (r/wowforever y otros) | No evaluada; la herramienta no accedía antes (ver [[Sources]]) | Recorte manual del usuario |

## Grupos de independencia

Dos fuentes del mismo grupo **no cuentan como dos confirmaciones** del mismo dato.

| Grupo | Raíz común | Fuentes | Consecuencia |
|---|---|---|---|
| A. Cliente del juego | Tablas DB2 del cliente Forever | wowforeverhelper (vía wago.tools), ForeverDB, Eternadex, The Forever Era, wowfwiki (beta) y, probablemente, Azeroth DB | Coinciden por construcción en stats, hechizos y recetas. La concordancia solo confirma la lectura del cliente, no lo que pasa en el servidor ni los hotfixes. Comparar **builds**, no sitios |
| B. Respaldo de Classic | CMaNGOS classic-db (GPL-3.0) | ForeverDB (etiquetado "Speculation"), The Forever Era (etiquetado "Classic data") | Siempre `probable_classic`. Si las dos coinciden, solo confirma que Classic era así |
| C1. Crowdsourcing de ForeverDB | Addon ForeverDB | ForeverDB | Pool independiente de C2 y C3; da número de jugadores |
| C2. Crowdsourcing de Eternadex | Addons EternaDex (subida manual) | Eternadex | Independiente de C1 y C3 |
| C3. Crowdsourcing de Azeroth DB | Addon World Recorder | Azeroth DB | Independiente de C1 y C2 |
| D. warcraft.wiki.gg | Wiki de comunidad (CC BY-SA) | wowforeverpath; wowforeverhelper en lo "Community reported" | wowforeverpath = warcraft.wiki.gg |
| E. Prensa y guías de beta | Method, Wowhead, Icy Veins, Warcraft Tavern… | foreverguide.app | No aporta independencia frente a Method |
| F. Blizzard | Posts oficiales | Todas las citan | Ir siempre al post original (ver [[Sources]]) |

Un dato del servidor (drop, posición de un NPC, dador de una misión) solo llega a `confirmed_forever` sin el export del jugador si lo confirman al menos **dos pools distintos** (C1, C2 o C3), o un pool más Blizzard. Esta regla es una propuesta, no política aprobada.

## Estrategia de adquisición

La prioridad del usuario no cambia: Blizzard y los exports del personaje están siempre por encima. Esta clasificación ordena solo las fuentes de este registro, más Method donde aplica.

| Dominio | 1.ª | 2.ª | 3.ª | Evitar o con cuidado | Notas |
|---|---|---|---|---|---|
| Objetos (stats) | ForeverDB (build actual, campo `liveClient`) | wowforeverhelper (procedencia SHA-256, pero prelanzamiento) | Eternadex / The Forever Era | wowfwiki (beta congelada) | Todo es cliente (grupo A): indicar la build |
| Objetos (fuentes y drops) | ForeverDB "seen in Forever" | Eternadex (C2) | Azeroth DB (C3) | Todo lo etiquetado CMaNGOS o "Classic data" | Drop rates solo con número de observaciones; si no, `unknown` |
| Misiones | ForeverDB (dador y receptor con origen y nº de jugadores) | Eternadex (5167 misiones, coordenadas) | Azeroth DB; artículos curados de wowfwiki | The Forever Era y wowforeverpath (base de Classic) | Coordenadas solo citando la fuente; nunca inventarlas |
| NPC, vendedores y entrenadores | ForeverDB (`seen=true`) | Eternadex | Azeroth DB | wowforeverhelper no tiene NPC | Los precios de vendedor de ForeverDB vienen del addon de jugadores |
| Hechizos y talentos | ForeverDB (hechizos + `liveClient`) | The Forever Era (spellbook frente a Classic) / wowforeverhelper (cambios por habilidad) | Azeroth DB (calculadora y Legacy) | wowforeverpath (derivado), foreverguide (secundario), "licensed export" de wowfwiki (origen desconocido) | Cruzar con las notas de Blizzard de [[Patch-Changes]] |
| Guías | Method (ya en uso) | ForeverDB (93 guías) / The Forever Era (55 guías en inglés, también en español) | Eternadex | foreverguide (sin uso sistemático) | Fichas `src-` según [[Vault-Guide]], con palabras propias |
| Profesiones | Azeroth DB (orden de subida, colores) | ForeverDB (recetas, mapas de hierbas y minerales) | wowforeverhelper (recetas del cliente) / The Forever Era / Eternadex (rutas con lista de compra) | — | Costes de materiales: solo desde los exports de AH del jugador |
| BiS | Method | ForeverDB (64) / The Forever Era (178) | Eternadex (38) | — | Es opinión editorial: confianza `low` y rango de nivel explícito |
| Mapas y recolección | ForeverDB (/maps, /rares) | Azeroth DB (nodos recogidos por jugadores) | The Forever Era (hierbas y minerales) / Eternadex | — | Coordenadas solo con fuente y fecha |

Canales técnicos por fuente:
1. **Sitemaps** (todos permitidos): sirven para descubrir URL y fechas `lastmod`. Descargar el índice no autoriza a descargar cada página en bloque cuando los términos lo prohíben (foreverguide.app, azeroth.wiki).
2. **ForeverDB**: `llms.txt` / `llms-full.txt` para resúmenes. La API, solo si el usuario decide pedir la clave él mismo (requiere Battle.net y aceptar el crédito); respetar 30 peticiones/min.
3. **wowfwiki `api.php`**: permitido por robots, pero sin licencia. Usarlo solo para consultas puntuales (IDs, una página), con ritmo bajo, y guardar hechos con palabras propias, nunca volcados.
4. **Azeroth DB**: a través del MCP (cuando termine la auditoría) o las interfaces que nombran sus términos; nunca `/api/` por crawler.

## Restricciones

- **No consultar wowhead.com** de ninguna forma automática: su robots.txt bloquea a los bots de Anthropic. Solo recortes del usuario.
- No acceder a rutas bloqueadas: wowforeverhelper `/search` y `/data/`; foreverdb `/api/` (sin clave), `/auth/`, `/me` y `/admin`; foreverguide `/api/` y `/characters`; eternadex `/entwurf/`; theforeverera `/mv/`; azeroth.wiki `/api/` y `/account`.
- **foreverguide.app**: nada de scripts, bots ni peticiones masivas (lo prohíben sus términos). Solo lectura manual puntual.
- **azeroth.wiki**: nada de scraping ni descarga masiva fuera de sus interfaces publicadas. No republicar su base de datos.
- **ForeverDB API**: no pedir clave ni iniciar sesión con Battle.net sin que el usuario lo decida. Si se usa, poner el crédito "Data from ForeverDB.net" con enlace y respetar los límites (429 → esperar `Retry-After`; 402 → parar).
- No esquivar 403, rate limits, anti-bot (Cloudflare), logins ni paywalls. Sin proxies ni cambios de User-Agent para colarse. Si un sitio bloquea, se anota aquí y se sigue con otro.
- **Licencias**: solo wowforeverpath (dataset) y la prosa de wowforeverhelper son CC BY-SA 4.0, y los datos del addon de ForeverDB son GPL-3.0. Todo lo demás (wowfwiki, Eternadex, The Forever Era, foreverguide, Azeroth DB) debe tratarse como todos los derechos reservados: en la bóveda, hechos con palabras propias y la URL. Nunca copiar tablas ni párrafos. Los recortes completos van a `07-Research/inbox/` (fuera de git).
- **No usar addons de recogida** (World Recorder, ForeverDB, EternaDex) ni el cliente Lexicon hasta revisarlos según [[Addons]] y CLAUDE.md. Sus subidas incluyen datos del personaje (World Recorder: nombre, reino, hermandad).
- Todo lo que venga de CMaNGOS o esté etiquetado "Classic data" o "Speculation" entra como `probable_classic`, nunca `confirmed_forever`.
- No contar dos fuentes del mismo grupo de independencia como confirmación doble.

## Fuentes

| URL | Tipo | Fecha de la página/datos | Consultada | ¿Anterior al 2026-11-02? |
|---|---|---|---|---|
| https://azeroth-db.github.io/ (+ sitemap, why, world-recorder) | Presentación de base de datos | sitemap 2026-10-12 | 2026-11-13 | Sí |
| https://api.github.com/orgs/azeroth-db/repos | Metadatos de GitHub | push 2026-11-05 | 2026-11-13 | No |
| https://azeroth.wiki/ (+ robots, terms, sitemap) | Base de datos / términos | sin fecha visible | 2026-11-13 | desconocido |
| https://wowfwiki.com/ (+ robots, siteinfo, sitemap, páginas Project:*, Datamined_data) | Wiki (MediaWiki) | portada editada el 2026-11-07; noticias del 2026-11-13; base de beta | 2026-11-13 | Mixto |
| https://wowforeverhelper.com/ (+ robots, sitemaps, about/data, about/legal) | Base de datos | snapshot 2026-10-23 | 2026-11-13 | Sí |
| https://foreverdb.net/ (+ robots, llms.txt, developers, about, sitemaps, addon-manifest.json) | Base de datos + guías + API | build extraída el 2026-11-13 | 2026-11-13 | No |
| https://eternadex.com/en/ (+ robots, sitemaps, ueber, impressum, beitragen) | Base de datos + guías | datos al 2026-11-07 | 2026-11-13 | No |
| https://www.wowforeverpath.com/guides/ (+ robots, sitemap, en/about, en/legal/terms) | App de guías | guías del 2026-11-08 | 2026-11-13 | No |
| https://foreverguide.app/guides (+ robots, sitemap, terms, credits, disclaimer) | Guías | sitemap 2026-10-18 | 2026-11-13 | Sí |
| https://theforeverera.com/en/guides/ (+ robots, sitemaps, en/about) | Guías + base de datos | build 70888, 2026-11-10 | 2026-11-13 | No |

## Preguntas pendientes
- ¿De dónde salen los datos del cliente de Azeroth DB? Sus páginas no lo dicen. Esperar a la auditoría del MCP.
- ¿Quién emite el "licensed export" de talentos y hechizos de wowfwiki, y bajo qué licencia?
- ¿Publicará wowforeverhelper su dataset con licencia abierta (dice "antes de cualquier open data release")?
- No se verificó el `NOTICE.txt` del addon de ForeverDB (GPL-3.0 + atribución): solo consta el comentario de su robots.txt.
- No se contaron las guías de Forever de azeroth.wiki (12 sitemaps sin procesar).
- ¿Decide el usuario pedir una clave de la API de ForeverDB? Requiere su cuenta de Battle.net.
- warcraft.wiki.gg (raíz del grupo D) no está evaluada en este registro.
