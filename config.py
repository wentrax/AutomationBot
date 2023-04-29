import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):    
    TG_BOT_TOKEN = "6032335088:AAHqrUvqR-0rulRNNiesZ-B02iwcSHYSTy8"   
    APP_ID = int("16448144")    
    API_HASH = "1073665850700150caf0e0cbb68216a2"    
    AUTH_USERS = [5163706369, 1533128706, 1985266909]  
    ADMIN_ID = "1533128706"
    TG_USER_SESSION_NAME = "lx_0980" 
    TG_USER_SESSION_STRING = "AgBQ3FyXGJL1zGqSUaDeISPE1g500k2Tl-0l1M1p9wqEG9_f96Ddzgo-nkt3fEyErFUfW9BZdGkKd1keimlA4VfRQfNsTlWU4LborGdeQd6lpkpY-OIG9Ws-0udU5lnFsXCnNa0WshIIgtL78-Bie1BtChJg4XS8vWWHMY9rneoDvxfJm51r2Fqi-axbNpRMPI5RPvcK37KrxbNDSdrrYoanO7sZgI8byf8lKe628LG-ygZpNhm0ILjF98tQ6VMNnBvljxDA8F3K75l4P_VtwnBIFjNSczjM0mlJ7EV9Ka-dsHN4sNRvijJQEqkGOyixvBMWh-iVsTTqW5dmNEyMRz9WAAAAATPH6AEA"
    FILTER_CHANNEL_ID = -1001922400671  
    FILES_FROM_CHANNEL = -1001739094949
    FILES_TO_CHANNEL = -1001506021749
            
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
