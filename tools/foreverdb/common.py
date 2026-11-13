"""Constantes compartidas del adaptador de la API de ForeverDB.

Hechos de la API leidos en https://foreverdb.net/developers el 2026-11-13.
"""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "data" / "foreverdb"
CACHE_DIR = DATA_DIR / "cache"
USAGE_PATH = DATA_DIR / "usage.json"
ENV_FILE = REPO_ROOT / ".env"
ENV_VAR = "FOREVERDB_API_KEY"

BASE_URL = "https://foreverdb.net/api/v1"
SITE_URL = "https://foreverdb.net"
# Cloudflare responde 403 (error 1010) al User-Agent por defecto de urllib.
USER_AGENT = "wow-companion/0.1 (personal Obsidian companion)"

# Limites del plan gratuito: 30/min y 5000/dia por cuenta. Nos quedamos por debajo.
MAX_PER_MINUTE = 25
MAX_PER_DAY = 4500
DEFAULT_TTL_DAYS = 7
MAX_LIMIT = 100
DEFAULT_LIMIT = 25
# Si el servidor pide esperar mas que esto, no bloqueamos: avisamos y paramos.
MAX_RETRY_WAIT_S = 120.0

# Atribucion obligatoria de los terminos de la API.
CREDIT_LINE = "Data from ForeverDB.net (https://foreverdb.net)"
CREDIT_MD = "[Data from ForeverDB.net](https://foreverdb.net)"

GATHERING_SLUGS = ("herbalism", "mining", "skinning", "fishing")
