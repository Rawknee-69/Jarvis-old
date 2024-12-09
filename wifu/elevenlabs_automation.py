import time
import tempfile
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import pyperclip
import re


fileopen = open("wifu\\password.txt","r")
passw = fileopen.read()
fileopen.close()


# Create a temporary profile directory
temp_profile_dir = tempfile.mkdtemp()

# Set Chrome options to use the temporary profile directory
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument(f"user-data-dir={temp_profile_dir}")
#chrome_options.binary_location = r"C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"


    # XPath expressions for the elements
sign_up_xpath = "/html/body/div[3]/div[1]/div/div/div[2]/div[3]/a[2]"
sign_up_xpaths = "/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/form/div[1]/div/input"
sign_up_pass = "/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/form/div[2]/div/input"
sign_up_buttonxx = "/html/body/div[3]/div[2]/div/div/div[2]/div/div[2]/form/div[4]/button"
tempmail_random_email_xpath = '//*[@id="random"]'
copy_mail_xpath = "/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div[2]"
mail_received_xpath = "/html/body/div[1]/main/div[2]/div[1]/div/div/div[1]/div[2]/div"
verify_button_iframe_xpath = "/html/body/div[1]/main/div[2]/div[1]/div/div/div[2]/div[2]/div[3]/iframe"
verify_button_xpath = "/html/body/center/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr/td/a"
after_verify_close_button = "/html/body/div[7]/div[2]/div/div/div[2]/div"
after_verify_email = "/html/body/div[6]/div/div/div/div[2]/div/div/div[2]/div/form/div[2]/input"
after_verify_pass = "/html/body/div[6]/div/div/div/div[2]/div/div/div[2]/div/form/div[3]/input"
after_verify_login = "/html/body/div[6]/div/div/div/div[2]/div/div/div[2]/div/form/div[4]/button"
refresh_mail = "/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div[1]"
profile_pic = "/html/body/div[3]/div[1]/div/div/div[2]/div[3]/div/button/div/div"
api_key = "/html/body/div[6]/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/input"
show_api_key = "/html/body/div[6]/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/button[1]"
copy_api_key_xpath = "/html/body/div[6]/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/input"

driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to the temp-mail website
    driver.get("https://temp-mail.id/")

    time.sleep(500)



    # Click on the element to generate a random email
    tempmail_random_email = driver.find_element(By.XPATH, tempmail_random_email_xpath)
    tempmail_random_email.click()

    # Wait for the 'Copy' button to be clickable and click it
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, copy_mail_xpath))).click()

    time.sleep(1)

    clipboard_text = pyperclip.paste()

    with open('wifu\\email.txt', 'w') as file:
      file.write(clipboard_text)

    fileopen = open("wifu\\email.txt","r")
    email = fileopen.read()
    fileopen.close()  
    
    print(email)


    pyautogui.hotkey('ctrl', 't')

    time.sleep(1)

    original_window_handle = driver.current_window_handle
    for window_handle in driver.window_handles:
        if window_handle != original_window_handle:
            driver.switch_to.window(window_handle)
            break

    driver.get("https://elevenlabs.io/")

    time.sleep(2)

    # Click the sign-up link
    sign_up_xpathx = driver.find_element(By.XPATH, sign_up_xpath)
    sign_up_xpathx.click()

    time.sleep(2)

    sign_up_xpathy = driver.find_element(By.XPATH, sign_up_xpaths)

    # Simulate typing into the input field
    sign_up_xpathy.send_keys(email)

    time.sleep(1)

    sign_up_pas = driver.find_element(By.XPATH, sign_up_pass)

    # Simulate typing into the input field
    sign_up_pas.send_keys(passw)


    sign_up_buttonx = driver.find_element(By.XPATH, sign_up_buttonxx)
    sign_up_buttonx.click()

    time.sleep(5)

    # Simulate pressing Ctrl+Tab

    pyautogui.hotkey('ctrl', 'tab')

    time.sleep(1)


    original_window_handle = driver.current_window_handle
    for window_handle in driver.window_handles:
        if window_handle != original_window_handle:
            driver.switch_to.window(window_handle)
            break



    refresh_now = driver.find_element(By.XPATH, refresh_mail)
    refresh_now.click()


    # Wait for the 'mail_received' element to be clickable and click it
    mail_received_element = WebDriverWait(driver, 300).until(
        EC.element_to_be_clickable((By.XPATH, mail_received_xpath))
    )
    mail_received_element.click()

    driver.execute_script('''
        var footerAds = document.getElementById("BR-Footer-Ads");
        if (footerAds) {
            footerAds.parentNode.removeChild(footerAds);
        }
    ''')
    # Switch to the iframe containing the verify button
    driver.switch_to.frame(driver.find_element(By.XPATH, verify_button_iframe_xpath))

    # Wait for the 'Verify' button to be clickable and click it
    verify_button = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, verify_button_xpath)))
    verify_button.click()
    new_tab_handle = driver.window_handles[-1]
    driver.switch_to.window(new_tab_handle)


    time.sleep(5)



    element = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div[2]/div/div/div[2]/div/div/div[2]/button"))
    )
    element.click()

    #Perform any further actions after clicking the verify button

    after_verify_emailx = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, after_verify_email))
    )
    after_verify_emailx.send_keys(email)

    time.sleep(1)

    after_verify_passc = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, after_verify_pass))
    )
    after_verify_passc.send_keys(passw)

    
    time.sleep(1)

    after_verify_loginc = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, after_verify_login))
    )
    after_verify_loginc.click()

    time.sleep(1)

    profile_picx = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, profile_pic))
    )
    profile_picx.click()

    time.sleep(1)


    api_keyx = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a.flex.items-center.gap-3.text-gray-700.block.px-4.py-2.text-sm"))
    )
    api_keyx.click()

    time.sleep(1)

    show_api_keyc = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, show_api_key))
    )
    show_api_keyc.click()

    copy_api_key_xpathx = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, copy_api_key_xpath))
    )
    copy_api_key_xpathx.click()

    # Set the position where you want to perform the double click
    x, y = 603, 340  # Replace with the coordinates you need

    # Simulate the first left-click
    pyautogui.click(x, y, clicks=1)

    # Add a small delay between the clicks (adjust as needed)
    time.sleep(0.1)  # You can adjust this delay

    # Simulate the second left-click
    pyautogui.click(x, y, clicks=1)



    pyautogui.hotkey('ctrl','a')
    pyautogui.hotkey('ctrl','c')

    clipboard_text_api = pyperclip.paste()

    with open('wifu\\api.txt', 'w') as file:
      file.write(clipboard_text_api)

    # Read the content from api.txt
    with open('wifu\\api.txt', 'r') as file:
        content = file.read()

    # Define the regular expression pattern to find the API Key
    pattern = r"API Key \(see documentation\)\s*\n\n(.*?)\n\n"

    # Find the API Key using the regular expression
    api_key_match = re.search(pattern, content, re.DOTALL)

    if api_key_match:
        api_keys = api_key_match.group(1).strip()
        
        # Write the extracted API Key to api_use.txt
        with open('wifu\\api_use.txt', 'w') as file:
            file.write(api_keys)
    
except Exception as e:
    print("Error:", e)

# Wait for demonstration purposes

# Close the Chrome instance
driver.quit()

# Delete the temporary profile directory after use
shutil.rmtree(temp_profile_dir)
