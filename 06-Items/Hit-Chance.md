---
type: system
tags: [forever, items, itemization, stats, hit]
faction: both
status: conflicting
confidence: low
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources: ["https://www.method.gg/wow-forever/how-does-hit-chance-work-in-wow-forever", "https://www.method.gg/wow-forever/itemization-updates-in-world-of-warcraft-forever-expertise-spell-damage-more"]
related: ["[[Itemization]]", "[[Priest-Talents]]", "[[Priest-Gear-and-Stats]]"]
---

# Probabilidad de golpe (Hit Chance)

> [!warning] Datos en conflicto: ver [[Conflicts]]
> Una sola guía con cifras, escrita en beta (2026-10-06). Contradice a la guía de itemización sobre Weapon Skill y algunas cifras no son coherentes entre sí.

## Resumen
- En Forever el golpe es un solo stat que reduce fallos de hechizos y ataques por igual.
- Las sanaciones no fallan: un Priest que cura no necesita golpe.
- Topes según Method contra objetivo de mismo nivel: hechizos 4 %, ataques 5 %, doble arma 24 %. Contra jefe de raid (+3 niveles): 17 %, 8 % y 29 %.
- Casi todo el equipo con golpe es de nivel 50+; a nivel 10-30 no merece la pena buscarlo (inferido).
- Puede quedar un 1 % de fallo incluso en el tope (sospecha del autor, sin probar).

## Topes de golpe (Method, con habilidad de arma al máximo)
| Tipo | Mismo nivel | Jefe de raid | Estado |
|---|---|---|---|
| Hechizo | 4 % | 17 % | conflicting |
| Ataque (1 arma) | 5 % | 8 % | conflicting |
| Doble arma | 24 % | 29 % | conflicting |

Dudas: el salto de 4 % a 17 % en hechizos frente a 5 % a 8 % en ataques y el 24 % de doble arma a mismo nivel no siguen una misma lógica. Podrían mezclar cifras de mismo nivel y de +3 niveles. Ninguna confirmada en el juego.

## Mecánica
| Afirmación | Estado |
|---|---|
| El golpe afecta a hechizos y ataques a la vez | confirmed_forever (dos guías de Method) |
| Más nivel del enemigo, más fallos; jefes y calaveras cuentan como +3 | confirmed_forever (Method) |
| Los fallos hacen 0 daño; las sanaciones no fallan | confirmed_forever (Method) |
| Weapon Skill afecta a fallos y golpes de refilón | conflicting: la guía de itemización dice que Expertise sustituye a Weapon Skill |
| 1 % de fallo residual en el tope | unknown |

## Equipo y talentos
- Stormgard Hood (misión Ground to Keep, Arathi Highlands): +0,5 % de golpe.
- Priest: Method cita "Holy Precision", +6 % por punto a hechizos Sagrados, hasta +18 %. **Sin verificar**; el nombre y la cifra no se han contrastado con el calculador de talentos de Forever. Ver [[Priest-Talents]].

## Qué dicen las guías
- Consenso: [[src-method-how-does-hit-chance-work-in-wow-forever]] y [[src-method-itemization-updates-in-world-of-warcraft-forever-expertise-spell-damage-more]] coinciden en el golpe unificado.
- Discrepancias: Weapon Skill frente a Expertise (ver arriba).

## Fuentes
| URL | Tipo | Fecha página | Consultada | ¿Antes del parche 2026-11-02? |
|---|---|---|---|---|
| https://www.method.gg/wow-forever/how-does-hit-chance-work-in-wow-forever | Guía Method | 2026-10-06 | 2026-11-13 | Sí |
| https://www.method.gg/wow-forever/itemization-updates-in-world-of-warcraft-forever-expertise-spell-damage-more | Guía Method | 2026-09-15 | 2026-11-13 | Sí |

## Preguntas pendientes
- Topes reales en el lanzamiento (nota de parche o prueba en el juego).
- ¿Existe un talento de golpe para Priest en Forever y cuánto da?
- ¿Weapon Skill o Expertise en la hoja de personaje?
