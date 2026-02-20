from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID") or "0")
SUPPORT_NAME = os.getenv("SUPPORT_NAME", "Евгений Попов")
SUPPORT_PHONE = os.getenv("SUPPORT_PHONE", "+79284567123")
SUPPORT_EMAIL = os.getenv("SUPPORT_EMAIL", "mitrait@yandex.ru")
DOCSHELL_SITE = os.getenv("DOCSHELL_SITE", "https://t.me/DocShell_Sochi")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не указан в .env файле!")
if ADMIN_ID == 0:
    print("Внимание: ADMIN_ID не указан → заявки никуда не придут")