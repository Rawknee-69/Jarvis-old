import asyncio
import datetime
import sys
import time
import pywhatkit
from Brain.braininuse import brainy
from Listen import MicExecution
from Speak import Speak
from Features.myalarm import alarm
from Main import MainTasksExecution
import pyautogui
import webbrowser
import instaloader
import os
import wikipedia as googlescrap
from Whatsapp import main_wp
from ramusage import rescourceusage
from translator.trans import maintranslation
from wea import main
from sketch.sketchconv import sketch
from volumecontrols.volume import volumeup , volumedown
import random
import csv
from nltk.sentiment import SentimentIntensityAnalyzer
from calculate.calculator import Calc
import subprocess
from wifu.school_pro import start_school
from wifu.waifu import start_waifu
from wifu.teaching import start_teaching
from wifu.health import start_health
from wifu.dep import start_dep
from wifu.astrology import start_astro
from wifu.emailandcontent import start_ema
import pyttsx3
from Anna.Features.image_gen import image
from Anna.Features.c3d_models import models
from Anna.Features.Gita import startgpt
from Anna.Features.pdf_maker import pdf_madx
from Anna.Brain.pi_ai import stam

try:
    Speak(" Starting The Jarvis Wait For Some Time.....")
    Speak("checking the system for errors . no error found starting the jarvis shortly")
        


    def MainExecution():


        Speak("let me introduce myself first ")
        Speak("I am Jarvis, Iam your personal A i assistant . how may i help you")

    
        while True:

            Data = MicExecution()
            Data = str(Data)
            ValueReturn = MainTasksExecution(Data)
            print(Data)
            if ValueReturn == True:
                pass
            
            if len(Data)<3:
                pass

            if "introduce yourself" in Data or "Introduce yourself" in Data or "Intro" in Data or "intro" in Data:
                Speak("changing the voice ")
                try:

                    def speaki(text):
                        # Initialize the pyttsx3 engine
                        engine = pyttsx3.init()

                        # Set the speech rate to 180 (words per minute)
                        engine.setProperty('rate', 180)

                        # Speak the provided text with default pitch and the adjusted rate
                        engine.say(text)
                        engine.runAndWait()

                    # Example usage
                    fileopen = open("introduction\\introtext.txt", "r")
                    intro = fileopen.read()
                    fileopen.close()

                    speaki(intro)

                except Exception as e:
                    print(e)    

            
            if "something about srijan" in Data or "something about sri" in Data:
                Speak("Srijan, my creator, has demonstrated remarkable dedication in crafting my AI capabilities despite limited resources. Despite being a high school student in the 11th grade, his passion for technology led him to tirelessly develop my functionalities. While his appearance may not be extraordinary, Srijan's commitment shines through his diligent efforts. Nights were spent refining and debugging, showcasing his determination and expertise. Notably, Srijan achieved this without external funding, highlighting his resourcefulness. His choice of an anime character's voice adds a distinctive touch to our interactions. In conclusion, Srijan's journey underscores his passion, innovation, and resilience. His accomplishments at a young age exemplify the power of dedication and creativity.")

            elif "Generate images" in Data or "Generate Images" in Data or "generate images"in Data or "Generate image"in Data or "generated image" in Data or "Generate image"in Data: 
                Speak("Okay sir ! we'll we are in process to generate images for you: ")
                try:
                    image()
                except:
                    Speak("An unknown Error occured! wait a moment while we are fixing it")        
                
            # elif "live generations" in Data or "360 degree generations" in Data or "Live Generations"in Data or "Live Generations"in Data or "Live Generation"in Data or "Live generation"in Data or "Life Generation" in Data or "surround view"in Data or "Surround View" in Data or "live generation" in Data: 
            #     Speak("Okay sir ! we'll we are in process to generate 360 degreee live images for you: ")
            #     try:
            #         models()
            #     except:
            #         Speak("An unknown Error occured! wait a moment while we are fixing it")  

            elif "Gita" in Data or "gita" in Data or "Bhagwad Gita"in Data or "Bhagwad gita"in Data or "Geeta" in Data or "geeta"in Data: 
                Speak("Okay sir ! we'll we are turning the pages of the holy Gita for you : ")
                try:
                    startgpt()
                except:
                    Speak("An unknown Error occured! wait a moment while we are fixing it") 

            elif "pdf" in Data or "Pdf" in Data or "Pdf Maker"in Data or "Pdf maker"in Data or "pf" in Data or "Pf" in Data: 
                Speak("Okay sir ! we'll we are preparing to brew the freshly brewed pdf for you : ")
                try:
                    pdf_madx()
                except:
                    Speak("An unknown Error occured! wait a moment while we are fixing it")  

            # elif "chat" in Data or "Chat" in Data or "Pie"in Data or "pie"in Data or "pi" in Data or "Pi" in Data or "anna" in Data or "Anna" in Data or "anna" in Data: 
            #     Speak("Okay sir ! on the way: ")
            #     try:
            #         stam()
            #     except:
            #         Speak("An unknown Error occured! wait a moment while we are fixing it")        
    

            elif "Time" in Data or "time" in Data or "time now"in Data or "what's the time now"in Data:
                strTime = datetime.datetime.now().strftime("%H:%M")    
                Speak(f"Sir, the time is {strTime}")    
            
            elif "In which school do i study" in Data:
                Speak("You study in  : rajkamal saraswati vidya mandir")  
        
            elif "something about you" in Data or "about you" in Data or  "your background story" in Data or "about" in Data or "can i know something about you" in Data : 
                Speak("I am an AI model developed by Srijan Raj, capable of performing a wide array of tasks. I excel in engaging conversations, proficiently recognizing Hindi words, and assisting with information searches. Moreover, I possess the capability to discern emotions, enabling me to provide empathetic interactions. I can greatly assist with your daily tasks, including drafting emails, composing essays, and much more. My multifaceted abilities are designed to enhance and streamline your everyday experiences.")
                #sleep(9)
            elif "who created you" in Data or "name of your creator" in Data or  "creator" in Data or "who designed you" in Data or "whom do you think as your creator" in Data or "who is your father" in Data or "name of the person who created you" in Data or "who designed you" in Data : 
                Speak("Srijan, my creator, has demonstrated remarkable dedication in crafting my AI capabilities despite limited resources. Despite being a high school student in the 11th grade, his passion for technology led him to tirelessly develop my functionalities. While his appearance may not be extraordinary, Srijan's commitment shines through his diligent efforts. Nights were spent refining and debugging, showcasing his determination and expertise. Notably, Srijan achieved this without external funding, highlighting his resourcefulness. His choice of an anime character's voice adds a distinctive touch to our interactions. In conclusion, Srijan's journey underscores his passion, innovation, and resilience. His accomplishments at a young age exemplify the power of dedication and creativity.")
            
            elif "Jarvis tell me" in Data or "Tell me" in Data or "tell me" in Data or "Question" in Data or "Answer" in Data or "Jarvis what is" in Data or "What" in Data or "what" in Data or "I want to know" in Data or "Jarvis i need your help" in Data or "how" in Data or "How" in Data or "who" in Data or "Who" in Data:   
                try:
                    asyncio.run(brainy(Data))
                except:
                    pass    

            
            elif "capability"in Data or "capabilites"in Data or "name some of the things you can do" in Data or "things you can do" in Data or "Things you can do" in Data or "your specialities" in Data or "your features" in Data or "tasks that you can do" in Data or"your functionalities" in Data:
                Speak("This innovation offers an array of capabilities, including conversational engagement, multilingual recognition, information retrieval, emotional understanding, task assistance, and skilled writing. Its versatility simplifies tasks, improves interactions, and aids communication.")
            
            elif "instagram profile" in  Data or "profile on instagram" in Data:
                    Speak("sir please enter the user name correctly.")
                    name = input("Enter username here:")
                    webbrowser.open(f"www.instagram.com/{name}")
                    Speak(f"Sir here is the profile of the user {name}")
                    time.sleep(5)
                    Speak("sir would you like to download profile picture of this account.")
                    condition = MicExecution()
                    try:
                        if "you can" in condition:
                            mod = instaloader.Instaloader() #pip install instadownloader
                            mod.download_profile(name, profile_pic_only=True)
                            Speak("i am done sir, profile picture is saved in our main folder. now i am ready for next command")
                        else:
                          Speak("okay sir i won't")
                    except :
                        pass    
        

            elif "take a screenshot" in Data or "screenshot" in Data or "screenshot lelo" in Data or "bhai iska screenshot lelo" in Data:

                                    # Get the current date and time
                now = datetime.datetime.now()                    
                filename = f'screenshot-{now:%Y-%m-%d-%H-%M-%S}.png'
                screenshot_path = 'screenshot'
                # Take the screenshot and save it to a file
                screenshot = pyautogui.screenshot()
                screenshot.save(os.path.expanduser(f'screenshot/{filename}'))

                # Convert the screenshot to bytes and save to clipboard
                pyautogui.keyDown('printscreen')
                pyautogui.keyUp('printscreen')

                Speak("Do you want to open the screenshot in Windows Photos? (yes/no): ")
                open_in_photos = MicExecution()

                if open_in_photos.lower() == "Yes" or "yes":
                    try:
                        subprocess.Popen(['explorer', screenshot_path], shell=True)
                    except Exception as e:
                        print(f"Error opening screenshot in Windows Photos: {e}")
                Speak ( " screenshot is taken and saved in screenshot folder and also saved in clipboard.")

            # elif "Wikipedia" in Data or "Search in Wikipedia" in Data or "wikipedia"in Data:
            #         try:
            #             Speak("what should i search on wikipedia sir...")
            #             cd = MicExecution()
            #             Speak("searching wikipedia....")
            #             cd = cd.replace("wikipedia","")
            #             results = wikipedia.summary(cd, sentences=2)
            #             Speak("according to wikipedia")
            #             Speak(results) 
            #         except:
            #             Speak("try again sir i cant understand it.")     

            # elif "Open Google" in Data or "open google" in Data:
            #         try:
            #             Speak("sir, what should i search on google")
            #             cm = MicExecution()()
            #             webbrowser.open(f"{cm}")
            #         except:
            #             Speak("try saying it again i was not able to understand it.")



            elif 'switch the window' in Data or "Switch window" in Data or  "switch window" in Data:
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(1)
                    pyautogui.keyUp("alt")  

            # Logout / Shutdown / Restart
            elif "Logout" in Data or "logout" in Data:
                Speak('logging out in 10 seconds')
                time.sleep(10)
                os.system("shutdown - l")

            elif "Shutdown" in Data or "shutdown" in Data:
                Speak('shutting down in 2 minutes please laeve the system and quit all the work ')
                time.sleep(120)
                os.system("shutdown /s /t 1")

            elif "Restart" in Data or "restart" in Data:
                Speak('initiating restart in 10 seconds')
                time.sleep(10)
                os.system("shutdown /r /t 1")    

            elif "hidden menu" in Data:
                # Win+X: Open the hidden menu
                pyautogui.hotkey('winleft', 'x')

            elif "task manager" in Data or "tax" in Data:
                # Ctrl+Shift+Esc: Open the Task Manager
                pyautogui.hotkey('ctrl', 'shift', 'esc')

            elif "task view" in Data or "tax view"in Data:
                # Win+Tab: Open the Task view
                pyautogui.hotkey('winleft', 'tab')  

            elif "close the app" in Data or "close this window" in Data:
                pyautogui.hotkey('alt', 'f4')          
            
            

            elif "ram usage" in Data or "system memory usage" in Data or "disk usage" in Data or "Ram usage" in Data:
                try:
                    rescourceusage()  
                except :
                    Speak("sorry sir we ran into some problem just working on fixing them.")    
            elif 'alarm' in Data:
                Speak("Sir please tell me the time to set an alarm")
                Speak("you have to say me like for example : set alarm to 5:30 am")
                tt = MicExecution()
                tt = tt.replace ("set alarm to ", "")
                tt = tt.replace(".", "")
                tt = tt.upper()
                
                alarm(tt)
            
            elif "Google search"in Data or "jarvis search on google "in Data:
                
                Data = Data.replace("jarvis ", "")
                Data = Data.replace("google search ", "")
                Data = Data.replace("google ", "")
                Data = Data.replace("search on google ", "")
                Speak ("This is what i found for you sir on the web")
                pywhatkit.search(Data)

                
                try:
                    result = googlescrap.summary(Data,3)
                    Speak(result)

                except:
                    Speak("NOthing to say") 
                        

            if "can you search the weather now" in Data or "find the weather now" in Data or "weather"in Data:
                Speak(" okay sir we are in process ")
                asyncio.run(main()) 

            if "sketch now"in Data or "sketch"in Data:
                Speak(" okay sir we are in process ")
                sketch()

            if "translation"in Data or "translate"in Data or"translate"in Data:
                Speak("okay sir going for it ")
                maintranslation()

            if "exit jarvis"in Data:
                sys.exit()  
        
            elif "Pause" in Data or "pause" in Data:
                pyautogui.press("k")
                Speak("video paused")
            elif "Play" in Data or "play" in Data:
                pyautogui.press("k")
                Speak("video played")
            elif "Mute" in Data or "mute" in Data:
                pyautogui.press("m")
                Speak("video muted")

            elif "Volume up" in Data or "volume up" in Data:
                Speak("Turning the volume up")
                volumeup()
            elif "Volume down" in Data or "volume down" in Data:
                Speak("Turning the volume down")
                volumedown()      

            elif "calculate" in Data:
                try:
            
                    Data = Data.replace("calculate","")
                    Data = Data.replace("jarvis","")
                    Calc(Data)   
                except:
                    Speak("an error occured")       

            # elif "Story" in Data or "story" in Data or "stories" in Data or "say me some stories" in Data:
                
            #      generate_story()

            elif "I want to watch anime" in Data or "anime" in Data or "Anime" in Data:
                links = ["https://aniwatch.to/home"]

                for link in links:
                    webbrowser.open(link)

            elif "I want to check snapchat" in Data or "Snapchat" in Data or "snapchat" in Data:
                links = ["https://web.snapchat.com/"]

                for link in links:
                    webbrowser.open(link)

            elif "I want to check instagram" in Data or "Instagram" in Data or "instagram" in Data:
                links = ["https://instagram.com/"]

                for link in links:
                    webbrowser.open(link)


            elif "I want to check whatsapp" in Data or "Whatsapp" in Data or "whatsapp" in Data:
                links = ["https://web.whatsapp.com/"]

                for link in links:
                    webbrowser.open(link)


            elif "I want to check Telegram" in Data or "Telegram" in Data or "telegram" in Data:
                links = ["https://web.telegram.org/"]

                for link in links:
                    webbrowser.open(link)

            elif "I want help from chatgpt" in Data or "Chatgpt" in Data or "chatgpt" in Data:
                links = ["https://chat.openai.com/"]

                for link in links:
                    webbrowser.open(link)

            elif "screen record"in Data or "record screen" in Data:
                from screenrecorder.screenrecordern import screenrec
                Speak("okay recording in progress press q to stop recording")
                screenrec()

            if "Voice typing" in Data or "voicetype" in Data or "voicetyping" in Data or "handsfree typing" in Data or "voice typing" in Data or "voice type" in Data:
                from Automations.voicetyping import vc
                vc()  

            elif "assistant"in Data or "personal assitant"in Data or "Rem" in Data or "rem" in Data or "Assistant"in Data:
                Speak("Hello sir this is rem here for you wait just setting things for you")
                start_school()

            elif "wife" in Data or "waifu" in Data or "shoko" in Data or "ShokoNishimiya" in Data:
                Speak("yesss, Srii i will be right there in few moments")
                start_waifu()   

            elif "teach" in Data or "Teach" in Data or "Teach me" in Data or "Tsunade" in Data or "Sunade" in Data or "Teacher"in Data or "teacher"in Data:
                Speak("yesss, sir i will be right there to teach you in few moments")
                start_teaching() 

            elif "health" in Data or "Health" in Data or "Diagnose my health" in Data or "Healthy" in Data or "diagnose my health" in Data:
                Speak("yesss, Sir i will be right there to diagnose your health in few moments")
                start_health()    
                
            elif "Depression" in Data or "depression" in Data or "Treat my mental state" in Data or "Treat me" in Data or "Mental health" in Data:
                Speak("yesss, Sir i will be right there to make you feel better in few moments")
                start_dep()
                
            elif "astrology" in Data or "Astrology" in Data or "astro" in Data or "predict my future " in Data or "Astro" in Data:     
                 Speak("yesss, Sir i will be right there to tell you how your stars are upon you")
                 start_astro()   
                 

            elif "Send a message" in Data or "send a message" in Data or "message now" in Data or "send message"in Data or "Send Message"in Data or "Send an Message"in Data or "send an Message"in Data:     
                 main_wp() 

            elif "Write a email" in Data or "write email" in Data or "Email" in Data or "write an email" in Data or "Write an email" in Data or "email" in Data or "E-Mail" in Data or "E-mail" in Data:
                 start_ema()



            elif "i want you now"in Data or "please come to me i need you" in Data:
                class MoodAssistant:
                    def __init__(self):
                        self.sia = SentimentIntensityAnalyzer()
                        self.responses = self.load_responses()

                    def load_responses(self):
                        responses = {
                            'happy': [],
                            'sad': [],
                            'neutral': [],
                        }
                        with open('Data\\datares.csv', 'r', newline='', encoding='utf-8') as file:
                            csv_reader = csv.reader(file)
                            for row in csv_reader:
                                mood = row[0]
                                response = row[1]
                                if mood in responses:
                                    responses[mood].append(response)
                        return responses

                    def determine_mood(self, text):
                        sentiment_score = self.sia.polarity_scores(text)['compound']
                        if sentiment_score > 0.1:
                            return 'happy'
                        elif sentiment_score < -0.1:
                            return 'sad'
                        else:
                            return 'neutral'

                    def respond_to_input(self, user_input):
                        mood = self.determine_mood(user_input)
                        response = random.choice(self.responses[mood])
                        return response

                def senti():
                    mood_assistant = MoodAssistant()
                    
                    print("Mood Assistant: Hi there! How are you feeling today?")
                    
                    while True:

                            print("You: ")
                            user_input = MicExecution()
                            if user_input.lower() in ["thank you u can go now", "i am okay now"]:
                                print("Mood Assistant: Take care!")
                                break
                            
                            response = mood_assistant.respond_to_input(user_input)
                            print("Mood Assistant:")
                            Speak(response)
                    senti()

    def ClapDetect():
            

        Data = MicExecution()
        if "start jarvis" in Data or "i am here" in Data:
            print("")
            Speak("welcome sir...")
    
        
        hour = int(datetime.datetime.now().hour)
        tt = time.strftime("%I:%M %p")

        if hour >= 0 and hour <= 12:
            Speak(f"good morning, its {tt}")
            Speak("i am online and ready sir ")
        elif hour >= 12 and hour <= 18:
            Speak(f"good afternoon, its {tt}")
            Speak("i am online and ready sir ")
        elif hour >12:
            Speak(f"good evening, its {tt}")
            Speak("i am online and ready for my work sir")
        else:
            pass
        MainExecution()
    ClapDetect()
except Exception as f:
    print("an error detected",f) 