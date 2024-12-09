from time import sleep
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import Listen
from selenium.webdriver.common.by import By

# Set the base response xpath (with [18]) and the xpath for the send button
base_response_xpath = "/html/body/div[1]/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[{}]/div/div[2]"
send_button_xpath = "/html/body/div[1]/div[1]/div[2]/div/main/div[2]/form/div/div[2]/button/span/svg/path"
search_bar_xpath = '//*[@id="prompt-textarea"]'
# flag_button_xpath = '/html/body/div[1]/div[1]/div[2]/div/main/div/div[1]/div/div/div/div[{}]/div/div[2]/div[2]/div/div/button[1]/svg'

# Set the URL of the page you're working with
page_url = "https://chat.openai.com/c/f20add2e-73ba-4552-b4a0-6fbd57b3af4f"  # Replace with the actual URL

chrome_process = subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "--remote-debugging-port=8123"])
# Initialize Brave browser
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "localhost:8123")
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Adjust the path accordingly
# Initialize Chrome webdriver using the PATH environment variable
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Navigate to the desired page
driver.get(page_url)
fileopen = open("last_iteration.txt", "r")
It = fileopen.read()
fileopen.close()
print(It)
last_iteration = int(It)  # Starting iteration
            
def interact_with_chat(question):
    global last_iteration
    search_bar = driver.find_element(By.XPATH, search_bar_xpath)
    search_bar.clear()
    search_bar.send_keys(question)
    search_bar.submit()
    sleep(1)  # Wait for a delay of 3 seconds
    response_xpath = base_response_xpath.format(last_iteration)
    response_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, response_xpath))
    )
    sleep(10)
    response_text = response_element.text
    print("Response received:\n", response_text)
    # Save the response to a text file
    filtered_response_text = filter_response(response_element.text)
    with open("response.txt", "w", encoding="utf-8") as file:
        file.write(filtered_response_text)

def filter_response(response):
    # Remove markdown formatting characters
    response = re.sub(r'\*{1,3}"', '', response)
    response = re.sub(r'\[[^\]]*\]\(\^[0-9]+\^\)', '', response)
    response = re.sub(r'\^[0-9]+\^', '', response)
    response = response.replace('[', '').replace(']', '')
    response = response.replace('This content may violate our content policy. If you believe this to be in error, please submit your feedback — your input will aid our research in this area.','')

    # Remove emojis
    emoji_pattern = re.compile("["
                               u"\U0001F300-\U0001F9FF"  # symbols & pictographs
                               u"\U0001FA00-\U0001FA6F"  # symbols - additional
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    response = emoji_pattern.sub(r'', response)

    return response

def start():
    global last_iteration
    while True:
        try:
            while True:
                #user_prompt = Listen.MicExecution()
                user_prompt = input("enter : ")
                print("")
                if user_prompt.lower() in ["exit", "close", "bye", "bye baby"]:
                    print("Okay, goodbye......")
                    chrome_process.kill()
                    driver.quit()  # Close the Chrome browser
                    return

                if len(user_prompt) >= 5:
                    break
                else:
                    print("")

            # Clear the response file for each new iteration
            with open("response.txt", "w", encoding="utf-8"):
                pass

            # Send the user's prompt using the function
            interact_with_chat(user_prompt)

            # Wait for the full response to be generated
            WebDriverWait(driver, 300).until(
                EC.presence_of_element_located((By.XPATH, base_response_xpath.format(last_iteration)))
            )

            # Increment the iteration for the next prompt
            last_iteration += 2

            # Store the last iteration in a text file
            with open("last_iteration.txt", "w", encoding="utf-8") as file:
                file.write(str(last_iteration))
        except Exception as e:
            print("An error occurred:", e)

start()
