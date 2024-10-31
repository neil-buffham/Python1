# Written by Neil Buffham. Information on code structuring practices gathered from online sources, but all code was written myself.
#ad_lib.py - Working version that runs the text to the edge of the screen. I'm working on developing one that doesn't split words at the end


#---------------------------------------------------------------------------------------------------------
# Test values to get the formatting right on the final story
'''
person_1 = "Frog"
person_2 = "Toad"
potime_1 = "1 year"
potime_2 = "20 minutes"
number_0 = "98"          #These need to be formatted to be strings, not integers. it's causing problems.
number_1 = "300"
number_2 = "24"
valuable_item = "golden handbag"
location_1 = "Germany"
location_2 = "Australia"
celeb_1 = "Oprah Winfrey"
celeb_2 = "George Bush"
celeb_3 = "Elon Musk"
fictperson_1 = "Dobby"
interjection_1 = "shoot"

print("-"*40)
print("These values have been substituted for user input to speed up the troubleshooting process:")
print("-"*40)
print("person_1 = " + person_1 )
print("person_2 = " + person_2)
print("potime_1 = " + potime_1)
print("potime_2 = " + potime_2)
print("number_0 = " + number_0)
print("number_1 = " + number_1)
print("number_2 = " + number_2)
print("valuable_item = " + valuable_item)
print("location_1 = " + location_1)
print("location_2 = " + location_2)
print("celeb_1 = "+ celeb_1)
print("celeb_2 = " + celeb_2)
print("celeb_3 = " + celeb_3)
print("fictperson_1 =" + fictperson_1)
print("interjection_1 = " + interjection_1)
'''
#---------------------------------------------------------------------------------------------------



# Welcome Messgae
print("-"*40)
print("Welcome to StoryGen1*")
print()
print("*(Any trademark infringement is unintentional)")
print("-"*40)
print()
print("Please provide the following information:")
print()



# information collection system
person_1 = input("A name: ")
person_2 = input("Another name: ")
potime_1 = input("A period of time: ")
potime_2 = input("A shorter period of time: ")
number_0 = input("A number from 0-999: ")
print("-"*40)
print("5/15 complete")
print("-"*40)
number_1 = input("Another number: ")
number_2 = input("One more number: ")
valuable_item = input("A valuable Item: ")
location_1 = input("A distant location: ")
location_2 = input("Another distant location: ")
print("-"*40)
print("10/15 complete")
print("-"*40)
celeb_1 = input("Name of a famous person: ")
celeb_2 = input("Name of another famous person: ")
celeb_3 = input("One last famous person: ")
fictperson_1 = input("Name of a book/movie character: ")
interjection_1 = input("An interjection: ")



#Capitalization of names and proper nouns. I used ".title" instead of "".capitalize" in case people put first and last names.
    # this could lead to something like "the netherlands" being displayed as "The Netherlands" mid-sentence, but I don't know how to fix that yet 
    # and am not going to find out today. haha sorry
person_1 = person_1.title()
person_2 = person_2.title()
potime_1 = potime_1.lower()
potime_2 = potime_2.lower()
valuable_item = valuable_item.lower()
location_1 = location_1.title()
location_2 = location_2.title()
celeb_1 = celeb_1.title()
celeb_2 = celeb_2.title()
celeb_3 = celeb_3.title()
fictperson_1 = fictperson_1.title()
interjection_1 = interjection_1.lower()



#Divider/story delivery
print("-"*40)
print("Thanks for playing! Here is your finished story:")
print("-"*40)



#  Story split into sections so that on the go word/value changes can be troubleshot by line.
output0 = (person_1 + " and their friend " + person_2 + " have known each other for " + potime_1 + ", but have only been friends for " + potime_2 + ", because of the time that ")
output1 = (person_2 + " threw " + person_1 + "'s " + valuable_item + " out of a window. Given the strength of their friendship, they decided that it was only fitting to travel to ")
output2 = (location_1 + " together. Because of their mutual dislike of travel scenes in literature, they agreed to warp time in a smooth ")
output3 = (number_0 + " minute montage to get there faster. This would later come into question in their legal trial, which was overseen by ")
output4 = (celeb_1 + ". While in " + location_1 + ", they inadvertently broke " + number_1 + " laws, not because they wanted to, but because ")
output5 = (celeb_2 + " was in town and they fell into a violent rampage under their charismatic spell. This has largely been considered a bad move on " + person_1 + " and " + person_2 +"'s part. Despite their close friendship, ")
output6 = (person_1 + " cracked under interrogation and ratted out " + person_2 + " for the crimes they had committed together. " + interjection_1.capitalize() + "! Yelled " + person_1 + " when they found out about this betrayal. " + "However, all ")
output7 = (number_2 + " minutes of footage from the interrogation room cameras were corrupted and the officer interrogating had to return to ruling ")
output8 = (location_2 + " so the admission wasn't used in court. Ultimately, " + celeb_3 + " decided to pardon both " + person_1 + " and " + person_2 + ", as well as " + fictperson_1)
output9 = (" on all accounts. In the end, the giant eagles from Lord of the Rings arrived and returned all three of them home. This was lucky, as ")
output10 = (person_2 + " had an entry in a " + valuable_item + " throwing contest later that day that they didn't want to miss.")



#  Print all the stuff combined together
print(output0 + output1 + output2 + output3 + output4 + output5 + output6 + output7 + output8 + output9 + output10)