
import math

print("Welcome to the velocity calculaotr. Please enter the following:")
print()

mass = float(input("Mass (in kg): "))
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time = float(input("Time (in seconds): "))
density = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
cross_s_area = float(input("Cross sectional area (in m^2): "))
drag_constant = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))
print()

math0 = float((1 / 2) * density * cross_s_area * drag_constant)

math1 = (math.sqrt(mass * gravity * math0))
math2 = -1 * ((math1 / mass) * time)
math3 = math.exp(math2)
math4 = 1 - math3
math5 = math.sqrt((mass * gravity) / math0)
math6 = math5 * math4

output_c = f"{math0:.3f}"
output_velocity = f"{math6:.3f}"

print(f"The inner value of c is: {output_c}")
print(f"The veolocity after 10.0 seconds is: {output_velocity}")