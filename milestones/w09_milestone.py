menu_items = ["1. Add item", "2. View cart", "3. Remove item", "4. Compute total", "5. Quit"]
menu_numbers = ["1","2","3","4","5"]
cart_contents = []
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
        print(f"'{adding_item}' has been added to the cart.")
        adding_to_cart = False
        in_menu = True

    #Option 2: View Cart function:
    while viewing_cart:
        print("The contents of the cart are: ")
        for item in cart_contents:
            print(item)
        print()
        viewing_cart = False
        in_menu = True

    #Option 3: Remove item function:
    while removing_item:
        print("This is where you would remove items")
        print()
        removing_item = False
        in_menu = True

    #Option 4: Compute total function:
    while computing_total:
        print("This is where the total would be computed")
        print()
        computing_total = False
        in_menu = True


