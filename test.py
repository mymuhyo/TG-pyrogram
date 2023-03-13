from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from lists_teletips.quotes_teletips import *
from lists_teletips.emojis_teletips import *
from PIL import Image, ImageDraw, ImageFont
import datetime
import pytz
import asyncio
import random

app = Client("my_account")

Time_Zone = "Asia/Ashgabat"

async def main_teletips():
    try:
        while True:
            if app.is_connected:
                Quotes_teletips = random.choice(quotes_teletips)
                Emojis_teletips = random.choice(emojis_teletips)
                TimeZone_teletips = datetime.datetime.now(pytz.timezone(f"{Time_Zone}"))
                Time_teletips = TimeZone_teletips.strftime("%I:%M %p")
                Date_teletips = TimeZone_teletips.strftime("%b %d")
                Image_teletips = Image.open("image.jpg")
                Image_font_teletips = ImageFont.truetype("ds-digit.ttf", 360)
                Image_text_teletips = f"{Quotes_teletips}"
                Image_edit_teletips = ImageDraw.Draw(Image_teletips)
                Image_edit_teletips.text((690, 550), Image_text_teletips, (0, 255, 255), font = Image_font_teletips)
                Image_teletips.save("Image_final_teletips.jpg")
                await app.update_profile(bio = f"{Emojis_teletips} {Quotes_teletips}" , last_name = f"| ⏰ {Time_teletips} | 📅 {Date_teletips}")
                await app.set_profile_photo(photo="Image_final_teletips.jpg")
                me = await app.get_me()
                photos = app.get_chat_photos("me")
                try:
                    await app.delete_profile_photos(photos[1].file_id)
                except Exception:
                    pass
                print(f"Profile Yangilandi {Time_teletips}")
            await asyncio.sleep(60)
    except FloodWait as e:
        await asyncio.sleep(e.x)

print("Ishaga tushdi")
asyncio.ensure_future(main_teletips())
app.run()