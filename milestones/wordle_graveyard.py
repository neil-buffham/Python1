
#bullcrap code
''''
        while count <= len(word):
            if word[count] == guess[count]:
                print(str.upper(guess[count]), end = "")
            elif word[count] != guess[count]:
                while countb <= len(word):
                    if word[count] == guess[countb]:
                        print(str.lower(guess[count]), end = "")
                    countb += 1
            else:
                print("_", end = "")
            count += 1
        count = 0
        print()
            
'''


#bullcrap code mk2
'''
    elif guess != word:
        playing = True
        count = 0
        for position, letter, in enumerate(word):
            if letter == guess[count]:
                print(f"position = {position} letter = {letter} guess[count] = {guess[count]}")
            elif letter != guess[count]:
                while countb <= (len(guess) - position):
                    if letter == guess[countb]:
                        in_word = True
                        print(guess[countb])
                    elif letter != guess[countb]:
                        in_word = False
                    countb +=1
                if in_word:
                    print(f"position = {position} letter = {letter} guess[count] = {guess[countb]} -- Not a match, but in word")
                elif not in_word:
                    print(f"position = {position} letter = {letter} guess[count] = {guess[countb]} -- Not a match. output _")
            count += 1
'''



#this code is only mildly bullcrap. it works, but prints out each time it checks a letter that didn't match against each letter of the secret word:
'''
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
                    if letterb == word[countb]:
                        print(f"position = {position} letter = {letter} guess letter = {letterb} -- Not a match, but in word")
                    elif letter != word[countb]:
                        print(f"position = {position} letter = {letter} guess letter = {letterb} -- Not a match. output _")
                    countb +=1
            
            count += 1
'''