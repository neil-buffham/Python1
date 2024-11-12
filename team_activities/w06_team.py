
#Determine number of riders, age, and height
age1 = int(input("What is the age of the first rider in years? "))
height1 = int(input("What is the height of the first rider in inches? "))
two_riders = str.lower(input("Is there a second rider? (yes/no) "))
if two_riders == "yes":
    age2 = int(input("What is the age of the second rider in years? "))
    height2 = int(input("What is the height of the second rider in inches? "))
elif two_riders == "no":
    age2 = False
    height2 = False

#Setup True/False Values as False
ride1 = False
ride1_tall_enough = False
ride1_18plus = False
ride1_solo = False
ride2_solo = False

ride2 = False
ride2_tall_enough = False
ride2_18plus = False

'''First Rider Logic poriton'''
#Height1
if height1 < 36:
    ride1_tall_enough = False
else:
    ride1_tall_enough = True
#age1
if age1 >= 18:
    ride1_18plus = True
else: 
    ride1_18plus = False
#Solo
if age1 >= 18 and height1 >=62:
    ride1_solo = True
#Can ride with others:
if ride1_tall_enough:
    ride1 = True

#print("Completed first rider boolean")


''' Second Rider Logic portion'''
if two_riders == "yes":
    #Height1
    if height2 < 36:
        ride2_tall_enough = False
    else:
        ride2_tall_enough = True
    #age1
    if age2 >= 18:
        ride2_18plus = True
    else: 
        ride2_18plus = False
        #Solo
    if age2 >= 18 and height2 >=62:
        ride2_solo = True
    #Can ride with others:
    if ride2_tall_enough:
        ride2 = True
#else:
#        print("-----no output chosen from second rider boolean")

#print("Completed second rider boolean")





#Troubleshooting portion for rider logic section:
'''
print(f".........two_riders: {two_riders}")
print(f".........ride1: {ride1}")
print(f".........ride2: {ride2}")
print(f".........ride1_18plus: {ride1_18plus}")
print(f".........ride2_18plus: {ride2_18plus}")
print(f".........{two_riders}")
'''

#logic portion for solo rider
if two_riders == "no":
    if ride1 == True: # check if the person is tall enough to ride at all
        if ride1_solo == True:
            print("You may ride solo")
        else:
            print("You may not ride solo")
    elif not ride1:
        print("You are too short (womp womp)")
elif two_riders == "yes":    #evaluate both riders together
    if ride1 == False:
        print("Rider 1 is to short")
    if ride2 == False:
        print("Rider 2 is too short")
    else:
        if ride1_18plus:
            print("You may both ride (ride1 adult)")
        if ride2_18plus:
            print("You may both ride (ride2 adult)")
#else:
    #print("-----no output chosen for rider logic portion")

#print("Completed the rider logic portion")





'''
        if ride2 == True:
            if (not ride1 and not ride2):
                print("Neither person is tall enough")
            elif (not ride1):
                print("The first rider is too short")
            elif (not ride2):
                print("The second rider is too short")
            elif (ride1_18plus or ride2_18plus):
                print("You may both ride.")
            elif (not ride1_18plus) and (not ride2_18plus):
                print("You need an adult to ride.")
'''




'''Not sure what I was thinking here:
#output portion for the decision
if ride1 == False:
    print("The first rider is too short.")
if ride1 == True:
    print("The first rider is tall enough")
if ride2 == False:
    print("The second rider is too short.")
if ride2 == True:
    print("The second rider is tall enough")
if two_riders == True and ride2 == True:
    print("Both riders may ride")
'''



''' This portion of code is wretched
#First Rider Logic
if two_riders == "no":
    if height1 < 36:
        print("Sorry, you may not ride.")
    elif height1 < 62:
        print("Sorry, you may not ride without a second rider.")
    elif height1 >= 62 and age1 >= 18:
        print("You may ride solo, or accompany someone else.")
    else:
        print("error/incomplete logic code.")
if two_riders == "yes":
    age2 = int(input("How old is the second person in years? "))
    height2 = int(input("How tall is the second person in inches? "))

    if height1 < 36 or height2 < 36:
        if height1 < 36 and height2 >= 36:
            print ("Person 1 may not ride, they are too short. ")
    if height2 < 36:
        print("Person 2 may not ride, they are too short.")

'''
