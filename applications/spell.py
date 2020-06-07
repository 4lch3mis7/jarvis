from gtts import gTTS
from playsound import playsound
import os


def spell(text):
    audio = gTTS(text=text, lang='en')
    audio.save('temp_audio.mp3')
    playsound('temp_audio.mp3')
    os.remove('temp_audio.mp3')

if __name__ == '__main__':
    spell('I can spell things correctly. Thanks a lot!')
