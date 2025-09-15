import time
import requests
from bs4 import BeautifulSoup

# Function to print messages with a delay for a more interactive feel
def slow_print(message, delay=1):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()
    time.sleep(delay)

# Introduction to the guitar
def introduction():
    slow_print("Welcome to the Guitar Learning Assistant!")
    slow_print("In this program, we'll walk through the basics of playing the guitar.")
    slow_print("Let's start by tuning your guitar. It's crucial to have your guitar in tune for good sound quality!")
    slow_print("We will use standard tuning (E A D G B E).")
    slow_print("Use a tuner app or a tuning device to match each string to the correct note.")
    input("Press Enter when your guitar is in tune and you're ready to continue...")

# Learning basic chords
def basic_chords():
    slow_print("Now, let's learn some basic chords.")
    slow_print("We'll start with the following open chords:")
    slow_print("1. E major (E) - Press down on the first fret of the third string (G) and second fret of the fifth string (A).")
    slow_print("2. A major (A) - Press down on the second fret of the second, third, and fourth strings (B, G, and D).")
    slow_print("3. D major (D) - Press down on the second fret of the first string (E) and third fret of the second string (B).")
    slow_print("Practice these chords until you're comfortable switching between them.")
    slow_print("You can strum down and up with a basic motion to get used to the rhythm.")
    input("Press Enter when you're ready to continue...")

# Strumming patterns
def strumming_patterns():
    slow_print("Next, let's talk about strumming patterns!")
    slow_print("A basic strumming pattern is:")
    slow_print("Down, Down, Up, Up, Down, Up (D, D, U, U, D, U).")
    slow_print("To practice this, start by strumming with your hand relaxed, and follow the pattern.")
    slow_print("Remember to keep the rhythm steady and consistent.")
    input("Press Enter when you're ready to continue...")

# Playing a simple song
def simple_song():
    slow_print("Great job! Now, let's try a simple song using the chords you learned.")
    slow_print("A good song to practice is 'Twinkle, Twinkle, Little Star'.")
    slow_print("The chord progression for this song is: C, G, Am, F.")
    slow_print("Try switching between these chords while strumming.")
    slow_print("Once you feel confident with the changes, try singing along while you play!")
    input("Press Enter when you're ready to continue...")

# Lost in Forever by Crystal Lake Lesson
def lost_in_forever():
    slow_print("Let's dive into 'Lost in Forever' by Crystal Lake.")
    slow_print("This song features fast power chords and aggressive strumming. We'll simplify it for beginners, but you can work on adding speed and intensity later!")
    
    # Tuning: The song is in Drop C tuning (C G C F A D), but we will use standard tuning for simplicity.
    slow_print("The song is originally in Drop C tuning (C G C F A D), but for simplicity, we'll stick to standard tuning (E A D G B E).")
    slow_print("If you're feeling comfortable, you can try tuning your guitar to Drop C to match the original sound.")
    input("Press Enter to continue...")
    
    slow_print("We'll focus on the main riff and the chorus to get you started.")
    
    # Main Riff: Simplified power chords (C5, G5, A#5, D#5)
    slow_print("The main riff is based on power chords. Here are the simplified chords you'll use:")
    slow_print("1. C5 (x 3 5 5 x x): Play the 3rd fret on the 5th string and the 5th fret on the 4th string.")
    slow_print("2. G5 (3 5 5 x x x): Play the 3rd fret on the 6th string and the 5th fret on the 5th string.")
    slow_print("3. A#5 (1 3 3 x x x): Play the 1st fret on the 5th string and the 3rd fret on the 4th string.")
    slow_print("4. D#5 (6 8 8 x x x): Play the 6th fret on the 5th string and the 8th fret on the 4th string.")
    
    slow_print("Practice switching between these power chords. Try strumming each one in time with the song.")
    slow_print("The main riff sounds like this: C5 -> G5 -> A#5 -> D#5.")
    input("Press Enter when you're ready to continue...")

    slow_print("Once you're comfortable with the main riff, let's move to the chorus.")
    
    # Chorus: Simplified chord progression (C5, G5, A#5)
    slow_print("The chorus is built around these power chords:")
    slow_print("1. C5 (x 3 5 5 x x): Play the 3rd fret on the 5th string and the 5th fret on the 4th string.")
    slow_print("2. G5 (3 5 5 x x x): Play the 3rd fret on the 6th string and the 5th fret on the 5th string.")
    slow_print("3. A#5 (1 3 3 x x x): Play the 1st fret on the 5th string and the 3rd fret on the 4th string.")
    
    slow_print("For the chorus, you'll play C5 -> G5 -> A#5 -> G5.")
    slow_print("Try to strum each power chord strongly and consistently.")
    input("Press Enter when you're ready to continue...")

    slow_print("Great job! Keep practicing the main riff and chorus until you're comfortable playing along with the song.")
    slow_print("The song has fast changes, so take your time getting the rhythm down before speeding up.")

# Dynamic Song Search (searches for chords online)
def fetch_song_chords_from_ultimate_guitar(song_name):
    slow_print(f"Searching for chords for '{song_name}'...")
    
    # Simulate a search result (in reality, this would be a web scraping or API request)
    # For this example, we simulate returning a simple chord progression for the requested song.
    
    song_chords = {
        "wonderwall": "The song uses the chords: Em, G, D, A, C.",
        "hotel california": "The song uses the chords: Am, E, G, D, F, C.",
        "smells like teen spirit": "The song uses the chords: F5, Bb5, Ab5, Db5.",
    }
    
    if song_name in song_chords:
        slow_print(f"Found chords for '{song_name}': {song_chords[song_name]}")
        slow_print("Try playing along with these chords!")
    else:
        slow_print(f"Sorry, we couldn't find chords for '{song_name}' right now.")
    
# Request a song from the user
def request_song():
    slow_print("What song would you like to learn today? (Type a song name or type 'exit' to quit):")
    song = input("Song: ").strip().lower()
    
    if song == 'twinkle twinkle little star':
        slow_print("Let's start with 'Twinkle, Twinkle, Little Star'.")
        slow_print("We already learned the chords: C, G, Am, F.")
        slow_print("The song's progression is C -> G -> Am -> F.")
        slow_print("Play along with this chord progression and try to sing along!")
    elif song == 'lost in forever':
        lost_in_forever()
    elif song == 'let it be':
        slow_print("Let's learn 'Let it Be' by The Beatles.")
        slow_print("This song uses the following chords: C, G, Am, F.")
        slow_print("The progression is C -> G -> Am -> F.")
        slow_print("Try to follow the pattern and practice!")
    elif song == 'exit':
        slow_print("Thank you for using the Guitar Learning Assistant! Good luck with your playing!")
        return False
    else:
        fetch_song_chords_from_ultimate_guitar(song)
    
    return True

# Main Program Loop
def main():
    introduction()
    basic_chords()
    strumming_patterns()
    simple_song()
    
    # Let user request songs and keep learning
    while True:
        if not request_song():
            break

# Start the learning program
if __name__ == "__main__":
    main()


