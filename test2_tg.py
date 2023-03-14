from pyrogram import Client, filters

app = Client("muhyohelp")


@app.on_message(filters.regex(r"(?i)\bhello\b"))
def hello_handler(client, message):
    # Respond to the message with a custom message
    message.reply_text("Hello, world!")


app.run()