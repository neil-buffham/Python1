#ask the user for the grade percent
grade_percent = float(input("What is your grade percentage?"))

#calculate letter grade
if grade_percent >= 90:
    letter = "A"
elif grade_percent >= 80:
    letter = "B"
elif grade_percent >= 70:
    letter = "C"
elif grade_percent >= 60:
    letter = "D"
else:
    letter = "F"

#calculate the + or - value for the grade
mod_calc = grade_percent % 10
if grade_percent > 90:
    letter_mod = ""
elif grade_percent <60:
    letter_mod = ""
elif mod_calc <3:
    letter_mod = "-"
elif mod_calc >7:
    letter_mod = "+"

# Output section:
# print(f"mod_calc value {mod_calc}")
print(f"The percentage is {grade_percent}")
print(f"The letter grade is {letter}{letter_mod}")
#determine passing status
if grade_percent < 70:
    print("You can get it next time. Buckle up and see a tutor")
else:
    print("Nice job, you passed")