from pyrogram import Client, filters

app = Client("muhyohelp")

@app.on_message(filters.command("help", prefixes="/"))
async def help_command(client, message):
    # Get the text after /help
    user_input = message.text[len("/help"):].strip()

    # If there is something after /help, reply with "Hello"
    if user_input:
        await client.send_message(message.chat.id, user_input)
    # If there is nothing after /help, send a generic help message
    else:
        await client.send_message(message.chat.id, "Example : /help test")
print("Tekshiring")
app.run()
