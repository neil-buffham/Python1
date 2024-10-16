grade_percent = float(input("What is your grade percentage?"))

#calculate letter grade
if grade_percent >= 90:
    print("The letter grade is A")
elif 80 <= grade_percent < 90:
    print("The letter grade is B")
elif 70 <= grade_percent < 80:
    print("The letter grade is C")
elif 60 <= grade_percent < 70:
    print("The letter grade is D")
else:
    print("The letter grade is F")

#determine passing status
if grade_percent < 70:
    print("You can get it next time. Buckle up and see a tutor")
elif grade_percent >=70:
    print("Nice job, you passed")
else:
    print("I don't know how you got that, man")