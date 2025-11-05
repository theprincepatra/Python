import speech_recognition as sr     # Speech recognition
import webbrowser                   # Web browsing
import pyttsx3                      # Text-to-speech
import musiclibrary                  # Artificial music file

recognizer = sr.Recognizer()         # Global recognizer object
engine = pyttsx3.init()              # Initialize text-to-speech

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if c.lower() == "open google":
        speak("Opening google")
        webbrowser.open("https://google.com")
    elif c.lower() == "open youtube":
        speak("Opening youtube")
        webbrowser.open("https://youtube.com")
    elif c.lower() == "open facebook":
        speak("Opening facebook")
        webbrowser.open("https://facebook.com")
    elif c.lower() == "open instagram":
        speak("Opening instagram")
        webbrowser.open("https://instagram.com")
    elif c.lower() == "open whatsapp":
        speak("Opening whatsapp")
        webbrowser.open("https://whatsapp.com")
    elif c.lower() == "open linkedin":
        speak("Opening linkedin")
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = " ".join(c.lower().split(" ")[1:])
        link = musiclibrary.music.get(song)

        if link:
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song in the library.")
            print(f"Song '{song}' not found.")
    elif c.lower() == "how are you":
        speak("I am fine, what's about you")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            word = "Sorry, I didn't catch that."  # Ensure word is always assigned
            try:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                word = r.recognize_google(audio)
            except sr.UnknownValueError:
                print("user: Sorry, I didn't catch that.")
            except sr.RequestError:
                print("user: Could not request results from Google Speech Recognition")

        print(f"user: {word}")
        speak("Great!! That's nice, enjoy your day.")

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
            word = r.recognize_google(audio)
            print(word)

            if word.lower() == 'service':
                speak("Yaa")
                with sr.Microphone() as source:
                    print("Jarvis is active, listening to your command!")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)  # Capture speech before passing
                    processCommand(command)

        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service; check your internet.")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
        except Exception as e:
            print("Error:", str(e))
