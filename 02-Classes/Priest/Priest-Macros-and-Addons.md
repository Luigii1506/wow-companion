---
type: topic
tags: [forever, priest, macros, addons, ui]
faction: both
status: unknown
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://www.method.gg/wow-forever/class-guides/shadow-priest/interface-addons-and-macros
  - https://www.method.gg/wow-forever/class-guides/holy-priest/interface-addons-and-macros
related: ["[[Priest]]", "[[Shadow-Priest]]", "[[Holy-Priest]]", "[[Priest-Leveling]]"]
---

# Priest — Macros y addons

> [!question] Sin evidencia suficiente
> Macros y addons recomendados por Method (2026-11-04 y 2026-11-10). **Ninguno se ha probado en el juego** en este proyecto: no se declara que funcionen hasta probarlos.

## Resumen
- Method recomienda solo dos addons generales: **Leatrix Plus** (calidad de vida) y **Forever Auras** (fork de WeakAuras para Forever). Ninguno específico de Priest.
- Para seguir CD y DoT, Method propone el **Cooldown Manager de Blizzard** editando sus filtros (la configuración por defecto de la beta no sirve).
- Macros útiles ya en leveling: **PW:S mouseover** (cae sobre ti si no hay objetivo amistoso) y **SW:Death con /stopcasting** para rematar mobs que huyen (desde el 32).
- Las demás macros (Greater Heal, PoH, PoM, Dispel) son de healer de endgame.

## Addons

| Addon | Para qué | Fuente | Probado |
|---|---|---|---|
| Leatrix Plus | Opciones de calidad de vida y automatización | Method Shadow | No |
| Forever Auras | Fork de WeakAuras para Forever | Method Shadow | No |
| Cooldown Manager (Blizzard, integrado) | CD y duración de DoT del objetivo | Method Shadow | No |

Nota: "automatización" en Leatrix Plus se refiere a opciones de interfaz del propio addon. Regla del proyecto: solo addons y API permitidas.

## Macros
Todas usan la prioridad mouseover amistoso vivo → objetivo → uno mismo, salvo que se indique.

| Macro | Uso | Fuente |
|---|---|---|
| PW:S mouseover | Escudo al aliado bajo el ratón o a ti | Shadow |
| Greater Heal mouseover | Duplicar para r1, r4 y máx. | Holy |
| Greater Heal con /stopcasting | Reinicia el cast; ahorra maná si otro curó | Holy |
| Inner Focus + Prayer of Healing | Cura de grupo gratis con +25 % crit | Holy |
| Dispel Magic inteligente | Limpia aliados o purga enemigos según el objetivo | Holy |
| Prayer of Mending mouseover | PoM sin cambiar de objetivo | Holy |
| SW:Death con /stopcasting | Rematar o tumbar totems | Holy |

Texto (reescrito para el personaje; sintaxis estándar de macros):

```
#showtooltip Power Word: Shield
/cast [@mouseover,help,nodead][@player] Power Word: Shield
```

```
#showtooltip Shadow Word: Death
/stopcasting
/cast [@mouseover,harm,nodead][@target,harm,nodead] Shadow Word: Death
```

```
#showtooltip Inner Focus
/cast Inner Focus
/cast [@mouseover,help,nodead][@target,help,nodead][@player] Prayer of Healing
```

Para Greater Heal, Prayer of Mending y otras curas: sustituir el nombre en `/cast [@mouseover,help,nodead][@target,help,nodead][@player] <Hechizo>`. Para Dispel Magic, Method encadena condiciones `help` y `harm` sobre mouseover y objetivo, con `[@player]` al final.

## Interfaz
- Shadow: nameplates con debuffs visibles; boss frames donde sea cómodo para multi-DoT.
- Holy: marcos de raid cerca del centro; atenuar a quien esté a más de 40 m; curas entrantes previstas; borde rojo a quien tenga agro.

## Qué dicen las guías
- [[src-method-class-guides-shadow-priest-interface-addons-and-macros]]: addons y Cooldown Manager; macro de PW:S.
- [[src-method-class-guides-holy-priest-interface-addons-and-macros]]: sin addons; seis macros de curación y SW:Death.

## Fuentes

| URL | Tipo | Fecha de la página | Consultada | ¿Anterior al parche del 02-11? |
|---|---|---|---|---|
| https://www.method.gg/wow-forever/class-guides/shadow-priest/interface-addons-and-macros | guide | 2026-11-04 | 2026-11-13 | No |
| https://www.method.gg/wow-forever/class-guides/holy-priest/interface-addons-and-macros | guide | 2026-11-10 | 2026-11-13 | No |

## Preguntas pendientes
- ¿Funcionan Leatrix Plus y Forever Auras en el cliente de Forever del jugador? Probar.
- ¿Admite el cliente de Forever los rangos en macros (`Greater Heal(Rank 1)`)? Method dice "duplicar para r1" pero no da la sintaxis.
- ¿Dónde se configura el Cooldown Manager en Forever?
