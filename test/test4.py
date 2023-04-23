import os
import requests
import json
import azure.cognitiveservices.speech as speechsdk
from pyrogram import Client, filters

AZURE_SPEECH_API_KEY = '13cb46f2b6314441a9812d9e2fefee7d'
AZURE_SPEECH_REGION = 'eastus'

app = Client("muhyotemp1")

# Keep track of the number of audio files received so far
num_audio_files = 0


@app.on_message(filters.voice)
async def speech_to_text(client, message):
    global num_audio_files
    voice = message.voice
    file_path = await client.download_media(voice)

    # Convert the voice file to text using Azure Speech Services
    headers = {'Ocp-Apim-Subscription-Key': AZURE_SPEECH_API_KEY}
    url = f'https://{AZURE_SPEECH_REGION}.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language=uz-UZ'
    params = {'format': 'conversation'}
    with open(file_path, 'rb') as f:
        data = f.read()
    response = requests.post(url=url, params=params, headers=headers, data=data)
    if response.status_code == 200:
        result_json = json.loads(response.text)
        if result_json['RecognitionStatus'] == 'Success':
            result = result_json['DisplayText']
        elif result_json['RecognitionStatus'] == 'EndOfDictation':
            result = "Hech nima yo'q"
        else:
            result = f"Error: {result_json['RecognitionStatus']}"
    else:
        result = 'Error: failed to convert voice to text'

    # Send the text to the user
    await message.reply(result, quote = True)

    # Delete the earliest audio files if there are more than 3
    num_audio_files += 3
    if num_audio_files > 3:
        oldest_file = f"voice{num_audio_files - 3}.oga"
        os.remove(oldest_file)

    # Save the audio file
    filename = f"voice{num_audio_files}.oga"
    os.rename(file_path, filename)


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
