import speech_recognition as sr
def voice_input(retries=5):
    r = sr.Recognizer()
    # import spell
    with sr.Microphone() as source:
        # spell('I am ready!')
        r.adjust_for_ambient_noise(source, duration=1)
        recorded_audio = r.listen(source)
    try:
        command = r.recognize_google(recorded_audio)
        return command
    except sr.UnknownValueError:
        if retries > 0:
            print('[-] I could not recognize you voice. Would you speak again?')
            return voice_input(retries=retries-1)   