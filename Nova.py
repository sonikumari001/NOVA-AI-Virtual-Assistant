import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# Set to female voice (usually index 1) if available, otherwise default
try:
    engine.setProperty('voice', voices[1].id)
except IndexError:
    engine.setProperty('voice', voices[0].id)

def speak(audio):
    """Speaks the given text."""
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    """Greets the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am Nova. Please tell me how may I help you")

def take_command():
    """Listens to microphone input and returns string output."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again please...")
            return "None"
    return query

def main():
    wish_me()
    while True:
        query = take_command().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            # You might want to add wikipedia import and logic here if requested, 
            # currently just placeholder based on typical assistant features, 
            # but user specifically asked for Youtube, Whatsapp, Instagram, Time.
            pass

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")

        elif 'open whatsapp' in query:
            speak("Opening WhatsApp")
            webbrowser.open("web.whatsapp.com")

        elif 'open instagram' in query:
            speak("Opening Instagram")
            webbrowser.open("instagram.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif 'quit' in query or 'exit' in query or 'stop' in query:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
