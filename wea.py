import asyncio
import aiohttp
import datetime
from Listen import Listen
import os
import pygame

voice2 = 'en-US-AnaNeural'
def Speak(data):
    #voice = 'en-US-SteffanNeural'
    command = f'edge-tts --voice "{voice2}" --text "{data}" --write-media "Body//Dataspeak//data.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Body//Dataspeak//data.mp3")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

async def fetch_weather(session, city):
    API_KEY = "e34c631e969f0bce0d910fb0599e97f2"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    
    async with session.get(request_url) as response:
        if response.status == 200:
            data = await response.json()
            weather = data['weather'][0]['description']
            temperature = round(data["main"]["temp"] - 273.15, 2)
            sunrise_time = data['sys']['sunrise']
            sunset_time = data['sys']['sunset']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            visibility = data.get('visibility', 'N/A')
            wind_speed = data['wind']['speed']

            Speak(f"Weather is {city}: {weather}")
            Speak(f"Temperature is {city}: {temperature} degree Celsius")
            sunrise_timex = datetime.datetime.fromtimestamp(sunrise_time).strftime('%Y-%m-%d %H:%M:%S AM')
            Speak(f"Sunrise time is {city}: {sunrise_timex}")
            sunset_timex = datetime.datetime.fromtimestamp(sunset_time).strftime('%Y-%m-%d %H:%M:%S PM')
            Speak(f"Sunset time is {city}: {sunset_timex}")
            Speak(f"Humidity is {city}: {humidity}%")
            Speak(f"Pressure is {city}: {pressure} hPa")
            Speak(f"Visibility is {city}: {visibility} meters")
            Speak(f"Wind speed is {city}: {wind_speed} metres per second")
        else:
            Speak(f"Failed to fetch weather data for {city}")

async def main():
    Speak("Please mention the city name:")
    city = Listen()
    if city:
        async with aiohttp.ClientSession() as session:
            await fetch_weather(session, city)
