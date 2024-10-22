import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "7425999899:AAGuAV6Oh7w_QsHuItN8PkxXDgqBWTFbfAk")

API_ID = int(os.environ.get("API_ID", "18946488"))

API_HASH = os.environ.get("API_HASH", "c163d4e28e63196c3806cf3b9b2885de")

STRING = os.environ.get("STRING", "")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
