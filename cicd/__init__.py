from pyrogram import Client
from cicd.config import Config


app = Client('my_bot',api_id=Config.API_ID,api_hash=Config.API_HASH,bot_token=Config.BOT_TOKEN)
