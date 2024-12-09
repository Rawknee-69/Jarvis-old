import sys
import time
import threading
sys.path.append("C:\\Users\\srija\\Desktop\\AIJarvisl\\")
from Speak import Speak
from Listen import MicExecution

# A list to store tasks and their completion status
tasks = []

def get_reminder_interval():
    Speak("After how many minutes would you like to receive reminders?")
    while True:
        try:
            minutes = int(MicExecution())
            return minutes * 60  # Convert minutes to seconds
        except ValueError:
            Speak("Invalid input. Please provide a numeric value.")

def read_tasks_from_file():
    global tasks
    with open("tasks.txt", "r") as file:
        tasks = [line.strip() for line in file.readlines()]

def write_tasks_to_file():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

def reminder_loop(interval):
    while True:
        for i, task in enumerate(tasks):
            if not task.startswith("Y"):
                Speak(f"Reminder: Have you completed task any of your task! Please say 'yes' or 'no'.")
                response = MicExecution().lower()
                if "yes" in response:
                    tasks[i] = "Y" + task
                    write_tasks_to_file()
                    Speak("Great job! Keep up the good work!")
        time.sleep(interval)

def scheduleday():
    global tasks
    read_tasks_from_file()
    
    while True:
        try:
            #Speak("Please tell me the number of tasks you will be performing today.")
            #Speak("For example: '4'. You only have to tell me the numeric value.")
            no_tasks = int(MicExecution())
            
            for _ in range(no_tasks):
                #Speak("Please tell me your task.")
                task = MicExecution()
                tasks.append(task)
            
            interval = get_reminder_interval()  # Get the reminder interval after tasks are entered
            reminder_thread = threading.Thread(target=reminder_loop, args=(interval,))
            reminder_thread.start()
            
            write_tasks_to_file()
            Speak("Tasks recorded. Your reminders have started. You can continue with other tasks.")
            
            break  # Exit the loop if input and tasks were successfully entered
        except ValueError:
            Speak("Invalid input. Please provide a numeric value for the number of tasks.")

# Run the main scheduling function
scheduleday()
