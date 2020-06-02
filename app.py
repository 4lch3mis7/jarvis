from gtts import gTTS
from speech_recognition import Microphone, Recognizer, UnknownValueError
import os

# Basic Configurations
audio_player = 'mpg123'


def spell(text):
    audio = gTTS(text=text, lang='en')
    audio.save('audio.mp3')
    os.system(f'{audio_player} audio.mp3')


def listen():
    pass

spell('hello!')



