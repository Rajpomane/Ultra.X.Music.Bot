

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
DEEPAK_SESSION = getenv("DEEPAK_SESSION", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "Umk")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "OFFICIALHACKERERA")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Timesisnotwaiting")
ALIVE_NAME = getenv("ALIVE_NAME", "OFFICIALHACKERERA")
BOT_USERNAME = getenv("BOT_USERNAME", "ULTRA_X_MUSIC_BOT")
OWNER_ID = getenv("OWNER_ID", "2091769666")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ULTRA_X_ASSISTANT")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "@OFFICIALHACKERERA")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "@OFFICIALHACKERERA")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2091769666").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/9fdec96f8f340b8946845.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/9fdec96f8f340b8946845.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/OFFICIALHACKERERA/ULTRA-X-MUSIC-BOT")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/12aa46a2c6da5ec20f8ac.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/5754a1c5b7f00258f3f7c.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/96b18c5757812de3b3b25.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/12aa46a2c6da5ec20f8ac.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/daf4f760b650632050353.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/12aa46a2c6da5ec20f8ac.jpg")
