import asyncio
import datetime
import os
import pytz
from pyrogram import Client, filters

app = Client("muhyotemp1")

user_id = 6000519043
entry_times = 0
is_online = True
current_day = datetime.datetime.now(pytz.timezone('Asia/Tashkent')).day
file_path = "entry_times.txt"

async def check_user_online(user_id):
    global entry_times
    global is_online
    global current_day

    while True:
        if app.is_connected:
            user_data = await app.get_users(user_id)
            last_online_data = user_data.last_online_date

            if last_online_data == None and is_online == True:
                is_online = False

            if last_online_data != None and is_online == False:
                is_online = True
                if datetime.datetime.now(pytz.timezone('Asia/Tashkent')).day != current_day:
                    current_day = datetime.datetime.now(pytz.timezone('Asia/Tashkent')).day
                    entry_times = 0
                entry_times += 1
                save_entry_times(entry_times)

        await asyncio.sleep(10)

def save_entry_times(entry_times):
    with open(file_path, "w") as f:
        f.write(str(entry_times + "marta"))

def load_entry_times():
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            entry_times = int(f.read())
        return entry_times
    else:
        return 0

@app.on_message(filters.command("et_lv", prefixes="/"))
async def send_me(client, message):
    global entry_times
    id = message.from_user.id
    await app.send_message(id, f"Bugun \"LV\" {entry_times} marotaba online bo'ldi")

@app.on_message(filters.command("et_me", prefixes="/"))
async def send_me(client, message):
    global entry_times
    id = message.from_user.id
    await app.send_message(id, f"Bugun \"LV\" {entry_times} marotaba online bo'ldi")

print("Tekshiring")
app.start()
app.run(check_user_online(user_id))