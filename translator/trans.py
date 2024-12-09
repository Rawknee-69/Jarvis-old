import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
import sys
sys.path.append("C:\\Users\\srija\\Desktop\\AIJarvisl\\")
from Speak import Speak
def recognize_speech():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        Speak("Please speak a sentence: you only have 15 seconds to speak")
        print("Listening....")
        Listen = recognizer.listen(source,0,15)

    try:
        sentence = recognizer.recognize_google(Listen)
        print("recognizing...")
        print (sentence)
        return sentence
    except sr.UnknownValueError:
        print("Sorry, could not understand Listen.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def get_target_language():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        Speak("Please speak the target language (e.g., 'Spanish'):")
        Listen = recognizer.listen(source,0,8)

    try:
        target_language = recognizer.recognize_google(Listen)
        return target_language.lower()
    except sr.UnknownValueError:
        print("Sorry, could not understand Listen.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def maintranslation():
    sentence = recognize_speech()

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        Speak("Please speak the target language (e.g., 'Spanish'):")
        Listen = recognizer.listen(source, 0,12)

    
    if sentence:
        print(f"You said: {sentence}")
        
        target_language = get_target_language()
        if target_language:
            translator = Translator()
            try:
                translated_text = translator.translate(sentence, dest=target_language).text
                
                print("Translation:", translated_text)

                Speak("would you like to save this translation yes or no ")
                choice = recognizer.recognize_google(Listen)
                choice.lower()
                
                if choice == "yes":
                    tts = gTTS(translated_text, lang=target_language)
                    tts.save("translation.mp3")
                    os.system("start translation.mp3")
                
                save_choice = input("Do you want to save the translation to a text file (yes/no)? ").lower()
                if save_choice == "yes":
                    with open("translation.txt", "w", encoding ="utf-8") as file:
                        file.write(translated_text)
                    os.system("start notepad translation.txt")
                else:
                    Speak("your translation is shown in consloe")    
            
            except ValueError as e:
                print("Error:", e)
             