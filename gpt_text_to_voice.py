import openai
import azure.cognitiveservices.speech as speechsdk
from pyrogram import Client, filters
from deep_translator import GoogleTranslator

# set up Azure API key
AZURE_SPEECH_API_KEY = '13cb46f2b6314441a9812d9e2fefee7d'
AZURE_SPEECH_REGION = 'eastus'

# set up OpenAI API key
openai.api_key = "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"

# create Pyrogram client
app = Client("muhyotemp1")

# define command handler
@app.on_message(filters.command("chat", prefixes=""))
async def ai_handler(client, message):
    # get user input
    user_input = message.text[len("chat"):].strip()
    translated_en = GoogleTranslator(source='auto', target='en').translate(text=user_input)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=translated_en,
        temperature=0.2,
        max_tokens=3000,
    )

    res_response = response.choices[0].text

    speech_config = speechsdk.SpeechConfig(subscription=AZURE_SPEECH_API_KEY, region=AZURE_SPEECH_REGION)
    translated = GoogleTranslator(source='en', target='uz').translate(text=res_response)

    # Uzbek voice
    speech_config.speech_synthesis_voice_name = "uz-UZ-MadinaNeural"
    # English voice
    # speech_config.speech_synthesis_voice_name = "en-US-AriaNeural"
    audio_config = speechsdk.audio.AudioOutputConfig(filename="output.wav")
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    result = synthesizer.speak_text_async(translated).get()

    # Send the audio to the user
    await app.send_audio(message.chat.id , "output.wav", caption=f"{translated}" )

    # await message.reply(res_response, quote=True)

print("Tekshiring")
# start Pyrogram client
app.run()