import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
rate = engine.getProperty("rate")
engine.setProperty("rate",245)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('li:')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            if 'simple' in command:
                command = command.replace('simple','')
                talk(command)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print(time)
                talk("currently it's "+time)
            elif 'who' in command:
                person = command.replace('who is','')
                info = wikipedia.summary(person, 1)
                talk(info)
                print(info)
            elif 'joke' in command:
                talk(pyjokes.get_joke())
            elif 'cmd' in command:
                os.system("start cmd")

            else:
                talk('please say command again')


    except:
        pass
    return command

def main():
    command = take_command()
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
while True:
    main()