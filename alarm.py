from gtts import gTTS
import os
import datetime
import time

# configurations
alarm_sound = 'This is the alarm time!'
audio_player = 'mpg123'


def spell(text):
    audio = gTTS(text=text, lang='en')
    audio.save('audio.mp3')
    os.system(f'{audio_player} audio.mp3')


def buzz():
    spell(alarm_sound)


def set_alarm(day, hour, minute):
    while 1:
        # check if today
        if day.lower() == 'today' or int(day) == int(datetime.datetime.now().day):
            print('Alarm is for today!')

            # check if this hour
            if int(hour) == int(datetime.datetime.now().hour):
                print('Alarm is gonna be ringing this hour!')

                # check if this minute
                if int(minute) == int(datetime.datetime.now().minute):

                    # Buzz the alarm
                    buzz()
                    break




try:
    set_alarm(day=3, hour=21, minute=7)
except Exception as msg:
    print(msg)
    spell('You should check the date format and set alarm again. Thank you!')