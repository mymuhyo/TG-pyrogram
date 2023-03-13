from pyrogram import Client

app = Client("my_account")


async def main():
    async with app:
        await app.send_message("me", "Abdulbosit test")


app.run(main())