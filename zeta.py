import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser
from ecapture import ecapture as ec

import wikipedia
from urllib3.util import url

listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('Hello sir, I am zeta')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        talk("Good Morning Sir !")

    elif 12 <= hour < 18:
        talk("Good Afternoon Sir !")

    else:
        talk("Good Evening Sir !")


wishMe()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'zeta' in command:
                command = command.replace('zeta', '')
                print(command)

    except:
        pass
    return command


def run_zeta():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'information about' in command:
        person = command.replace('information about', '')
        info = pywhatkit.info(person)
        print(info)
        talk(info)

    elif 'open my facebook' in command:
        facebook = command.replace('open my facebook', '')
        info = pywhatkit.info('facebook.com' + facebook)
        print(info)
        talk('opening facebook' + info)

    elif 'open github' in command:
        github = command.replace('open my github', '')
        info = pywhatkit.info('https://github.com' + github)
        print(info)
        talk('opening github' + info)

    elif 'how are you' in command:
        talk('well sir , how are you')
        engine.runAndWait()

    elif 'open youtube' in command:
        talk("Here you go to Youtube\n")
        webbrowser.open("youtube.com")

    elif 'search' in command:

        command = command.replace("search", "")
        command = command.replace("play", "")
        webbrowser.open(command)

    elif 'is love' in command:
        talk("It is 7th sense that destroy all other senses")
        engine.runAndWait()

    elif 'do you know everything' in command:
        talk('There is reason why we don\'t have an answer to everything yet. If we become all-knowing,'
             'the purpose of life will be destroyed')
        engine.runAndWait()


    elif 'camera' in command or 'take photo' in command:
        ec.capture(0, "zeta Camera ", "img.jpg")

    elif 'good night' in command:
        talk('good night and sweet dreams')
        engine.runAndWait()

    elif 'good morning' in command:
        talk('good morning sir')

    elif 'thank you' in command or 'thanks' in command:
        talk('my pleasure')

    elif 'i am avanish' in command:
        talk('nice to see you sir')
        talk('.. how can i help you')

    elif 'what you like to drink' in command:
        talk('what I like to drink most is beer that belong to others')
        engine.runAndWait()

    elif 'fine' in command or 'well' in command:
        talk('great')


run_zeta()
