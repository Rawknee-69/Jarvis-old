import asyncio
import os
import re
from sydney import SydneyClient #pip install sydney-py
import sys

os.environ["BING_U_COOKIE"] = "1bljA1DJvmAFnq-43L62j7aYHhl7CfztNc5cBaiuM4jZu-hvazkCQy2DAX4eyuMfqEhKdAhk3QesKh7I5SdgRNRYZ4c2agBWUlH5K-AckKrCTy9iu1nCEoU1qveEZ6yM2dAR3HYVSL_n9QInMMy1BfUmG1Dc2e3zplgeNEN5NmY-DTQehZpnEVZ6cp6xzqV5h8l92nuUeeaw6aw36cZuPA1WOSIqflUIGuZKJX6sh8sE"

def filter_response(response):
    # Remove markdown formatting characters
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

    # Remove "Searching the web for:" line
    response = response.replace('Searching the web for:', '')

    # Remove backticks
    response = response.replace('`', '')

    return response

#Data = "what is machine learning"
async def brainy() -> None:
    while True:
        async with SydneyClient() as sydney:
            with open("C:\\Users\\srija\\Desktop\\Anna\\TextFiles\\bing_chat.txt", "w", encoding='utf-8') as chat_log:
                    prompt = input("Enter your prompt : ")
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

                    filtered_response_text = filter_response(response_text)

                    print()

                    with open('C:\\Users\\srija\\Desktop\\Anna\\TextFiles\\bingchat.txt', 'w', encoding='utf-8') as f:
                        f.write(filtered_response_text)

asyncio.run(brainy())                    

# Call the brainy function to start the loop