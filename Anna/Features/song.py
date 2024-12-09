import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from extract_the_link import searchsong
import warnings
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
warnings.simplefilter("ignore")

print("now enter the name of the song you were dying to listen for")
searchsong()

fileopen = open("Anna\\cookies\\song_link.txt","r")
song_links = fileopen.read()
fileopen.close()
print (song_links)

def playsong():
    try:

        Link = song_links
        chrome_options = Options()
        subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "--remote-debugging-port=6969"])
        options = webdriver.ChromeOptions()
        #chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument('--log-level=3')
        options.add_experimental_option("debuggerAddress", "localhost:6969")
        driver = webdriver.Chrome(options=options)
        driver.get(Link)
        print("please wait patiently the song playback will be done as fast as your internet connection")
        element = WebDriverWait(driver, 100).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[5]/button"))
        )
        element.click()
    except Exception as e:
        print("Check your internet connection",e )    



playsong()    