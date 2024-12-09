import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Get a list of all of the available voices
voices = engine.getProperty('voices')

# Print the number of voices
print(len(voices))