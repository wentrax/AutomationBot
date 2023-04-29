import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):    
    TG_BOT_TOKEN = "6093418154:AAGs0LQa19RBe9r1pkDizg7Q_OaoCSj4FfQ"   
    APP_ID = int("16448144")    
    API_HASH = "1073665850700150caf0e0cbb68216a2"    
    AUTH_USERS = [5163706369, 1533128706, 1985266909]  
    ADMIN_ID = "1533128706"
    TG_USER_SESSION_NAME = "lx_0980" 
    TG_USER_SESSION_STRING = "AgBwOG_r3FR-cHz0BlOydD-gd9IpambFKyXfCWOXL3pchjadjSMG35n5OfCG-nnnyFfk-LwWbTzlxenp0CS3THYgYKZUFWzVExdq4PWH3gIIsE1i0vJoY1qM2fQvZ6tliAVE2SAvqNJk2KE5J4UqB_lCG_VWh06BGSlGO8a1jX3EF_78aHXRux2A9qQQfpLNi9Ua_2tzPp8on42t_f64WuYCHVHqTp5te2h9XKxqXn9-hVTQz7YFkDJPCf4ymaEPOsV1JAhbQVMFzht34SfxFgh5ZYw2b5C242rq4VNBePMvwGWo7Y86AVtPfkQ4oiQsCfxvFpBx_HchjOL-BsxubBxrAAAAATPH6AEA"   
    FILTER_CHANNEL_ID = -1001922400671  
    FILES_FROM_CHANNEL = -1001739094949
    FILES_TO_CHANNEL = -1001506021749
            
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
