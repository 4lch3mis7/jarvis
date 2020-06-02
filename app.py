from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib


def talkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')


# listens for commands
def myCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("I am ready for your next command")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said: " + command + '\n')
        return command
    # loop back to continue to listen for commands
    except sr.UnknownValueError:
        # assistant(myCommand())
        myCommand()


# if statements for executing commands
def assistant(command):
    if 'open Reddit python' in command:
        browser_path = '/usr/bin/firefox'
        url = 'http://reddit.com/r/python'
        webbrowser.get(browser_path).open(url)

    if 'what\'s up' in command:
        talkToMe('Chill bro!')

    if 'email' in command:
        talkToMe('Who is the recipient?')
        recipient = myCommand()
        if 'prasant' in recipient.lower():
            talkToMe('What should i say?')
            content = myCommand()

            # init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            # identify to server
            mail.ehlo()

            # encrypt session
            mail.starttls()

            # login
            mail.login('prashantpaudel556@gmail.com', 'fuck787898')

            # send message
            mail.sendmail('Prasant Paudel', 'prashantpaudel555@gmail.com')

            # close connection
            mail.close()

            talkToMe('Email sent.')

talkToMe('I am ready for your command.')

while 1:
    assistant(myCommand())




