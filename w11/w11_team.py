with open('w11\hr_system.txt') as hr_file:
    for item in hr_file:
        output = item.strip()
        output = output.split()
        print(f'Name: {output[0]}, Title: {output[2]}')

    print()
    print("End of document")