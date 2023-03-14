from pyrogram import Client, filters
from pyrogram.handlers import *
from pyrogram.raw import functions, types
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
    user_username = messange.from_user.username
    time = messange.date
    text = messange.text
    date_date = f"{time:%m.%d}"
    date_time = f"{time:%H:%M:%S}"

    kuchukcha = "@"

    if user_username == None:
        user_username = "Yo'q"
        kuchukcha = ""
    else :
        user_username = messange.from_user.username

    xabar = f" ID : ** `{id}` ** \nIsm : ** [{first_name}](tg://user?id={id}) ** \nUsername : ** {kuchukcha}{user_username}** \nSana : ** {date_date} ** \nVaqt: **{date_time}** \n Xabar : ** {text} **  "


    await messange.reply_text("Habaringiz @muhyo07 ga yuborildi Agar 3 soat ichida javob yozmasa Iltimos qaytattan yozing")
    await app.send_message('muhyo07', f'{xabar}' )



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

asyncio.ensure_future(time())

app.run()