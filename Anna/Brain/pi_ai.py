# Import necessary packages
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pathlib
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

def setup_driver():
    warnings.simplefilter("ignore")
    url = "https://pi.ai/talk"
    scriptDirectory = pathlib.Path().absolute()
    chrome_driver_path = 'Anna\\Brain\\chromedriver.exe'
    chrome_options = Options()
    #chrome_options.add_argument("--headless=new")
    chrome_options.add_argument('--log-level=3')
    service = Service(chrome_driver_path)
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    chrome_options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.get(url)
    sleep(5)
    print("Wait for some time, we are establishing connections with the server.\n")
    print("So please be patient...\n")
    print()
    print("Remember you have 10 seconds to convey your message")

    return driver

def stam():
    driver = setup_driver()
    #sleep(1000)
    def Login(Id, Passcode):
        try:
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div/div/div[1]/a[2]").click()
            sleep(1)
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div/div/div[2]/div[2]/a[1]").click()
            sleep(2)
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div/div[3]/div[2]/div/div/div/div/div/div[1]/div[2]/button").click()
            #sleep(2)
            #driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[1]/div/div/div[1]/div/div[1]/div[2]/button").click()
            sleep(5)
            driver.find_element(by=By.XPATH, value='//*[@id="email"]').send_keys(str(Id))
            sleep(1)
            driver.find_element(by=By.XPATH, value='//*[@id="pass"]').send_keys(Passcode)
            sleep(1)
            driver.find_element(by=By.XPATH, value='//*[@id="loginbutton"]').click()
            sleep(10)
            driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/div/div/div[2]/div[1]/button[2]').click()
            sleep(2)
        except Exception as e:
            print(e)

    def Introduction():
        try:
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div/div/div[3]/div[1]/div[4]/div/div/textarea").send_keys("Introduction")
        except:
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div/div/div[3]/div[1]/div[4]/div/div/textarea").send_keys("Introduction")

        sleep(1)
        driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div/div/div[3]/div[1]/div[4]/div/button").click()
        sleep(1)
        driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[2]/div/div[2]/button").click()
        # sleep(1)

        try:
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div/div/div[3]/div[3]/button").click()
        except:
            pass

        try:#/html/body/div[1]/main/div/div/div[3]/div[3]/div/div[1]/button[1]
            #VoicesToBeChoosen = "1"
            XPathVoice = f"/html/body/div[1]/main/div/div/div[3]/div[3]/div/div[1]/button[1]"
            driver.find_element(by=By.XPATH, value=XPathVoice).click()
            sleep(1)
            driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div/div/div[3]/div[3]/div/div[2]/button[2]/div/svg").click()
            # sleep(1)
            # driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[2]/div/div[2]/button").click()
            try:
                driver.find_element(by=By.XPATH, value="/html/body/div[1]/main/div/div/div[3]/div[3]/div/div[2]/button[2]/div/svg").click()
            except:
                pass
        except:
            pass

    def PopUpRemover():
        try:
            popup = driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[4]/div/div/div[1]").is_enabled()
            if str(popup) == "True":
                driver.refresh()
                sleep(2)
            else:
                pass
        except:
            pass

    def QuerySender(Query):
        Query = str(Query)
        try:
            driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[1]/div[4]/div/div/div/div/textarea").send_keys(Query)
        except:
            driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[1]/div[4]/div/div[2]/div/div/textarea").send_keys(Query)
        sleep(0.5)

    def ButtonClicker():
        while True:
            SendButton = driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[1]/div[4]/div/div/div/button").is_enabled()
            if True == SendButton:
                driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[1]/div[4]/div/div/div/button").click()
                sleep(1)
                break

    def CheckBackSoon(Query):
        Button = driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div").text
        if "Apologies, an unexpected error has occurred. Please check back again soon." == str(Button):
            driver.refresh()
            driver.refresh()
            driver.refresh()
            sleep(2)
            QuerySender(Query=Query)
            ButtonClicker()
        else:
            pass

    def AnswerReturn(Query):
        Query = str(Query)
        try:
            driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[1]/div[4]/div/div/div/div/textarea").send_keys(Query)
        except:
            driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[1]/div[4]/div/div[2]/div/div/textarea").send_keys(Query)
        sleep(0.5)
        while True:
            SendButton = driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[1]/div[4]/div/div/div/button").is_enabled()
            if True == SendButton:
                try:
                    Text = driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[1]/div[2]/div/div/div[3]/div/div/div[2]/div").text
                    print(Text)
                    sleep(0.5)
                    try:
                        driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[1]/div[4]/div/div/div/div/textarea").clear()
                    except:
                        driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[1]/div[4]/div/div[2]/div/div/textarea").clear()
                    sleep(0.5)
                except:
                    Text = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div/div/div[1]/div[2]/div/div/div[3]/div/div/div[2]/div').text
                    print(Text)
                    sleep(0.5)
                    try:
                        driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[1]/div[4]/div/div/div/div/textarea").clear()
                    except:
                        driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[1]/div[4]/div/div[2]/div/div/textarea").clear()
                    sleep(0.5)
                FileHistory = open("Anna\\TextFiles\\Chatnumberpi.txt", "w")
                FileHistory.write('1')
                FileHistory.close()
                break
            else:
                FileRead = open("Anna\\TextFiles\\Chatnumberpi.txt", "r")
                Data = FileRead.read()
                FileRead.close()
                if str(Data) == '80':
                    driver.refresh()
                    sleep(2)
                    try:
                        Text = driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[1]/div[2]/div/div/div[3]/div/div/div[2]/div").text
                        print(Text)
                        sleep(0.5)
                        try:
                            driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[1]/div[4]/div/div/div/div/textarea").clear()
                        except:
                            driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[1]/div[4]/div/div[2]/div/div/textarea").clear()
                        sleep(0.5)
                    except:
                        Text = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div/div/div[1]/div[2]/div/div/div[3]/div/div/div[2]/div').text
                        print(Text)
                        sleep(0.5)
                        try:
                            driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[1]/div[4]/div/div/div/div/textarea").clear()
                        except:
                            driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[1]/div[4]/div/div[2]/div/div/textarea").clear()
                        sleep(0.5)
                    break
                else:
                    FileRead = open("Anna\\TextFiles\\Chatnumberpi.txt", "r")
                    Data = FileRead.read()
                    FileRead.close()
                    FileHistory = open("Anna\\TextFiles\\Chatnumberpi.txt", "w")
                    NewData = int(Data) + 1
                    NewData = str(NewData)
                    FileHistory.write(NewData)
                    FileHistory.close()
                    sleep(0.5)

    FileDetailsFacebook = open("Anna\\TextFiles\\facebook.txt", "r")
    IdPassDetail = FileDetailsFacebook.read()
    FileDetailsFacebook.close()
    Id, Passcode = str(IdPassDetail).split(",")
    Login(Id=Id, Passcode=Passcode)
    PopUpRemover()
    Introduction()

    while True:
        print("")
        print("\nYour turn : \n")
        Query = MicExecution() 
        print("")
        try:
            if "bye" in Query:
                sleep(8)
                driver.quit()
                sys.exit()
            else:
                pass
            if not Query or len(Query) < 2:
             print("Please ask a valid question.")
             continue
            QuerySender(Query=Query)
            ButtonClicker()
            CheckBackSoon(Query=Query)
            AnswerReturn(Query=Query)

        except Exception as e:
            print(e)
