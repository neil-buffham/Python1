# Only variables strictly necessary for the first round of checking: ----------------------------------------------------------------------------
word = "frog"
running = True
playing = True
letter_count = len(word)

# Intro portion: ---------------------------------------------------------------------------------------------------------------
print("Welcome to the word guessing game!")
hint = (letter_count * "_")
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

            # Check if each letter matches first the letter in the same position in the guess, then in the word at all------
            for position, guess_letter, in enumerate(guess):
                if guess_letter == word[position]:
                    print(f"position = {position} word_letter = {word[position]} guess_letter = {guess_letter}    Correct!")


                else:
                    if guess_letter in word:
                            print(f'position = {position} word_letter = {word[position]} guess_letter = {guess_letter}    Not correct, but in word.')
                    else:
                        print(f'position = {position} word_letter = {word[position]} guess_letter = {guess_letter}    Not correct.')

    play_again = str.lower(input("Would you like to play again? (Yes/No)"))

    if play_again == "yes":
        playing = True
    elif play_again == "no":
        print("Thank you for playing")
        running = False
        playing = False