# Test values for cementign formatting style/method:
'''
name1 = "Fred"
name2 = "Weasley"
email = "fredweasley@byui.edu"
phone = "123-456-7890"
title = "Bee watch-watcher"
idn = "1930950293"
hair = "Blonde"
eyes = "Blue"
month = "September"
train = "No"
'''

#Begin of functional code
print("Please enter the following information:")
print()

#Ask the user each of these questions, and store the answer for regurgitation
name1 = input("What is your first name?")
name2 = input("What is your last name?")
email = input("What is your email address?")
phone = input("What is your phone number?")
title = input("What is your job title?")
idn = input("What is your ID number?")
hair = input("What is your hair color?")
eyes = input("What is your eye color?")
month = input("What month do/did you start?")
train = input("Are you in training?")


print()
print("The ID Card is:")

#Main portion of the ID card
print("-"*40)
print(name1,name2)
print(title)
print("ID: " + idn)
print()
print(email)
print(phone)

#Supplimentary portion of ID Card.
# The "<" indicates the value within {} will be alligned to a left margin at the specified distance
print()
print(f"{"Hair: " + hair : <25}{"Eyes: " + eyes : <50}")
print(f"{"Month: " + month : <25}{"Training: " + train : <50}")
print("-"*40)

#Print a blank line to give the card some space
print()