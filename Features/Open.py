from pickle import TRUE
import keyboard
import pyautogui
import webbrowser
from time import sleep

def OpenExe(Query):
    Query = str(Query).lower()

    if "Visit" in Query:
        Nameofweb = Query.replace("visit ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif "visit" in Query:
        Nameofweb = Query.replace("launch ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return TRUE

    elif "open" in Query:
        Nameoftheapp = Query.replace("open ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(2)
        keyboard.press('enter')
        sleep(0.5)
        return True

    elif "start" in Query:
        Nameoftheapp = Query.replace("start ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(2)
        keyboard.press('enter')
        sleep(0.5)
        return True    



