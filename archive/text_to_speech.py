import azure.cognitiveservices.speech as speechsdk
from pyrogram import Client, filters

AZURE_SPEECH_API_KEY = '13cb46f2b6314441a9812d9e2fefee7d'
AZURE_SPEECH_REGION = 'eastus'

app = Client("muhyotemp1")

@app.on_message(filters.text)
async def text_to_speech(client, message):
    text = message.text
    speech_config = speechsdk.SpeechConfig(subscription=AZURE_SPEECH_API_KEY, region=AZURE_SPEECH_REGION)
    speech_config.speech_synthesis_voice_name = "uz-UZ-MadinaNeural"
    audio_config = speechsdk.audio.AudioOutputConfig(filename="output.wav")
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    result = synthesizer.speak_text_async(text).get()

    # Send the audio to the user
    await app.send_audio(message.chat.id , "output.wav", caption=f"{text}" )

print("Tekshiring")
app.run()