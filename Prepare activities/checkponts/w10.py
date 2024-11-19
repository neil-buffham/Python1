shopping = []
listing = True
entry = ""

print("Please enter the items of the shoping list (type: quit to finish):")
while listing:
    entry = input("Item: ")
    if entry != "quit":
        shopping.append(entry)
    else:
        listing = False

print()
print("The shopping list with indexes is:")
for i in range(len(shopping)):
    print(f"{i}. ", end="")
    print(shopping[i])