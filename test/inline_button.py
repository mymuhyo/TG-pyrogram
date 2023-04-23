from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

api_id = '26163245'
api_hash = '8928271745e15652485f24c961c145c6'
bot_token = '6165024744:AAG6Gljx2VgZlQvMnn3KKByMK_lm476wktM'
# Create a Pyrogram client instance
app = Client(
    "morse_coderbot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

# Define a command handler function that sends a message with a button
@app.on_message(filters.command("start"))
def start_command_handler(client, message):
    # Create a message with a button
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("Delete❌", callback_data="pressed")]])
    message_text = "Hello, press the button below to send a message"
    message.reply_text(message_text, reply_markup=keyboard)

# Define a button click handler that sends a message
@app.on_callback_query()
def button_click_handler(client, query):
    if query.data == "pressed":
        message = query.message.id
        chat_id = query.message.chat.id
        app.delete_messages(chat_id=chat_id, message_ids=message)
        app.send_message(chat_id,'✅')

# Start the client
app.run()