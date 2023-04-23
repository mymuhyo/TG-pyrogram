import time
import asyncio
from pyrogram import Client, filters
from pyrogram.handlers import UserStatusHandler

app = Client("muhyotemp1")

user_id = '1896596326'

start_time = 0

async def check_user_online(user_id):

    while True:
        if app.is_connected:
            user_data = await app.get_users(user_id)
            global start_time
            global online_minutes

            last_online_data = user_data.last_online_date

            if last_online_data == None :
                start_time = time.time()
                print("Online")

            if last_online_data != None and start_time != 0:
                end_time = time.time()
                online_minutes = int((end_time - start_time) / 60)
                print(f'The user was online for {online_minutes} minutes')
                start_time = 0

        await asyncio.sleep(10)


@app.on_message(filters.command("last", prefixes="/"))
async def send_me(Client , messange):
    id = messange.from_user.id
    await app.send_message('muhyo07' , f"The user was online for {online_minutes} minutes" )


print("Tekshiring")
app.start()
app.run(check_user_online(1896596326))