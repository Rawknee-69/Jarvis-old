from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
warnings.simplefilter("ignore")


Link = "https://gpt4login.com/use-chatgpt-online-free/"

chrome_options = Options()
chrome_options.headless = True
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(Link)

# File Operations :- Writing, Reading

def FileReader():
    File = open("TextFiles\\Chatnumber.txt","r")
    Data = File.read()
    File.close()
    return Data

def FileWriter(Data):
    File = open("TextFiles\\Chatnumber.txt","w")
    File.write(Data)
    File.close()

# Sending The Query To The Website :-

def ChatGPTBrain(Query):
    Query = str(Query)
    driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[2]/div/textarea").send_keys(Query)
    sleep(1)
    driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[2]/button/span").click()
    Data = str(FileReader())

# Getting Replies :- 

    while True:

        sleep(0.5)
        
        try:
            AnswerXpath = f"/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[1]/div[{Data}]/span[2]"
            Answer = driver.find_element(by=By.XPATH,value=AnswerXpath).is_displayed()
            if str(Answer)=="True":
                break

        except:
            pass


    AnswerXpath = f"/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[1]/div[{Data}]/span[2]"
    Answer = driver.find_element(by=By.XPATH,value=AnswerXpath).text
    NewData = int(Data) + 2
    FileWriter(Data=str(NewData))
    return Answer

# Rest Of The Code 


def startgpt():
    print("")
    print("Initiating the GPT-4 model.")
    FileWriter(Data='3')

    while True:
            
            
        try:
            File = open("Body\\SpeechRecognition.txt","r")
            Data = File.read()
            File.close()
            FileHistory = open("TextFiles\\chathistory.txt","r")
            DataHistory = FileHistory.read()
            FileHistory.close()

            if str(Data)==str(DataHistory):
                sleep(0.5)
                pass

            else:
                Result = ChatGPTBrain(Data)
                print(Result)
                
                FileHistory = open("TextFiles\\chathistory.txt","w")
                FileHistory.write(Data)
                FileHistory.close()
                
        
        except Exception as e:
            print(e)
startgpt()
