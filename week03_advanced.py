#Written by Neil Buffham

#input portion
child_price = float(input("What is the price in $ of a children's meal? "))
adult_price = float(input("What is the price in $ of an adult's meal? "))
drink_price = float(input("What is the price in $ of a fountain drink? "))
child_qty = int(input("How many children? "))
adult_qty = int(input("How many adults? "))
drink_qty = int(input("How many total drinks? "))
tax_rate = 0.01*float(input("What the the sales tax rate? "))
print()

#calculations
sub_child = child_qty*child_price
sub_adult = adult_qty*adult_price
sub_drink = drink_qty*drink_price
subtotal = round(sub_child+sub_adult+sub_drink, 2)

tax = tax_rate * subtotal
tax1 = float(f"{tax:.2f}")
total = float(f"{(tax1 + subtotal):.2f}")

#Output totals
print(f"Subtotal: ${subtotal}")
print(f"Sales tax: ${tax1}")
print(f"Total: ${total}")
print()

#ask for payment and calculate change
tender = float(input("What is the payment amount? "))
change = tender-total
print(f"Change: ${change:.2f}")
