import datetime
import winsound
import threading

def alarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing, "%I:%M %p"))
    altime = altime[11:-3]
    Horeal = altime[:2]
    Horeal = int(Horeal)
    Mireal = altime[3:5]
    Mireal = int(Mireal)
    print(f"Done, alarm is set for {Timing}")

    while True:
        if Horeal == datetime.datetime.now().hour and Mireal == datetime.datetime.now().minute:
            print("Alarm is ringing")
            winsound.PlaySound('abc', winsound.SND_LOOP)
        elif Horeal < datetime.datetime.now().hour or (Horeal == datetime.datetime.now().hour and Mireal < datetime.datetime.now().minute):
            break

def main():
    alarm_time = input("Enter the alarm time (hh:mm AM/PM): ")
    
    alarm_thread = threading.Thread(target=alarm, args=(alarm_time,))
    alarm_thread.daemon = True  # Setting daemon to True will make the thread exit when the main program exits
    alarm_thread.start()
    
    # Your main code continues here
    while True:
        # Your main code logic goes here
        pass

if __name__ == "__main__":
    main()
