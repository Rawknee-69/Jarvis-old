import pyttsx3

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


# You can call set_voice_parameters() before each speak() call to adjust parameters dynamically.
