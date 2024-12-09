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
"https://files.appsgeyser.com/hola_17591058.apk"
start_next = "/html/body/div[2]/div[2]/div/div/div[5]/form/div[1]/div[1]/div/div[2]"
app_next = "/html/body/div[2]/div[2]/div/div/div[5]/form/div[1]/div[2]/div/div[2]"
app_name = '//*[@id="CustomModelForm_name"]'
app_name_next = "/html/body/div[2]/div[2]/div/div/div[5]/form/div[1]/div[3]/div/div[3]"
icon_next = "/html/body/div[2]/div[2]/div/div/div[5]/form/div[1]/div[4]/div/div[5]"
create_n = '//*[@id="submit-button"]'
download_one = '//*[@id="downloadButtonWithText"]'
downlaod_ones_now = "/html/body/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div[1]/div[2]/div[2]/a/button"
login_google = '/html/body/div[1]/div[3]/div[2]/div[4]/div[1]/div'

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
    Link = "https://appsgeyser.com/create-vpnPremium-app/"

    chrome_driver_path = 'C:\\Users\\srija\\Desktop\\Anna\\Brain\\chromedriver.exe'
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={user_agent}")
    #chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("user-data-dir=C:\\Users\\srija\\Desktop\\Anna\\localhost\\")  # Path to your custom profile
    chrome_options.add_argument("--remote-debugging-port=6969")
    chrome_options.add_argument("--hide-crash-restore-bubble")
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.get(Link)
    print("starting services please wait a moment")
    print("\nCaution: !!! THis is under !!! ALPHA TESTING !!! So , it may not produce as good result .")
    sleep(5)
    print("Enter the app name:  ")
    appnae = input("\nEnter the app name: ")

    driver.find_element(by=By.XPATH,value=start_next).click()
    sleep(3)
    driver.find_element(by=By.XPATH,value=app_next).click()
    sleep(3)
    driver.find_element(by=By.XPATH,value=app_name).send_keys(appnae)
    sleep(3)
    driver.find_element(by=By.XPATH,value=app_name_next).click()
    sleep(3)
    driver.find_element(by=By.XPATH,value=icon_next).click()
    sleep(3)
    driver.find_element(by=By.XPATH,value=create_n).click()
    sleep(3000)
    driver.find_element(by=By.XPATH,value=login_google).click()
    sleep(8)
    driver.find_element(by=By.XPATH,value=download_one).click()
    sleep(3)
    driver.find_element(by=By.XPATH,value=downlaod_ones_now).click()

pdf_madx()