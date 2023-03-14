from pyrogram import Client, filters
import asyncio

api_id = '26163245'
api_hash = '8928271745e15652485f24c961c145c6'
app = Client(name="muhyohelp", api_id=api_id, api_hash=api_hash)



@app.on_message(filters.command(["boshla"]))
async def handle_commands(client, messange):
  username = messange.from_user.username

  await app.send_message(f"{username}", f"{messange.date}")



print("Teshiring")
app.run()

loop = asyncio.get_event_loop()