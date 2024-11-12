numbers = []
new_number = ""

print("Enter a list of numbers, type 0 when finished.")

while new_number != 0:
    new_number = int(input("Enter number: "))
    if new_number != 0:
        numbers.append(new_number)

numbers_sum = sum(numbers)
numbers_average = sum(numbers)/len(numbers)
numbers_max = max(numbers)


positives = []
for number in numbers:
    if number > 0:
        positives.append(number)

numbers_pos_min = min(positives)


sorted_numbers = sorted(numbers)


print(f"The sum is: {numbers_sum}")
print(f"The average is: {numbers_average}")
print(f"The largest number is: {numbers_max}")
print(f"The smallest positive number is: {numbers_pos_min}")
print(f"The sorted list is:")
for number in sorted_numbers:
    print(number)