## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
BOT_NAME = getenv("BOT_NAME", "Umk")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "OFFICIALHACKERERA")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Timesisnotwaiting")
ALIVE_NAME = getenv("ALIVE_NAME", "OFFICIALHACKERERA")
BOT_USERNAME = getenv("BOT_USERNAME", "ULTRA_X_MUSIC_BOT")
OWNER_ID = getenv("OWNER_ID", "1669178360")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ULTRA_X_ASSISTANT")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "@OFFICIALHACKERERA")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "@OFFICIALHACKERERA")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/12aa46a2c6da5ec20f8ac.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/12aa46a2c6da5ec20f8ac.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/12aa46a2c6da5ec20f8ac.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/12aa46a2c6da5ec20f8ac.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/12aa46a2c6da5ec20f8ac.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/12aa46a2c6da5ec20f8ac.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/12aa46a2c6da5ec20f8ac.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/12aa46a2c6da5ec20f8ac.jpg")
