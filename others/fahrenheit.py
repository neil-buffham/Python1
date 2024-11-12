#ask the user for a value in Fahrenheit, format it as a float
fahrenheit_temp = float(input("What is the temperature in Fahrenheit? "))

#Convert the float value to celsius
celsius_temp = ((fahrenheit_temp - 32) * (5 / 9))

#print the converted value
print(f"The temperature in Celsius is {celsius_temp:.1f} degrees")