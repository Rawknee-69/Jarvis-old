import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Set the voice
voice = engine.getProperty('voices')[4]
engine.setProperty('voice', voice.id)

# Set the speech rate
engine.setProperty('rate', 150)

# Set the speech volume
engine.setProperty('volume', 1)

# Create a function to speak the text
def speak(text):
  engine.say(text)
  engine.runAndWait()

# Start the voice assistant
print('Welcome to the voice assistant!')
while True:
  # Get the user's input
  user_input = input('What would you like to do? ')

  # If the user wants to exit, break out of the loop
  if user_input == 'exit':
    break

  # Otherwise, speak the user's input
  speak(user_input)

# Close the engine
engine.close()