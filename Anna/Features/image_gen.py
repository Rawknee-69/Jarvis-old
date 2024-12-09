import datetime
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
import urllib.request  # Import urllib.request
import speech_recognition as sr 
from googletrans import Translator
import os
import pygame
import string

voice2 = 'en-US-AnaNeural'

def filter_text(data):
    # Remove emojis
    data = data.encode('ascii', 'ignore').decode('utf-8')
    
    # Remove punctuation except comma and full stop
    allowed_punctuations = string.punctuation.replace('.', '').replace(',', '')
    data = ''.join(char for char in data if char not in allowed_punctuations)
    
    # Remove question marks and brackets
    data = data.replace('?', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '')

    return data.strip()

def Speak(data):
    filtered_data = filter_text(data)
    command = f'edge-tts --voice "{voice2}" --text "{filtered_data}" --write-media "Body//Dataspeak//data.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Body//Dataspeak//data.mp3")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Increased ticks per second for smoother playback

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,15) # Listening Mode.....
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="hi")

    except:
        return ""
    
    query = str(query).lower()
    return query

# 2 - Translation

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You : {data}.")
    return data

# 3 - Connect

def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data

def sanitize_filename(filename):
    # Replace invalid characters with underscores
    return "".join(c if c.isalnum() or c in (' ', '_', '-') else '_' for c in filename)
def image():
    chrome_driver_path = 'C:\\Users\\srija\\Desktop\\AIJarvisl\\Anna\\Brain\\chromedriver.exe'
    chrome_options = Options()
    chrome_options.add_argument("--hide-crash-restore-bubble")
    chrome_options.add_argument("--window-size=1366,768")
    #chrome_options.add_argument("--headless=new")
    Speak("Rule!!! : You will only have 10 seconds to ask your question:  ")
    Speak("Say what you want to make: ")
    prompt = input("enter: ")
    # Sanitize the prompt to remove invalid characters
    prompt = sanitize_filename(prompt)
    link = f"https://image.pollinations.ai/prompt/{prompt}"


    print("Generating your image. Please wait for at least 20 seconds. It depends on your internet speed.")

    service = Service(chrome_driver_path)

    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(link)

    current_url = driver.current_url
    
    # Close the Chrome driver
    driver.quit()

    # Define a folder where you want to save the image
    folder_path = "generatedimages"

    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    time_stamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"image_{prompt[:5]}_{time_stamp}.jpg"  # File name without folder path

    # Download the image using urllib and save it with the generated filename
    urllib.request.urlretrieve(current_url, os.path.join(folder_path, filename))
    full_file_path = os.path.abspath(os.path.join(folder_path, filename))  # Get the full file path

    # Replace forward slashes with double backslashes using a regular expression
    formatted_file_path_crop = full_file_path
    image_pathc = formatted_file_path_crop.replace("\\", "\\\\")

    output_folder = "generatedimages\\"  # Replace with your desired folder

    # Create the folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    filename = os.path.basename(formatted_file_path_crop)
    output_path = os.path.join(output_folder, filename)

    

    # Open the image file
    original_image = Image.open(formatted_file_path_crop)

    # Get the dimensions of the original image
    width, height = original_image.size

    # Define how much you want to crop from the bottom (in pixels)
    crop_height = 42  # Adjust this value as needed

    # Crop the image from the bottom
    cropped_image = original_image.crop((0, 0, width, height - crop_height))

    # Save or display the cropped image
    cropped_image.save(output_path)
    cropped_image.show()
