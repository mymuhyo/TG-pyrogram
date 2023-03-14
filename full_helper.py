from pyrogram import Client, filters
from pyrogram.handlers import *
from lists_teletips.quotes import *
from lists_teletips.emojis import *
import datetime
import pytz
import asyncio
import random

api_id = '26163245'
api_hash = '8928271745e15652485f24c961c145c6'
Time_Zone = "Asia/Ashgabat"
app = Client("muhyohelp",api_id = api_id,api_hash = api_hash)

async def send_me(Client , messange):
    id = messange.chat.id
    first_name = messange.from_user.first_name
    username = messange.from_user.username
    time = messange.date
    text = messange.text

    xabar = f" ID : ** {id} ** \nIsm : ** {first_name} ** \nUsername : ** @{username}** \nVaqt : ** {time} ** \nXabar : ** {text} **  "

    await app.send_message('yoqub407' , f'{xabar}' )

async def time():
        while True:
            if app.is_connected:

                Quotes_teletips = random.choice(quotes)
                Emojis_teletips = random.choice(emojis)

                TimeZone_teletips = datetime.datetime.now(pytz.timezone(f"{Time_Zone}"))

                Time_teletips = TimeZone_teletips.strftime("%I:%M")
                Date_teletips = TimeZone_teletips.strftime("%b %d")

                await app.update_profile(bio = f"{Emojis_teletips} {Quotes_teletips}" , last_name = f"| ⏰ {Time_teletips}")
            await asyncio.sleep(30)



print("Ishga tushdi")

app.add_handler(MessageHandler(send_me))
asyncio.ensure_future(time())

app.run()