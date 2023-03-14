from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.handlers import message_handler
from lists_teletips.quotes_teletips import *
from lists_teletips.emojis_teletips import *
from PIL import Image, ImageDraw, ImageFont
import datetime
import pytz
import asyncio
import random
import os

Date_Time_Userbot_teletips=Client(
    name = "date_time_userbot_teletips",
    api_id = '26163245',
    api_hash = '8928271745e15652485f24c961c145c6',
    session_string = "AgGPOC0AGeXHhykoZds7ELqmdAy-tSiJgrP5i5vcVyZxmqfdrqkH1fUxIR16w_MXoR4Ux6gu-VKuK6CLFLTiW5bgI4GBAL8IvPfD08xYLwipLEkEe6B0DA1De_6OVx0Ed-U7g8FfyXbHdZ6s8Ov8meBmxFn2Kh7OeTKq8iZ5wuB81FQpcGZhE6bmO2bdJW49izGlHJHi4Al5vqwwEIuL1ohoPOJAHl9wmV0bUgHcvJXjsFpDdxmfQAVbx6PfsCOl6Y9inynfPpDfczI1iyu51ApmoKpVFDfdzTk5570r5pVagZFqqXOl86hPaGfhOX7xK9n4qtDsZIEV-nY23k61s6_qhrMUbAAAAAFLb8KLAA"
)

Time_Zone = "Asia/Ashgabat"
async def send_messange(Client , messange):
    send_messange("yoqub407" , messange)


async def main_teletips():
    try:
        while True:
            if Date_Time_Userbot_teletips.is_connected:
                Quotes_teletips = random.choice(quotes_teletips)
                Emojis_teletips = random.choice(emojis_teletips)
                TimeZone_teletips = datetime.datetime.now(pytz.timezone(f"{Time_Zone}"))
                Time_teletips = TimeZone_teletips.strftime("%I:%M %p")
                Date_teletips = TimeZone_teletips.strftime("%b %d")
                await Date_Time_Userbot_teletips.update_profile(bio = f"{Emojis_teletips} {Quotes_teletips}" , last_name = f"| ⏰ {Time_teletips} | 📅 {Date_teletips}")

                print("Profile Updated!")
            await asyncio.sleep(60)
    except FloodWait as e:
        await asyncio.sleep(e.x)

print("DATE TIME USERBOT IS ALIVE!")
asyncio.ensure_future(main_teletips())
Date_Time_Userbot_teletips.run()

#Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
