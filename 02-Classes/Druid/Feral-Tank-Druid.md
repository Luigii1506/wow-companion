---
type: spec
tags: [forever, druid, feral, bear, tank, endgame]
level_min: 60
level_max: 60
faction: both
status: confirmed_forever
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://www.method.gg/wow-forever/class-guides/feral-tank-druid
  - https://www.method.gg/wow-forever/class-guides/feral-tank-druid/talents
  - https://www.method.gg/wow-forever/class-guides/feral-tank-druid/rotation-and-playstyle
  - https://www.method.gg/wow-forever/class-guides/feral-tank-druid/bis-gear-and-stats
  - https://www.method.gg/wow-forever/class-guides/feral-tank-druid/enchants-and-consumables
  - https://www.method.gg/wow-forever/class-guides/feral-tank-druid/races-professions-and-other
  - https://www.method.gg/wow-forever/class-guides/feral-tank-druid/interface-addons-and-macros
  - https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json
  - https://foreverdb.net/class/Druid/talents
related: ["[[Druid]]", "[[Druid-Leveling]]", "[[Feral-DPS-Druid]]", "[[Balance-Druid]]", "[[Restoration-Druid]]"]
---

# Feral Tank Druid

> [!success] Confirmado en Forever
> Guía de endgame de Method (Perseis, 2026-11-04, parche 1.60.1). El autor avisa de que está incompleta. Las APL suponen un comportamiento de Lacerate que no se pudo probar. Builds decodificadas del widget. BiS "Work In Progress". Un dato choca con la guía Feral DPS (multiplicador del arma); pendiente de registrar en [[Conflicts]].

## Resumen
- Oso al estilo TBC/WotLK: **Primal Bite en CD, 5 cargas de Lacerate siempre activas, debuffs en el jefe y Maul para gastar rabia**. `confirmed_forever` (APL "mejor estimación")
- Con **doble especialización** ya no hay que elegir entre oso puro e híbrido. Tres builds: **Hybrid Bear/Cat 8/33/10** (vale para todo), **Hybrid Variant 9/32/10** (solo un objetivo) y **Mono-Bear 9/32/10** (tanque principal).
- Tanque de **vida efectiva (EHP)**: Stamina y Armor primero; el DPS del arma es lo más ofensivo.
- **Barkskin se puede usar en forma**; Frenzied Regeneration cura un porcentaje pero no salva en raid.
- Razas: Tauren (Horde), Night Elf (Alliance), Skyborne para quien persigue parses (elementales).
- Débil tanqueando más de 3 enemigos; defensivos más flojos que otros tanques.

## Talentos

Decodificadas del widget de Method (datos 1.60.1-2nov; nombres de ForeverDB). Estado `confirmed_forever`.

| Talento | Hybrid (8/33/10) | Variant (9/32/10) | Mono-Bear (9/32/10) | Nota |
|---|---|---|---|---|
| Genesis / Nature's Reach | 5 / 2 | 5 / 2 | 5 / 2 | |
| Nature's Majesty | 1 | 2 | 2 | +2 % crit por rango |
| Ferocity | 5 | 5 | 5 | Vale algo menos (rabia casi infinita) |
| Feral Swiftness | 2 | 2 | 2 | Mono-Bear: por la velocidad en gato |
| Feral Instinct | 3 | — | 3 | +30 % Swipe |
| Thick Hide | 3 | 3 | 3 | Mejor que en vanilla |
| Savage Fury / Feral Charge / Sharpened Claws / Predatory Strikes | 2 / 1 / 2 / 3 | 2 / 1 / 2 / 3 | 2 / 1 / 2 / 3 | |
| Lacerate | 1 | 1 | 1 | |
| Predatory Discipline | 1 | 1 | — | Solo para llegar a Shifting Power |
| Blood Frenzy | — | 2 | 1 | Variant: permite usar Ferocious Bite |
| Leader of the Pack / Natural Instinct | 1 / 2 | 1 / 2 | 1 / 2 | |
| Rend and Tear | 5 | 5 | 5 | |
| Primal Bite | 1 | 1 | 1 | |
| Shifting Power | 1 | 1 | — | |
| Heart of the Wild / Naturalist | 5 / 5 | 5 / 5 | 5 / 5 | HotW: +20 % Stamina en oso |

- Hybrid: ~95 % del daño de Mono-Cat y ~98 % de Mono-Bear, sin perder nada defensivo. En gato: Claw de relleno y Shred solo con Omen of Clarity; sin Ferocious Bite.
- Variant: cambia Feral Instinct por Blood Frenzy y Nature's Majesty; a ~1 % de Mono-Cat, peor en multiobjetivo.
- Mono-Bear: renuncia a habilidades de gato a cambio de +2 % crit y algo de rabia.
- No recomendados: Furor (queda muerto) y Natural Reactions (caro y profundo).

Orden del widget:
- **Hybrid**: Ferocity 10–14 → Feral Instinct 15–17 → Thick Hide 18–20 → Feral Swiftness 21–22 → Savage Fury 23–24 → Feral Charge 25 → Sharpened Claws 26–27 → Lacerate 28 → Predatory Discipline 29 → Predatory Strikes 30–32 → LotP 33 → Natural Instinct 34–35 → Rend and Tear 36–40 → Primal Bite 41 → Shifting Power 42 → HotW 43–47 → Naturalist 48–52 → Genesis 53–57 → Nature's Reach 58–59 → Nature's Majesty 60.
- **Variant**: HotW 10–14 → Naturalist 15–19 → Genesis 20–24 → Nature's Majesty 25–26 → Nature's Reach 27–28 → Ferocity 29–33 → Feral Swiftness 34–35 → Thick Hide 36–38 → Savage Fury 39–40 → Feral Charge 41 → Sharpened Claws 42–43 → Blood Frenzy 44–45 → Predatory Discipline 46 → Lacerate 47 → Predatory Strikes 48–50 → LotP 51 → Natural Instinct 52–53 → Rend and Tear 54–58 → Primal Bite 59 → Shifting Power 60.
- **Mono-Bear**: Genesis 10–14 → Nature's Majesty 15–16 → Nature's Reach 17–18 → HotW 19–23 → Naturalist 24–28 → Ferocity 29–33 → Feral Swiftness 34–35 → Feral Instinct 36–38 → Thick Hide 39–41 → Savage Fury 42–43 → Feral Charge 44 → Sharpened Claws 45–46 → Lacerate 47 → Predatory Strikes 48–50 → LotP 51 → Blood Frenzy 52 → Natural Instinct 53–54 → Rend and Tear 55–59 → Primal Bite 60.
- Legacy: hacia Reagent Economy con Gourmand y Permanence (endgame); subiendo, árbol de aventura (Talented, Frequent Flier). Los dos widgets de Legacy usan otro formato y **no se decodificaron**.

## Rotación

| Situación | Prioridad (Method) | Estado |
|---|---|---|
| 10 s antes | Bear → (opcional) equipar WHH y EI → Enrage → volver a tu equipo | confirmed_forever |
| Pull | Maul en cola → Faerie Fire → Feral Charge → Mighty Rage o Greater Stoneshield (opcional) | confirmed_forever |
| 1 objetivo | Lacerate si hay 5 cargas y quedan ≤3 s → Faerie Fire si falta reducción de armadura → Primal Bite → Demoralizing Roar si falta → Lacerate → Maul con >35 rabia | confirmed_forever (Lacerate sin probar) |
| 2 objetivos | Faerie Fire → Primal Bite → Demoralizing Roar → Lacerate si no hay sangrado → Swipe → Maul | confirmed_forever |
| 3+ | Faerie Fire → Demoralizing Roar → Swipe → Maul | confirmed_forever |

- Reducción de armadura menor: Faerie Fire o la curse/debuff equivalente de otra clase; reducción de AP: Demoralizing Roar u otro equivalente.

## Stats y equipo

| Stat | Efecto (Method, guía Feral Tank) |
|---|---|
| Weapon DPS | Zarpa = DPS del arma × 2,5 (conflicto: ×1 en [[Feral-DPS-Druid]]); 14 AP = +1 DPS de arma |
| Strength | 1 = 2 AP |
| Agility | 1 = 0,05 % crit, 0,05 % esquiva, 2 de armadura |
| Hit | Cap 8 % |
| Expertise | 6,5 % sin esquivas; 14 % sin paradas |
| Armor | Máx. 75 % de reducción; armadura del equipo ×4,6 en Dire Bear |
| Defense | 1 = 0,04 % fallo/esquiva y −0,04 % crit recibido; cap blando 440 |
| Feral Combat Skill | 1 = −0,04 % fallo/esquiva/parada y +0,04 % crit; aparece en el equipo de Forever |

- Ofensivo: DPS del arma > Strength; Hit, Expertise y Feral Combat Skill excelentes; Crit bueno; Haste mediocre.
- Defensivo: Stamina y Armor > Agility > Dodge; Defense desconocido.
- Sin pesos de stats. Pre-raid BiS, BiS, tier y abalorios: **desconocido** ("Work In Progress").

## Encantamientos y consumibles

| Slot | Encantamiento (Method) | Alternativa |
|---|---|---|
| Arma | Crusader | Strength, Impact |
| Collar | Deflection | Strength |
| Capa | Defense | Agility, Dodge |
| Pecho / Guantes / Piernas / Pies | Wild Leather Armor Kit | Stamina, Strength o Speed según slot; Rugged Armor Kit |
| Muñecas | Deflection | Stamina, Strength |
| Cabeza / Hombros | TBD | — |

- Posible bug: la armadura de los kits recibe el multiplicador de oso; si se confirma, Rugged Armor Kit sería BiS en casi todos los slots.
- Consumibles: Weightstone o Sharpening Stone (suben la zarpa), Mighty Rage Potion (rabia y +60 Str 20 s), Greater Stoneshield, Elixir of the Giants, Chops, Dragonbreath Chili.

## Razas y profesiones
- **Tauren** (Horde): Endurance, War Stomp (CD 90 s, en forma), Plainsrunning (+60 %, también en sigilo), Cultivation.
- **Night Elf** (Alliance): Elune's Light con Berserk en oso; Quickness y Shadowmeld poco útiles.
- **Skyborne**: Elemental Insight domina contra elementales; Wind Blessed 2 % haste (mal stat para oso); Skysight (Horde) da movilidad.
- Profesiones: **Engineering** (parece que la Sapper se usa en forma).

## Interfaz, addons y macros
- Leatrix Plus, Threat Plates, Threat Classic 2, y Method Raid Tools, DBM o BigWigs (sin probar).
- Macros: `/cast [noform:1] Dire Bear Form`; botón combinado por forma; power shift; Growl a focus/mouseover/objetivo; Travel/Aquatic/Cat.

## En grupo con un Rogue
- Un oso con la build Hybrid tanquea y aporta Leader of the Pack (crit) y Faerie Fire (armadura), que suben el daño del Rogue; si no hace falta tanque, pasa a gato. *Buffs según Method; uso en dúo inferido.*

## Qué dicen las guías
- [[src-method-class-guides-feral-tank-druid]], [[src-method-class-guides-feral-tank-druid-talents]], [[src-method-class-guides-feral-tank-druid-rotation-and-playstyle]], [[src-method-class-guides-feral-tank-druid-bis-gear-and-stats]], [[src-method-class-guides-feral-tank-druid-enchants-and-consumables]], [[src-method-class-guides-feral-tank-druid-races-professions-and-other]], [[src-method-class-guides-feral-tank-druid-interface-addons-and-macros]].
- **Conflicto**: multiplicador del arma ×2,5 (aquí) frente a ×1 ([[src-method-class-guides-feral-dps-druid-bis-gear-and-stats]]).
- Hit cap de 8 % igual que en [[src-method-how-does-hit-chance-work-in-wow-forever]].

## Fuentes

| URL | Tipo | Fecha página | Consultada | ¿Pre-parche? |
|---|---|---|---|---|
| https://www.method.gg/wow-forever/class-guides/feral-tank-druid (+ 6 subpáginas) | Guía Method | 2026-11-04 | 2026-11-13 | No |
| https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json | Datos de la calculadora (Method) | 1.60.1 (02-11) | 2026-11-13 | No |
| https://foreverdb.net/class/Druid/talents | Datos de cliente | sin fecha | 2026-11-13 | No |

[Data from ForeverDB.net](https://foreverdb.net)

## Preguntas pendientes
- ¿Cómo funciona realmente Lacerate? Las APL son una estimación.
- ¿Es un bug que los kits de armadura reciban el multiplicador de oso?
- ¿Multiplicador del arma ×2,5 o ×1?
