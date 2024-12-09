import subprocess
import emoji
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import Listen
import sys
sys.path.append("C:\\Users\\srija\\Desktop\\AIJarvisl\\")
from Speak import Speak


def filter_response(response):
    # Your filter response code here
    # For example:
    response = response.replace('[', '').replace(']', '')
    response = re.sub(r'\*{1,3}"', '', response)
    response = re.sub(r'\[[^\]]*\]\(\^[0-9]+\^\)', '', response)
    response = re.sub(r'\^[0-9]+\^', '', response)
    response = response.replace('This content may violate our content policy. If you believe this to be in error, please submit your feedback — your input will aid our research in this area.', '')
    
    # Use emoji.demojize to remove emojis
    response = emoji.demojize(response)
    
    return response

def interact_with_chat(driver, question, last_iteration):
    try:
        search_bar_xpath = '//*[@id="prompt-textarea"]'
        flag_button_xpath = '/html/body/div[1]/div[1]/div[2]/div/main/div[1]/div[1]/div/div/div/div[{}]/div/div/div[2]/div[2]/div/div/button[1]'
        base_response_xpath = "/html/body/div[1]/div[1]/div[2]/div/main/div[1]/div[1]/div/div/div/div[{}]/div/div/div[2]"
        
        search_bar = driver.find_element(By.XPATH, search_bar_xpath)
        search_bar.clear()
        search_bar.send_keys(question)
        search_bar.submit()
        
        while True:
            try:
                WebDriverWait(driver, 100).until(
                    EC.visibility_of_element_located((By.XPATH, flag_button_xpath.format(last_iteration)))
                )
                break
            except TimeoutException:
                pass
        
        response_xpath = base_response_xpath.format(last_iteration)
        response_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, response_xpath))
        )
        
        response_text = response_element.text
        print("Response received:\n", response_text)
        print(response_text)
        Speak(response_text)
        
        filtered_response_text = filter_response(response_element.text)
        with open("wifu//response.txt", "w", encoding="utf-8") as file:
            file.write(filtered_response_text)
            
    except Exception as e:
        print("An error occurred:", e)

def start_waifu_interaction(driver, last_iteration):
    try:
        Speak("OK, I'm ready to listen. Just Speak.")
        Speak("Okay now tell me your name so we can proceed to the conversation")
        while True:
            user_prompt = Listen.MicExecution()
            
            if user_prompt.lower() in ["exit", "close", "bye", "bye baby"]:
                print("Okay, goodbye......")
                return

            if len(user_prompt) >= 3:
                interact_with_chat(driver, user_prompt, last_iteration)
                last_iteration += 2
                with open("wifu//last_iteration.txt", "w", encoding="utf-8") as file:
                    file.write(str(last_iteration))
            else:
                print("Please enter a longer prompt.")

    except Exception as e:
        print("An error occurred:", e)

def start_waifu():
    try:
        chrome_process = subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "--remote-debugging-port=8123"])
        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress", "localhost:8123")
        options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        
        page_url = "https://chat.openai.com/c/f20add2e-73ba-4552-b4a0-6fbd57b3af4f"
        driver.get(page_url)
        
        fileopen = open("wifu//last_iteration.txt", "r")
        last_iteration = int(fileopen.read())
        fileopen.close()
        
        start_waifu_interaction(driver, last_iteration)
        
        driver.quit()
        chrome_process.kill()
    except Exception as e:
        print("An error occurred:", e)
