from pyrogram import Client, filters


api_id = '26163245'
api_hash = '8928271745e15652485f24c961c145c6'
bot_token = '6165024744:AAG6Gljx2VgZlQvMnn3KKByMK_lm476wktM'
app = Client(
    "morse_coderbot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)


user_ids = ['1896596326', '5782583352']


@app.on_message(filters.private)
async def forward_message(client, message):
        print(message)
        text = message.text
        if message.chat.id == int(user_ids[0]):
            await app.send_message(int(user_ids[1]) ,text)
        else:
            await app.send_message(int(user_ids[0]) ,text)

app.run()