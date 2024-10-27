loan_size = int(input("On a scale from 1-10 how large is the loan?"))
credit_history = int(input("On a scale from 1-10, how good is your credit history?"))
income = int(input("On a scale from 1-10, how high is your income?"))
down_payment = int(input("On a scale from 1-10, how large is your down payment?"))


#Loan qualification calculations
if loan_size >= 5:
    if credit_history and income >= 7:
        eligible = True
    elif credit_history or income >=7:
        if down_payment >= 5:
            eligible = True
        else:
            eligible = False
    else:
        eligible = False
elif loan_size < 4:
    eligible = False
elif income or down_payment >= 7:
    eligible = True
elif income and down_payment >= 4:
    eligible = True
else:
    eligible = False


#Decision output portion:
if eligible:
    print("Your loan application has been approved")
elif not eligible:
    print("Your loan applicaiton has been denied")
else:
    print("Error")