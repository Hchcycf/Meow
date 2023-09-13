import os
import asyncio
import sys
import time

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

__version__ = "v0.1"

if os.path.exists(".env"):
    load_dotenv(".env")
    

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "11822563"))
API_HASH = os.getenv("API_HASH", "12bfd8057541544a482312319d7fe4ae")
SESSION = os.getenv("SESSION", "BAB3G-aJDgUBS69mGHlLqd2xCxeYM_iLl80eE_JhfKsPF2wzKKqVYK62_G-w4sMT5KGrzDQ4UP0FDNIXcZ2kWpoZaYU94zKYpnFrr-GBktCC2UUWspzLOO23X4zjW9XerJRVrwInNWNH1X61uDWxA7gtK6qgRjLCyc4qOGvWuUFwdP2g_Tx-Jcdkv1xdzaxQwSacO8OXZ3qUoSAH1kX0M7ToxW-v_6b3Y763kewfIuOlNgBbfYltvyXMaWKVdm9wIsv1hMbvB0hrLuRTQUn83iOzcFNEd0Mb5YQjZ4NJTeQjqbnpf6C0ALKI_R-eVnWaLmDXMxaGPCGmvDsvfl9I495vAAAAAUr8w8oA")
HNDLR = os.getenv("HNDLR", ".")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "5553046474").split()))
ALIVE_PIC = os.getenv("ALIVE_PIC", "https://telegra.ph/file/5c8fda9e1fbc5cbb7b881.jpg")
ALIVE_MSG = os.getenv("ALIVE_MSG", "https://telegra.ph/file/5c8fda9e1fbc5cbb7b881.jpg")
PING_MSG = os.getenv("PING_MSG", "https://telegra.ph/file/5c8fda9e1fbc5cbb7b881.jpg")
LOGS_CHANNEL = os.getenv("LOGS_CHANNEL", None)

contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)
# SUDO_USERS = list(filter(lambda x: x, map(int, os.getenv("SUDO_USERS", "1517994352 1789859817").split())))
#----------------------------------------------
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="Modules"))
call_py = PyTgCalls(bot)

# Terms
# Privacy
# Security

hl = HNDLR[0]
start_time = time.time()

