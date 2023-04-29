import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):
    # Get a bot token from @botfather
    TG_BOT_TOKEN = "6093418154:AAGs0LQa19RBe9r1pkDizg7Q_OaoCSj4FfQ"

    # Get from my.telegram.org
    APP_ID = int("16448144")

    # Get from my.telegram.org
    API_HASH = "1073665850700150caf0e0cbb68216a2"

    # Authorized users to use this bot
    AUTH_USERS = [5163706369, 1533128706, 1985266909]

    # session name
    TG_USER_SESSION_NAME = "lx_0980")

    # tg user session string
    TG_USER_SESSION_STRING = ""

    # your channel id 
    FILTER_CHANNEL_ID = -1001922400671

    # file forward channel ID
    FILES_FROM_CHANNEL = -1001739094949
    FILES_TO_CHANNEL = -1001506021749
    
        
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
