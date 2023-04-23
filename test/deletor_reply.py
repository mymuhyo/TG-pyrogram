from pyrogram import Client, filters

app = Client("muhyotemp1")

@app.on_message(filters.reply & filters.user(app.get_me().id) & filters.command("/delete"))
def ai_handler(client, message):
    app.delete_messages(chat_id=message.reply.chat.id , message_ids=message.reply.message_id)
    app.delete_messages(
        chat_id=message.chat.id,
        message_ids=message.message_id
    )

app.start()
app.run()
