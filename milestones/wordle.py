word = "frog"
playing = True
inputword = ""
tries = 0
wordlength = len(word)

print("Welcome to the word guessing game!")

while playing:
    hint = (wordlength * "_")
    #print (f" Hint: {hint}")
    inputword = str.lower(input("What is your guess? "))
    tries += 1
    if inputword == word:
        playing = False
        print("Congratulations! You guessed it!")
        print(f"It took you {tries} guesses.")
    elif inputword != word:
        playing = True
        print("Your guess was not correct.")
    

