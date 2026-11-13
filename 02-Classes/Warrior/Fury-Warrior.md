---
type: spec
tags: [forever, warrior, fury, endgame]
level_min: 10
level_max: 60
faction: both
status: confirmed_forever
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://www.method.gg/wow-forever/class-guides/fury-warrior
  - https://www.method.gg/wow-forever/class-guides/fury-warrior/talents
  - https://www.method.gg/wow-forever/class-guides/fury-warrior/rotation-and-playstyle
  - https://www.method.gg/wow-forever/class-guides/fury-warrior/bis-gear-and-stats
  - https://www.method.gg/wow-forever/class-guides/fury-warrior/enchants-and-consumables
  - https://www.method.gg/wow-forever/class-guides/fury-warrior/races-professions-and-other
  - https://www.method.gg/wow-forever/class-guides/fury-warrior/interface-addons-and-macros
  - https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json
  - https://foreverdb.net/class/Warrior/talents
related: ["[[Warrior]]", "[[Warrior-Leveling]]", "[[Arms-Warrior]]", "[[Protection-Warrior]]", "[[Hit-Chance]]"]
---

# Fury Warrior

> [!success] Confirmado en Forever
> Guía de endgame de Method (Babyhoof, 2026-11-04, parche 1.60.1). Build decodificada con el archivo de talentos del 02-11 y nombres de ForeverDB. BiS "Work In Progress".

## Resumen
- Fury **casi no cambia respecto a Classic**: talentos movidos, se quita el bug de cola de Heroic Strike y nueva normalización de rabia. `confirmed_forever`
- Build de raid **17/34/0**: Bloodthirst (40), Flurry, Death Wish, Dual Wield Spec.; en Arms, Deep Wounds, Impale e Imp. Overpower para el "stance dance".
- Rotación: Execute > Bloodthirst > Whirlwind > Overpower; Heroic Strike/Cleave con >60 de rabia.
- Stats: **Hit 8 % (soft cap) > Crit > Haste > Strength > Agility > Hit sobre 8 % > Stamina**.
- Night Elf raza S; Skyborne gana valor en Fury por la Haste.

## Talentos

### Build "Standard Raid" (Method) — 17/34/0
| Nivel | Talento | Árbol |
|---|---|---|
| 10–14 | Cruelty 5/5 | Fury |
| 15–19 | Unbridled Wrath 5/5 | Fury |
| 20–22 | Furious Precision 3/3 | Fury |
| 23–24, 59–60 | Enrage 4/5 | Fury |
| 25–29 | Dual Wield Specialization 5/5 | Fury |
| 30 | Reckless Swings 1/1 | Fury |
| 31–32 | Improved Execute 2/2 | Fury |
| 33 | Death Wish 1/1 | Fury |
| 34, 58 | Improved Berserker Rage 2/2 | Fury |
| 35–37 | Flurry 3/3 | Fury |
| 38–39 | Improved Whirlwind 2/2 | Fury |
| 40 | Bloodthirst 1/1 | Fury |
| 41–43 | Improved Rend 3/3 | Arms |
| 44–46 | Improved Heroic Strike 3/3 | Arms |
| 47–49 | Improved Tactical Mastery 3/3 | Arms |
| 50–51 | Improved Overpower 2/2 | Arms |
| 52–54 | Deep Wounds 3/3 | Arms |
| 55 | Anger Management 1/1 | Arms |
| 56–57 | Impale 2/2 | Arms |

### Talentos clave (texto del cliente, ForeverDB)
| Talento | Efecto | Estado |
|---|---|---|
| Furious Precision (nuevo) | +10 % de golpe con la mano izquierda | confirmed_forever |
| Dual Wield Specialization | +25 % daño de mano izquierda y +50 % de rabia de sus golpes | confirmed_forever |
| Unbridled Wrath | 60 % de generar 1 rabia extra al golpear | confirmed_forever |
| Death Wish | +20 % daño físico e inmunidad a miedo; recibes +5 % de daño (en Classic bajaba armadura) | confirmed_forever |
| Improved Whirlwind (nuevo) | −2 s de CD y +30 % de daño al enemigo más cercano | confirmed_forever |
| Bloodthirst | 45 % del AP + 30 y +10 % de velocidad 10 s | confirmed_forever |

- Legacy: Gourmand y Permanence.

## Rotación
| Paso | Acción (Method) | Estado |
|---|---|---|
| 1 | Battle Shout | confirmed_forever |
| 2 | Execute (objetivo <20 %) | confirmed_forever |
| 3 | Overpower si el proc caduca en <2 s | confirmed_forever |
| 4 | Bloodthirst | confirmed_forever |
| 5 | Whirlwind | confirmed_forever |
| 6 | Overpower con proc | confirmed_forever |
| 7 | Sunder Armor si te lo asignan | confirmed_forever |
| 8 | Heroic Strike / Cleave con >60 de rabia | confirmed_forever |

- Utilidad por importancia: Sunder Armor > Demoralizing Shout > Thunder Clap. Si te la asignan, va primero; Protection Warrior suele cubrir dos de ellas.

## Stats y equipo
- **Hit hasta 8 % > Crit > Haste > Strength > Agility > Hit por encima de 8 % > Stamina**. Ver [[Hit-Chance]].
- Pre-raid BiS, BiS, tier y trinkets: **desconocido** ("Work In Progress").

## Encantamientos y consumibles
- Igual que Arms: Crusader; Lesser Arcanum of Voracity (cabeza, piernas); collar Strength (alt. Agility); capa Agility; Greater Stats; Superior Strength (muñecas, guantes); Minor Speed.
- Piedras Dense (acumulan con Windfury Totem), Mighty Rage Potion, Flask of Natural Precision, Mightfish Steak.

## Razas y profesiones
- Tiers: **S Night Elf** · A Human, Skyborne, Dwarf, Undead, Troll · B Gnome, Orc · C Tauren (≤2 % entre todas).
- Skyborne: Wind Blessed (+2 % Haste) rinde mucho en Fury (más rabia y daño). Troll: Berserking algo por debajo.
- Engineering + cualquiera (Mining habitual) + First Aid.

## Interfaz, addons y macros
- Cooldown Manager con swing timer; medidor de amenaza obligatorio; DBM/BigWigs; Plater/Platynator. Macros `/startattack` y Sunder por mouseover. Addons sin probar por nosotros.

## En grupo con un Rogue
Battle Shout y Sunder Armor para el daño físico del Rogue; mucho daño y amenaza propia, así que el Rogue suele quedar por debajo en la tabla de amenaza. Ambos piden Windfury Totem.

## Qué dicen las guías
- [[src-method-class-guides-fury-warrior]], [[src-method-class-guides-fury-warrior-talents]], [[src-method-class-guides-fury-warrior-rotation-and-playstyle]], [[src-method-class-guides-fury-warrior-bis-gear-and-stats]], [[src-method-class-guides-fury-warrior-enchants-and-consumables]], [[src-method-class-guides-fury-warrior-races-professions-and-other]], [[src-method-class-guides-fury-warrior-interface-addons-and-macros]].
- La guía de leveling ([[src-method-wow-forever-warrior-leveling-guide-and-talents]]) solo usa Fury para Unbridled Wrath y Enrage dentro de Arms.

## Fuentes
| URL | Tipo | Fecha de la página | Consultada | ¿Anterior al parche del 02-11? |
|---|---|---|---|---|
| https://www.method.gg/wow-forever/class-guides/fury-warrior (+ 6 subpáginas) | guide | 2026-11-04 | 2026-11-13 | No |
| https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json | datos de la calculadora (Method) | 2026-11-02 | 2026-11-13 | No |
| https://foreverdb.net/class/Warrior/talents | datos de cliente | sin fecha | 2026-11-13 | No |

[Data from ForeverDB.net](https://foreverdb.net)

## Preguntas pendientes
- ¿Cuánto hit extra por encima del 8 % compensa con doble arma? Method no da cifra.
- BiS pre-raid y armas: pendiente.
