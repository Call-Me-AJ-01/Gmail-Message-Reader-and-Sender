def speak_msg(text):
    import pyttsx3 as r
    engine = r.init()
    engine.setProperty('rate',125)
    engine.say(text)
    engine.runAndWait()
