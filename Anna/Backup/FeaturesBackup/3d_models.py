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
from load_model import laod_3Dmodels
import pygetwindow as gw


def models():
    agreement_checkbox_xpath ='//*[@id="tos"]'
    dismiss_this_message = '//*[@id="dismiss"]'
    confirm_button_xpath = "/html/body/div[3]/div[2]/div[2]/button"
    get_started_confirm = "/html/body/div[4]/div[2]/div[3]/div/button" 
    prompt_field = "/html/body/div[1]/div/div[2]/form/div[2]/div[1]/textarea"
    generate_button_xpath = "/html/body/div[1]/div/div[2]/form/div[2]/div[2]/div[2]/button[2]"
    embed_code_copy = '/html/body/div[1]/div/div[2]/form/div[1]/div[2]/button[2]'
    checkpost = "/html/body/div[1]/div/div[2]/div/div"
    # Ignore unnecessary warnings
    

    try:
        # Define the URL
        url = "https://skybox.blockadelabs.com/"

        # Set up Chrome options
        chrome_driver_path = 'C:\\Users\\srija\\Desktop\\Anna\\Brain\\chromedriver.exe'
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        chrome_options = Options()
        chrome_options.add_argument(f"user-agent={user_agent}")
        #chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--hide-crash-restore-bubble")
        chrome_options.add_argument("--allow-clipboard")
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.maximize_window()
        driver.minimize_window()
        driver.get(url)
        window = gw.getWindowsWithTitle('Blockade Labs Skybox - AI-Generated 3D Worlds')[0]
        window.hide()

        sleep(3)

        driver.find_element(By.XPATH, agreement_checkbox_xpath).click()
        driver.find_element(By.XPATH, dismiss_this_message).click()
        driver.find_element(By.XPATH, confirm_button_xpath).click()
        sleep(2)
        driver.find_element(By.XPATH, dismiss_this_message).click()
        driver.find_element(By.XPATH, get_started_confirm).click()
        sleep(0.3)
        driver.find_element(By.XPATH,prompt_field).click()
        sleep(0.1)
        driver.find_element(By.XPATH, dismiss_this_message).click()
        driver.find_element(By.XPATH, get_started_confirm).click()
        sleep(0.001)
        prompt = input ("Enter The WOrlD YOu IMagInE : ")
        sleep(0.1)
        driver.find_element(By.XPATH, prompt_field).send_keys(prompt)
        sleep(0.01)
        driver.find_element(By.XPATH, generate_button_xpath).click()
        print (f"\n Generating your image please be paitent.\n")
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
                    
        print("All most there")

        driver.find_element(By.XPATH, embed_code_copy).click()
        sleep(1)
        print("presenting it ....")



        laod_3Dmodels()


    except Exception as e:
        print(e)    
models()        #it requires some time in genertaing it

# so this was it 