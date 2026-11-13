# WoW Companion — WoW Forever

A personal, non-commercial companion for **World of Warcraft: Forever**: an Obsidian knowledge base plus small Python tools, queried with an AI assistant (Claude Code) while playing.

- `00-Dashboard/` — home page and level-bracket playbooks
- `02-Classes/` … `10-Tips/` — curated knowledge notes (classes, professions, economy, world, items, systems, tips), each with sources and a verification status that separates confirmed Forever behavior from Classic assumptions
- `07-Research/` — source registry, one digest per guide page, conflicts between sources
- `tools/` — data adapters (client data from wago.tools; ForeverDB API planned)
- `_System/` — vault rules, templates, Obsidian Bases tables and the index builder

Open the folder as an Obsidian vault and start at `00-Dashboard/HOME.md`.

## Data sources & credits

This project summarizes and links to the following sources. Data and guides remain the property of their owners; notes cite the exact page they come from.

- <a href="https://foreverdb.net">Data from ForeverDB.net</a> — WoW Forever item, quest, vendor, profession and gathering data (API, read-only, personal key). Every note that uses ForeverDB data links back to it.
- [wago.tools](https://wago.tools) — WoW Forever client data tables (DB2 CSV exports), used locally and not redistributed.
- [Azeroth DB](https://azeroth.wiki) — WoW Forever records via its official MCP server.
- [Method.gg](https://www.method.gg/wow-forever), [The Forever Era](https://theforeverera.com), [Eternadex](https://eternadex.com), [Warcraft Tavern](https://www.warcrafttavern.com), [Kami-Labs](https://kami-labs.fr) and other guide sites listed in `07-Research/Source-Registry.md` — guides summarized in our own words with links.
- [Blizzard Entertainment](https://worldofwarcraft.blizzard.com) — official patch notes, hotfixes and developer posts.

World of Warcraft and WoW Forever are trademarks of Blizzard Entertainment. This project is not affiliated with or endorsed by Blizzard Entertainment or any of the sites above.

## Rules

- Only data access that each source permits (official APIs, published exports, permitted pages). No scraping of sites that disallow it, no bypassing of rate limits or bot protection.
- Character data comes only from in-game addon exports (no memory reading, no client automation).
