import os
from os import getenv
from dotenv import load_dotenv
if os.path.exists("local.env"):
    load_dotenv("local.env")
load_dotenv()
admins = {}

#:::::::::::::@OFFICIALHACKERERA

API_ID = int(getenv("API_ID", "15756780"))
API_HASH = getenv("API_HASH", "83ec148262010024e30ef9cbf34333c8")
BOT_TOKEN = getenv("BOT_TOKEN", "5527973315:AAFfJVu1uT5--oPjQOmf56lDfq_siDWzBM8")
DEEPAK_SESSION = getenv("DEEPAK_SESSION", "BQB1dQFAUI0Mqb9J_RuD_wGmXqvJRx_maFK8LQ8ug3YoZ7WXv-dZf3pimxInaJtHUHW0Ek1pGWP84c7hOllZukBesejU4UkZg-DrSADA5mOY_-uN6TXsbOVjh02NOM3xzzfbOA63c9W3Jhk3TCiWMbAgikNoAtw7kQsAZkVyo1s2gyiCN9rbGkLjeDnKHZEWuq4GecH6LBP8zp4GXTstdoC9gIEJLUIyD-BPLKxCIC0t7BKDtR-6-Tf7m5qzDf3X8LU21cfenAp5aVJQ-OivWufP6A2oRMizRWXy5uBacXF5X_709gs_wpNP0VoCYPvAI5uUOkzOMly7BHo-zx6gUJypAAAAAT7h5bAA")
OWNER_ID = getenv("OWNER_ID", "2035388821")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001767639800"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2035388821").split()))
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://Garw:garw@cluster0.tmib6.mongodb.net/cluster0?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "OFFICIALHACKERERA")
BOT_NAME = getenv("BOT_NAME", "Ultra X Music")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ULTRA_X_ASSISTANT")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "HEPPYLIFI")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "OFFICIALHACKER789")
OWNER_USERNAME = getenv("OWNER_USERNAME", "OFFICIALHACKERERA")
ALIVE_NAME = getenv("ALIVE_NAME", "OFFICIALHACKERERA")
BOT_USERNAME = getenv("BOT_USERNAME", "ULTRA_X_MUSICBOT")






UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ANIL-XD/A-X-MUSIC-BOT")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "master")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "5000"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/9fdec96f8f340b8946845.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/26bdcfef66aeec799295d.jpg")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
EMOJI = getenv("EMOJI", "🥀")
