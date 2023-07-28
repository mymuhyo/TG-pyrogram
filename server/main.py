from pyrogram import Client
from source.lists import quotes , emojis
import datetime
import pytz
import asyncio
import random
api_id = 26163245
api_hash = "8928271745e15652485f24c961c145c6"

app = Client(
    "muhyotemp",
    api_id=api_id, api_hash=api_hash
)

async def time_bio_changer():
        while True:
            if app.is_connected:

                Quotes_choiced = random.choice(quotes)
                Emojis_choiced = random.choice(emojis)

                time_zone = "Asia/Ashgabat"
                full_time = datetime.datetime.now(pytz.timezone(f"{time_zone}"))
                min_sec = full_time.strftime("%I:%M")
                # date_month = full_time.strftime("%b %d")
                # Update profile
                await app.update_profile(bio = f"{Emojis_choiced} {Quotes_choiced}" , last_name = f"| ⏰ {min_sec}")
            await asyncio.sleep(30)

asyncio.ensure_future(time_bio_changer())

print("Tekshiring")
app.run()