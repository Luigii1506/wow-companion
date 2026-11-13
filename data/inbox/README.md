# Cómo subir exports desde el PC Windows

**Antes del primer export:** confirma que el repositorio es privado.

## Primera vez

1. Instala Git y clona el repositorio.
2. En Battle.net abre WoW Forever y elige «Show in Explorer» para localizar la carpeta del juego.
3. Copia `_forever_/WTF` a un lugar fuera del juego como respaldo.
4. Instala [Dossier: Your Character, Ready for AI](https://www.curseforge.com/wow/addons/dossier-your-character-ready-for-ai) en `_forever_/Interface/AddOns`. Comprueba el autor: `coyos`.
5. Entra al juego y anota cualquier error de Lua.

## Después de cada sesión

1. Abre el banco y cada ventana de profesión una vez.
2. Escribe `/dossier`, usa Select All, activa el export detallado y pulsa **Create Export**.
3. Copia el texto y guárdalo en UTF-8 como `data/inbox/dossier/AAAA-MM-DD_HHMM.txt`, con tu hora local.
4. Sube el archivo:

```powershell
git pull
git add data/inbox
git commit -m "Export AAAA-MM-DD"
git push
```

## SavedVariables (solo cuando se pida)

1. Escribe `/reload` en el juego o cierra sesión correctamente.
2. Busca el archivo del addon en una de estas carpetas:
   - `_forever_/WTF/Account/<cuenta>/SavedVariables/`
   - `_forever_/WTF/Account/<cuenta>/<reino>/<personaje>/SavedVariables/`
3. Copia solo ese archivo como `data/inbox/savedvariables/AAAA-MM-DD_HHMM_<Addon>.lua`.

## Reglas

- Cada export es un archivo nuevo. No edites ni sobrescribas los anteriores.
- Nunca subas `Config.wtf`, la carpeta `WTF` completa, contraseñas ni datos de Battle.net.
- Revisa el texto antes de subirlo si tus notas o tu correo contienen algo privado.
