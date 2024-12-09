import os
import re
from sydney import SydneyClient
import pyttsx3
import sys

import asyncio

os.environ["BING_U_COOKIE"] = "16g2-ovlcO8vCSNLi8eqgFE9ULqzxdQGhdHshHnk8KRS33JBU4awel6eSUi1Lr1PaNaC8qZh_0aoU9AGbYRNrrZ0WtvUTafBgBlAAX6Hl9CSe63Lw4a_1adbXdC1TzWrTi3akGG0b8DhkitTI772qUDyK7uxnP4ObHH9DTiAk2AteeMpPp3hQ8-WruXchXZqu418bhRc3qPh8HxfCzFoLAYq9P9_2NiK17W8AC6_tgzs"

def filter_response(response):
    # Remove markdown formatting characters
    response = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', response)
    response = re.sub(r'\*{1,3}"', '', response)
    response = re.sub(r'\[[^\]]*\]\(\^[0-9]+\^\)', '', response)
    response = re.sub(r'\^[0-9]+\^', '', response)
    response = response.replace('[', '').replace(']', '')

    # Remove emojis
    emoji_pattern = re.compile("["
        u"\U0001F300-\U0001F9FF"  # symbols & pictographs
        u"\U0001FA00-\U0001FA6F"  # symbols - additional
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "]+", flags=re.UNICODE)
    response = emoji_pattern.sub(r'', response)
    
    # Remove specific text
    response = response.replace('Searching the web for:', '')
    response = response.replace(',', '')
    response = re.sub(r'\[\^[0-9]+\^\]', '', response)
    response = response.replace('**', '')

    return response

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # You can adjust the speaking rate (words per minute) as needed
    engine.say(text)
    engine.runAndWait()

def split_and_save_paragraphs(data, filename):
    paragraphs = data.split('\n\n')
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)
    data = paragraphs[:2]
    separator = ', '
    joined_string = separator.join(data)
    return joined_string

async def brainy(Data) -> None:
    async with SydneyClient() as sydney:
        with open("DataBase\\chat_log.txt", "a", encoding='utf-8') as chat_log:
                prompt = Data
                chat_log.write(f"You: {prompt}\n")
                chat_log.flush()

                if prompt == "reset and make it creative":
                    await sydney.reset_conversation(style="creative")
                elif prompt == "reset and make it precise":
                    await sydney.reset_conversation(style="precise")
                elif prompt == "reset and make it balanced":
                    await sydney.reset_conversation(style="balanced")
                elif prompt == "Exit":
                    sys.exit()

                print("Jarvis: ", end="", flush=True)
                response_text = ''
                async for response in sydney.ask_stream(prompt):
                    print(response, end="", flush=True)
                    chat_log.write(f"Jarvis: {response}\n")
                    chat_log.flush()
                    response_text += response
                print("\n")
                
                paragraphs = response_text.split('\n\n')
                filtered_paragraphs = [p for p in paragraphs if not p.strip().startswith("For more information")]

                # Reconstruct the filtered response
                filtered_response_text = '\n'.join(filtered_paragraphs)

                # Use the filter_response function to further clean the text
                filtered_response_text = filter_response(filtered_response_text)

                with open('speaking.txt', 'w', encoding='utf-8') as f:
                    f.write(filtered_response_text)

                if filtered_response_text:
                    # Speak the text using the pyttsx3 engine
                    speak_text(filtered_response_text)

                # Save the first two paragraphs to a separate file
                split_and_save_paragraphs(response_text, 'first_two_paragraphs.txt')


