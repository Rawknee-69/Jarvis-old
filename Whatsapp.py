from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from Speak import Speak
import pathlib
from selenium.webdriver.chrome.service import Service
import speech_recognition as sr 
from googletrans import Translator

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

def whatsapp_sender_setup():
    script_directory = pathlib.Path().absolute()

    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("--profile-directory=Default")
    options.add_argument(f"user-data-dir={script_directory}\\userdata")
    os.system("")
    os.environ["WDM_LOG_LEVEL"] = "0"
    service = Service(executable_path=r'C:\\Users\\srija\\Downloads\\chromedriverwin64s\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    #driver.get("https://web.whatsapp.com/")
    Speak("Initializing The Whatsapp Software...")


    return driver

def whatsapp_sender(driver, contact_name):
    ListWeb = {
    }
    
    print(contact_name)
    Speak("What's The Message By The Way?")
    message = MicExecution()
    number = ListWeb.get(contact_name)
    if number:
        LinkWeb = 'https://web.whatsapp.com/send?phone='+number+'&text='+message
        driver.get(LinkWeb)

        try:
            #/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span
            #/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span
            element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'))
            WebDriverWait(driver, 100).until(element_present)
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
            Speak("Message Sent")
        except:
            print("Invalid Number")
            Speak("That's an invalid number, please check the number again.")
    else:
        print("Invalid Contact Name")
        Speak("Sorry, I couldn't find the contact name. Please check the name again.")

def hola(contact_name):
    driver = whatsapp_sender_setup()
    whatsapp_sender(driver, contact_name)
    driver.quit()

def main_wp():
    Speak("This will allow you to send a WhatsApp message to your contacts.")
    Speak("To continue, you can say something like 'name of your contact.'")
    # Speak("Just keep in mind you have only 15 seconds to say your message.")

    # Get the contact name from MicExecution
    contact_name = MicExecution()

    if contact_name:
        hola(contact_name)
        return True
    else:
        return False
