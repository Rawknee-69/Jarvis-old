import sys
sys.path.append("C:\\Users\\srija\\Desktop\\AIJarvisl\\")
from Speak import Speak
from Listen import MicExecution

def scheduleday():
    tasks = []  # Empty list
    Speak("Do you want to clear old tasks? Please speak YES or NO")
    query = MicExecution().lower()  # Convert the query to lowercase for easier comparison
    
    if query in ["yes", "y"]:
        with open("tasks.txt", "w") as file:
            file.write("")
        
    Speak("Please tell me the number of tasks you will be performing today.")
    Speak("For example: '4'. You only have to tell me the numeric value.")
    no_tasks = int(MicExecution())
    
    for i in range(no_tasks):
        Speak(f"Please tell me your task number {i + 1}")
        task = MicExecution()
        tasks.append(task)
        
        with open("tasks.txt", "a") as file:
            file.write(f"{i + 1}. {task}\n")

scheduleday()
