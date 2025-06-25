import os
import speech_recognition as sr
from gtts import gTTS
import playsound

def listen_and_respond():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        response = process_command(text)
        speak(response)
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
    except sr.RequestError:
        print("Speech recognition service unavailable.")

def process_command(text):
    text = text.lower()
    if "hello" in text:
        return "Hi there! How can I assist you?"
    elif "your name" in text:
        return "I am your AI assistant."
    else:
        return "Sorry, I don't understand that yet."

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "voice_response.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

if __name__ == "__main__":
    listen_and_respond()
