import pygame
import os
import psutil


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



def rescourceusage():
    try:
        cpu_usage = psutil.cpu_percent()

        # Get the RAM usage
        ram_usage = psutil.virtual_memory().percent

        # Get the disk usage
        disk_usage = psutil.disk_usage("/").percent

        p = cpu_usage
        s = ram_usage
        t = disk_usage
        Speak("the disk usage: in percentage")     
        Speak(t)
        Speak("And The ram usage in : percentage ")
        Speak(s)
        Speak("And finally the cpu usage: in percentage ")
        Speak(p) 
    except:
        Speak("there was a problem encountered trying to fix it ! Just try again sir.")             
 