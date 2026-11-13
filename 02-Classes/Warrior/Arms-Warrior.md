---
type: spec
tags: [forever, warrior, arms, endgame]
level_min: 10
level_max: 60
faction: both
status: confirmed_forever
confidence: medium
last_verified: 2026-11-13
game_version: "Forever 1.60.1"
sources:
  - https://www.method.gg/wow-forever/class-guides/arms-warrior
  - https://www.method.gg/wow-forever/class-guides/arms-warrior/talents
  - https://www.method.gg/wow-forever/class-guides/arms-warrior/rotation-and-playstyle
  - https://www.method.gg/wow-forever/class-guides/arms-warrior/bis-gear-and-stats
  - https://www.method.gg/wow-forever/class-guides/arms-warrior/enchants-and-consumables
  - https://www.method.gg/wow-forever/class-guides/arms-warrior/races-professions-and-other
  - https://www.method.gg/wow-forever/class-guides/arms-warrior/interface-addons-and-macros
  - https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json
  - https://foreverdb.net/class/Warrior/talents
related: ["[[Warrior]]", "[[Warrior-Leveling]]", "[[Fury-Warrior]]", "[[Protection-Warrior]]", "[[Hit-Chance]]"]
---

# Arms Warrior

> [!success] Confirmado en Forever
> Guía de endgame de Method (Babyhoof, 2026-11-04, parche 1.60.1). Build decodificada con el archivo de talentos 1.60.1 del 02-11 y nombres de ForeverDB. BiS "Work In Progress".

## Resumen
- En Forever Arms pasa a ser **DPS sostenido a un objetivo con cleave a ráfagas** (Sweeping Strikes); deja de ser una spec de PvP. `confirmed_forever`
- Build de Method: **32/19/0** con Mortal Strike (41), Weaponmaster, Bloodthrill y Fury hasta Enrage. `confirmed_forever`
- Prioridad dinámica: Rend activo → Overpower con proc de Bloodthrill → Mortal Strike → Slam. `confirmed_forever`
- Stats: **Hit hasta 8 % > Crit > Haste > Strength > Agility > Stamina**.
- Night Elf es la raza S; Engineering imprescindible.

## Talentos

### Build "Standard Arms" (Method) — 32/19/0
| Nivel | Talento | Árbol |
|---|---|---|
| 10–12 | Improved Rend 3/3 | Arms |
| 13–14, 24 | Improved Heroic Strike 3/3 | Arms |
| 15–17 | Improved Tactical Mastery 3/3 | Arms |
| 18–19 | Improved Overpower 2/2 | Arms |
| 20 | Anger Management 1/1 | Arms |
| 21–23 | Deep Wounds 3/3 | Arms |
| 25–27 | Two-Handed Weapon Specialization 3/3 | Arms |
| 28–29 | Impale 2/2 | Arms |
| 30 | Spearing Strike 1/1 | Arms |
| 31 | Sweeping Strikes 1/1 | Arms |
| 32–33 | Bloodthrill 2/2 | Arms |
| 34–38 | Weaponmaster 5/5 | Arms |
| 39–40 | Improved Slam 2/2 | Arms |
| 41 | Mortal Strike 1/1 | Arms |
| 42–46 | Cruelty 5/5 | Fury |
| 47–51 | Unbridled Wrath 5/5 | Fury |
| 52–56 | Enrage 5/5 | Fury |
| 57 | Reckless Swings 1/1 | Fury |
| 58–59 | Improved Execute 2/2 | Fury |
| 60 | Lingering Rage 1/5 | Fury |

### Talentos clave (texto del cliente, ForeverDB)
| Talento | Efecto | Estado |
|---|---|---|
| Bloodthrill (nuevo) | Golpes de mano principal contra objetivos con tu Rend: 20 % de habilitar Overpower | confirmed_forever |
| Weaponmaster (nuevo) | Según arma: hacha/asta +5 % crit; maza/bastón ignora 15 % de armadura; espada 5 % de ataque extra | confirmed_forever |
| Spearing Strike (nuevo) | 75 % de daño de arma; +75 % contra gigantes, dragonantes y objetivos montados | confirmed_forever |
| Improved Slam | −5 s de CD, −0,5 s de casteo y GCD; Slam ya no reinicia el swing | confirmed_forever |
| Anger Management | 1 de rabia cada 3 s en combate | confirmed_forever |
| Reckless Swings (nuevo, Fury) | 4 siguientes golpes generan +5 de rabia | confirmed_forever |

- Legacy: Method recomienda **Gourmand** y **Permanence**.
- Leveling: ver [[Warrior-Leveling]] (Method sube Arms 2H en grupo).

## Rotación
| Situación | Prioridad (Method) | Estado |
|---|---|---|
| Un objetivo | Battle Shout → Rend → Overpower (proc) → Mortal Strike → Slam → Sunder si toca → Heroic Strike con >60 rabia | confirmed_forever |
| Cleave | Battle Shout → Rend en el principal → Sweeping Strikes → Overpower → MS → Cleave (>60) → Whirlwind (Berserker Stance) → Slam | confirmed_forever |

- Si te asignan Demoralizing Shout y Thunder Clap, van primero.
- Bloodthrill no acumula y Overpower tiene 5 s de CD: gastar el proc al momento.
- Sweeping Strikes: 5 ataques; los autoataques también los consumen.

## Stats y equipo
- **Hit hasta 8 % > Crit % > Haste % > Strength > Agility > Stamina**. El 8 % es el tope de cuerpo a cuerpo contra jefe (ver [[Hit-Chance]]).
- Pre-raid BiS, BiS, tier y trinkets: **desconocido** ("Work In Progress" en Method).

## Encantamientos y consumibles
| Slot | Encantamiento | Alternativa |
|---|---|---|
| Arma | Crusader | — |
| Cabeza / piernas | Lesser Arcanum of Voracity | — |
| Collar | Strength | Agility |
| Capa | Agility | — |
| Pecho | Greater Stats | — |
| Muñecas / guantes | Superior Strength | — |
| Botas | Minor Speed | — |

- Dense Weightstone / Dense Sharpening Stone (en Forever **acumulan con Windfury Totem**), Mighty Rage Potion, Flask of Natural Precision, Mightfish Steak. Lista parcial según el propio autor.

## Razas y profesiones
- Tiers: **S Night Elf** · A Human, Skyborne, Dwarf, Undead, Troll · B Gnome, Orc · C Tauren. Todas a ≤2 % salvo combates muy cortos.
- Undead "simula alto" pero rinde peor en cleave. Dwarf: 1 % hit + Beast Slaying.
- **Engineering** (Dense Dynamite, Goblin Sapper Charge) + cualquier otra (Mining habitual) + **First Aid**.

## Interfaz, addons y macros
- Cooldown Manager con temporizador de swing. Medidor de amenaza obligatorio (Details o ThreatClassic2); DBM/BigWigs; Plater o Platynator. Addons sin probar por nosotros.
- Macro `/cast <habilidad>` + `/startattack` (sin rabia el autoataque no arranca solo); Sunder Armor por `[@mouseover]`.

## En grupo con un Rogue
Aporta Battle Shout y Sunder Armor (el Rogue puede dejar Expose Armor), daño de cleave y, si hace falta, Demoralizing Shout. Ambos dependen de Windfury Totem si hay Shaman.

## Qué dicen las guías
- [[src-method-class-guides-arms-warrior]] y [[src-method-class-guides-arms-warrior-talents]]: build única 32/19/0.
- [[src-method-class-guides-arms-warrior-rotation-and-playstyle]]: prioridades.
- [[src-method-class-guides-arms-warrior-bis-gear-and-stats]]: stats; BiS WIP. Contradicción interna: Haste es el 3.er stat, pero [[src-method-class-guides-arms-warrior-races-professions-and-other]] dice que Arms valora poco la Haste.
- [[src-method-class-guides-arms-warrior-enchants-and-consumables]], [[src-method-class-guides-arms-warrior-interface-addons-and-macros]].
- Leveling: [[src-method-wow-forever-warrior-leveling-guide-and-talents]] (mismos talentos núcleo sin puntos).

## Fuentes
| URL | Tipo | Fecha de la página | Consultada | ¿Anterior al parche del 02-11? |
|---|---|---|---|---|
| https://www.method.gg/wow-forever/class-guides/arms-warrior (+ 6 subpáginas) | guide | 2026-11-04 | 2026-11-13 | No |
| https://www.method.gg/dfc/ForeverTalentsData-1.60.1-2nov.json | datos de la calculadora (Method) | 2026-11-02 | 2026-11-13 | No |
| https://foreverdb.net/class/Warrior/talents | datos de cliente | sin fecha | 2026-11-13 | No |

[Data from ForeverDB.net](https://foreverdb.net)

## Preguntas pendientes
- ¿Qué arma 2H rinde más con Weaponmaster? Method no lo dice.
- ¿Cuánto vale la Haste para Arms? La guía se contradice.
- BiS pre-raid: pendiente de Method.
