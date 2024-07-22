import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'alexa' in command:
                command = command.replace('alexa', '')
                talk(command)
        return command

def run_alexa():
    command = take_command()
    print(command)

    if 'play' in command or 'youtube' in command:
        song = command.replace('play','').replace('youtube','')
        talk(f'Playing {song} in Youtube')
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk(f'The Current time is {time}')

    elif 'date' in command or 'today' in command:
        date = datetime.datetime.now().strftime('%d %B %Y')
        print(date)
        talk(f'Today is {date}')

    elif 'who is' in command or 'info' in command:
        person = command.replace('wikipedia','')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'open google' in command:
        talk("Opening Google\n")
        webbrowser.open("google.com")

    elif 'open youtube' in command:
        talk("Opening Youtube\n")
        webbrowser.open("youtube.com")

    elif 'joke' in command:
        jokes = talk(pyjokes.get_joke())
        print(jokes)
        talk(jokes)

    else:
        talk('Please say the command again.')

while True:
    run_alexa()
