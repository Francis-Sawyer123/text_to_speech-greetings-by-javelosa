import pyttsx3
import datetime
import speech_recognition as sr

engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("My name is wolfgang how can i help you?")

def time():
    Time=datetime.datetime.now().strftime("%I:%M %Y-%m-%d")
    speak(Time)

def greet():
    speak("Welcome back again owner")
    speak("the current Time and date is")
    time()
    
    hour=datetime.datetime.now().hour

    if hour >= 6 and hour<12:
        speak("GOOD MORNING")
    elif hour >= 12 and hour<18:
        speak("GOOD AFTERNOON")
    elif hour >= 18 and hour<24:
        speak("GOOD EVENING")
    else:
        speak("Adios owner")
    speak("Wolfgang Is at your service, what can i do for you?")

def takec():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenning...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognized")
        query = r.recognize_google(audio,language = 'en-in')
        print(query)
    
    except Exception as e:
        print(e)
        speak("Say it again")
        return "none"
    return query

greet()
takec()


