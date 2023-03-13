#ChauhanMahesh/Vasusen/DroneBots/COL

from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 9774346
API_HASH = "a92aed7d74654a563af4b07efbcd88e9"
BOT_TOKEN = "6278815762:AAF6Vkg0hki1ZxxOmAzWbeCsZRPyTXI0Kfc"
FORCESUB = 1809733770
ACCESS = int("-1001809733770")
MONGODB_URI = "mongodb+srv://RyanMusic:Rextor99@cluster0.pxtgxfl.mongodb.net/?retryWrites=true&w=majority"
AUTH_USERS = 907544310

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
