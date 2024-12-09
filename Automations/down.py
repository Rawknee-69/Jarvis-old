import random
import csv
import sys
import time
import speech_recognition as sr
from googletrans import Translator
from nltk.sentiment import SentimentIntensityAnalyzer

def Listen(last_active_time):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)  # Listen for up to 8 seconds
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="hi")
        print(query)  # Recognize speech using Google Web Speech API

    except sr.UnknownValueError:
        print("")
        return "", last_active_time

    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")
        return "", last_active_time

    query = query.lower()
    last_active_time = time.time()  # Update the last active time
    return query, last_active_time



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



sys.path.append("")
from Speak import Speak


class MoodAssistant:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()
        self.responses = self.load_responses()

    def load_responses(self):
        responses = {
            'happy': [],
            'sad': [],
            'neutral': [],
        }
        with open('Data\\datares.csv', 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                mood = row[0]
                response = row[1]
                if mood in responses:
                    responses[mood].append(response)
        return responses

    def determine_mood(self, text):
        sentiment_score = self.sia.polarity_scores(text)['compound']
        if sentiment_score > 0.1:
            return 'happy'
        elif sentiment_score < -0.1:
            return 'sad'
        else:
            return 'neutral'

    def respond_to_input(self, user_input):
        mood = self.determine_mood(user_input)
        response = random.choice(self.responses[mood])
        return response

def senti():
    mood_assistant = MoodAssistant()
    
    print("Mood Assistant: Hi there! How are you feeling today?")
    
    last_active_time = time.time()  # Initialize the last active time
    
    while True:
        current_time = time.time()
        time_since_last_active = current_time - last_active_time
        
        if time_since_last_active >= 600:  # Check if 10 minutes have passed
            print("Mood Assistant: I am feeling bored, let's talk")
            Speak("I am feeling bored, let's talk")
            last_active_time = current_time
        
        print("You: ")
        user_input, last_active_time = Listen(last_active_time)
        
        if user_input.lower() in ["exit", "quit"]:
            print("Mood Assistant: Take care!")
            break
        
        response = mood_assistant.respond_to_input(user_input)
        print("Mood Assistant:")
        Speak(response)


senti()
