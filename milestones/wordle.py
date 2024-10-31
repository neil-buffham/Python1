word = "frog"
playing = True
inputword = ""
tries = 0
letter_count = len(word)

'''
for index in range(letter_count):
    letter = word[index]
    print(f"Index: {index} Letter: {letter}")
'''






# Guessing portion:
'''
print("Welcome to the word guessing game!")
while playing:
    hint = (letter_count * "_")
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
'''    

