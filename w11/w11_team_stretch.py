with open('w11\hr_system.txt') as hr_file:
    for item in hr_file:
        output = item.strip()
        output = output.split()
        salary = int(output[3])
        paycheck = salary / 24

        if output[2] == "Engineer":
            paycheck = paycheck + 1000
        
        salary = (f"{salary:.2f}")
        paycheck = (f"{paycheck:.2f}")


        print(f'{output[0]} (ID: {output[1]}), {output[2]} - ${paycheck}')

    print()
    print("End of document")