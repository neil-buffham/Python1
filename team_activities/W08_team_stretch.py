quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."


divisible = 0

counter = 0
playing = True

while playing: 
    number = int(input("Please enter a number: "))

    for i, letter in enumerate(quote):
        if i % number == 0:
            print(str.upper(letter), end="")
        else:
            print(letter, end="")
    print()
    check_playing = str.lower(input("Would you like to enter another number? "))
    if check_playing == "yes":
        playing = True
    else:
        playing = False
        print("Goodbye")
