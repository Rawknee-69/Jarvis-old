import requests
from pydub import AudioSegment
from pydub.playback import play
import io
fileopen = open("wifu//api_use.txt","r")
api_use = fileopen.read()
fileopen.close()


fileopen = open("wifu//speechid.txt","r")
speechid = fileopen.read()
fileopen.close()

fileopen = open("wifu//response.txt","r")
res = fileopen.read()
fileopen.close()


def EL_TTS(message):

    url = f'https://api.elevenlabs.io/v1/text-to-speech/{speechid}'
    headers = {
        'accept': 'audio/mpeg',
        'xi-api-key': api_use,
        'Content-Type': 'application/json'
    }
    data = {
        'text': message,
        'voice_settings': {
            'stability': 0.75,
            'similarity_boost': 0.75
        }
    }

    response = requests.post(url, headers=headers, json=data, stream=True)
    audio_content = AudioSegment.from_file(io.BytesIO(response.content), format="mp3")
    play(audio_content)
EL_TTS("hello how are you")


    
 