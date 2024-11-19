accounts = []
balances = []
listing = True
entry1 = ""
entry2 = ""

print("enter the names and balances of bank accounts (type: quit to finish):")
while listing:
    entry1 = input("What is the name of this account? ")
    if entry1 != "quit":
        accounts.append(entry1)
        entry2 = input("What is the balance?: ")
        balances.append(entry2)
    else:
        listing = False

print()
print("The shopping list with indexes is:")
for i in range(len(shopping)):
    print(f"{i}. ", end="")
    print(shopping[i])