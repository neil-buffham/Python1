import random


playing = True
output = ""
correct = False
tries = 0

#The loop it all happens in
while playing:
    magic_number = random.randint(1, 10)
    while not correct:
        guess = int(input("What is your guess? "))
        tries = tries + 1

        if guess == magic_number:
            output = "You guessed it!"
            correct = True
            print(output)
        elif guess > magic_number:
            output = "Lower"
            print(output)
        elif guess < magic_number:
            output = "Higher"
            print(output)

    print(f"You guessed the magic number in {tries} tries.")
    play_again = str.lower(input("Would you like to play again? (Yes/No) "))

    if play_again == "yes":
        playing = True
        tries = 0
        correct = False
    if play_again == "no":
        playing = False