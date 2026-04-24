'''
DEVELOPER(S): Luke Gonzales
COLLABORATORS: Samantha
DATE: 4/13/2026
'''

"""
This code recommends a song by The Weeknd based on the user's mood.
The user can choose a mood category and optionally view their song history.
"""

import random

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
    "moody": [
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

HISTORY_FILE = "weeknd_song_history.txt"


def get_mood_choice():
    while True:
        mood = input("What type of mood are you interested in? Sad, Upbeat, or Moody: ").strip().lower()
        if mood in SONGS_BY_MOOD:
            return mood
        print("Please enter Sad, Upbeat, or Moody.")


def choose_song_by_mood(mood):
    song = random.choice(SONGS_BY_MOOD[mood])
    save_song_to_history(mood, song)
    return song


def show_song():
    mood = get_mood_choice()
    song = choose_song_by_mood(mood)
    print(f"Your song by The Weeknd based on your mood is: {song}")


def save_song_to_history(mood, song):
    with open(HISTORY_FILE, "a", encoding="utf-8") as history_file:
        history_file.write(f"Mood: {mood.title()} | Song: {song}\n")


def show_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as history_file:
            history = history_file.read().strip()
    except FileNotFoundError:
        print("No song history has been saved yet.")
        return

    if history:
        print("\nSong History")
        print(history)
    else:
        print("No song history has been saved yet.")


def return_to_menu():
    input("\nPress Enter to return to the main menu...")


def main():
    while True:
        print("\nMain Menu")
        print("1. Get a song")
        print("2. View song history")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_song()
            return_to_menu()
        elif choice == "2":
            show_history()
            return_to_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
