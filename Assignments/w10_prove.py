menu_items = ["1. Add item", "2. View cart", "3. Remove item", "4. Compute total", "5. Quit"]
menu_numbers = ["1","2","3","4","5"]
cart_contents = []
cart_prices = []
selection = ""
in_menu = True

adding_to_cart = False
viewing_cart = False
removing_item = False
computing_total = False

running = True
valid_selection = False


print("Welcome to the Shopping Cart Program!")
while running:
        

    while in_menu:
        adding_to_cart = False
        viewing_cart = False
        removing_item = False
        computing_total = False
        selection = ""
        unformatted_selection = ""

        running = True
        valid_selection = False
        #Menu:
        print()
        print("Please select one of the following:")
        for option in menu_items:
            print(option)
        print()
        while not valid_selection:
            selection = input("Please enter an action: ")
            if selection not in menu_numbers:
                valid_selection = False
            elif selection in menu_numbers:
                valid_selection = True
         
        #this if statement double verifies, and probably isn't needed.
        #The interior of the if statement is needed, it selects the option.
        if selection in menu_numbers:
            if selection == "1":
                adding_to_cart = True
                in_menu = False
                selection = ""
            if selection == "2":
                viewing_cart = True
                in_menu = False
                selection = ""
            if selection == "3":
                removing_item = True
                in_menu = False
                selection = ""
            if selection == "4":
                computing_total = True
                in_menu = False
                selection = ""
            if selection == "5":
                running = False
                in_menu = False
                selection = ""
                print("Thank you. Goodbye.")
        else:
            selection = int(input("Please enter an action: "))


    #Option 1: Add to cart function:
    while adding_to_cart:
        adding_item = input(("What would you like to add? "))
        adding_cost = float(input(f"What is the price of '{adding_item}'? "))
        cart_contents.append(adding_item)
        cart_prices.append(adding_cost)
        print(f"'{adding_item}' has been added to the cart.")
        adding_to_cart = False
        in_menu = True

    #Option 2: View Cart function:
    while viewing_cart:
        print("The contents of the cart are: ")
        for i in range(len(cart_contents)):
            j = i + 1
            print(f"{j}. ", end = "")
            print(cart_contents[i], end = "")
            print(" - $", end = "")
            print(f"{cart_prices[i]:.2f}")
        print()
        viewing_cart = False
        in_menu = True

    #Option 3: Remove item function:
    while removing_item:
        remove_j = int(input("Which item would you like to remove? "))
        remove_i = (remove_j - 1)

        #section to check if that is a valid list index
        valid_index = len(cart_contents)
        #print(f"len(cart_contents) = {valid_index}")
        if remove_i >= valid_index:
            print("Sorry, that is not a valid item number.")
        elif remove_i < 0:
            print("Sorry, that is not a valid item number.")
        else:
            print(f'Item "{cart_contents[remove_i]}" removed.')
            cart_contents.pop(remove_i)
            cart_prices.pop(remove_i)

        print()
        remove_j = ""
        remove_i = ""
        removing_item = False
        in_menu = True

    #Option 4: Compute total function:
    while computing_total:
        total = sum(cart_prices)
        num_of_items = len(cart_contents)
        avg_cost_unformatted = total / num_of_items
        avg_cost = f"{avg_cost_unformatted:.2f}"
        print(f"The total price of the items in the shopping cart is ${total:.2f}")
        print(f"Number of items: {num_of_items}")
        print(f"Average cost: ${avg_cost}")
        print()
        computing_total = False
        in_menu = True


