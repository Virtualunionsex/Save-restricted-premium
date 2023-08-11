#ChauhanMahesh/Vasusen/DroneBots/COL

from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 26775038
API_HASH = "40dc918d6f9bdd391f2fbfb5bbd0328c"
BOT_TOKEN = "6382292112:AAHZDf9xgTUEpllpkclidKn_toO02hvYr58"
FORCESUB = -1001743550303
ACCESS = int("-1001743550303")
MONGODB_URI = "mongodb+srv://projeklisatiga:Malik10_@cluster0.tgthj.mongodb.net/?retryWrites=true&w=majority"
AUTH_USERS = 6452204836 

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
