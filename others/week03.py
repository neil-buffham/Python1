child_price = float(input("What is the price in $ of a children's meal? "))
adult_price = float(input("What is the price in $ of an adult's meal? "))
child_qty = int(input("How many children? "))
adult_qty = int(input("how many adults? "))
tax_rate = 0.01*float(input("What the the sales tax percent? "))
print()

#calculations
sub_child = child_qty*child_price
sub_adult = adult_qty*adult_price
subtotal = sub_child + sub_adult

tax = tax_rate * subtotal
tax1 = round(tax, 2)
total = tax1 + subtotal
total1 = round(total, 2)

#Output totals
print(f"Subtotal: ${subtotal}")
print(f"Sales tax: ${tax1}")
print(f"Total: ${total1}")
print()

#ask for payment and calculate change
tender = float(input("What is the payment amount? "))
change = tender-total
change1 = round(change, 2)
print(f"Change: ${change1}")


'''
In a bit of research online, some people recommended using floats only for the cent value, and restricting dollar values to integers.
This would be more secure, although this program won't be used on actual money. Also, I'm not proud of using the round function on 
lines 14, 16, and 27, but it was still holding onto .000000000000x cent values from the tax formatting, even down on line 28.
'''