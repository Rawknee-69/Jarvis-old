from googlesearch import search
import re

def searchsong():
    try:
        # Ask the user for the name of the song
        song_name = input("Enter the name of the song: ")

        # Clean the input to remove non-alphanumeric characters
        cleaned_input = re.sub(r'[^a-zA-Z0-9 ]', '', song_name)

        # Prepare the search query
        search_query = f"{cleaned_input} YouTube"

        song_link = None  # Initialize song_link to None

        # Perform the Google search
        for result in search(search_query, num=1, stop=1, pause=2):
            if "youtube.com/watch?" in result:
                song_link = result
                break  # Exit the loop after finding the link

        if song_link:
            print(f"Playing '{cleaned_input}' from {song_link}")
            # Save song_link to a text file
            with open("cookies\\song_link.txt", "w") as file:
                file.write(song_link)
        else:
            print(f"No YouTube results found for '{cleaned_input}'")

    except Exception as e:
        print("Error:", e)


