
import math

print("Welcome to the velocity calculator. Please enter the following:")
print()
'''
mass = float(input("Mass (in kg): "))
gravity = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
time = float(input("Time (in seconds): "))
density = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
cross_s_area = float(input("Cross sectional area (in m^2): "))
drag_constant = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))
print()
'''
mass = float(5)
gravity = 9.8
time = float(1)
density = float(1.3)
cross_s_area = 0.001846
drag_constant = float(0.5)


math0 = float((1 / 2) * density * cross_s_area * drag_constant)

math1 = (math.sqrt(mass * gravity * math0))
math2 = -1 * ((math1 / mass) * time)
math3 = math.exp(math2)
math4 = 1 - math3
math5 = math.sqrt((mass * gravity) / math0)
math6 = math5 * math4

output_c = f"{math0:.3f}"
output_velocity1 = float(f"{math6:.3f}")

print(f"The inner value of c is: {output_c}")
print(f"The velocity after {time} seconds is: {output_velocity1}")


output_velocity2 = float(0)
output_velocity3 = float(0)

while output_velocity3 > output_velocity2:
    time2 = float(.01)
    
    math20 = float((1 / 2) * density * cross_s_area * drag_constant)

    math21 = (math.sqrt(mass * gravity * math0))
    math22 = -1 * ((math21 / mass) * time2)
    math23 = math.exp(math22)
    math24 = 1 - math23
    math25 = math.sqrt((mass * gravity) / math20)
    math26 = math25 * math24

    output_2c = f"{math20:.3f}"
    output_velocity1 = float(f"{math26:.3f}")
    time2 =time2 + 0.01

    output_c = f"{math20:.3f}"
    output_velocity2 = float(f"{math26:.3f}")
    
    #calculate output velocity 3____________________________
    time3 = float(.01)

    math31 = (math.sqrt(mass * gravity * math0))
    math32 = -1 * ((math21 / mass) * time3)
    math33 = math.exp(math22)
    math34 = 1 - math33
    math35 = math.sqrt((mass * gravity) / math0)
    math36 = math25 * math34

    output_2c = f"{math20:.3f}"
    output_velocity1 = float(f"{math26:.3f}")
    time2 =time2 + 0.01

    output_c = f"{math20:.3f}"
    output_velocity2 = float(f"{math26:.3f}")
    else:
        print(f"The terminal velocity is: {output_velocity2}")
        print(f"{time2} seconds")