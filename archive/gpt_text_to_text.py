import openai
import azure.cognitiveservices.speech as speechsdk
from pyrogram import Client, filters

# set up OpenAI API key
openai.api_key = "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"

# create Pyrogram client
app = Client("muhyotemp1")

# define command handler
@app.on_message(filters.command("ai"))
async def ai_handler(client, message):
    # get user input
    user_input = message.text[len("/ai"):].strip()
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        temperature=0.2,
        max_tokens=3000,
    )

    res_response = response.choices[0].text
    # Send the audio to the user
    await message.reply(res_response, quote=True)

print("Tekshiring")
# start Pyrogram client
app.run()
