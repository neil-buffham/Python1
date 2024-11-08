import random

# Only variables strictly necessary for the first round of checking: ----------------------------------------------------------------------------
words = [
    "apple", "curve", "bike", "window", "garden", "quick", "fire", "stone", "branch", "car",
    "jump", "cat", "edge", "whistle", "floor", "mug", "lamp", "bend", "shark", "stair",
    "laugh", "dog", "train", "brush", "grape", "grin", "butter", "hand", "market", "cloud",
    "whale", "paper", "shovel", "rubble", "spoon", "grape", "sink", "dust", "pillow", "wire",
    "plaza", "glove", "sink", "dusty", "lane", "truck", "swim", "stone", "key", "brush",
    "button", "spine", "soap", "bone", "hook", "spoon", "ship", "branch", "snow", "rain",
    "watch", "tray", "walk", "fork", "tree", "neck", "rock", "clamp", "pocket", "handle",
    "plate", "book", "whip", "light", "coat", "flower", "cut", "track", "chain", "bore",
    "scrap", "bite", "brush", "wire", "desk", "tire", "rope", "bell", "slide", "knot", 
    "slip", "grip", "curve", "desk", "trail", "clamp", "match", "wrist", "sink", "plate",
    "apartment", "backpack", "notebook", "umbrella", "trolley", "mountain", "stomach", "luggage",
    "fanatic", "scaffold", "notion", "balloon", "barrel", "cabinet", "biscuit", "stapler",
    "tornado", "raccoon", "helicopter", "volcano", "skeleton", "dashboard", "timetable"
]


word = random.choice(words)
running = True
playing = True
letter_count = len(word)

# Intro portion: ---------------------------------------------------------------------------------------------------------------
print("Welcome to the word guessing game!")
hint = (letter_count * "_ ")
print (f" Hint: {hint}")

    # Guessing portion: ------------------------------------------------------------------------------------------------------------
while running:
    tries = 0
    while playing:
        guess = str.lower(input("What is your guess? "))  #Get user input
        
        
        tries += 1  #increase Try count

        #Word length verification section------------------------------------------------------------
        if letter_count != len(guess):
            while letter_count != len(guess):
                print("Sorry, the guess must have the same number of letters as the secret word.")
                guess = str.lower(input("What is your guess? "))
                tries += 1



        #Check if the user input was correct, and print a finish message if so.
        if guess == word:
            playing = False
            print("Congratulations! You guessed it!")
            print(f"It took you {tries} guesses.")

        #if the word wasn't correct, begin analyzing letters
        elif guess != word:
            # Check if each letter matches first the letter in the same position in the guess, then in the word at all
            print("Your hint is: ", end="")  # Start printing on the same line
            for position, guess_letter in enumerate(guess):
                if guess_letter == word[position]:
                    print(f"{str.upper(guess_letter)}", end=" ")  # Correct letter in the correct position
                else:
                    if guess_letter in word:
                        print(f"{str.lower(guess_letter)}", end=" ")  # Correct letter but in the wrong position
                    else:
                        print("_", end=" ")  # Incorrect letter
            print()
                        

    play_again = str.lower(input("Would you like to play again? (Yes/No)"))

    if play_again == "yes":
        playing = True
    elif play_again == "no":
        print("Thank you for playing")
        running = False
        playing = False