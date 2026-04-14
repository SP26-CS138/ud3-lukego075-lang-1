'''
DEVELOPER(S): Luke Gonzales
COLLABORATORS: Samantha
DATE: 4/13/2026
'''

"""
This code reccomends a song by The Weeknd based on the user's mood. 
Leave one blank line.  The rest of this docstring should contain an
overall description of the program.
"""

##########################################
# IMPORTS:
# 
##########################################
# <replace this line with import statement(s)>
import random

##########################################
# FUNCTIONS:
def get_mood_choice():
    while True:
        mood = input("What type of mood are you interested in? Sad, Upbeat, or Moody: ").strip().lower()
        if mood in SONGS_BY_MOOD:
            return mood
        print("Please enter Sad, Upbeat, or Moody.")

def main():
    mood = get_mood_choice()
    song = random.choice(SONGS_BY_MOOD[mood])
    print(f"Your song by the Weeknd based on your mood is: {song}")

##########################################
# Mood choice allows the user to choose between three moods: sad, upbeat, and moody.
#the program then selects a song at random from the correstponding list of songs for that mood


##########################################
# MAIN PROGRAM:
##########################################
# <replace this line with your main program>
SONGS_BY_MOOD = {
    "sad": [
        "Privilege",
        "Twenty Eight",
        "Echoes of Silence",
        "Call Out My Name",
        "Until I Bleed Out",
        "I Was Never There",
        "Try Me",
        "Repeat After Me",
        "The Birds pt. 2",
        "Tears in the Rain",
        "The Knowing",
        "Adaptation",
        "Baptized in Fear",
        "Wasted Times",
        "Valerie",
        "Starry Eyes",
        "Pretty",
        "Wanderlust",
        "Professional",
        "Without a Warning",
        "Snowchild",
        "Real Life",
    ],
    "upbeat": [
        "I Heard You're Married",
        "Best Friends",
        "Is There Someone Else?",
        "Out of Time",
        "Sacrifice",
        "Moth To A Flame",
        "Take My Breath",
        "A Lonely Night",
        "Save Your Tears",
        "Love to Lay",
        "Attention",
        "All I Know",
        "Rockin",
        "Party Monster",
        "I Feel It Coming",
        "Reminder",
        "Blinding Lights",
        "In Your Eyes",
        "Can't Feel My Face",
        "In the Night",
        "After Hours",
        "Gasoline",
        "How Do I Make You Love Me?",
        "Faith",
        "Starboy",
        "False Alarm",
        "Too Late",
        "Heartless",
        "Six Feet Under",
        "The Hills",
        "Wake Me Up",
        "Cry For Me",
        "Sao Paulo",
        "Timeless",
        "Given Up On Me",
        "The Abyss",
    ],
    "moody":[
        "High for This",
        "What You Need",
        "House of Balloons / Glass Table Girls",
        "The Morning",
        "Wicked Games",
        "The Party & The After Party",
        "Coming Down",
        "Loft Music",
        "Life of the Party",
        "Thursday",
        "The Zone (Ft. Drake)",
        "Gone",
        "Rolling Stone",
        "Heaven Or Las Vegas",
        "Valerie",
        "Montreal",
        "Outside",
        "XO / The Host",
        "Initiation",
        "Same Old Song (Ft. Juicy J)",
        "The Fall",
        "Next",
        "Acquainted",
        "Kiss Land",
        "Love in the Sky",
        "Escape From LA",
        "Niagara Falls",
        "As You Are",
        "Die For You",
        "Nothing Without You",
        "One Of the Girls",
    ],
}
def show_song():
    mood = get_mood_choice()
    song = random.choice(SONGS_BY_MOOD[mood])
    print(f"Your song by the Weeknd based on your mood is: {song}")

def return_to_menu():
    input("\nPress Enter to return to the main menu...")

def main():
    while True:
        print("\nMain Menu")
        print("1. Get a song")
        print("2. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_song()
            return_to_menu()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Please enter 1 or 2.")

if __name__ == "__main__":
    main()
