from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
warnings.simplefilter("ignore")
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
import pygetwindow as gw
import speech_recognition as sr 
from googletrans import Translator
import os
import pygame
import string
import keyboard
import pyperclip
import pyautogui


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

def laod_3Dmodels():

    clipboard_data = pyperclip.paste()


    chrome_driver_path = 'C:\\Users\\srija\\Desktop\\AIJarvisl\\Anna\\Brain\\chromedriver.exe'
    url = clipboard_data
    chrome_options = Options()
    
    chrome_options.add_argument("--hide-crash-restore-bubble")
    chrome_options.add_argument("user-data-dir=C:\\Users\\srija\\Desktop\\AIJarvisl\\Anna\\localhost")
    chrome_options.add_argument("--remote-debugging-port=6969")
    driver = webdriver.Chrome(options=chrome_options)
    pyautogui.press('f11')
    driver.get(url)

    Speak("Press 'q' to close and return")
    with open("Anna\\TextFiles\\gen_img_links.txt", 'a') as file:
        file.write(url + '\n')

    while True:
        if keyboard.is_pressed('q'):
            break    


def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,15) # Listening Mode.....
    
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


def models():
    agreement_checkbox_xpath ='//*[@id="tos"]'
    dismiss_this_message = '//*[@id="dismiss"]'
    confirm_button_xpath = "/html/body/div[3]/div[2]/div[2]/button"
    get_started_confirm = "/html/body/div[4]/div[2]/div[3]/div/button" 
    prompt_field = "/html/body/div[1]/div/div[2]/form/div[2]/div[1]/textarea"
    generate_button_xpath = "/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/button[2]"
    embed_code_copy = '/html/body/div[1]/div/div[2]/form/div[1]/div[2]/button[2]'
    checkpost = "/html/body/div[1]/div/div[2]/div/div"
    style = '//*[@id="select-button"]'
    style_realistics = "/html/body/div[3]/div/div/div[2]/div/div/div/div/div/div/div[1]"
    style_real = "/html/body/div[3]/div/div/div[2]/div/div[3]/div/div/div/div/div[1]/div"
    # Ignore unnecessary warnings
    #/html/body/div[3]/div[2]/div[2]/div/fieldset[2]/button
    #/html/body/div[4]/div[2]/div[2]/button
    try:
        # Define the URL
        url = "https://skybox.blockadelabs.com/"

        # Set up Chrome options
        chrome_driver_path = 'C:\\Users\\srija\\Desktop\\AIJarvisl\\Anna\\Brain\\chromedriver.exe'
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        chrome_options = Options()
        chrome_options.add_argument(f"user-agent={user_agent}")
        #chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--hide-crash-restore-bubble")
        chrome_options.add_argument("--allow-clipboard")
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()
        driver.get(url)
        window = gw.getWindowsWithTitle('Blockade Labs Skybox - AI-Generated 3D Worlds')[0]
        window.hide()

        sleep(3)

        driver.find_element(By.XPATH, agreement_checkbox_xpath).click()
        driver.find_element(By.XPATH, dismiss_this_message).click()
        sleep(1)
        driver.find_element(By.XPATH, confirm_button_xpath).click()
        sleep(2)
        driver.find_element(By.XPATH, dismiss_this_message).click()
        driver.find_element(By.XPATH, get_started_confirm).click()
        sleep(3)
        driver.find_element(By.XPATH,prompt_field).click()
        sleep(0.1)
        driver.find_element(By.XPATH, dismiss_this_message).click()
        driver.find_element(By.XPATH, get_started_confirm).click()
        sleep(0.001)
        Speak("you have 15 seconds to say : ")
        Speak ("Say The WOrlD YOu IMagInE : ")
        prompt = MicExecution()
        sleep(0.1)
        driver.find_element(By.XPATH, prompt_field).send_keys(prompt)
        sleep(0.01)
        driver.find_element(By.XPATH,style).click()
        sleep(1)
        driver.find_element(By.XPATH,style_realistics).click()
        sleep(1)
        driver.find_element(By.XPATH,style_real).click()
        sleep(1)
        
        driver.find_element(By.XPATH, generate_button_xpath).click()
        Speak ("Generating your image please be paitent.\n")
        Speak("It will take time like 2 to 4 minutes depending on your internet speed but trust me it would be worth it..")
        while True:
                    try:
                        # Check if the flag_button_xpath element is present
                        WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, checkpost))
                        )
                        
                        # If the element is present, wait until it disappears
                        WebDriverWait(driver, 100).until_not(
                            EC.presence_of_element_located((By.XPATH, checkpost))
                        )
                        
                    except TimeoutException:
                        break
                    
        Speak("All most there")

        driver.find_element(By.XPATH, embed_code_copy).click()
        sleep(1)
        Speak("presenting it ....")



        laod_3Dmodels()


    except Exception as e:
        print(e)    
        #it requires some time in genertaing it

# so this was it 
models()