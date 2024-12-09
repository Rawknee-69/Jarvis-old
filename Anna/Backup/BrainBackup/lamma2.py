import re
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



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
        search_bar_xpath = '/html/body/div[1]/div[1]/div/div[2]/form/div/div/textarea'
        base_response_xpath = '/html/body/div[1]/div[1]/div/div[1]/div/div[{}]/div[1]/div'
        flag_button_xpath = "/html/body/div[1]/div[1]/div/div[2]/form/div/div[2]"
        warning_button_xpath = "/html/body/div[1]/div[1]/div[1]/div/h2"
        search_bar = driver.find_element(By.XPATH, search_bar_xpath)
        search_bar.clear()
        search_bar.send_keys(question)
        search_bar.submit()
        while True:
            try:
                # Check if the flag_button_xpath element is present
                WebDriverWait(driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, flag_button_xpath))
                )
                
                # If the element is present, wait until it disappears
                WebDriverWait(driver, 100).until_not(
                    EC.presence_of_element_located((By.XPATH, flag_button_xpath))
                )
                
            except TimeoutException:
                # If TimeoutException is raised, it means the element is not present,
                # so you can continue with your normal code here
                break
        
        response_xpath = base_response_xpath.format(last_iteration)
        response_element = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, response_xpath))
        )
        
        response_text = response_element.text

        print("\n Response received:\n", response_text ,"\n")
  
        
        filtered_response_text = filter_response(response_element.text)
        with open("TextFiles\\ChatNumeberLamma.txt", "w", encoding="utf-8") as file:
            file.write(filtered_response_text)
            
    except Exception as e:
        print("An error occurred:", e)

def start_lamma_interaction(driver, last_iteration):
    try:
        print("Okay now tell me your name so we can proceed to the conversation")
        while True:
            user_prompt = input("please input the text : ")
            
            if user_prompt.lower() in ["exit", "close", "bye"]:
                print("Okay, goodbye......")
                return

            if len(user_prompt) >= 5:
                interact_with_chat(driver, user_prompt, last_iteration)
                last_iteration += 2
                with open("TextFiles\\ChatNumeberLamma.txt", "w", encoding="utf-8") as file:
                    file.write(str(last_iteration))
            else:
                print("Please enter a longer prompt.")

    except Exception as e:
        print("An error occurred:", e)

def start_lamma():
    try:
        chrome_driver_path = 'Brain\\chromedriver.exe'
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--hide-crash-restore-bubble")
        chrome_options.add_argument("--window-size=1366,768")
        chrome_options.add_argument("user-data-dir=C:\\Users\\srija\\Desktop\\Anna\\localhost\\")  # Path to your custom profile
        chrome_options.add_argument("--remote-debugging-port=6969")
        #chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        #chrome_options.add_argument('--log-level=3')
        driver = webdriver.Chrome(options=chrome_options)
        
        page_url = "https://huggingface.co/chat/"
        driver.get(page_url)
        last_iteration = 2
        with open("TextFiles\\ChatNumeberLamma.txt", "w", encoding="utf-8") as file:
            file.write(str(last_iteration))

        fileopen = open("TextFiles\\ChatNumeberLamma.txt", "r")
        last_iteration = int(fileopen.read())
        fileopen.close()

        start_lamma_interaction(driver, last_iteration)
        
        driver.quit()
    except Exception as e:
        print("An error occurred:", e)
      
start_lamma()