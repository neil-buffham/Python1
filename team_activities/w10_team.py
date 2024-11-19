accounts = []
balances = []
listing = True
entry1 = ""
entry2 = ""

#--------------Account setup portion
print("Enter the names and balances of bank accounts (type: quit when done)")
while listing:
    entry1 = input("What is the name of this account? ")
    if entry1 != "quit":
        accounts.append(entry1)
        entry2 = float(input("What is the balance?: "))
        if entry2 == "quit":
            print("-----------------listing = False from entry2")
            listing = False
            #break
        elif entry2 != "quit":
            balances.append(entry2)
    else:
        listing = False


#------------Print out list of accounts and their indexes
print()
print("Account information: ")
for i in range(len(accounts)):
    print(accounts[i], end="")
    print(" - $", end = "")
    print(balances[i])

print()

#-------------Portion to find the max number:
max_index = 0
max_balance = balances[i]

for i in range (1,len(balances)):
    if balances[i] > max_balance:
        max_balance = balances[i]
        max_index = i

highest_name = accounts[i]

accounts_total = sum(balances)
accounts_average = sum(balances) / len(balances)
accounts_avg = format(accounts_average, ".2f")

#------------Output portion for account values
print(f"Total: ${accounts_total}")
print(f"Average: ${accounts_avg}")
print(f"Highest balance: {highest_name}: ${max_balance}")
print()

#------------Portion to update accounts:

chosen_index = ""
updating = True


while updating:
    updating_decision = input('Do you want to update an account?')
    if updating_decision == "yes":
        updating = True
    else:
        updating = False
        break
    chosen_index = int(input("What account index do you want to update? "))
    updated_balance = float(input("What is the new amount? "))
    balances[chosen_index] = updated_balance

    #Display updated accounts:
    print()
    print("Account information: ")
    for i in range(len(accounts)):
        print(accounts[i], end="")
        print(" - $", end = "")
        print(balances[i])
    print()
#Display updated accounts:
print()
print("Account information: ")
for i in range(len(accounts)):
    print(accounts[i], end="")
    print(" - $", end = "")
    print(balances[i])
print()