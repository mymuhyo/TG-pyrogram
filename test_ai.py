import openai
import azure.cognitiveservices.speech as speechsdk
from pyrogram import Client, filters
from pyrogram import Client, filters
from deep_translator import GoogleTranslator

AZURE_SPEECH_API_KEY = '13cb46f2b6314441a9812d9e2fefee7d'
AZURE_SPEECH_REGION = 'eastus'

# set up OpenAI API key
openai.api_key = "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"

# create Pyrogram client
app = Client("muhyotemp1")

# define command handler
@app.on_message(filters.command("ai"))
async def ai_handler(client, message):
    # get user input
    user_input = message.text[len("/ai"):].strip()

    translator = GoogleTranslator(source='uz', target='en')
    translated = translator.translate(user_input)
    # generate AI text with OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        temperature=0.7,
    )

    res_response = response.choices[0].text

    translator = GoogleTranslator(source='en', target='uz')
    translated = translator.translate(res_response)

    speech_config = speechsdk.SpeechConfig(subscription=AZURE_SPEECH_API_KEY, region=AZURE_SPEECH_REGION)
    speech_config.speech_synthesis_voice_name = "uz-UZ-MadinaNeural"
    audio_config = speechsdk.audio.AudioOutputConfig(filename="output.wav")
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    result = synthesizer.speak_text_async(translated).get()

    # Send the audio to the user
    await app.send_audio(message.chat.id , "output.wav", caption=f"{translated}" )

# start Pyrogram client
app.run()
