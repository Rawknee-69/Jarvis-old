from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bardapi import BardCookies
import datetime
import re
import warnings
warnings.simplefilter("ignore")

def open_browser():
    chrome_driver_path = 'Brain\\chromedriver.exe'
    url = "https://bard.google.com/"
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--hide-crash-restore-bubble")
    chrome_options.add_argument("--window-size=1366,768")
    chrome_options.add_argument("user-data-dir=C:\\Users\\srija\\Desktop\\Anna\\localhost\\")  # Path to your custom profile
    chrome_options.add_argument("--remote-debugging-port=6969")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    cookies = driver.get_cookies()
    sleep(1)
    with open('cookies\\cookies.txt', 'w') as file:
        file.write (str(cookies))
    #keyboard.press_and_release('ctrl + shift + w')    

open_browser()

def CookieScrapper():
    try:
        # Read the content of cookies.txt and replace single quotes with double quotes
        with open('cookies\\cookies.txt', 'r') as file:
            cookies_data = file.read()

        # Replace single quotes with double quotes
        cookies_data = cookies_data.replace("'", '"')

        # Write the modified data back to cookies.txt
        with open('cookies\\cookies.txt', 'w') as file:
            file.write(cookies_data)

        # Import json and parse the cookies data
        import json
        cookie_data = json.loads(cookies_data)

        # Function to transform cookie data
        def transform_cookie(cookie):
            transformed_cookie = {
                "domain": cookie['domain'],
                "expiry": cookie['expiry'],
                "httpOnly": cookie['httpOnly'],
                "name": cookie['name'],
                "path": cookie['path'],
                "sameSite": "Lax",  # Specify "Lax" for sameSite based on your use case
                "secure": cookie['secure'],
                "value": cookie['value']
            }
            return transformed_cookie

        # Transform the cookie data
        transformed_data = [transform_cookie(cookie) for cookie in cookie_data]

        # Save the transformed data to a text file
        with open('cookiee.txt', 'w') as txt_file:
            txt_file.write(json.dumps(transformed_data, indent=4))

        print("Transformed data saved to 'cookie.txt'")
    except:
        pass


# Read the content of cookies.txt
    with open('cookies\\cookies.txt', 'r') as file:
        cookies_data = file.read()

    # Define the cookie names you want to extract
    cookie_names = ["__Secure-1PSID", "__Secure-1PSIDCC", "__Secure-1PSIDTS"]

    # Initialize a dictionary to store the extracted values
    extracted_cookies = {}

    # Iterate through the cookie names and extract their values
    for cookie_name in cookie_names:
        # Construct a regular expression pattern to match the cookie
        pattern = fr'"name": "{cookie_name}"[^{{]*"value": "([^"]+)"'

        # Search for the pattern in the cookies data
        match = re.search(pattern, cookies_data)

        if match:
            # Extract the value and store it in the dictionary
            value = match.group(1)
            extracted_cookies[cookie_name] = value
        

    # Write the extracted values to a JSON file
    with open('cookies\\cookies.json', 'w') as file:
        json.dump(extracted_cookies, file, indent=4)
  

# Call the function to perform the transformation and save it to a text fi



    with open('cookies\\cookies.json', 'r') as json_file:
        json_data = json.load(json_file)

    SID = "__Secure-1PSID"
    TS = "__Secure-1PSIDTS"
    CC = "__Secure-1PSIDCC"

    SIDValue = json_data.get(SID)
    TSValue = json_data.get(TS)
    CCValue = json_data.get(CC)
    if SIDValue is not None:
        print("1 verification success")
    else:
        print(f"{SID} not found in the JSON data.")

    if TSValue is not None:
        print("2 verification success")
    else:
        print(f"{TS} not found in the JSON data.")

    if CCValue is not None:
        print("3 verification success")
    else:
        print(f"{CC} not found in the JSON data.")

    cookie_dict = {
        "__Secure-1PSID": SIDValue,
        "__Secure-1PSIDTS": TSValue,
        "__Secure-1PSIDCC": CCValue,
    }

    return cookie_dict

cookie_dict = CookieScrapper()

bard = BardCookies(cookie_dict=cookie_dict)

# Text Modification Function -

def split_and_save_paragraphs(data, filename):
    paragraphs = data.split('\n\n')
    with open(filename, 'w') as file:
        file.write(data)
    data = paragraphs[:2]
    separator = ', '
    joined_string = separator.join(data)
    return joined_string

# Main Execution

while True:
    Question = input("Enter The Query : ")
    RealQuestion = str(Question)
    results = bard.get_answer(RealQuestion)['content']
    current_datetime = datetime.datetime.now()
    formatted_time = current_datetime.strftime("%H%M%S")
    filenamedate = str(formatted_time) + str(".txt")
    filenamedate = "Brain\\DataBase\\" + filenamedate
    print(split_and_save_paragraphs(results, filename=filenamedate))