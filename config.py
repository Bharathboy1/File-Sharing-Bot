#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6302453400:AAGHvg2IqqUCz0PYfLXPkqc0R9o0FB08nlM")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "4234473"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "6d9e82c9edc244b0c0a20d8fa89f9784")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001215329736"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "634637418"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb://rename:rename@ac-x0xofim-shard-00-00.wzkakkz.mongodb.net:27017,ac-x0xofim-shard-00-01.wzkakkz.mongodb.net:27017,ac-x0xofim-shard-00-02.wzkakkz.mongodb.net:27017/?ssl=true&replicaSet=atlas-ar97qb-shard-0&authSource=admin&retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "bharath")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001914868571"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI AM STORAGE BOT FOR @FILMZTUBE I CAN ONLY STORE FILES AND GIVE YOU DON'T MESSAGE HERE.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>{filename}\n\n🎬ᴊᴏɪɴ ɴᴏᴡ: <a href='https://t.me/filmztube'>ғɪʟᴍᴢᴛᴜʙᴇ</a></b>"
)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>❌Don't send me messages directly I'm only File Share bot!\n\n🎬ᴊᴏɪɴ ɴᴏᴡ: <a href='https://t.me/filmztube'>ғɪʟᴍᴢᴛᴜʙᴇ</a></b>"

ADMINS.append(OWNER_ID)
ADMINS.append(1447209433)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
