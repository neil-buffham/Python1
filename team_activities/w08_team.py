favorite = str.lower(input("What is your favorite letter? "))

word = "Commitment"
word = word.lower()

for letter in word:
    if letter.lower() == favorite:
        print("_", end="")
    else:
        print(letter, end="")




#Section 2 of the team activity code:

for letter in word:
    if letter.lower() == favorite:
        print(letter.upper(), end="")
    else:
        print(letter, end="")
