import os

class Config(object):
    API_ID = os.environ.get("API_ID",'')
    API_HASH = os.environ.get("API_HASH",'')
    BOT_TOKEN = os.environ.get('BOT_TOKEN','')
    BOT_USERNAME = os.environ.get('','')