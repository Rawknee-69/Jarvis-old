from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.chrome.service import Service
warnings.simplefilter("ignore")
import speech_recognition as sr 
from googletrans import Translator
import os
import pygame
import string
import sys
voice2 = 'en-US-AnaNeural'

def filter_text(data):
    # Remove emojis
    data = data.encode('ascii', 'ignore').decode('utf-8')
    
    # Remove punctuation except comma and full stop
    allowed_punctuations = string.punctuation.replace('.', '').replace(',', '')
    data = ''.join(char for char in data if char not in allowed_punctuations)
    
    # Remove question marks and brackets
    data = data.replace('?', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '')

    return data.strip()

def Speak(data):
    filtered_data = filter_text(data)
    command = f'edge-tts --voice "{voice2}" --text "{filtered_data}" --write-media "Body//Dataspeak//data.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Body//Dataspeak//data.mp3")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Increased ticks per second for smoother playback

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()




def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,20) # Listening Mode.....
    
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
Link = "https://gitagpt.org/#"
pop_up_close = '//*[@id="email-popup-close"]'
first_chat_input = '//*[@id="query-input-gita"]'
send_button = '//*[@id="ask-button"]'

def setup_driver():
    warnings.simplefilter("ignore")
    chrome_driver_path = 'C:\\Users\\srija\\Desktop\\AIJarvisl\\Anna\\Brain\\chromedriver.exe'
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={user_agent}")
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--hide-crash-restore-bubble")
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.get(Link)
    sleep(1)

    driver.find_element(by=By.XPATH, value=pop_up_close).click()

    return driver

def FileReader():
    File = open("Anna\\TextFiles\\Gita.txt", "r")
    Data = File.read()
    File.close()
    return Data

def FileWriter(Data):
    File = open("Anna\\TextFiles\\Gita.txt", "w")
    File.write(Data)
    File.close()

def ChatGPTBrain(Query, driver):
    Query = str(Query)
    driver.find_element(by=By.XPATH, value=first_chat_input).send_keys(Query)
    sleep(1)
    driver.find_element(by=By.XPATH, value=send_button).click()
    Data = str(FileReader())

    while True:
        sleep(0.5)

        try:
            check_point = f"/html/body/div[3]/ul/li[{Data}]/div/div/div[1]/a[2]/img"
            Answer = driver.find_element(by=By.XPATH, value=check_point).is_displayed()
            break

        except:
            pass

    AnswerXpath = f"/html/body/div[3]/ul/li[{Data}]/div/div"
    Answer = driver.find_element(by=By.XPATH, value=AnswerXpath).text
    NewData = int(Data) + 2

    unwanted_phrase = "Do follow us on"
    if unwanted_phrase in Answer:
        Answer = Answer.replace(unwanted_phrase, "")

    unwanted_phrases = "Donate to our cause to keep this website running."
    if unwanted_phrases in Answer:
        Answer = Answer.replace(unwanted_phrases, "")

    unwanted_phrasess = " Retry Share"
    if unwanted_phrasess in Answer:
        Answer = Answer.replace(unwanted_phrasess, "")

    unwanted_phrasesss = " Arjuna"
    if unwanted_phrasesss in Answer:
        Answer = Answer.replace(unwanted_phrasesss, "Srijan")

    # Replace "GitaGpt.org" with "home"
    if "GitaGpt.org" in Answer:
        Answer = Answer.replace("GitaGpt.org", "home")
        
    answer_lines = Answer.split('\n')
    answer_lines = answer_lines[:4]
    Answer = '\n'.join(answer_lines)

    FileWriter(Data=str(NewData))
    return Answer

def startgpt():
    driver = setup_driver()
    print("")
    Speak("Starting BHagwat GITA FOR YOU.")
    Speak("Here lord KRISHNA hiMsElF ANSweRs YoUr QueSTiOnS\n")
    Speak("Rule!!! : You will only have 20 seconds to ask your question:  ")
    FileWriter(Data='2')

    while True:
        try:
            print("\nEnter your question: ")
            Data = MicExecution()
            if "bye" in Data:
                sleep(1)
                driver.quit()
                sys.exit()

            if not Data or len(Data) < 2:
                print("Please ask a valid question.")
                continue  
            Speak("Answering your questions...")
            Result = ChatGPTBrain(Data, driver)
            print("")
            Speak(Result)
            print("")

        except Exception as e:
            print(e)