from googlesearch import search
import re
import speech_recognition as sr 
from googletrans import Translator

def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) # Listening Mode.....
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="hi")

    except:
        return ""
    
    query = str(query).lower()
    return query

# 2 - Translation

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You : {data}.")
    return data

# 3 - Connect

def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data

def searchsong():
    try:
        print("Say the name of the song: ")
        print("8 seconds")
        # Ask the user for the name of the song
        song_name = MicExecution()

        # Clean the input to remove non-alphanumeric characters
        cleaned_input = re.sub(r'[^a-zA-Z0-9 ]', '', song_name)

        # Prepare the search query
        search_query = f"{cleaned_input} YouTube"

        song_link = None  # Initialize song_link to None

        # Perform the Google search
        for result in search(search_query, num=1, stop=1, pause=2):
            if "youtube.com/watch?" in result:
                song_link = result
                break  # Exit the loop after finding the link

        if song_link:
            print(f"Playing '{cleaned_input}' from {song_link}")
            # Save song_link to a text file
            with open("Anna\\cookies\\song_link.txt", "w") as file:
                file.write(song_link)
        else:
            print(f"No YouTube results found for '{cleaned_input}'")

    except Exception as e:
        print("Error:", e)


