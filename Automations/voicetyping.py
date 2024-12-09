import speech_recognition as sr
import re

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

def voice_typing():
    # Record audio from the microphone
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source,0,10)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Error requesting results; {e}")

def process_commands(text):
    # Process special voice commands
    text = re.sub(r"period", ".", text)
    text = re.sub(r"comma", ",", text)
    text = re.sub(r"new line", "\n", text)
    text = re.sub(r"backspace", "", text)
    text = re.sub(r"delete \w+", "", text)
    return text

def save_to_file(text):
    with open("voice_text.txt", "w") as file:
        file.write(text)
        print("Text saved to voice_text.txt")

def vc():
    recognized_text = voice_typing()
    if recognized_text:
        recognized_text = process_commands(recognized_text)
        print("Recognized Text:", recognized_text)
        save_to_file(recognized_text)

