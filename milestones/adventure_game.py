'''

choice_1_input = input("There are two doors in front of you, do you chose the LEFT or RIGHT door?")
choice_1 = choice_1_input.lower()

if choice_1 == "left":
    choice_2 = input("The door creaks as you open it, and a couple tiled steps lead you around a corner and into a large room. It is dark, and you can only make out a little of the floor in front of you. Feeling around on the wall you find a light switch. It lets out a distinctly old clunk as you flip it, and after some hesitation an uneven cluster of flourescent light banks flicker on, revealing a large swimming pool, half full of murky water. You can see another switch bank on the far wall. Do you choose to JUMP in, or GO look at the light switches? ")
elif choice_1 == "right":
    choice_2 = input("You open the right door, and the floor creaks loudly. Looking down you can tell it hasn't seen use for a decade, or tender care for quite some time longer than that. Stepping Gingerly, you proceed across the room, wincing with each loud creak. The floor caves below you, and you tumble for a ways. A sharp pain in you ankle announces you have reached the bottom, and as you look up you notice two figures standing in front of you. One is holding a scythe and wearing a dark hooded robe that hides his face, and the other looks like a humanoid robot in a black morph suit. Do you choose to approach the SCYTHE holding figure or the ROBOT? ")
else: 
    choice_1_input = input("Please select either LEFT or RIGHT: ")
    print("At this point it would loop back to the regular story, but I am not going to program that today.")
'''




level_1ab = "There are two doors in front of you, do you chose the LEFT or RIGHT door? "

level_1a_2ab = "The door creaks as you open it, and a couple tiled steps lead you around a corner and into a large room. It is dark, and you can only make out a little of the floor in front of you. Feeling around on the wall you find a light switch. It lets out a distinctly old clunk as you flip it, and after some hesitation an uneven cluster of flourescent light banks flicker on, revealing a large swimming pool, half full of murky water. You can see another switch bank on the far wall. Do you choose to JUMP in, or GO look at the light switches? "

level_1a_2a_3ab = "You take the plunge. The water stings your eyes, and a minute or two after you surface the debris in the water settles. You dip your head under again, and notice a fish swimming lazily on the far side of the pool, above a chain coiled on what appears to be a drain plug. Do you GRAB the fish or PULL the drain? "

end_a = "The fish slips out of your grasp (it’s smooth in every direction) but you wrestle it back. It ominously turns its head towards you, whispers the most esoteric knowledge you have ever heard, and dissolves into the grungy water. "

end_b = "You swim over to the drain, and tug on it first gently, then vigorously. Nothing happens. Then, you notice the chain follows up the side of the pool. You pull yourself up onto the edge of the pool, and notice a pulley on the wall towards the ceiling and a crank at chest level with some chain coiled on it. The pulley and crank let out a series of clunks as you turn them, and eventually the pool begins to drain. … Hours later you realize that your socks are just not going to dry. For some reason they won’t come off of your feet, and they continually seep murky water. "

level_1a_2b_3cde = "As you approach the light switches on the far wall you notice a square grey tarp covering a roughly three foot square portion of the wall, just off of the floor. It crumbles slightly as you peel it back, revealing a dusty slide that curves out of sight deep into the wall. Letting the tarp fall back down, you take a closer look at the light switches. One matches the older style you saw earlier, and one seems straight out of a mad scientist lab. Do you choose to flip the LEVER, flip the regular SWITCH, or jump in the SLIDE?"

end_c = "With a rumbling creak the roof slides open and blinding light and thundering noise from helicopters flood in simultaneously. You hear someone yell “FBI, GET DOWN!” and something sharp hits you in the neck. You notice someone with a blowgun on the roofline as your vision blurs to black. "

end_d = "The switch has a similar sound to the last one you flipped, and half of the already sparse light banks shut off. You can’t seem to find a way back out of the room, as when you return to the initial room there isn’t a door out. The other door is still there though … "

end_e = "You hop in the slide, and get most of the way down before friction stops you. Scooting around the last bend in the slide you see your old pals in an even larger pool, with the sound of gentle splashes and the occasional “Marco!” echoing throughout the room. "



level_1b_2cd = "You open the right door, and the floor creaks loudly. Looking down you can tell it hasn't seen use for a decade, or tender care for quite some time longer than that. Stepping Gingerly, you proceed across the room, wincing with each loud creak. The floor caves below you, and you tumble for a ways. A sharp pain in you ankle announces you have reached the bottom, and as you look up you notice two figures standing in front of you. One is holding a scythe and wearing a dark hooded robe that hides his face, and the other looks like a humanoid robot in a black morph suit. Do you choose to approach the SCYTHE holding figure or the ROBOT? "

level_1b_2c_3fgh = "You approach the scythe-wielding figure, and he begins briskly walking down a dark hallway behind and to his left, the scythe making a hollow thud against the floor as he goes. You follow slowly at first, but begin to catch up. Do you choose to ask his NAME, where he is GOING, or TAP him on the shoulder? "

end_f = "You can feel cold air drift from his hood as he suddenly stops. His face still concealed, he says: “I’m you, or at least I will be you. No more questions. We must leave this place. "

end_g = "Without hesitating, he speaks with a deep, rocky voice. “Back. You needed another chance. It’s okay, many need it but few are granted the opportunity. It wasn’t easy to arrange this, don’t make me regret it."

end_h = "Your hand passes straight through his shoulder, and your body is violently pulled into the space you thought he was occupying. You can feel yourself becoming taller, your clothes morphing, your shirt smoothly stretching into a robe, the hood sliding over your head. Moments later, all you can feel is the scythe in your hand as all other senses of touch and texture slip numbly out of existence. The continued thunk of wood against stone makes you believe you are still walking but the experience is otherwise surreal. You finally reach a door, and glancing down realize that you, or rather your hands, are holding a wispy sign with a single word written on it. Realization hits like a cold slap as you realize what it says, and wish you didn’t recognize the name. "

level_1b_2d_3ij = "With motion punctuated by motor whine and the metallic thunk of its footsteps, the robot turns and motions for you to follow. A little bit creeped by the last room, you hesitantly proceed. The hallway leads outside, and a sleek car, difficult to make out in the dark, is waiting with the door open. The robot slides into the far seat, and you take the remaining one. A moment of realization hits you as the car pulls away. Do you decide to ask WHO sent the robot, or WHERE you are going? "

end_i = "With a calculated hesitation, the robot calmly responds “Aperture Science”, and hands you an orange jumpsuit."

end_j = "There is silence for just long enough you wonder if the robot heard you. Finally, its “head” turns to face you, and an oddly calm voice responds: “The moon.” A second pane of glass slides up against the inside of the window, and with a mixture of rumbles, the car shakily lifts off of the ground. "



#diagnostic print values to test variable formatting
'''
print(f"level_1ab: {level_1ab}")
print(f"level_1a_2ab: {level_1a_2ab}")
print(f"level_1a_2a_3ab: {level_1a_2a_3ab}")
print(f"end_a: {end_a}")
print(f"end_b: {end_b}")
print(f"level_2a_2b_3cde: {level_2a_2b_3cde}")
print(f"end_c: {end_c}")
print(f"end_d: {end_d}")
print(f"end_e: {end_e}")
print(f"level_1b_2cd: {level_1b_2cd}")
print(f"level_1b_2c_3fgh: {level_1b_2c_3fgh}")
print(f"end_f: {end_f}")
print(f"end_g: {end_g}")
print(f"end_h: {end_h}")
print(f"level_1b_2d_3ij: {level_1b_2d_3ij}")
print(f"end_i: {end_i}")
print(f"end_j: {end_j}")
'''

level_1_active = False
level_2_active = False
level_3_active = False
level_1 = False
level_1_fail = False

level_1_select_a = False
level_1_select_b = False

level_2_select_a = False
level_2_select_b = False
level_2_select_c = False
level_2_select_d = False

level_2 = False
level_2_fail = False

level_3_select_a = False
level_3_select_b = False
level_3_select_c = False
level_3_select_d = False
level_3_select_e = False
level_3_select_f = False
level_3_select_g = False
level_3_select_h = False
level_3_select_i = False
level_3_select_j = False

level_3 = False

#level_1 = str.lower(input(print(level_1ab)))
print(level_1ab)
level_1_active = True
level_1 = str.lower(input(""))


#---------------------------------------------------------------------------------------------
#Logical processing for Level one
#---------------------------------------------------------------------------------------------
while level_1_active:

    #Failure detection portion
    if level_1 == "left":
        level_1_fail = False
    elif level_1 == "right":
        level_1_fail = False
    elif level_1 != "left":
        if level_1 != "right":
                level_1_fail = True

    if level_1_fail:
        while level_1_fail:
            level_1 = str.lower(input("Please choose LEFT or RIGHT "))
            if level_1 == "left":
                level_1_fail = False
            if level_1 == "right":
                level_1_fail = False
    else:
        print()

    #Calculate decision and move to level 2
    if level_1 == "left":
        level_2_active = True
        level_1_select_a = True
        level_1_active = False
    elif level_1 == "right":
        level_2_active = True
        level_1_select_b = True
        level_1_active = False
    else:
        print("Error in logic of level 1")


#---------------------------------------------------------------------------------------------
#Logical processing for Level two
#---------------------------------------------------------------------------------------------
while level_2_active:
#First option from level 1:   ****************************************
    if level_1_select_a:
        print(level_1a_2ab)
        level_2 = str.lower(input())
#Failure detection poriton
        if level_2 == "jump":
            level_2_fail = False
        elif level_2 == "go":
            level_2_fail = False
        elif level_2 != "go":
            if level_2 != "jump":
                level_2_fail = True

        if level_2_fail:
            while level_2_fail:
                level_2 = str.lower(input("Please choose JUMP or GO "))
                if level_2 == "jump":
                    level_2_fail = False
                if level_2 == "go":
                    level_2_fail = False

        #calculate decision and move to step 3:
        if level_2 == "jump":
            level_2_select_a = True
            level_3_active = True
            level_2_active = False
        elif level_2 == "go":
            level_2_select_b = True
            level_3_active = True
            level_2_active = False
        else:
            print("Error in logic of level 2 a/b")

#Second option from Level 1:   ****************************************
    elif level_1_select_b:
        print(level_1b_2cd)
        level_2 = str.lower(input())

#Failure detection poriton
        if level_2 == "scythe":
            level_2_fail = False
        elif level_2 == "robot":
            level_2_fail = False
        elif level_2 != "scythe":
            if level_2 != "robot":
                level_2_fail = True

        if level_2_fail:
            while level_2_fail:
                level_2 = str.lower(input("Please choose SCYTHE or ROBOT "))
                if level_2 == "scythe":
                    level_2_fail = False
                if level_2 == "robot":
                    level_2_fail = False


        #Calculate decision and move to step 3:
        if level_2 == "scythe":
            level_2_select_c = True
            level_3_active = True
            level_2_active = False
        elif level_2 == "robot":
            level_2_select_d = True
            level_3_active = True
            level_2_active = False
        else:
            print("Error in logic of level 2 c/d")
    else:
        print("Error in logic of level 2")



#Troubleshooting from level 3 not being activated:
'''
print()
print("****************Completed logic level two")
print()
print(f'level_2_select_c: {level_2_select_a}')
print(f'level_3_active: {level_3_active}')
print(f'level_2_active: {level_2_active}')
'''


#---------------------------------------------------------------------------------------------
#Logical processing for Level three
#---------------------------------------------------------------------------------------------

while level_3_active:
#First option from level 2:   ****************************************
    if level_2_select_a:
        print(level_1a_2a_3ab)
        level_3 = str.lower(input())
    #Failure detection poriton
        if level_3 == "grab":
            level_3_fail = False
        elif level_3 == "pull":
            level_3_fail = False
        elif level_3 != "grab":
            if level_3 != "pull":
                level_3_fail = True

        if level_3_fail:
            while level_3_fail:
                level_3 = str.lower(input("Please choose GRAB or PULL "))
                if level_3 == "grab":
                    level_3_fail = False
                if level_3 == "pull":
                    level_3_fail = False

        #Calculate decision and select final output:
        if level_3 == "grab":
            level_3_select_a = True
            level_3_active = False
        elif level_3 == "pull":
            level_3_select_b = True
            level_3_active = False
        else:
            print("Error in logic of level 3 a/b")

#Second option from level 2:   ****************************************
    elif level_2_select_b:
        print(level_1a_2b_3cde)
        level_3 = str.lower(input())

#Failure detection poriton
        if level_3 == "lever":
            level_3_fail = False
        elif level_3 == "switch":
            level_3_fail = False
        elif level_3 == "slide":
            level_3_fail = False
        elif level_3 != "lever":
            if level_3 != "switch":
                if level_3 != "slide":
                  level_3_fail = True

        if level_3_fail:
            while level_3_fail:
                level_3 = str.lower(input("Please choose LEVER, SWITCH, or SLIDE "))
                if level_3 == "lever":
                    level_3_fail = False
                if level_3 == "switch":
                    level_3_fail = False
                if level_3 == "slide":
                    level_3_fail = False

        #Calculate decision and select final output:
        if level_3 == "lever":
            level_3_select_c = True
            level_3_active = False
        elif level_3 == "switch":
            level_3_select_d = True
            level_3_active = False
        elif level_3 == "slide":
            level_3_select_e = True
            level_3_active = False
        else:
            print("Error in logic of level 3 c/d/e")

#Third option from level 2:   ****************************************
    elif level_2_select_c:
        print(level_1b_2c_3fgh)
        level_3 = str.lower(input())

#Failure detection poriton
        if level_3 == "name":
            level_3_fail = False
        elif level_3 == "going":
            level_3_fail = False
        elif level_3 == "tap":
            level_3_fail = False
        elif level_3 != "name":
            if level_3 != "going":
                if level_3 != "tap":
                    level_3_fail = True

        if level_3_fail:
            while level_3_fail:
                level_3 = str.lower(input("Please choose NAME, GOING, or TAP "))
                if level_3 == "name":
                    level_3_fail = False
                if level_3 == "going":
                    level_3_fail = False
                if level_3 == "tap":
                    level_3_fail = False

        #Calculate decision and select final output:
        if level_3 == "name":
            level_3_select_f = True
            level_3_active = False
        elif level_3 == "going":
            level_3_select_g = True
            level_3_active = False
        elif level_3 == "tap":
            level_3_select_h = True
            level_3_active = False
        else:
            print("Error in logic of level 3 f/g/h")

#Fourth option from level 2:   ****************************************
    elif level_2_select_d:
        print(level_1b_2d_3ij)
        level_3 = str.lower(input())

#Failure detection poriton
        if level_3 == "who":
            level_3_fail = False
        elif level_3 == "where":
            level_3_fail = False
        elif level_3 != "who":
            if level_3 != "where":
                level_3_fail = True

        if level_3_fail:
            while level_3_fail:
                level_3 = str.lower(input("Please choose WHO or WHERE "))
                if level_3 == "who":
                    level_3_fail = False
                if level_3 == "where":
                    level_3_fail = False

        #Calculate decision and select final output:
        if level_3 == "who":
            level_3_select_i = True
            level_3_active = False
        elif level_3 == "where":
            level_3_select_j = True
            level_3_active = False
        else:
            print("Error in logic of level 3 i/j")
    else:
        print("Error in logic of level 3")
        level_3_active: False

#---------------------------------------------------------------------------------------------
#Logical processing for ending output
#---------------------------------------------------------------------------------------------
if level_3_select_a:
    print(end_a)
elif level_3_select_b:
    print(end_b)
elif level_3_select_c:
    print(end_c)
elif level_3_select_d:
    print(end_d)
elif level_3_select_e:
    print(end_e)
elif level_3_select_f:
    print(end_f)
elif level_3_select_g:
    print(end_g)
elif level_3_select_h:
    print(end_h)
elif level_3_select_i:
    print(end_i)
elif level_3_select_j:
    print(end_j)
else:
    print("Error: end not calculated")