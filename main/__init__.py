#ChauhanMahesh/Vasusen/DroneBots/COL

from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 16246834
API_HASH = "29b3ffa9245c07f05375b92f38e8f13d"
BOT_TOKEN = "5716827359:AAE3NJPyZkXHATL8m3AmLVxFy0-NNhKOOog"
FORCESUB = -1001528080636
ACCESS = int("-1001743550303")
MONGODB_URI = "mongodb+srv://Copet0:Malik10_@cluster0.0grdtud.mongodb.net/?retryWrites=true&w=majority"
AUTH_USERS = 1715348447

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
