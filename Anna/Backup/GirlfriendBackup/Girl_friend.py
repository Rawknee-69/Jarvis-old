from time import sleep 
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.by import By  
import warnings  
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC 
import re
from selenium.webdriver.support.ui import WebDriverWait

def filter_response(response):
    # Your filter response code here
    # For example:
    response = response.replace('[', '').replace(']', '')
    response = re.sub(r'\*{1,3}"', '', response)
    response = re.sub(r'\[[^\]]*\]\(\^[0-9]+\^\)', '', response)
    response = re.sub(r'\^[0-9]+\^', '', response)
    response = response.replace('This content may violate our content policy. If you believe this to be in error, please submit your feedback — your input will aid our research in this area.','')
    emoji_pattern = re.compile("["
                               u"\U0001F300-\U0001F9FF"
                               u"\U0001FA00-\U0001FA6F"
                               u"\U0001F600-\U0001F64F"
                               u"\U0001F680-\U0001F6FF"
                               u"\U0001F1E0-\U0001F1FF"
                               "]+", flags=re.UNICODE)
    response = emoji_pattern.sub(r'', response)
    return response

def interact_with_chat(driver, question, last_iteration):
    try:
        search_bar_xpath = '/html/body/div[1]/div/div[2]/div[2]/footer/div/textarea'
        base_response_xpath = "/html/body/div[1]/div/main/div/div[2]/div/div[{}]/div/div[1]/div[2]/div"
        send_button_xpath = "/html/body/div[1]/div/div[2]/div[2]/footer/div/button"
        flag_button_check = "/html/body/div[1]/div/main/div/div[2]/div/div[{}]/div/div[2]/button[1]"
        search_bar = driver.find_element(By.XPATH, search_bar_xpath)
        search_bar.clear()
        search_bar.send_keys(question)
        search_bar = driver.find_element(By.XPATH, send_button_xpath).click()
        
        # Wait for flag_button_check to appear
        button_check = flag_button_check.format(last_iteration)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, button_check))
        )

        response_xpath = base_response_xpath.format(last_iteration)
        response_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, response_xpath))
        )
        
        response_text = response_element.text
        print("\n\nResponse received:\n\n", response_text)
        
        filtered_response_text = filter_response(response_element.text)
        with open("TextFiles\\gf_respnse.txt", "w", encoding="utf-8") as file:
            file.write(filtered_response_text)
            
    except Exception as e:
        print("An error occurred:", e)

def start_waifu_interaction(driver, last_iteration):
    try:
        print("OK, I'm ready to listen. Just enter.")
        print("Okay now tell me your name so we can proceed to the conversation")
        while True:
            user_prompt = input(" enter : ")
            
            if user_prompt.lower() in ["exit", "close", "bye", "bye baby"]:
                print("Okay, goodbye......")
                return

            if len(user_prompt) >= 0:
                interact_with_chat(driver, user_prompt, last_iteration)
                last_iteration += 2
                with open("TextFiles\\Girlfriend.txt", "w", encoding="utf-8") as file:
                    file.write(str(last_iteration))
            else:
                print("Please enter a longer prompt.")

    except Exception as e:
        print("An error occurred:", e)

def start_waifu():
    try:
        warnings.simplefilter("ignore")
        url = "https://charstar.ai/chat/b5082729-fb67-40f7-b95a-7d1b30c2fb37?id=cf9ff53e-9ac6-42cb-8592-d5bd186b4b65"  

        chrome_driver_path = 'C:\\Users\\srija\\Desktop\\Anna\\Brain\\chromedriver.exe'
        chrome_options = Options()
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        chrome_options.add_argument(f"user-agent={user_agent}")
        
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--hide-crash-restore-bubble")
        chrome_options.add_argument("--allow-clipboard")
        chrome_options.add_argument("user-data-dir=C:\\Users\\srija\\Desktop\\Anna\\localhost\\")  # Path to your custom profile
        chrome_options.add_argument("--remote-debugging-port=6969")
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.maximize_window()
        driver.get(url)
                
        fileopen = open("TextFiles\\Girlfriend.txt", "r")
        last_iteration = int(fileopen.read())
        fileopen.close()
        
        start_waifu_interaction(driver, last_iteration)
        
        driver.quit()
    except Exception as e:
        print("An error occurred:", e)

start_waifu()
