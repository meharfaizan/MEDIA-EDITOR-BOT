import os

class Config(object):
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5442493323:AAGE585VqW2Rjn8p7fTamBdyiSsg9dktdgE")

    APP_ID = int(os.environ.get("APP_ID", "6534707"))

    API_HASH = os.environ.get("API_HASH", "4bcc61d959a9f403b2f20149cbbe627a")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1430593323").split())
  
    
