from time import sleep
import keyboard
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import warnings
warnings.simplefilter("ignore")
import pyperclip
import pyautogui



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

    print("Press 'q' to close and return")
    with open("Anna\\TextFiles\\gen_img_links.txt", 'a') as file:
        file.write(url + '\n')

    while True:
        if keyboard.is_pressed('q'):
            break    
