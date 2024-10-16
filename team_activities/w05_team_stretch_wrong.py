grade_percent = float(input("What is your grade percentage?"))

#calculate letter grade
if grade_percent >= 93:
    letter = "A"
elif grade_percent >= 90:
    letter = "A-"
elif grade_percent >= 87:
    letter = "B+"
elif grade_percent >= 83:
    letter = "B"
elif grade_percent >= 80:
    letter = "B-"
elif grade_percent >= 77:
    letter = "C+"
elif grade_percent >= 73:
    letter = "C"
elif grade_percent >= 70:
    letter = "C-"
elif grade_percent >= 67:
    letter = "D+"
elif grade_percent >= 63:
    letter = "D"
elif grade_percent >= 60:
    letter = "D-"
else:
    letter = "F"


print(f"The letter grade is {letter}")
#determine passing status
if grade_percent < 70:
    print("You can get it next time. Buckle up and see a tutor")
elif grade_percent >=70:
    print("Nice job, you passed")
else:
    print("I don't know how you got that, man")