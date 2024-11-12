#no free golden tickets
ride1_1217_gold = False
ride2_1217_gold = False


#Determine number of riders, age, and height
age1 = int(input("What is the age of the first rider in years? "))
height1 = int(input("What is the height of the first rider in inches? "))
if age1 >= 12:
    if age1 < 18:
        ride1_1217_gold = str.lower(input("Do you have a Golden Ticket? (yes/no) "))
two_riders = str.lower(input("Is there a second rider? (yes/no) "))
if two_riders == "yes":
    age2 = int(input("What is the age of the second rider in years? "))
    height2 = int(input("What is the height of the second rider in inches? "))
    if age2 >= 12:
        if age2 < 18:
            ride2_1217_gold = str.lower(input("Does the second rider have a Golden Ticket? (yes/no) "))
elif two_riders == "no":
    age2 = False
    height2 = False


#Setup Boolean Values as False
ride1 = False
ride1_tall_enough = False
ride1_together = False
ride1_solo = False
ride1_14_plus = False
ride1_16_plus = False
ride1_18_plus = False

ride2 = False
ride2_tall_enough = False
ride2_together = False
ride2_solo = False
ride2_14_plus = False
ride2_16_plus = False
ride2_18_plus = False



'''First Rider Boolean poriton'''
#Height1
if height1 < 36:
    ride1_tall_enough = False
else:
    ride1_tall_enough = True
#Solo
if age1 >= 18 and height1 >=62:
    ride1_solo = True
#Can ride with others:
if ride1_tall_enough:
    ride1 = True
#age14
if age1 >= 14 and age1 < 18:
    ride1_14_plus = True
elif age1 < 14:
    ride1_14_plus = False
#age16
if age1 >= 16 and age1 < 18:
    ride1_16_plus = True
elif age1 < 16:
    ride1_16_plus = False
#age18
if age1 >= 18:
    ride1_18_plus = True
else: 
    ride1_18_plus = False





''' Second Rider Boolean portion'''
if two_riders == "yes":
    #Height1
    if height2 < 36:
        ride2_tall_enough = False
    else:
        ride2_tall_enough = True
    if age2 >= 18 and height2 >=62:
        ride2_solo = True
    #Can ride with others:
    if ride2_tall_enough:
        ride2 = True
    #age14
    if age2 >= 14 and age2 < 18:
        ride2_14_plus = True
    elif age2 < 14:
        ride2_14_plus = False
    #age16
    if age2 >= 16 and age2 < 18:
        ride2_16_plus = True
    elif age2 < 16:
        ride2_16_plus = False
    #age18
    if age2 >= 18:
        ride2_18_plus = True
    else: 
        ride2_18_plus = False
        #Solo




#logic portion for riders
if two_riders == "no":
    if ride1 == True: # check if the person is tall enough to ride at all
        if ride1_solo == True:
            print("You may ride solo (18+ yrs and 62+ in)")
        elif ride1_1217_gold == True:
            print("You may ride solo (Golden Passport age 12-17)")
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
        if ride1_18_plus or ride2_18_plus:
            print("You may both ride (Adult)")
        elif ride1_1217_gold == "yes" or ride2_1217_gold == "yes":
            print("You may both ride (Golden Passport)")
        elif ride1_14_plus:
            if ride2_16_plus:
                print("You may both ride (14+ yrs / 16+ yrs)")
        elif ride2_14_plus:
            if ride1_16_plus:
                print("You may both ride (16+ yrs / 14+ yrs)")
        else:
            print("You may not ride together (No adult, golden ticket, or don't meet the 16yr / 14yr requirement.)")