from pyrogram import Client, filters
from source.lists import morse_dict
api_id = '26163245'
api_hash = '8928271745e15652485f24c961c145c6'
bot_token = '6165024744:AAG6Gljx2VgZlQvMnn3KKByMK_lm476wktM'
# Create a Pyrogram client instance
app = Client(
    "morse_coderbot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)


# Define a dictionary containing English letters for each Morse code symbol
reverse_morse_dict = {value: key for key, value in morse_dict.items()}


codeCommand = ['code', 'decode']
@app.on_message(filters.command(codeCommand))
def morse_converter(client, message):
    # Get the message text (without the command)
    FirstName = message.from_user.first_name
    text = message.text.split(maxsplit=1)[1]
    # Check which command was used
    if message.command[0] == 'code':
        # Convert English text to Morse code
        morse_text = ' '.join([morse_dict.get(c.upper(), '') for c in text])
        # Send the Morse code back to the user
        message.reply_text(f"Tabriklayman {FirstName}.\nShiftlandi \nJavob 👇👇👇:\n`{morse_text}`")
    elif message.command[0] == 'decode':
        # Convert Morse code to English text
        english_text = ''.join([reverse_morse_dict.get(symbol, '') for symbol in text.split()])
        # Send the English text back to the user
        message.reply_text(f"Tabriklayman {FirstName}.\nShifr ochildi \nJavob 👇👇👇:  \n`{english_text}`")


@app.on_message(filters.text)
def other(client, message):
    id = message.chat.id

    response_Other = f"Bu bot faqat shifrlash yoki shifrdan ochish uchun \nMisol uchun \nAgar siz gapingizni shifrlamoqchi bo'lsangiz `/code` ko'rishida yozing va bitta joy tashlab qaysi gapni shiftlamoqchi bo'lganingizni yozing Misol uchun :\n`/code shifrlanadigan soz` \n Shiftdan ochmoqchi bo'lsangiz `/decode` dan so'ng hohlagan gapingizni yozing Misol uchun\n`/decode ... .- .-.. --- --` \n\n Muommo chiqsa Iltimos @muhyo07 ga murojat qiling"

    message.reply_text(response_Other, quote=False)

print("Tekshiring")
# Start the client
app.run()
