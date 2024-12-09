import wikipedia as wikiscrap
import pywhatkit
import sys
sys.path.append("C:\\Users\\srija\\Desktop\\AIJarvisl\\")
from Listen import MicExecution

from Speak import Speak

def main():
    Speak ("what you want to know from google")
    query = MicExecution()
    
    # Modify query to remove certain keywords
    query = query.replace("jarvis", "**")
    query = query.replace("google search", "")
    query = query.replace("google", "**")
    
    print("This Is What I Found On The Web!")

    # Perform Google search
    pywhatkit.search(query)

    try:
        # Get Wikipedia summary
        result = wikiscrap.summary(query, sentences=3)
        Speak(result)
    except:
        Speak("No Speakable Data Available!")

main()
