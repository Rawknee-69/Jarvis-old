from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.chrome.service import Service
warnings.simplefilter("ignore")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import speech_recognition as sr 
from googletrans import Translator
import os
import pygame
import string

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
        audio = r.listen(source,0,10) # Listening Mode.....
    
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


def pdf_madx():
    Link = "https://wepik.com/ai-presentations"

    chrome_driver_path = 'C:\\Users\\srija\\Desktop\\Anna\\Brain\\chromedriver.exe'
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={user_agent}")
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("user-data-dir=C:\\Users\\srija\\Desktop\\Anna\\localhost\\")  # Path to your custom profile
    chrome_options.add_argument("--remote-debugging-port=6969")
    chrome_options.add_argument("--hide-crash-restore-bubble")
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.get(Link)


    language = "/html/body/main/div/div[1]/div[1]/div/div/form/div[2]/div[2]/select"
    language_eng = "/html/body/main/div/div[1]/div[1]/div/div/form/div[2]/div[2]/select/option[3]"
    get_started = "/html/body/main/div/div[1]/div[2]/div[1]/div[2]/button"
    enter_the_prompt = "/html/body/main/div/div[1]/div[1]/div/div/form/div[1]/input"
    Templete_to_design = "/html/body/main/div/div[1]/div[1]/div/div/form/div[3]/label[4]/img"
    generate_pdf = "/html/body/main/div/div[1]/div[1]/div/div/form/button"
    downlaad_button = "/html/body/div[1]/div/div/header/div[3]/div/div[2]/button"
    downlaod_as_pdf = "/html/body/div[1]/div/div/header/div[3]/div/div[2]/div/div/div[2]/div/button[4]/div/div[1]"
    final_downlaod = "/html/body/div[1]/div/div/header/div[3]/div/div[2]/div/div/div[2]/button"

    Speak("Describe the content you want presentation on: ")

    Speak("for example : Motorcars and Electric cars major differences ")

    Speak("You have 12 seconds to describe so you can start: ")
   
    prompt = MicExecution()


    driver.find_element(by=By.XPATH,value=get_started).click()
    driver.find_element(by=By.XPATH,value=Templete_to_design).click()
    driver.find_element(by=By.XPATH,value=enter_the_prompt).send_keys(prompt)
    driver.find_element(by=By.XPATH,value=language).click()
    driver.find_element(by=By.XPATH,value=language_eng).click()
    driver.find_element(by=By.XPATH,value=generate_pdf).click()

    download = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, downlaad_button))
        )
    download.click()
    driver.find_element(by=By.XPATH,value=downlaod_as_pdf).click()
    sleep(2)
    driver.find_element(by=By.XPATH,value=final_downlaod).click()
    Speak("15 seconds to go sir")
    sleep(15)
    Speak("Done sir! TAke a minute to look at it")
pdf_madx()