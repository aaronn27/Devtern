import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

# Initialize the recognizer
listener = sr.Recognizer()
# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice property
voices = engine.getProperty('voices')

# Set the voice to male 
#engine.setProperty('voice', voices[0].id)

# Set the voice to female 
engine.setProperty('voice', voices[1].id)

def talk(text):
    """
    Convert text to speech and speak it.
    """
    engine.say(text)
    engine.runAndWait()

def take_command():
    """
    Listen for a command from the user and return it as a string.
    """
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
    """
    Process the command and execute corresponding actions.
    """
    command = take_command()
    print(command)

    # Play a song or open a YouTube video
    if 'play' in command or 'youtube' in command:
        song = command.replace('play','').replace('youtube','')
        talk(f'Playing {song} in Youtube')
        pywhatkit.playonyt(song)
        
    # Tell the current time
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk(f'The Current time is {time}')
        
     # Tell the current date
    elif 'date' in command or 'today' in command:
        date = datetime.datetime.now().strftime('%d %B %Y')
        print(date)
        talk(f'Today is {date}')
        
    # Provide information about a person from Wikipedia
    elif 'who is' in command or 'info' in command:
        person = command.replace('wikipedia','')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
        
    # Open Google in the web browser
    elif 'open google' in command:
        talk("Opening Google\n")
        webbrowser.open("google.com")

    # Open YouTube in the web browser
    elif 'open youtube' in command:
        talk("Opening Youtube\n")
        webbrowser.open("youtube.com")

    # Tell a joke
    elif 'joke' in command:
        jokes = talk(pyjokes.get_joke())
        print(jokes)
        talk(jokes)

    # Handle unrecognized commands
    else:
        talk('I’m sorry, I didn’t understand the command. Could you please repeat it?')

# Continuously run the voice assistant
while True:
    run_alexa()
