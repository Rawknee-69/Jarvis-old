import datetime
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
import urllib.request  # Import urllib.request

def sanitize_filename(filename):
    # Replace invalid characters with underscores
    return "".join(c if c.isalnum() or c in (' ', '_', '-') else '_' for c in filename)

chrome_driver_path = 'Brain\\chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument("--hide-crash-restore-bubble")
chrome_options.add_argument("--window-size=1366,768")
chrome_options.add_argument("--headless=new")

prompt = input("Enter the prompt: ")
# Sanitize the prompt to remove invalid characters
prompt = sanitize_filename(prompt)
link = f"https://image.pollinations.ai/prompt/{prompt}"
print(link)

print("Generating your image. Please wait for at least 20 seconds. It depends on your internet speed.")

service = Service(chrome_driver_path)

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(link)

current_url = driver.current_url
print(current_url)

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

print(image_pathc)

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
