---
type: spec
tags: [forever, priest, shadow, endgame]
level_min: 40
level_max: 60
faction: both
status: confirmed_forever
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://www.method.gg/wow-forever/class-guides/shadow-priest
  - https://www.method.gg/wow-forever/class-guides/shadow-priest/talents
  - https://www.method.gg/wow-forever/class-guides/shadow-priest/rotation-and-playstyle
  - https://www.method.gg/wow-forever/class-guides/shadow-priest/bis-gear-and-stats
  - https://www.method.gg/wow-forever/class-guides/shadow-priest/enchants-and-consumables
  - https://www.method.gg/wow-forever/class-guides/shadow-priest/races-professions-and-other
  - https://www.method.gg/wow-forever/class-guides/shadow-priest/interface-addons-and-macros
  - https://www.method.gg/wow-forever/wow-forever-priest-leveling-guide-and-talents
  - https://www.method.gg/dfc/ForeverTalentsData-1.60.1.json
  - https://nether.wowhead.com/forever/tooltip/spell/15473
  - https://nether.wowhead.com/forever/tooltip/spell/1326159
  - https://nether.wowhead.com/forever/tooltip/spell/1309950
related: ["[[Priest]]", "[[Priest-Talents]]", "[[Priest-Leveling]]", "[[Priest-Gear-and-Stats]]", "[[Priest-Macros-and-Addons]]", "[[Holy-Priest]]", "[[Discipline-Priest]]"]
---

# Shadow Priest

> [!success] Confirmado en Forever
> Guía de endgame de Method (Amaxagon, 2026-11-04, parche 1.60.1) y datos de talentos 1.60.1. BiS y gran parte de los encantamientos siguen "Work In Progress". El ajuste de daño de la spec no es final, según el propio autor.

## Resumen
- Spec de DoT: **SW:Pain y Devouring Plague siempre activos, Mind Blast y SW:Death en CD, Mind Flay de relleno**. PW:S se puede lanzar sin salir de Shadowform (Method).
- Build de raid de Method: **17/0/34** con Dark Inspiration 5/5, Shadowform y Discipline hasta Meditation. Para leveling 40–60 Method usa otra variante (16/0/35) sin Dark Inspiration.
- Stats: **Hit (cap) > Spell Damage > Crit > Intellect > Spirit**. El crit vale más que en Classic porque los DoT critican y Shadowform da +100 % al bonus de daño crítico Shadow.
- **Undead es raza S** para Shadow (la mejor de Horde, con margen pequeño sobre Troll). Profesiones de endgame: Engineering y quizá Tailoring.
- Para el personaje (Undead ~9): Shadow es el destino del 40 (respec), no la spec actual. Ver [[Priest-Leveling]].

## Talentos

Build "General" de Method (decodificada del widget de la guía; nombres con tooltips de Wowhead Forever). Estado: `confirmed_forever` (guía post-parche).

| Árbol | Talento | Rangos | Nota |
|---|---|---|---|
| Shadow | Shadow Focus | 5/5 | +5 % hit Shadow (BiS page y tooltip) |
| Shadow | Improved Shadow Word: Pain | 2/2 | +6 s de duración (tooltip, rango máx.) |
| Shadow | Shadow Reach | 1/2 | Opcional el 2.º punto |
| Shadow | Improved Mind Blast | 4/5 | −CD de Mind Blast |
| Shadow | Mind Flay | 1/1 | Requiere nivel 20 |
| Shadow | Improved Mind Flay | 2/2 | Cada tick +20 % sobre el anterior (tooltip) |
| Shadow | Shadow Weaving | 3/3 | En Forever solo amplifica **tu** daño |
| Shadow | Vampiric Embrace | 1/1 | Cura al grupo un 20 % del daño Shadow; 30 s, CD 30 s (tooltip) |
| Shadow | Dark Inspiration | 5/5 | MB o Mind Flay completo: +15 % Spirit a ti y al grupo 10 s (tooltip) |
| Shadow | Devouring Contagion | 2/2 | DP −50 % de maná; se propaga a 2 enemigos si el objetivo muere (tooltip) |
| Shadow | Darkness | 5/5 | +10 % daño Shadow |
| Shadow | Shadowform | 1/1 | +10 % daño Shadow, −50 % coste Shadow, +100 % bonus crítico, −15 % daño físico recibido, sin curas (tooltip) |
| Shadow | Early Demise | 2/2 | +30 % crit de SW:Death bajo 20 % de vida (tooltip) |
| Discipline | Twin Disciplines | 5/5 | +5 % a instantáneos (SW:P, SW:D, DP, Mind Flay según Method) |
| Discipline | Mental Strength | 5/5 | % de Intellect (cifra en conflicto, ver [[Priest-Talents]]) |
| Discipline | Inner Focus | 1/1 | |
| Discipline | Meditation | 3/3 | Opcional si sobra maná |
| Discipline | Silent Resolve | 3/3 | Opcional si no hay problemas de amenaza |

Opcionales que cita Method: Twilight Focus (resistir el retroceso de casteo; útil en Vael'astraz, BWL), Silence (nicho: trash, adds interrumpibles, raids de 10, mazmorras), Improved PW:Shield (nicho, estilo SoD: VE + escudos para prescindir de un healer).

Orden del widget de raid (empieza en el 10, pero es una build de 60): Shadow Focus 5 → Imp. SW:P 2 → Shadow Reach 1 → Imp. MB 4 → Mind Flay → Imp. MF 2 → Shadow Weaving 3 → VE → Dark Inspiration 5 → Devouring Contagion 2 → Darkness 5 → Shadowform (41.º punto) → Early Demise 2 → Twin Disciplines 5 → Mental Strength 5 → Inner Focus → Meditation 3 → Silent Resolve 3.

### Leveling (Method, guía de leveling)
- **Respec al 40 (0/0/31)**: Spirit Tap 5/5 primero, luego Imp. SW:P, Imp. MB, Mind Flay (20), Imp. MF, VE (25), Shadow Weaving, Shadow Focus 5, Devouring Contagion, Darkness, Shadowform (40).
- **41–60 (16/0/35)**: Twin Disciplines 5, Early Demise 2, Martyrdom 2, Mental Strength 5, Inner Focus, Meditation 3, Shadow Reach 2. Sin Dark Inspiration ni Silent Resolve.
- Detalle punto por punto en [[Priest-Talents]].

## Rotación

| Situación | Prioridad (Method) | Estado |
|---|---|---|
| Un objetivo | MB (pre-cast) → SW:P si quedan <3 s → Devouring Plague → MB → SW:Death → Mind Flay | confirmed_forever |
| Cleave | MB pre-cast → SW:P principal (<3 s) → SW:P secundario (<3 s) → DP en el que muera antes → MB → SW:D → Mind Flay | confirmed_forever |
| Leveling 40–60 | PW:S → MB → SW:P → SW:D en CD → MB en CD → Mind Flay; refrescar PW:S y SW:P en mobs duros | confirmed_forever |

- Objetivos que mueren pronto: solo MB, SW:D y Mind Flay, sin DoT.
- VE: tras los DoT si buscas daño; antes si la curación importa.
- Amenaza: puedes saltar el pre-cast de MB.
- Sin AoE puro: SW:P en tantos objetivos como se pueda.
- Buffs: PW:F a todos; Divine Spirit a quien tenga maná; Fear Ward a tanques o a un Shaman; Shadow Protection según el daño.
- SW:Death: en Forever hace un 30 % de tu vida máxima de daño propio si no mata (oficial 02-11, ver [[Priest-Spells]]).

## Stats y equipo
- **Hit (cap) > Spell Damage > Crit > Intellect > Spirit** (Method). Stamina solo para sobrevivir.
- No hay cifra de hit cap en Method. Shadow Focus aporta 5 %.
- Pre-raid BiS, BiS, tier y trinkets: **desconocido** ("Work In Progress").

## Encantamientos y consumibles

| Slot | Encantamiento (Method) | Alternativa |
|---|---|---|
| Arma 2H | Spellblasting | Mighty Spell Power |
| Arma 1H | Spell Power | — |
| Cabeza / piernas | Arcanum of Focus | Piernas: Mystic Rugged Armor Kit |
| Hombros | Chromatic Mantle of the Dawn | — |
| Capa | Greater Resistance | Subtlety |
| Pecho | Mystic Rugged Armor Kit | Greater Stats |
| Muñecas | Greater Spellpower | — |
| Guantes | Shadow Power | — |
| Pies | Speed | Mystic Rugged Armor Kit |
| Collar | Spell Power (nuevo en Forever) | — |

- En Forever **se pueden acumular varios elixires**; las pociones comparten CD.
- Flask of Supreme Power; elixires Owl, Greater Mageblood, Greater Arcane, Shadow Power, Greater Spirit (+ defensivos Greater Fortitude, Major Troll's Blood, Greater Defense).
- Pociones: **Major Spellblasting** (prioridad), Elemental Purging, Major Mana, Dragonfire; protecciones y Free Action / Limited Invulnerability.
- Comida Baked Salmon; aceite Brilliant Wizard Oil.
- Estado: `confirmed_forever` como recomendación de guía; efectos de los consumibles nuevos (IDs 25xxxx) **desconocidos**.

## Razas y profesiones
- Tiers: S Undead, Night Elf · A Troll, Human · B Gnome, Dwarf. Raciales "muy menores" en PvE.
- Engineering para raid/PvP; Tailoring por posibles BoP BiS (sin confirmar).
- El personaje tiene Herbalism + Skinning: no encaja con la recomendación de endgame, pero Method dice que si Tailoring no resulta clave el segundo hueco es libre. Cambiar profesiones es decisión del jugador; no hay urgencia a nivel 9.

## Interfaz, addons y macros
- Seguir CD y DoT con el Cooldown Manager de Blizzard (editando filtros) o un addon. Addons generales: Leatrix Plus, Forever Auras. Macro mouseover de PW:S. Ver [[Priest-Macros-and-Addons]].

## Qué dicen las guías
- Consenso: Shadowform al 40 tras leveling Disc/híbrido ([[src-method-wow-forever-priest-leveling-guide-and-talents]], Timesaver/Maxroll en [[Priest-Talents]]).
- La build de raid de Method ([[src-method-class-guides-shadow-priest-talents]]) es 17/0/34 como la de Maxroll vía Timesaver, pero con otro orden y otras elecciones en Disc (Method: Silent Resolve; Maxroll: Wand Specialization, Mental Agility).
- Stats: Method ([[src-method-class-guides-shadow-priest-bis-gear-and-stats]]) pone hit primero; Warcraft Tavern (beta) daba Int/SP > Stam/Spirit. Son contextos distintos (raid frente a leveling).
- Rotación: [[src-method-class-guides-shadow-priest-rotation-and-playstyle]]. Consumibles: [[src-method-class-guides-shadow-priest-enchants-and-consumables]]. Razas: [[src-method-class-guides-shadow-priest-races-professions-and-other]] (Undead S) frente a la guía Holy (Undead A). Interfaz: [[src-method-class-guides-shadow-priest-interface-addons-and-macros]]. Portada: [[src-method-class-guides-shadow-priest]].

## Fuentes

| URL | Tipo | Fecha de la página | Consultada | ¿Anterior al parche del 02-11? |
|---|---|---|---|---|
| https://www.method.gg/wow-forever/class-guides/shadow-priest (+ 6 subpáginas) | guide | 2026-11-04 | 2026-11-13 | No |
| https://www.method.gg/wow-forever/wow-forever-priest-leveling-guide-and-talents | guide | 2026-11-06 | 2026-11-13 | No |
| https://www.method.gg/dfc/ForeverTalentsData-1.60.1.json | datos de la calculadora (Method) | 1.60.1 | 2026-11-13 | No |
| https://nether.wowhead.com/forever/tooltip/spell/<id> | community DB (tooltips) | sin fecha | 2026-11-13 | Desconocido |

## Preguntas pendientes
- ¿Cuál es el hit cap de hechizos en Forever? Method no da cifra.
- ¿Qué objetos son BiS pre-raid? Pendiente de Method.
- ¿Efectos de Major Spellblasting Potion, Elixir of the Owl y otros consumibles nuevos?
- ¿El nivel de requisito "30" que muestra el tooltip de Vampiric Embrace contradice su colocación en el punto 16 (nivel 25)?
