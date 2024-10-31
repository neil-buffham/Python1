# ask user their age and return age plus one as a string
age = input("How old are you? ")
age_plus1 = (int(age)+1)
age_plus1_str = (str(age_plus1))
print("On your next birthday, you will be "+ age_plus1_str)
print()

#Ask user number of egg cartons, return number of eggs
cartons = input("How many egg cartons do you have? ")
cartons_int = int(cartons)
eggs = (cartons_int*12)
print("You have", eggs, "eggs")
print()


cookies = (input("How many cookies do you have? "))
people = (input("How many people are there? "))
cookies_n = int(cookies)
people_n = int(people)
ration = (cookies_n / people_n)
print("Each person may have", ration, "cookies")