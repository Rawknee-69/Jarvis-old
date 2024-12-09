from plyer import notification

from pygame import mixer
file = open("tasks.txt","r")
content = file.read()
file.close()
mixer.init()
mixer.music.load("Body\\Dataspeak\\data.mp3")
mixer.music.play()
notification.notify(
    title = "My schedule :-",
    message = content,
    timeout = 15)