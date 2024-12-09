import random
import os
import pygame

voice2 = 'en-US-AnaNeural'
def Speak(data):
    #voice = 'en-US-SteffanNeural'
    command = f'edge-tts --voice "{voice2}" --text "{data}" --write-media "Body//Dataspeak//data.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("Body//Dataspeak//data.mp3")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(7)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


# Story templates
story_templates = [
    "Once upon a time, there was a {character} who lived in a {location}. {character} was {trait} and had a dream of {dream}. One day, {event} happened, and everything changed. {character} embarked on a journey to {goal}. Along the way, they encountered {obstacle} and learned a valuable lesson about {lesson}. In the end, {outcome}. The end.",
    "In a faraway land called {land}, there was a {character} known for their {trait}. They dreamed of {dream}, and one day, destiny called. {event} sparked an adventure, and {character} set out to {goal}. However, the path was not easy, as they faced {obstacle} and had to overcome their fears of {fear}. In the end, {outcome}. And so, the tale of {character} will be remembered forever.",
    "{character}, a {trait} soul, resided in a {location}. They always wanted to {dream}, and fate granted them the chance when {event} occurred. This led them on a quest to {goal}. During the journey, they encountered {obstacle} and discovered the true meaning of {lesson}. Finally, {outcome}. And thus, {character}'s story became a legend."
]

# Word banks for randomization
characters = ["brave knight", "clever wizard", "fearless adventurer", "curious explorer", "kind-hearted princess", "wise king", "noble queen", "brave warrior", "mysterious sorcerer", "cunning thief"]
locations = ["enchanted forest", "mysterious castle", "hidden cave", "magic kingdom", "ancient ruins", "frozen wasteland", "floating islands", "underwater city", "forgotten temple", "whimsical wonderland"]
traits = ["courageous", "wise", "determined", "inquisitive", "compassionate", "loyal", "fearless", "charismatic", "intelligent", "adventurous"]
dreams = ["finding a hidden treasure", "saving their kingdom", "discovering a magical artifact", "exploring new worlds", "bringing peace to the realm", "becoming a legendary hero", "unraveling a long-lost secret", "mastering ancient magic", "reuniting with long-lost family", "overcoming their darkest fears"]
events = ["a shooting star streaked across the sky", "a mysterious letter arrived", "a magical portal opened", "a powerful prophecy was foretold", "a legendary creature appeared", "a celestial event changed everything", "an ancient curse was broken", "a magical book revealed its secrets", "a forgotten artifact resurfaced", "a wise sage appeared with a message"]
goals = ["fulfill their destiny", "unravel the ancient prophecy", "save their loved ones", "bring peace to the realm", "restore the balance of nature", "retrieve the sacred relic", "conquer the evil forces", "find the source of eternal youth", "restore the lost magic", "unite the divided kingdoms"]
obstacles = ["a wicked sorcerer", "a powerful dragon", "a dark curse", "a treacherous maze", "an army of undead", "a vengeful spirit", "a jealous rival", "a cunning witch", "an ancient guardian", "a mind-controlling enchantment"]
lessons = ["friendship", "courage", "forgiveness", "self-discovery", "perseverance", "sacrifice", "love", "humility", "trust", "empathy"]
fears =["afraid"]
outcomes = ["they lived happily ever after", "they became a legend", "their name echoed across the lands", "they found true meaning in life", "they achieved inner peace", "their bravery inspired generations", "they became a wise ruler", "they embraced their magical heritage", "they restored harmony to the world", "they found their true family"]
land = ["Enchanted Forest",
    "Mysterious Castle",
    "Hidden Cave",
    "Magic Kingdom",
    "Ancient Ruins",
    "Frozen Wasteland",
    "Floating Islands",
    "Underwater City",
    "Forgotten Temple",
    "Whimsical Wonderland",
    "Eternal Abyss",
    "Celestial Garden",
    "Emerald Meadows",
    "Fiery Volcano",
    "Golden Sands",
    "Silver Glades",
    "Gloomy Marshes",
    "Crystal Caves",
    "Lost Oasis",
    "Twilight Valley",
    "Starlit Sky",
    "Moonlit Sea",
    "Dusky Desert",
    "Rainbow Peaks",
    "Whispering Woods",
    "Evergreen Vale",
    "Mystic Sanctuary",
    "Dreamer's Haven",
    "Sapphire Springs",
    "Crimson Highlands",
    "Hidden Lagoon",
    "Serenity Plateau",
    "Azure Grotto",
    "Ethereal Isles",
    "Jade Archipelago",
    "Silent Glacier",
    "Ember Ridge",
    "Tranquil Bay",
    "Mythical Plateau",
    "Cascading Falls",
    "Gilded Ridge",
    "Shimmering Sands",
    "Spectre Marsh",
    "Harmony Haven",
    "Enigma Labyrinth",
    "Echoing Chasm",
    "Enchanted Moon",
    "Whispering Wind",
    "Eternal Twilight",
    "Silent Aurora",
    "Mystic Mirage",
    "Twinkling Star",
    "Dancing Flame",
    "Soothing Breeze",
    "Wandering Echo",
    "Ephemeral Whirlpool",
    "Sparkling Ember",
    "Lost Whisper",
    "Eternal Blossom",
    "Tranquil Cascade",
    "Glimmering Shadow",
    "Crimson Whisper",
    "Lustrous Halo",
    "Gentle Zephyr",
    "Ethereal Echo",
    "Moonlit Mirage",
    "Mystic Mirage",
    "Luminous Cascade",
    "Eternal Embrace",
    "Glistening Echo",
    "Whispering Whirlpool",
    "Enchanted Ember",
    "Celestial Cascade",
    "Soothing Whirlpool",
    "Wandering Glimmer",
    "Ephemeral Moon",
    "Gentle Aurora",
    "Gilded Ember",
    "Spectre Whisper",
    "Dancing Halo",
    "Twinkling Moon",
    "Glimmering Mirage",
    "Silent Zephyr",
    "Harmony Cascade",
    "Eternal Aurora",
    "Enigma Halo",
    "Gentle Whisper",
    "Soothing Aurora",
    "Crimson Glimmer",
    "Twinkling Halo",
    "Ephemeral Echo",
    "Dancing Zephyr",
    "Whispering Aurora",
    "Lustrous Glimmer",
    "Glimmering Halo",
    "Enigma Moon",
    "Soothing Ember",
    "Ephemeral Mirage",
    "Silent Mirage",
    "Mystic Ember",
    "Enchanted Zephyr",
    "Celestial Whirlpool",
    "Glistening Whisper",
    "Gentle Ember",
    "Luminous Mirage",
    "Eternal Mirage",
    "Whispering Moon",
    "Gentle Halo",
    "Enigma Glimmer",
    "Spectre Cascade",
    "Soothing Moon",
    "Dancing Ember",
    "Twinkling Whirlpool",
    "Lustrous Whisper",
    "Glistening Echo",
    "Soothing Halo",
    "Silent Cascade",
    "Enchanted Halo",
    "Gilded Whisper",
    "Celestial Zephyr",
    "Mystic Moon",
    "Crimson Mirage",
    "Twinkling Cascade",
    "Ephemeral Zephyr",
    "Gentle Whirlpool",
    "Whispering Ember",
    "Spectre Aurora",
    "Dancing Glimmer",
    "Lustrous Zephyr",
    "Ephemeral Halo",
    "Soothing Cascade",
    "Glistening Zephyr",
    "Silent Glimmer",
    "Eternal Moon",
    "Mystic Whirlpool",
    "Enchanted Whisper",
    "Gilded Cascade",
    "Twinkling Ember",
    "Gentle Moon",
    "Luminous Halo",
    "Eternal Glimmer",
    "Whispering Cascade",
    "Ephemeral Whisper",
    "Soothing Glimmer",
    "Silent Ember",
    "Mystic Aurora",
    "Glistening Moon",
    "Gentle Cascade",
    "Dancing Moon",
    "Crimson Echo",
    "Twinkling Mirage",
    "Ephemeral Aurora",
    "Spectre Halo",
    "Soothing Zephyr",
    "Glistening Glimmer",
    "Lustrous Cascade",
    "Whispering Zephyr",
    "Enchanted Moon",
    "Gentle Mirage",
    "Eternal Ember",
    "Crimson Glimmer",
    "Soothing Whirlpool",
    "Ephemeral Echo",
    "Silent Aurora",
    "Mystic Mirage",
    "Twinkling Star",
    "Dancing Flame",
    "Soothing Breeze",
    "Wandering Echo",
    "Ephemeral Whirlpool",
    "Sparkling Ember",
    "Lost Whisper",
    "Eternal Blossom",
    "Tranquil Cascade",
    "Glimmering Shadow",
    "Crimson Whisper",
    "Lustrous Halo",
    "Gentle Zephyr",
    "Ethereal Echo",
    "Moonlit Mirage",
    "Mystic Mirage",
    "Luminous Cascade",
    "Eternal Embrace",
    "Glistening Echo",
    "Whispering Whirlpool",
    "Enchanted Ember",
    "Celestial Cascade",
    "Soothing Whirlpool",
    "Wandering Glimmer",
    "Ephemeral Moon",
    "Gentle Aurora",
    "Gilded Ember",
    "Spectre Whisper",
    "Dancing Halo",
    "Twinkling Moon",
    "Glimmering Mirage",
    "Silent Zephyr",
    "Harmony Cascade",
    "Eternal Aurora",
    "Enigma Halo",
    "Gentle Whisper",
    "Soothing Aurora",
    "Crimson Glimmer",
    "Twinkling Halo",
    "Ephemeral Echo",
    "Dancing Zephyr",
    "Whispering Aurora",
    "Lustrous Glimmer",
    "Glimmering Halo",
    # ... (list of land names, as provided earlier)
]


def generate_story():
    # Randomly select a story template
    template = random.choice(story_templates)

    # Randomly select words for the story
    character = random.choice(characters)
    location = random.choice(locations)
    trait = random.choice(traits)
    dream = random.choice(dreams)
    event = random.choice(events)
    goal = random.choice(goals)
    obstacle = random.choice(obstacles)
    lesson = random.choice(lessons)
    outcome = random.choice(outcomes)
    selected_land = random.choice(land)  # Use a different variable name for the selected land

    # Fill in the template with selected words
    story = template.format(
        character=character,
        location=location,  # Use 'location' instead of 'place'
        trait=trait,
        dream=dream,
        event=event,
        goal=goal,
        obstacle=obstacle,
        lesson=lesson,
        outcome=outcome,
        land=selected_land,  # Use the new variable here

    )

    return story
