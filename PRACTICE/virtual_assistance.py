#pip install pyttsx3 SpeechRecognition pyaudio

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import platform

from gtts import gTTS
import pygame, os, uuid

def speak(text):
    print(f"🤖 Assistant: {text}")
    tts = gTTS(text=text, lang="en")
    filename = f"voice_{uuid.uuid4().hex}.mp3"
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # wait until finished
        pass

    os.remove(filename)


    
#function to listen to user's voice
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio,language='en-in')
            print("You said:",command)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry I don't understand that...")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is down")
            return ""

#function to repond to the user command
def run_assistance():
    speak("Hello I am your virtual assistance, how can I help you")
    while True:
        command = listen()
        
        if 'time' in command:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Current time is " + now)
        
        elif 'date' in command:
            today = datetime.date.today().strftime("%B %d, %Y")
            speak("Today's date is " + today)
            
        elif 'open google' in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        
        elif 'open youtube' in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
            
        elif 'open chatgpt' in command:
            speak("Opening chatgpt")
            webbrowser.open("https://chat.openai.com")
            
        elif 'open github' in command:
            speak("Opening github")
            webbrowser.open("https://www.github.com")
            
        elif 'open calendar' in command:
            speak("Opening Google Calendar")
            webbrowser.open("https://calendar.google.com")
        
        elif 'your name' in command:
            speak("I am your virtual assistant")
            
        elif 'stop' in command or 'exit' in command:
            speak("Ok bye,Have a good day!!")
            break
        else:
            speak("Please say the command again.")

#run the assistant
run_assistance()        