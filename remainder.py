from gtts import gTTS
import os
import datetime
import time
from json_obj import JsonObject

# CONFIGURATIONS
my_alarm_sound = 'This is the alarm time!'
my_audio_player = 'mpg123'
my_json_file = 'alarm_time.json'


def spell(text):
    audio = gTTS(text=text, lang='en')
    audio.save('audio.mp3')
    os.system(f'{my_audio_player} audio.mp3')


def buzz():
    spell(my_alarm_sound)


def convert_day_str_to_int(day):
    # Check if day is in string type (i.e. today, tomorrow)
    # If is, then convert it to corresponding day integer
    if type(day) is str:
        if str(day).lower() == 'today':
            return datetime.datetime.now().day
        elif str(day).lower() == 'tomorrow':
            return datetime.datetime.now().day + 1
        else:
            spell('It seems like you have entered incorrect day!\
             Please check date format.')
            exit()


def set_alarm(day, hour, minute):

    # Converting 'today', 'tomorrow' into integer day
    day = convert_day_str_to_int(day)

    # Store Alarm Time in Json
    alarm_time = JsonObject(day=day, hour=hour, minute=minute)
    alarm_time.write_to(my_json_file)


    while 1:
        # Read Data from Json
        alarm_time = JsonObject().read_from(my_json_file)
        print(alarm_time)

        # check if today
        if alarm_time['day'] == datetime.datetime.now().day:
            spell('Hi there, I wanted to remind you that the alarm is for today!')

            # check if this hour
            if alarm_time['hour'] == datetime.datetime.now().hour:
                spell('Alarm is gonna be ringing this hour!')

                # check if this minute
                if int(minute) == int(datetime.datetime.now().minute):
                    # Buzz the alarm
                    buzz()
                    break
        time.sleep(1)


try:
    set_alarm(day='tody', hour=8, minute=7)
except Exception as msg:
    print(msg)
    spell('You should check the date format and set alarm again. Thank you!')
