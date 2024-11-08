word = "frog"
playing = True
guess = ""
tries = 0
letter_count = len(word)
count = 0
countb = 0
countc = 0
#processing_letter = False

temp = True
in_word = False

'''
for index in range(letter_count):
    letter = word[index]
    print(f"Index: {index} Letter: {letter}")
'''


# Guessing portion:

print("Welcome to the word guessing game!")
hint = (letter_count * "_")
print (f" Hint: {hint}")
while playing:

    #Keep our counters clean
    count = 0
    countb = 0

    guess = str.lower(input("What is your guess? "))
    tries += 1
    if guess == word:
        playing = False
        print("Congratulations! You guessed it!")
        print(f"It took you {tries} guesses.")
    elif guess != word:
        playing = True
        count = 0
        for position, letter, in enumerate(word):
            if letter == guess[count]:
                print(f"position = {position} letter = {letter} guess[count] = {guess[count]}")
            elif letter != guess[count]:



                # in this section of code, letterb represents the position of a letter in the secret word. Letterb is increased once each time it cycles through. 
               
               #This keeps our while loop running
                

                #loop. Tell us the position of the letter, and the letter, from the guess.
                for positionb, letterb, in enumerate(guess):
                    countb = 0
                    for positionc, letterc, in enumerate(word):
                        while not in_word:    
                            if letterb == letterc:
                                in_word = True
                            elif letter != letterc:
                                in_word = False
                    countb +=1
                if not in_word:
                    print(f"position = {position} letter = {letter} guess letter = {letterb} -- Not in the word(2)")
                elif in_word:
                    print(f"position = {position} letter = {letter} guess letter = {letterb} -- Not a match, but in word")
                
            count += 1

#This code works fine, but prints either the final letter of the word if it isn't in the word 