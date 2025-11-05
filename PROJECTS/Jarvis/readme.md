# 🧠 Jarvis – A Python Voice Assistant

Jarvis is a **speech-based AI assistant** built using Python that can **listen, understand, and perform real-time actions** based on your voice commands.  
It can open websites like Google, YouTube, Instagram, etc., and even **play songs** from a custom music library.

---

## 🚀 Features

- 🎤 **Speech Recognition** – Listens to your voice commands using the microphone.  
- 🔊 **Text-to-Speech** – Replies back using a natural-sounding voice.  
- 🌐 **Smart Web Access** – Opens popular sites like Google, YouTube, Instagram, WhatsApp, and more.  
- 🎶 **Play Music** – Plays requested songs from a `musiclibrary` module.  
- 💬 **Conversation** – Responds to greetings like “how are you”.  
- 🧩 **Modular Design** – Easy to extend with more commands and features.  

---

## 🧠 How It Works

1. Jarvis initializes with a **speech recognizer** and a **text-to-speech engine**.  
2. It listens continuously for the keyword **"service"** to activate.  
3. Once active, it captures your next voice command.  
4. Commands like `"open google"` or `"play despacito"` trigger corresponding actions.  
5. Jarvis responds using **pyttsx3** for voice feedback.  

---

## 🛠️ Technologies Used

- **Python 3.x**
- [speech_recognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- **webbrowser** (built-in)
- **os** (built-in)
- **musiclibrary.py** (custom file for song URLs)

---

## 📂 Folder Structure

