---
type: playbook
tags: [forever, playbook, paladin, undead, retribution, leveling, horde, dungeons, macros]
level_min: 1
level_max: 40
faction: horde
status: confirmed_forever
confidence: medium
last_verified: 2026-11-24
game_version: "Forever 1.60.1"
sources:
  - https://mobalytics.gg/wow-forever/classes/retribution-paladin-guide
  - https://www.method.gg/wow-forever/wow-forever-paladin-leveling-guide-and-talents
  - https://www.method.gg/wow-forever/class-guides/retribution-paladin
  - "Addon ForeverDB, datos 2026-11-13.ea2bb422: misiones, recompensas, botín de mazmorras observado en Forever, vendedores, recetas"
  - "Azeroth DB (azeroth.wiki), cliente Forever: objetos, talentos, encantamientos, misiones"
related: ["[[Paladin]]", "[[Paladin-Leveling]]", "[[Retribution-Paladin]]", "[[Leveling-Route-Undead]]", "[[Ruins-of-Lordaeron]]", "[[Camping]]", "[[UI]]", "[[Races]]", "[[Enchanting]]", "[[Playbook-Hunter-1-30]]", "[[Mage-Route-23-30]]"]
---

# Playbook: Undead Paladin Retribution 1–30 (con vista al 40)

> [!abstract] Para quién
> Main de la Horde. En Forever, **el único Paladin de la Horde es el Undead**. Está en el mismo reino que el Troll Mage (Tailoring + Enchanting, con oro) y el Troll Hunter. Juega sobre todo **solo**, quiere aguantar y ganar el 1 contra 1. Esta guía junta lo mejor de **Mobalytics** (Jampanos, actualizada 2026-11-15) y **Method** (Jurdi, 2026-11-09 y 2026-11-14). Cada objeto y misión está comprobado en los datos de Forever (addon ForeverDB y azeroth.wiki, 2026-11-24).

## Resumen
- **Regla número uno: el dps del arma lo es todo.** 1 de dps de arma = 14 de poder de ataque ≈ 7 de Strength (Mobalytics). Cada vez que veas un arma de dos manos con más dps, cámbiala. §6.
- **Talentos**: el orden nivel a nivel de Mobalytics. Solo: Deflection primero (aguantas más). En grupo o sin maná: Benediction (Method). §2.
- **Rotación**: sello puesto; Judgement y Holy Strike cada vez que estén listos. A partir del 20, **Seal of Command** con arma lenta. **Hammer of Justice → Judgement** duplica el daño del Judgement. §3.
- **Mazmorras**: en Forever las **misiones de mazmorra dan mucha más XP y mejor equipo**, y matar dentro da poca XP. Lleva todas las misiones antes de entrar y haz una sola run (Mobalytics). Para un Undead, la mejor es **Ruins of Lordaeron** (15–22). §5.
- **Profesiones**: Mining + Blacksmithing hasta ~95, luego aparca Blacksmithing hasta el 60. **Cooking**: casi toda la comida da +5 % de XP. §8.
- **Macros** listas para copiar en §4.

## Qué tomé de cada guía
| Tema | Mobalytics | Method | En esta guía |
|---|---|---|---|
| Talentos 10–30 | Orden **nivel a nivel**, al día con el cambio de talentos del 31-10 | Solo el orden general (Benediction → Sanctified → Improved Judgement → Pursuit of Justice antes del 21) | Mobalytics, con el cambio de Method si te falta maná |
| Prioridad de stats para subir | **Weapon DPS ≫ Sta = Spi = Str = Agi > Hit/Crit > SP > AP** | Solo la de endgame (Hit > Expertise > SP > Str = AP > Int > Crit) | Mobalytics hasta el 60, Method en el 60 |
| Rotación | Detalles: Seal of Command a 7 procs por minuto (mejor arma lenta), Judgement doble contra aturdidos | Lista de prioridad completa (un objetivo, área, Holy Shock) | Las dos |
| Macros | — | Mouseover de BoP, Freedom y Cleanse | Las de Method y algunas más (§4) |
| Armas | Lista de armas fijas de la Horde hasta el 60 | Armas de leveling y picos de poder | Unidas y comprobadas en los datos de Forever (§6) |
| Profesiones | No subir profesiones de artesanía mientras subes; Cooking +5 % XP | Blacksmithing + Mining | Mining + Blacksmithing hasta ~95, Cooking y First Aid |
| Mazmorras | Prepara todas las misiones; una sola run | Fuentes de objetos | Plan por nivel (§5) |

## 1. Niveles 1–10: Tirisfal Glades
| Paso | Dónde | Qué |
|---|---|---|
| 1–5 | **Deathknell** | Entrenador **Aramis Hammerhand** (31.1, 66.3). Aprende **Mining** ya y compra pico: en Forever se puede en las zonas de inicio (Mobalytics) |
| 4 | Brill | **Wooden Mallet** (5,0 dps, 7 s). Mobalytics la sitúa en Oliver Dwor (Brill); ForeverDB, en Angus Hammerhand (21.2, 45.8) y Gordon Wendham (Undercity 61.9, 42.1) |
| ~5 | Brill | *The Great Outdoors* con Eleanor Shackleton (57.2, 55.5): desbloquea las hogueras y Cooking. Ver [[Camping]] |
| 5–10 | **Brill** | Entrenadora **Shari Stilwell** (60.3, 52.6). Haz todas las misiones de Brill |
| 10 | Costa oeste | *Murlocs at the Gates* (Breton Samuels 21.8, 45.3): Driftwood Smasher |
| 11–13 | Brill | *Deaths in the Family* (Coleman Farthing 61.7, 52.3) → **The Family Crypt** (Magistrate Sevren 61.3, 50.8): **Bonecracker** (9,1 dps, Str +3) |

**Hechizos** `confirmed_forever` (Method):
- **1:** Seal of Righteousness.
- **2:** Holy Light.
- **4:** Judgement, Blessing of Might.
- **6:** **Holy Strike** (nuevo), Divine Protection.
- **8:** **Hammer of Justice**, Purify.
- **10:** Seal of Fury, Righteous Fury, Blessing of Protection.
- **12:** Redemption.
- **14:** Blessing of Wisdom.
- **16:** Retribution Aura.
- **20:** **Consecration** y **Blessing of Kings** (de base en Forever).
- **30:** Repentance (talento).
- **40:** montura de clase.
- **44:** Hammer of Wrath.

Entrena **cada nivel par**. Otros entrenadores: Garen Largo (Undercity 47.4, 15.0) y Alodan (Thunder Bluff 25.4, 14.4).

## 2. Talentos nivel a nivel
Orden de Mobalytics (1–30, 0/0/21). Efectos por punto, del cliente de Forever (azeroth.wiki).

| Nivel | Talento | Qué hace |
|---|---|---|
| 10–14 | **Deflection** 5/5 | +1 % de parada por punto (+5 %): aguantas más jugando solo |
| 15–17 | **Conviction** 3/3 | +1 % de crítico cuerpo a cuerpo por punto |
| 18–19 | **Improved Judgement** 2/2 | −1 s de reutilización de Judgement por punto |
| **20** | **Seal of Command** | Tu sello de daño: cambias de Seal of Righteousness a este |
| 21–22 | **Pursuit of Justice** 2/2 | Más velocidad a pie y en montura (+8 % el rango 1; 15 % el máximo según Method) |
| 23–24 | Sanctified Judgement 2/3 | 33 % de probabilidad de que Judgement devuelva el 20 % del coste del sello (rango 1) |
| 25 | **Sacred Arbiter** | Holy Strike hace +20 % de daño y renueva los efectos de Judgement del objetivo |
| 26 | Sanctified Judgement 3/3 | |
| 27–29 | **Two-Handed Weapon Specialization** 3/3 | +2 % de daño con arma de dos manos por punto |
| 30 | **Repentance** | Incapacita a un enemigo. Con Seal of Command, el Judgement hace el doble contra él (§3) |

**Cuándo cambiarlo (de Method):**
- **En grupo o si paras mucho a beber:** cambia Deflection por **Benediction** 5/5 (−2 % de coste de maná en instantáneos por punto). Mobalytics lo propone para grupo y Method lo pone primero.
- **Del 31 al 40** (Method): Vengeance, **Champion of the Light** (tu Intellect da poder con hechizos), Unyielding Faith 1 punto y **Unsealed Wrath** (el talento final). Después, en Holy, Divine Strength → Improved Seals → Holy Conduit (maná), y en Protection, Precision (golpe).
- La build de endgame (Holy primero) **no es para subir de nivel**.
- **Dual spec** al 40: 50 g en cualquier entrenador de Paladin (Method).

## 3. Rotación
### Contra un enemigo
**Del 1 al 19:**
1. **Seal of Righteousness** siempre puesto. En Forever, Judgement **no gasta el sello**.
2. **Judgement** cada vez que esté listo. **No usa el tiempo global de reutilización** (Method): se mezcla con todo.
3. **Holy Strike** cada vez que esté listo.
4. Autoataque.

**Del 20 en adelante** (Method + Mobalytics):
1. **Seal of Command** puesto. Hace un 70 % del daño del arma en Holy, a 7 procs por minuto, así que **cuanto más lenta el arma, mejor** (Mobalytics).
2. **Judgement** cada vez que esté listo.
3. **Holy Strike** cada vez que esté listo.
4. **Exorcism** contra no-muertos y demonios.
5. **Consecration** solo si te sobra maná.
6. A partir del 44: **Hammer of Wrath** con el enemigo por debajo del 20 %.

**Del 40 en adelante, con Unsealed Wrath** (Method): con 3 cargas de Unsealed Wrath, cambia a Seal of Righteousness para aplicarlo y vuelve a Seal of Command.

### Trucos para ir más rápido
- **Hammer of Justice → Judgement**: con Seal of Command, Judgement hace **el doble** contra un enemigo aturdido o incapacitado (Mobalytics). Úsalo para abrir contra enemigos duros, y desde el 30 también con **Repentance → Judgement**. Pulsa los dos por separado para que el aturdimiento entre antes.
- **Arma lenta**: entre dos armas con el mismo dps, elige la de mayor velocidad (3,5 o más). Así rinden más Seal of Command y Holy Strike (Mobalytics).
- **Consecration** da el triple de daño a los 4 primeros enemigos que entran en ella (Mobalytics). Úsala con 3 o más encima, nunca contra uno solo.

### En área (20+)
Consecration primero, después Judgement y Holy Strike sobre el que más vida tenga.

### Supervivencia y maná
- **Holy Light** entre peleas (macro de autocuración en §4).
- Si la pelea se tuerce: **Divine Protection** y luego cúrate.
- **Hammer of Justice** corta un hechizo enemigo: **no tienes interrupción** (lo dicen las dos guías).
- **Blessing of Wisdom** si te quedas sin maná; si no, **Might**. Desde el 20, **Kings** (+10 % a todos los stats).
- **Cannibalize** sobre cadáveres humanoides o no-muertos: 35 % de vida y maná en 10 s (Mobalytics).
- Las bendiciones son **exclusivas**: solo puedes tener una tuya por objetivo. Si usas Freedom o Protection, vuelve a poner Might o Kings después (Mobalytics).

### 1 contra 1 (inferido de las habilidades)
1. Abre con Hammer of Justice → Judgement.
2. **Will of the Forsaken** contra miedo, encantamiento y sueño (Warlock, Priest).
3. **Blessing of Freedom** contra raíces y ralentizaciones (Frost Mage).
4. Divine Protection cuando vayas bajo y cúrate.
5. Guarda Hammer of Justice para cortar el hechizo grande del rival.

## 4. Macros
Copia cada una en **Esc → Macros**. Las tres primeras son las de Method. El resto son mías, con la misma sintaxis: **pruébalas en el juego antes de fiarte**. Son macros normales del juego: una acción por pulsación, sin automatizar nada.

**Blessing of Protection** sobre el aliado bajo el ratón, o sobre tu objetivo (Method):
```
#showtooltip Blessing of Protection
/cast [@mouseover,help][] Blessing of Protection
```

**Blessing of Freedom** (Method):
```
#showtooltip Blessing of Freedom
/cast [@mouseover,help][] Blessing of Freedom
```

**Cleanse** (Method). Hasta tenerlo, cambia "Cleanse" por "Purify":
```
#showtooltip Cleanse
/cast [@mouseover,help][] Cleanse
```

**Botón principal**: empieza a atacar, lanza Judgement si está listo y luego Holy Strike. Judgement no usa el tiempo global, así que caben los dos en una pulsación. Si en el juego solo sale uno, sepáralos en dos botones:
```
#showtooltip Holy Strike
/startattack
/cast Judgement
/cast Holy Strike
```

**Autocuración sin perder al enemigo**: cura al aliado bajo el ratón o al que tengas seleccionado; si tienes un enemigo seleccionado, te cura a ti:
```
#showtooltip Holy Light
/cast [@mouseover,help,nodead][help,nodead][@player] Holy Light
```

**Bendición inteligente** (cambia "Blessing of Might" por la que quieras):
```
#showtooltip Blessing of Might
/cast [@mouseover,help,nodead][help,nodead][@player] Blessing of Might
```

**Hammer of Justice al enemigo bajo el ratón** (para cortar al curandero o al caster sin cambiar de objetivo):
```
#showtooltip Hammer of Justice
/cast [@mouseover,harm,nodead][] Hammer of Justice
```

**Botón de pánico**:
```
#showtooltip Divine Protection
/stopcasting
/cast Divine Protection
```

**Un botón para dos sellos**: sin tecla, Seal of Command; con Shift, Seal of Righteousness. Te sirve para Unsealed Wrath al 40:
```
#showtooltip
/cast [mod:shift] Seal of Righteousness; Seal of Command
```

**Interfaz de Forever** (Mobalytics, viene del cliente moderno):
- **Edit Mode** (`/editmode`): mueve cualquier marco.
- **Damage Meter** y **Swing Timer**: actívalos buscando su nombre en Opciones.
- **Cooldown Manager**: actívalo en Opciones y abre `/cdm`. Pon Judgement, Holy Strike, Hammer of Justice y Divine Protection en "Essential Cooldowns", y tu sello y bendición en "Tracked Buffs".
- **Addons** que recomienda Mobalytics, **sin probar aquí**: DungeonJournal (`/dj`, misiones y requisitos de cada mazmorra), RestedXP (guías del 1 al 20) y PallyPower (raids).

## 5. Mazmorras para un Undead Paladin
Niveles: botín observado en ForeverDB. Mobalytics: **las misiones de mazmorra dan mucha más XP y equipo que en Classic, y matar dentro da poca XP**. Recoge todas las misiones antes de entrar y haz una run por mazmorra.

| Nivel | Mazmorra | Misiones clave (Horde) | Para ti |
|---|---|---|---|
| 13–18 | **Ragefire Chasm** (Orgrimmar) | Cadena *Hidden Enemies* (Thrall, 31.9, 37.8; 9+). *The Power to Destroy...* (Varimathras, Undercity) | **Axe of Orgrimmar** (azul, 16,1 dps). Aprende Hachas de dos manos en Orgrimmar (Mobalytics) |
| **15–22** | **Ruins of Lordaeron** (encima de Undercity) | *The Wrath of Rath'mael* (Deathguard Kristof 65.2, 60.2) → **Forsaken Greataxe**. *Light's Justice* (Morbin Lightbane, UC 58.0, 89.5). *The New Plague* (Theodore Griffs, UC 46.5, 71.8). *Unending Torment* (Faranell, UC 48.8, 69.0) → Monstrous Cleaver. *A Frightened Request* (Tabitha, Sepulcher 44.5, 42.9). *Crest of Lordaeron*. Unas 4.600–5.450 XP cada una | **Sword of the Fallen** (Str +6, Int +9), Corpse Chopper, Grip of Fear (manos, Str +6), Vilewalkers (Str +7), Death Bindings (Str +5) |
| 15–24 | **Wailing Caverns** (Barrens) | *Deviate Hides*: 3.100 XP en Forever | Mutant Scale Breastplate (Str +10, 33 %), Cobrahn's Grasp (Str +7) |
| 17–26 | Deadmines (Westfall, zona Alliance) | — | Rhahk'Zor's Hammer (azul, 18,4 dps, SP +8, Sta +8; 31 %). El **Goblin Woodcarver** suelta la Whitestone Oak Lumber de la cadena de Wolfsbane |
| 20–30 | **Shadowfang Keep** (Silverpine) | Tres misiones Horde, dos en The Sepulcher | **Arced War Axe** (Springvale, 71 %; 21,7 dps, Str +9, Sta +9), Phantom Armor (Sta +12) |
| 24–32 | **Blackfathom Deeps** (Ashenvale) | Cinco misiones Horde (Zoram'gar) | **Reef Axe** (22,4 dps, Str +8, SP +8), Strike of the Hydra (25,6 dps, 55 %), Algae Fists (Str +8) |
| 26–33 | **Excavation Site: Wetlands** | Tres misiones Horde, **15.300 XP** (beta). **Earthen Echo** (31; entrega en Thunder Bluff, Bashana Runetotem 71.0, 34.0) | **Heavehammer** (azul, 27,7 dps, AP +32, armadura +60) |
| 29–38 | **Razorfen Kraul** (Barrens sur) | *Going, Going, Guano!* (Undercity) | **Corpsemaker** (Ramtusk, 40 %; 28,9 dps, Str +15, Sta +8), Tusken Helm (Str +13) |
| 30–38 | **Scarlet Monastery** (Tirisfal NE) | Graveyard: dos misiones, 11.150 XP | Armory: **Ravager** (Herod, 15 %; 37,3 dps), Raging Berserker's Helm, Herod's Shoulder (Method) |
| 35–40 | The Drowned City (costa de Stranglethorn) | **A Tale Spun Around the Fire**; requisito, la cadena *The Vile Reef* (Kin'weelay, STV 32.3, 27.7; 37) | **Ceremonial Mallet** (37,2 dps, Sta +15, AP +22) |

**Cómo jugar en grupo:**
- **Bendiciones:** Might a guerreros, pícaros y cazadores. Wisdom a casters y curandero. Desde el 20, Kings.
- **Aura:** Retribution Aura (16).
- **Utilidad:** Protection sobre el que tenga el aggro y esté a punto de morir (macro). Freedom sobre el que esté enraizado. Purify contra veneno y enfermedad.
- **Sin interrupción:** guarda Hammer of Justice para el hechizo peligroso.
- **No uses Righteous Fury** si no tanqueas. Seal of Fury es tu única provocación.

## 6. Armas de dos manos: siempre la mejor
Regla de Mobalytics: **más dps de arma gana**. 1 dps ≈ 7 de Strength, así que un arma con 2 dps más vale como 14 de Strength.

| Nivel | Arma | dps | Stats | De dónde | Grupo |
|---|---|---|---|---|---|
| 4 | Wooden Mallet | 5,0 | — | Vendedor, 7 s (§1) | No |
| 10 | Giant Mace | 9,0 | — | Angus Hammerhand, Tirisfal (21.2, 45.8), 26 s | No |
| 11 | **Heavy Copper Maul** (verde, BoE) ✅ *la tienes* | 10,8 | Str +4 | Blacksmithing 65 o subasta | No |
| 13 | Bonecracker | 9,1 | Str +3 | *The Family Crypt* | No |
| 16 | **Axe of Orgrimmar** (azul) | 16,1 | Sta +6, Spi +6 | *Hidden Enemies* (RFC) | Sí |
| 16 | Rock Hammer | 12,6 | — | Benijah Fenner, Undercity (58.6, 32.3), 63 s | No |
| 16 | Rhahk'Zor's Hammer (azul) | 18,4 | SP +8, Sta +8 | Deadmines (31 %) | Sí |
| 16 | Corpse Chopper (azul) | 18,2 | — | Bjork, Ruins (44 %) | Sí |
| 18 | **Sword of the Fallen** (azul) | 19,7 | Str +6, Int +9 | Bjork / Rath'mael, Ruins | Sí |
| 21 | Maul | 16,0 | — | Benijah Fenner, Undercity, 1 g 9 s | No |
| 21 | **Arced War Axe** (azul) | 21,7 | Str +9, Sta +9 | Springvale, SFK (71 %) | Sí |
| 22 | **Forsaken Greataxe** (azul) | 20,5 | Str +8, Sta +4 | *The Wrath of Rath'mael* (Ruins) | Sí |
| 22 | Reef Axe (azul) | 22,4 | Str +8, SP +8 | Geilhast, BFD (18 %) | Sí |
| 24 | Demolition Hammer | 17,6 | Str +9 | *Weapons of Choice* (Tatternack Steelforge, Camp Taurajo 45.1, 57.7) | No |
| ~26 | **Wolfsbane** (azul, espada) | **25,6** | Int +10, Sta +9 | Misión de clase Undead Paladin (abajo) | Partes |
| 26 | Strike of the Hydra (azul) | 25,6 | — | Aku'mai, BFD (55 %) | Sí |
| 28 | Brute Hammer | 19,1 | Sta +8, Str +4 | *Arikara* (Thousand Needles) | No |
| 29 | **Corpsemaker** (azul) | 28,9 | Str +15, Sta +8 | Ramtusk, RFK (40 %) | Sí |
| 30 | War Hammer | 22,3 | — | Galthuk, Orgrimmar (82.2, 18.6) | No |
| 31 | **Heavehammer** (azul) | 27,7 | AP +32 | *Earthen Echo* (Excavation Site) | Sí |
| 37 | Ravager (azul) | 37,3 | — | Herod, SM Armory (15 %) | Sí |
| 37+ | **Ceremonial Mallet** | 37,2 | Sta +15, AP +22 | *A Tale Spun Around the Fire* (Drowned City) | Sí |

**Tu camino:**
- **Solo:** Heavy Copper Maul → **Rock Hammer (16)**: +1,8 dps, unos 12 de Strength, supera los Str +4 de tu maza → Maul (21) o Demolition Hammer (24) → **Wolfsbane** → War Hammer (30).
- **Con grupo:** Heavy Copper Maul → Axe of Orgrimmar (16) → Sword of the Fallen o Forsaken Greataxe (18–22) → Arced War Axe o Reef Axe → Wolfsbane o Strike of the Hydra (26) → Corpsemaker (29) → Heavehammer (31) → Ravager o Ceremonial Mallet (37).

**Wolfsbane, misión de clase** (Method y Mobalytics: "cadena enorme"; pasos en ForeverDB y azeroth.wiki, solo Undead):
1. *Diplomatic Incident*, nivel 22: Danitha Morr, Tirisfal (22.1, 44.7).
2. *A Curious Pair*: Trevan Rol, The Sepulcher (43.4, 41.0).
3. *A Grim Fate*.
4. *Into Fenris Keep* (65.0, 34.2).
5. *Lumina Windsinger* (65.6, 23.3).
6. *The Windshaper's Wrath*.
7. *The Debt* (24).
8. *A Moon-Kissed Blade* (25). Pide Whitestone Oak Lumber (la suelta el Goblin Woodcarver), Enchanted Silver Ingot y Purified Kor Gem. De dónde salen los dos últimos: `unknown`.
9. *The Moonsilver Blade*.
10. *Old Fire-Eye* (26): mata a Old Fire-Eye cerca de las puertas de Gilneas (sur de Silverpine). Recompensa: Wolfsbane.

Es una espada: necesitas **Espadas de dos manos**. Mobalytics avisa de que la Forsaken Greataxe aguanta bien hasta tenerla.

**Habilidades de arma:** casi todas las azules de mazmorra son **hachas** (y Sword of the Fallen y Wolfsbane, **espadas**). Aprende Hachas y Espadas de dos manos pronto, con un maestro de armas:
- Archibald, Undercity (57.1, 32.6).
- Hanashi o Sayoc, Orgrimmar (~81, 19).
- Ansekhwa, Thunder Bluff (41.2, 62.3).

Mobalytics dice que las hachas se aprenden en Orgrimmar. En Classic, una habilidad nueva empezaba en 1 y había que subirla pegando (`probable_classic`).

**Encantar el arma con el Mage:** solo armas **BoE sin equipar**: de vendedor, verdes o la Heavy Copper Maul antes de ponértela. **2H – Minor Impact: +4 de daño en Forever** (Strange Dust + Small Glimmering Shard). Las de misión y mazmorra son BoP: esas no puede encantarlas.

## 7. Armadura y stats
**Prioridad para subir** (Mobalytics): **dps del arma ≫ Stamina = Spirit = Strength = Agility > Hit/Crit > Spell Power > Attack Power**.
- **Spirit** rinde mucho: menos tiempo parado bebiendo.
- **Stamina** rinde mucho al principio: cada punto es mucha vida.
- **Agility** da crítico cuerpo a cuerpo, esquiva y armadura. Mejora con Vengeance.
- **Intellect**: maná y, con Champion of the Light (31+), poder con hechizos.

En el 60, la de Method: Hit (8 %) > Expertise (6,5 %) > SP > Str = AP > Int > Crit.

**Por ranura:**
- Mallas hasta el 40, placas desde el 40 (Method). Method dice que **del 1 al 35 no hay armadura "de Paladin"**: ponte cualquier pieza con los stats de arriba.
- **Gemmed Copper Boots** (azul, BoP, nivel 10, Str +4, Sta +4): Blacksmithing 35. Las fabricas tú.
- **Acolyte's Silvered Chain Helm** (azul, nivel 20, SP +7, curación +21, Sta +9): Blacksmithing 95. Method la prefiere a los cascos de tanque o daño.
- Armadura de mazmorra con Strength: ver la columna "Para ti" de §5.
- **El Mage** compra en la subasta pecho y brazales de malla **BoE** con Str o Sta, los encanta y te los manda:
  - Bracer – Minor Strength: Str +3.
  - Chest – Stamina.
  - Chest – Minor Stats: +2 a todo.

## 8. Profesiones, comida y campamento
| Profesión | Por qué | Hasta dónde |
|---|---|---|
| **Mining** | Mena para Blacksmithing y oro. Su objeto de campamento, **Lodestone**, da poder de ataque, pero no se suma a Blessing of Might: con él ponte Kings o Wisdom | Súbela mientras subes de nivel |
| **Blacksmithing** | **Rough Weightstone** (mazas) o **Rough Sharpening Stone** (hachas y espadas) desde skill 1; Gemmed Copper Boots (35), Heavy Copper Maul (65), Acolyte's Silvered Chain Helm (95). Su objeto de campamento, **Sharpening Wheel**, da Strength | **Hasta ~95.** Luego se encarece mucho (Mobalytics): aparcar hasta el 60, donde vuelve con equipo nuevo y Tier |
| **Cooking** | **Casi toda su comida da +5 % de XP** al matar con Well Fed, y el bonus **no depende del nivel de la comida** (Mobalytics). También fabrica el Basic Campfire Kit | Lo justo para comida fácil con carne de bestias |
| **First Aid** | Vendas sin maná; en Forever también hace pociones de vida (con hierbas) | Con la tela que te sobre |

**Más XP:** Cozy Sleeping Bag (+3 %), Beer Basted Boar Ribs (+5 % de XP al matar) y Camp Tent de Leatherworking (+5 % de descanso por hora). Lo de las Ribs y el saco es de Method; la tienda, de Mobalytics.

Mobalytics recomienda no subir profesiones de artesanía en serio hasta el 60: con montura y oro va más rápido.

## 9. Lo que te da el Mage
- **Bolsas**: Woolen Bag (8 casillas: 3 Bolt of Woolen + 1 Fine Thread). Mándale 2–4.
- **Oro** para entrenamientos, armas y habilidades de arma, por correo.
- **Encantamientos**: dos personajes de la misma cuenta no pueden estar conectados a la vez, así que solo puede encantar objetos **BoE** en su mochila y mandarlos (`probable_classic`).

| Encantamiento | Skill | Efecto en Forever | Materiales |
|---|---|---|---|
| **2H Weapon – Minor Impact** | 100 | **+4 de daño** | Strange Dust + Small Glimmering Shard |
| 2H Weapon – Lesser Impact | 145 | +5 de daño | Soul Dust + Large Glimmering Shard |
| Bracer – Minor Strength | 80 | Str +3 | 3 Strange Dust |
| Bracer – Lesser Strength | 140 | Str +4 | Soul Dust |
| Chest – Stamina | 120 | Stamina | 2 Strange Dust + Lesser Astral Essence |
| Chest – Minor Stats | 150 | +2 a todo | Lesser Astral Essence, Soul Dust, Large Glimmering Shard |

## 10. Ruta 1–40
| Nivel | Zona | Hitos |
|---|---|---|
| 1–10 | Tirisfal (Deathknell → Brill) | §1 |
| 10–16 | **Silverpine** (The Sepulcher) | *Arugal's Folly* (Dalar Dawnweaver 44.2, 39.9): Logsplitter (10,8 dps; la última parte es de grupo) |
| 13–18 | Ragefire Chasm (opcional) | Axe of Orgrimmar |
| 15–22 | **Ruins of Lordaeron** | §5: la mejor de tu tramo |
| 20–30 | **Hillsbrad** (Tarren Mill) | 21 misiones Horde de 24–33, ninguna de grupo, 5 nuevas de Forever |
| 22–26 | Silverpine y Tirisfal | **Cadena de Wolfsbane** (§6) |
| 22–27 | Shadowfang Keep | Arced War Axe |
| 24–28 | Ashenvale / Stonetalon / Barrens | *Weapons of Choice*: Demolition Hammer. BFD. Ver [[Mage-Route-23-30]] |
| 27–30 | **Thousand Needles** (Freewind Post) | 19 misiones, ninguna de grupo |
| 29–33 | Razorfen Kraul y Excavation Site | Corpsemaker, Heavehammer |
| 30–38 | Scarlet Monastery | Graveyard (11.150 XP), Armory (Ravager) |
| 36+ | **Riverglades** (zona nueva de Forever) | Ver [[Forever-New-Zones]]. Shen'dralas desde el 38 |
| 40 | Cualquier entrenador | Montura de clase, placas, dual spec (50 g) |

## 11. Errores comunes
- No mirar el dps del arma. Es lo que más te hace subir rápido.
- Seguir la build de endgame mientras subes.
- Usar arma de una mano + escudo para subir.
- Consecration contra un solo enemigo.
- Matar en bucle dentro de una mazmorra: la XP buena está en las **misiones**.
- No aprender Hachas y Espadas de dos manos: casi todas las azules lo son.
- Lanzar Freedom o Protection y olvidarte de volver a ponerte Might o Kings.
- Subir Blacksmithing más allá de ~95 mientras subes de nivel.

## Fuentes
| Fuente | Tipo | Fecha | Consultada |
|---|---|---|---|
| https://mobalytics.gg/wow-forever/classes/retribution-paladin-guide (Jampanos) | Guía de leveling y Ret | 2026-11-15 | 2026-11-24 |
| https://www.method.gg/wow-forever/wow-forever-paladin-leveling-guide-and-talents (Jurdi) | Guía de leveling | 2026-11-14 | 2026-11-24 |
| https://www.method.gg/wow-forever/class-guides/retribution-paladin (rotación, stats, macros) | Guía de endgame | 2026-11-09 (1.60.1) | 2026-11-24 |
| Addon ForeverDB | Misiones, recompensas, botín observado, vendedores, recetas | 2026-11-13 | 2026-11-24 |
| azeroth.wiki (cliente Forever) | Objetos, talentos, misiones de Wolfsbane, encantamientos | — | 2026-11-24 |

## Preguntas pendientes
- De dónde salen la Enchanted Silver Ingot y la Purified Kor Gem para Horde (cadena de Wolfsbane).
- Qué arma enseña cada maestro de armas en Forever, y si las habilidades de arma suben como en Classic.
- Si la macro del botón principal lanza Judgement y Holy Strike en una sola pulsación.
- Si un BoE encantado por el Mage llega sin ligarse.
- Coste de la montura de clase del 40.
- La pestaña de rotación de Mobalytics no se pudo leer (se carga dinámicamente): la rotación de esta guía es la de Method más los datos de hechizos de Mobalytics.
