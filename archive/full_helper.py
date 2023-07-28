from pyrogram import Client, filters
from pyrogram.handlers import *
from pyrogram.raw import functions, types
from source.lists import quotes, emojis
import datetime
import pytz
import asyncio
import random

api_id = '26163245'
api_hash = '8928271745e15652485f24c961c145c6'
Time_Zone = "Asia/Ashgabat"
app = Client("muhyohelp",api_id = api_id,api_hash = api_hash)

status_update = functions.account.UpdateStatus(offline=False)


async def send_me(Client , messange):
    id = messange.from_user.id
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

    if id != 1896596326  :
        xabar = f" ID : ** `{id}` ** \nIsm : ** [{first_name}](tg://user?id={id}) ** \nUsername : ** {kuchukcha}{user_username}** \nSana : ** {date_date} ** \nVaqt: **{date_time}** \nXabar : ** {text} **  "
        await messange.reply_text("Habaringiz @muhyo07 ga yuborildi Agar 3 soat ichida javob yozmasa Iltimos qaytattan yozing")
        await app.send_message('muhyohistory' , f'{xabar}' )
    else:
        await messange.reply_text("Ishlaypti")



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