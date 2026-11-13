---
type: class
tags: [priest, forever, leveling]
level_min: 1
level_max: 60
faction: both
status: conflicting
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-–-updated-november-2/2360696/9
  - https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-–-updated-november-2/2360696
  - https://worldofwarcraft.blizzard.com/news/24301514
  - https://www.method.gg/wow-forever/wow-forever-priest-leveling-guide-and-talents
  - https://www.warcrafttavern.com/forever/guides/priest-leveling/
  - https://kami-labs.fr/en/wow-forever/pretre-wow-forever-leveling-baguette/
  - https://kami-labs.fr/en/wow-forever/patch-notes-2-novembre-notes-de-lancement/
  - https://www.warcrafttavern.com/forever/news/wow-forever-pre-launch-class-changes-bug-fixes/
  - https://timesaver.gg/tools/wow-forever/talent-calculator/priest
  - https://www.warcrafttavern.com/forever/guides/undead_racials/
  - https://wow.gg/guides/wow-forever-racial-changes-15-10-2026
  - https://www.dtgre.com/2026/11/wow-forever-spell-training-too-expensive-save-gold.html
  - https://finalboss.io/world-of-warcraft-forever-prepare-warrior-and-priest-builds-for-launch
  - https://news.blizzard.com/en-gb/article/24315281/wow-forever-hotfixes-november-9-2026
  - https://eu.forums.blizzard.com/en/wow/t/class-tuning-incoming-10-november/640100
  - https://eu.forums.blizzard.com/en/wow/t/fix-priest-leveling/640242
  - https://us.forums.blizzard.com/en/wow/t/wands-nerfed-okaynow-what/2360848
  - https://www.method.gg/wow-forever/class-guides/shadow-priest/rotation-and-playstyle
related: ["[[Priest]]", "[[Priest-Talents]]", "[[Priest-Spells]]", "[[Priest-Wands]]", "[[Priest-Gear-and-Stats]]", "[[Shadow-Priest]]", "[[Discipline-Priest]]", "[[Conflicts]]"]
---

# Priest — Leveling en WoW Forever (1–30, esbozo 30–60)

> [!warning] Datos en conflicto: ver [[Conflicts]]
> La tesis de beta "la wand reemplaza a Smite" quedó obsoleta (24-09). Las builds post-parche difieren desde el nivel 17. Recomendaciones basadas en guías, sin export del personaje.

Notas relacionadas: [[Priest]] · [[Priest-Talents]] · [[Priest-Spells]] · [[Priest-Wands]] · [[Priest-Gear-and-Stats]] · [[Discipline-Priest]] · [[Shadow-Priest]]

## Resumen

- **Para un Undead ~9 (Method, 06-11)**: talentos 10–11 Wand Specialization 2/2 → 12–16 Spirit Tap 5/5 → 17–18 Improved SW:Pain 2/2 → 19–23 Twin Disciplines 5/5. Rotación desde el 10: PW:S → Mind Blast → SW:Pain → wand. Detalle en [[Priest-Talents]].
- El Priest de Forever sube de nivel con **wand + DoT + Power Word: Shield**. Los talentos empiezan en el **nivel 10** (oficial). El plan más citado después del parche es **Discipline/híbrido con Wand Specialization 2/2 y Spirit Tap 5/5 hasta el 39**, y **respec a Shadow en el 40** para Shadowform (Method, Timesaver/Maxroll).
- Según una guía de la beta (Kami Labs, 23-09), la wand "reemplaza a Smite" porque su daño escalaba con spell power. **Blizzard eliminó ese escalado el 24-09-2026**: las wands "no longer gain any additional damage from the user's spell damage". Esa tesis queda **obsoleta** en su forma original. La wand sigue siendo central (Method la llama "the most important slot" hasta el 40), pero porque es daño sin coste de maná, no porque escale.
- Las notas del 2 de noviembre **no traen buffs numéricos de daño para Priest**. Los buffs con cifras que se publicaron son de otras clases. Los cambios de Priest son correcciones (PW:S, SW:Death, Dark Sacrifice, Holy Binding, VE, Shadowform). Los mobs de nivel alto tienen más vida.
- Para un Priest Undead de nivel ~9: el primer punto de talento llega al 10, junto con Mind Blast, Shadow Word: Pain r2 y la misión de Touch of Weakness. Lo prioritario es conseguir una [[Priest-Wands|wand]] (Lesser Magic Wand, nivel 5, crafteada por Enchanting).

## Cómo funciona

Bucle de combate en solitario según las fuentes (cada una con su fecha):

| Tramo | Rotación propuesta | Fuente | Estado |
|---|---|---|---|
| 1–3 | Smite hasta que el mob esté bajo o te quedes sin maná; luego melee | Method (06-11) | confirmed_forever (guía post-parche) |
| 4–9 | Pre-cast Smite → SW:Pain → Smite → melee. Ahorra maná. SW:Pain primero si hay competencia por el tag | Method (06-11) | confirmed_forever |
| Temprano (1–30) | Disparar con la wand, Lesser Heal si estás bajo, PW:S para evitar interrupciones, SW:Pain cuando el maná lo permita | Warcraft Tavern (beta) | probable (guía de beta, sin fecha) |
| 10–39 | Pre-cast PW:S → pre-cast Mind Blast → SW:Pain → wand → melee si no te queda maná | Method (06-11) | confirmed_forever |
| Beta ~20 | SW:Pain a varios mobs → Psychic Scream cuando llegan a melee → rematar con la wand. Evitar Mind Flay | Kami Labs (23-09) | conflicting (anterior a los cambios de wands del 24-09 y de Mind Flay del 16-10) |
| Disc 30+ | PW:S → Smite al pull → SW:Pain → Penance → wand/DoT para rematar | Warcraft Tavern (beta) | probable |
| Shadow 40–60 | PW:S → Mind Blast → SW:Pain → SW:Death en CD → Mind Blast en CD → Mind Flay de relleno | Method (06-11) | confirmed_forever |

Mecánicas de Forever que cambian el bucle:
- **Los DoT taguean al instante**: según Method, "instant tagging mobs, unlike in previous iterations of classic". `confirmed_forever` (guía post-parche, no oficial).
- **Los DoT/HoT no hacen snapshot**: se recalculan de forma dinámica (Warcraft Tavern). `confirmed_forever` (guía).
- **La wand exige estar quieto 0,5 s** antes de disparar (oficial, 16-10). Penaliza el kiteo con wand. `confirmed_forever`.
- **Las wands ya no escalan con spell damage** (oficial, 24-09). `confirmed_forever`.
- **Ningún hechizo nuevo se coloca solo en la barra** (oficial, 02-11). Después de entrenar hay que arrastrarlo a mano. `confirmed_forever`.
- **Spirit Tap y la regla de 5 segundos**: Kami estima que regenerar fuera de la regla de 5 s con Spirit Tap rinde mucho más que Meditation. Es una estimación de beta, `probable_classic`. Meditation fue "increased substantially" (oficial), así que la comparación puede haber cambiado.

## Datos específicos de WoW Forever

### Cambios de Priest en el parche de lanzamiento (notas 2026-11-02, post del 03-11)
Fuente oficial: hilo de Kaivax. Todas las filas son `confirmed_forever`.

| Cambio | Efecto en leveling |
|---|---|
| PW:Shield se puede reemplazar por otro de rango igual o superior | Menor |
| SW:Death: si no mata, el daño propio sube del 10 % al **30 %** de la vida máxima. Ya no hace daño propio si falla (miss) | Importante a partir del 32: usarlo sobre todo para rematar |
| Dark Sacrifice (racial Undead) ya no rompe CC | Menor |
| Binding Heal se elimina del árbol Holy y entra **Holy Binding** (Flash Heal a otro te cura un 50 %) | Solo Holy |
| Devouring Contagion no se propaga desde critters | Menor |
| La curación de Vampiric Embrace ya no hace crítico | Menor |
| Cure/Abolish Disease ya no sacan de Shadowform | Shadow 40+ |
| Costes de entrenamiento normalizados: **206–207 g en total del 1 al 60** para todas las clases. Excepción: las habilidades raciales de Priest | Afecta al presupuesto de la montura |
| Clases con más daño en general; criaturas de nivel alto con más vida | No hay cifras de Priest |
| Respawns más rápidos en las zonas bajas al lanzamiento; XP de misiones ajustada | Contexto |
| Se elimina la penalización de rango bajo en la mayoría de talentos de proc | Menor para Priest |

Kami Labs (03-11) añade que, según los datos del juego, Binding Heal sigue existiendo como hechizo de entrenador con 6 rangos desde el nivel 25. Las notas oficiales hablan de "removed". **Conflicting**: ver [[Priest-Spells]].

### Después del lanzamiento (oficial)
- **Hotfixes del 09-11** (Blizzard News), todos `confirmed_forever`:
  - "Experience rewarded for all enemy kills in dungeons increased by 50%". Hacer mazmorras gana valor frente a las misiones.
  - Shadowform ya no se rompe al lanzar Fear Ward.
  - Power Infusion persiste correctamente sobre aliados.
  - El 06-11, "Unending Torment" (de The Abomination's Head, The Baron) pasa a estar disponible para la Horde al nivel 15 en lugar del 16.
- **Ajuste de clases del 10-11** (Kaivax, 06-11): solo afecta a mascotas de Hunter, Voidwalkers, Affliction y Enhancement. **No anuncia cambios para Priest.** `confirmed_forever`.

### Evidencia de la comunidad (foros oficiales, posts de jugadores, no de Blizzard)
`community`. Son opiniones y mediciones sin verificar. No cuentan como datos confirmados.
- **"Fix Priest Leveling"** (foro EU, 07-08/11, después del lanzamiento):
  - Un jugador dice que el Priest mata "25% slower than Classic" por la subida de vida de los mobs. Otro tarda "over 45 sec" con algunos mobs de nivel 30. Otro dice que un mob amarillo necesita 2–3 SW:Pain mientras usa la wand.
  - Devouring Plague se percibe como muy caro: un jugador dice un 20 % del maná y otro un 25 % (cifras que no coinciden). Varios recomiendan no usarlo con mobs débiles.
  - Mind Flay se considera flojo a nivel bajo (unos 35 por tick, según un jugador).
  - Consejos de los jugadores:
    - Shadow + Spirit Tap.
    - Rotación SW:Pain → Devouring Plague → Mind Blast → wand o Mind Flay.
    - PW:S → DoT → wand.
    - Comprar equipo verde barato en el AH (equipo de nivel 25 por más de 30 plata, según un jugador).
    - Un jugador lleva 2 puntos en un talento llamado "Improved Wands" y una wand de velocidad 1.2 de una misión Worgen (no aplica a Undead).
  - Opiniones en contra: varios jugadores dicen que el leveling está "completely fine" al 25, que el Priest recibió "one of the best overhauls", o que matan más rápido que en Classic. La curación se siente fuerte en mazmorras (críticos de más de 700).
  - Estado: `conflicting` (las percepciones se contradicen).
- **"Wands nerfed, okay...now what?"** (foro US de la beta, 24–25/09): los jugadores comentan que se eliminó el escalado de las wands con spell power. Un tester de nivel 20 con 28 de spell damage pega 40–50 por disparo. Dicen que los Priest no Shadow son los más perjudicados y que Wizard Oil no se puede aplicar a una wand. Ver [[Priest-Wands]].
  - La eliminación del escalado **está confirmada por las notas oficiales del 24-09**. Las cifras de daño y lo del Wizard Oil son `unknown` (una sola fuente de la comunidad).

### Cambios de Priest durante la beta que siguen vigentes (oficial)
- 24-09: Renew puede hacer crítico; wands sin escalado de spell damage.
- 01-10: Devouring Plague puede hacer crítico; las wands crafteadas comunes y poco comunes se venden al vendedor por 1 cobre.
- 08-10: se reajustan los rangos 1–4 de Smite para que cada rango sea una mejora. Se reduce el daño y la curación de Penance (el rango 1 cuesta un 50 % más de maná).
- 16-10: CD de Devouring Plague 24 s; CD de SW:Death 18 s (el artículo oficial del 30-09 decía 15 s). Cada tick de Mind Flay hace un 10/20 % más que el anterior. Nuevo talento Dark Inspiration. CD de VE 30 s. Wand: 0,5 s quieto.

### Diseño oficial (Class Deep Dive, 30-09, beta)
- Talentos desde el nivel 10, con hitos de 11, **16**, 21 y 31 puntos. Los talentos se cambian en el entrenador de una capital. **Dual Spec al nivel 40.**
- Baseline: Fear Ward y Devouring Plague al 20 para todas las razas. Divine Spirit baseline al 30. SW:Death baseline al 32.
- Penance es el talento de oro de 21 puntos de Disc. Shadowform es talento de Shadow. El artículo no da el nivel de Shadowform. Las guías dicen **40**, lo que cuadra con 31 puntos si se empieza en el 10.

### Raciales Undead relevantes para Priest
| Racial | Dato en Forever | Fuente | Estado |
|---|---|---|---|
| Touch of the Grave (nuevo, pasivo) | Probabilidad de drenar hasta el 5 % de tu vida máxima al hacer daño directo (o en el impacto inicial de un DoT/AoE). Priest: **30 %** (antes 10 %, 15-10). ICD **15 s** (antes 25 s, oficial 26-10 y 02-11). SW:Pain lo activa al lanzarlo, no con los ticks | wow.gg (19-10), Warcraft Tavern, Blizzard | confirmed_forever |
| Cannibalize | Restaura vida **y maná**, 7 %/s durante hasta 10 s, sobre cadáveres Undead/Humanoid | Warcraft Tavern (sin fecha) | confirmed_forever (guía, medium) |
| Will of the Forsaken | Elimina Charm/Fear/Sleep pero ya **no da inmunidad** | Warcraft Tavern | confirmed_forever (guía) |
| Shadow Resistance racial | **Eliminada** | Warcraft Tavern | confirmed_forever (guía) |
| Touch of Weakness (racial de Priest) | Nivel 10, aprendido por misión | Conquest Capped (07-11), oficial ("unchanged") | confirmed_forever |
| Dark Sacrifice (racial de Priest) | Nivel 20, por misión. Convierte vida en maná con el tiempo; el maná escala con Spirit | Blizzard (30-09, 24-09) | confirmed_forever |

Inferencia (no verificada): Cannibalize con maná y Dark Sacrifice reducen el tiempo de beber. Touch of the Grave escala con la vida máxima, así que la Stamina aporta algo de daño.

## Diferencias frente a Classic

- Classic: Wand Specialization 5/5. **Forever: 2/2** (13 %/25 %) según el artículo oficial y Kami/Timesaver.
- Classic: Shadow Resistance racial. Forever: eliminada. En su lugar está Touch of the Grave.
- Classic: Devouring Plague exclusivo de Undead. Forever: baseline para todas las razas al 20. **Pierdes esa ventaja racial.**
- Classic: Penance, Soul Warding, Twin Disciplines, Power in Light, Dark Inspiration, Early Demise y Devouring Contagion no existen.
- Los DoT taguean al instante y no hacen snapshot.
- Las wands tienen spell power como stat (+1/+2), pero su daño no escala con él.
- Costes de entrenamiento: en Forever son uniformes por nivel. El total es de 206–207 g.

## Recomendaciones prácticas

Basado en conocimiento externo. No hay export del personaje. El nivel 9 lo indicó el usuario y está sin confirmar.

1. **Ahora (nivel 9)**: consigue una Lesser Magic Wand (nivel 5) si no tienes una. No tienes Enchanting, así que toca AH o un enchanter. El precio es desconocido: hay que consultar el AH del reino. Detalles en [[Priest-Wands]].
2. **Nivel 10**: entrena Mind Blast, SW:Pain r2 y Lesser Heal r3 (Method añade Resurrection). Haz la misión de **Touch of Weakness**. Primer punto de talento: **Wand Specialization**, rango 1 al 10 y rango 2 al 11. Este orden lo comparten Method, Timesaver/Maxroll, Holy/Icy Veins y Kami. Ver [[Priest-Talents]].
3. **12–16**: Spirit Tap 5/5. La rotación pasa a PW:S → Mind Blast → SW:Pain → wand.
4. **17–23**: Method toma Improved SW:Pain 2/2 (17–18) y luego Twin Disciplines 5/5 (19–23). Maxroll pone Twin Disciplines desde el 17 y Holy Precision al 20. `conflicting` (preferencia de autor).
5. **13+**: valora la Greater Magic Wand (nivel 13, 17,5 DPS en DB). **15+**: Sizzle Stick (misión de Wailing Caverns). **18+**: Gravestone Scepter (misión de BFD, 29 DPS en DB).
6. **Oro de entrenamiento**: Method aconseja no subir todos los rangos si quieres la montura al 40. dtgre recomienda priorizar SW:Pain, PW:S y Renew en solitario y retrasar Mind Vision, Mana Burn, Fade y los rangos de Smite si casi no lo usas.
7. **Profesiones**: Herbalism + Skinning es la combinación "menos intrusiva" (Method): da plata para rangos y agua. No da wands ni equipo. Method solo recomienda craftear en lanzamiento: Tailoring + Enchanting para fabricarse la Lesser Magic Wand (Runed Copper Rod; subir con Enchant Bracer - Inferior Stamina; desencantar Heavy Linen Gloves). First Aid vale menos para un Priest.
8. **Descanso (Method)**: Camp Tent da +5 % de rested XP a cualquier nivel; Pouch of Violet Dust dobla la duración de los buffs de hoguera (no el de la tienda); Cozy Sleeping Bag (cadena de misiones) crea zona de descanso y da +3 % de XP. Ver [[Camping]].
9. **Mazmorras (Method)**: puedes curar mazmorras incluso como Shadow; lleva agua de tu nivel.
10. **30 → 40**: elige entre seguir en Disc (Penance llega al 37 con Method, al 35 con Maxroll/Timesaver, o al 30 si se va todo a Disc) o pasarte a Shadow. En el 40: respec a Shadow (Shadowform) y Dual Spec.

## Tablas / niveles / requisitos

| Nivel | Hito | Estado |
|---|---|---|
| 5 | Primera wand equipable (Lesser Magic Wand) | confirmed_forever (Wowhead Forever) |
| 10 | Primer talento; Mind Blast; misión racial Touch of Weakness | confirmed_forever |
| 12 | Inner Fire | confirmed_forever |
| 14 | Psychic Scream | confirmed_forever |
| 20 | Devouring Plague, Fear Ward, Flash Heal, Holy Fire; Dark Sacrifice (misión); Mind Flay (talento) | confirmed_forever |
| 25 | Talento de 16 puntos (Soul Warding / Binding Heal→Holy Binding / Vampiric Embrace) | confirmed_forever (cálculo: 16 puntos al 25) |
| 25 | Inicio del sistema Legacy de la cuenta (FinalBoss, en una guía de Warrior) | probable (una sola guía) |
| 30 | Penance (talento de 21 puntos), Divine Spirit baseline | confirmed_forever |
| 32 | Shadow Word: Death | confirmed_forever |
| 40 | Shadowform (talento de 31 puntos), Dual Spec | confirmed_forever (Dual Spec, oficial); Shadowform al 40 según guías |

## Qué dicen las guías
- Consenso: wand como mejora clave hasta el 40, PW:S + DoT + wand, Disc/híbrido hasta el 39 y Shadow al 40 ([[src-method-wow-forever-priest-leveling-guide-and-talents]], Timesaver/Maxroll, Warcraft Tavern).
- Discrepancias: Kami (beta) proponía Shadow temprano con SW:P en masa; Method y Maxroll difieren en los talentos 17–39 (ver [[Priest-Talents]]); la comunidad discute si el Priest sube lento tras el parche.
- Rotación Shadow de endgame (no de leveling): [[src-method-class-guides-shadow-priest-rotation-and-playstyle]].

## Fuentes

| URL | Tipo | Consultada | Fecha de la fuente | ¿Anterior al parche del 02-11? |
|---|---|---|---|---|
| https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-–-updated-november-2/2360696/9 | official | 2026-11-10 | post 2026-11-03 | No (es el parche) |
| https://us.forums.blizzard.com/en/wow/t/wow-forever-beta-development-notes-–-updated-november-2/2360696 | official (hilo completo) | 2026-11-10 | 24-09 a 04-11 | Mixto |
| https://worldofwarcraft.blizzard.com/news/24301514 | official | 2026-11-10 | 30-09 (beta) | Sí |
| https://www.method.gg/wow-forever/wow-forever-priest-leveling-guide-and-talents | guide | 2026-11-10 y 2026-11-13 | actualizada 2026-11-06 | No |
| https://www.method.gg/wow-forever/class-guides/shadow-priest/rotation-and-playstyle | guide | 2026-11-13 | 2026-11-04 | No |
| https://www.warcrafttavern.com/forever/guides/priest-leveling/ | guide | 2026-11-10 | sin fecha; builds "for the Beta, capped at level 30" | Probablemente sí |
| https://kami-labs.fr/en/wow-forever/pretre-wow-forever-leveling-baguette/ | guide/news (resumen de un vídeo de Scriblet) | 2026-11-10 | 2026-09-23 | Sí (también es anterior al cambio de wands del 24-09) |
| https://kami-labs.fr/en/wow-forever/patch-notes-2-novembre-notes-de-lancement/ | news | 2026-11-10 | 2026-11-03 | No |
| https://www.warcrafttavern.com/forever/news/wow-forever-pre-launch-class-changes-bug-fixes/ | news | 2026-11-10 | 2026-11-04 | No |
| https://timesaver.gg/tools/wow-forever/talent-calculator/priest | community tool (builds atribuidas a Maxroll/Icy Veins) | 2026-11-10 | actualizada 2026-11-04; árbol leído del cliente el 06-11 | No |
| https://www.warcrafttavern.com/forever/guides/undead_racials/ | guide | 2026-11-10 | sin fecha | Desconocido |
| https://wow.gg/guides/wow-forever-racial-changes-15-10-2026 | guide/news | 2026-11-10 | 2026-10-19 | Sí |
| https://www.dtgre.com/2026/11/wow-forever-spell-training-too-expensive-save-gold.html | community blog | 2026-11-10 | 05/06-11 | No |
| https://finalboss.io/world-of-warcraft-forever-prepare-warrior-and-priest-builds-for-launch | guide (Warrior; solo aporta Dual Spec al 40 y Legacy al 25) | 2026-11-10 | publicada 02-10, actualizada 27-10 | Sí |
| https://news.blizzard.com/en-gb/article/24315281/wow-forever-hotfixes-november-9-2026 | official (hotfixes) | 2026-11-10 | 06-11 y 09-11 | No |
| https://eu.forums.blizzard.com/en/wow/t/class-tuning-incoming-10-november/640100 | official (post de Kaivax) | 2026-11-10 | 06-11 | No |
| https://eu.forums.blizzard.com/en/wow/t/fix-priest-leveling/640242 | community (jugadores en el foro oficial; sin respuesta de Blizzard) | 2026-11-10 (aportado por el coordinador y verificado) | 07–08/11 | No |
| https://us.forums.blizzard.com/en/wow/t/wands-nerfed-okaynow-what/2360848 | community (foro de la beta; sin respuesta de Blizzard) | 2026-11-10 (aportado por el coordinador y verificado) | 24–25/09 | Sí |

No se pudieron leer: mobalytics.gg (403 en `priest-leveling-guide-1-60`, `priest-leveling-guide` y la guía de kargoz), icy-veins.com (403) y massivelyop.com (403). En su lugar se leyó el artículo oficial de Blizzard que MassivelyOP resume.


## Preguntas pendientes
- ¿El nivel real del personaje es 9? Confirmar con un export.
- ¿Spirit Tap funciona igual que en Classic (Spirit ×2 y regeneración durante el casteo)? Ninguna fuente oficial lo describe.
- ¿Cuánto daño tiene hoy Smite frente a la wand? (Smite se reajustó el 08-10, las wands el 24-09). No hay pruebas post-parche.
- ¿Cómo encaja Legacy/"Talented" (Warcraft Tavern dice que adelanta talentos hasta 5 niveles)? ¿Desde qué nivel?
- ¿El daño de Priest subió el 02-11? Las notas no dan cifras de Priest. Los jugadores perciben que el Priest mata más lento por la vida de los mobs, pero otros lo niegan, y el ajuste del 10-11 no toca al Priest.
- ¿Cuánto maná cuesta realmente Devouring Plague? En el foro se habla de un 20 % y de un 25 %.
- ¿Con el +50 % de XP en mazmorras (09-11), compensa más hacer RFC, WC o BFD que las rutas de misiones? Falta medirlo.
- ¿A qué nivel exacto se aprende Shadowform? Es inferido (40) y no aparece en ninguna fuente oficial.
