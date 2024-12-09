import os
import pygame
import string
import textwrap
import subprocess
import time

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

def speak_segment(segment, segment_number):
    audio_file_name = f"Body//Dataspeak//data{segment_number}.mp3"
    command = f'edge-tts --voice "{voice2}" --text "{segment}" --write-media "{audio_file_name}"'
    
    subprocess.run(command, shell=True, check=True)

def Speak(data):
    filtered_data = filter_text(data)

    pygame.init()
    pygame.mixer.init()

    # Create the initial 'data.mp3' file
    initial_audio_file = f"Body//Dataspeak//data.mp3"
    command = f'edge-tts --voice "{voice2}" --text "{filtered_data}" --write-media "{initial_audio_file}"'
    subprocess.run(command, shell=True, check=True)

    pygame.mixer.music.load(initial_audio_file)
    pygame.mixer.music.play()

    # Wait for the initial audio playback to finish
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    # Delete the initial audio file
    os.remove(initial_audio_file)

    # Play subsequent audio segments one after the other
    segment_number = 1
    while True:
        # Generate the next segment while the previous one is playing
        next_segment = filtered_data[segment_number * 250:(segment_number + 1) * 250]
        if next_segment:
            speak_segment(next_segment, segment_number)
        
            # Wait for the next segment to finish playing
            audio_file_name = f"Body//Dataspeak//data{segment_number}.mp3"
            pygame.mixer.music.load(audio_file_name)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(0.1)

            # Delete the audio file after playback
            os.remove(audio_file_name)

            segment_number += 1
        else:
            break




# Example usage:
fileopen = open("test.txt","r")
test = fileopen.read()
fileopen.close()
# Example usage:


