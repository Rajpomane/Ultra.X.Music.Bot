import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
from config import API_HASH, API_ID, BOT_TOKEN, DEEPAK_SESSION
from pyrogram import Client
from pytgcalls import PyTgCalls

bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "Deepak.Player"},
)


user = Client(
    DEEPAK_SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
)


Test = Client(DEEPAK_SESSION, api_id=API_ID, api_hash=API_HASH, plugins={'root': 'Deepak.Player'})
call_py = PyTgCalls(
    Test,
    cache_duration=100,
    overload_quiet_mode=True,
)


Deepak = Client( 
    "Chatbot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN,
    plugins={"root": "Deepak"},
)





tgbot = TelegramClient('tgbot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
