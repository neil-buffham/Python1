

#Section 1:
'''
user_number = int(input("Please type a positive number: "))

while user_number <=0:
    print("Sorry, that is a negative number. Please try again.")
    user_number = int(input("Please type a positive number: "))

print(f"The number is: {user_number}")
'''

#Section 2:
loop = "yes"
candy = "no"

while loop == "yes":
    candy = str.lower(input("May I have a piece of candy? "))
    if candy == "yes":
        loop = "no"


print("Thank you.")