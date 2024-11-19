friends = []
listing = True
entry = ""


while listing:
    entry = input("Type the name of a friend: ")
    if entry != "end":
        friends.append(entry)
    else:
        listing = False

print()
print("Your friends are:")
for friend in friends:
    print(friend)
