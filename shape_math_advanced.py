#original code built for the base requirements"
'''
square_side = float(input("What is the length of a side of the square? "))
square_area = square_side*square_side
print("The area of the square is:", square_area)
rectangle_width = float(input("What is the length of the rectangle? "))
rectange_length = float(input("What is the width of the rectangle? "))
rectangle_area = rectangle_width*rectange_length
print("The area of the rectangle is:", rectangle_area)
circle_radius = float(input("What is the radius of the circle? "))
circle_area = 3.14*(circle_radius*circle_radius)
print("The area of the circle is:", circle_area)
'''



#Importing math library
import math

#modified to involve cm^2 and use pi intead of "3.14"
square_side = float(input("What is the length in cm of a side of the square? "))
square_area = square_side*square_side
print("The area of the square is:", square_area, "cm^2", "or", (square_area/10000), "m^2")
rectangle_width = float(input("What is the length of the rectangle in cm? "))
rectange_length = float(input("What is the width of the rectangle in cm? "))
rectangle_area = rectangle_width*rectange_length
print("The area of the rectangle is:", rectangle_area, "cm^2", "or", (rectangle_area/10000), "m^2")
circle_radius = float(input("What is the radius of the circle in cm? "))
circle_area = math.pi*(circle_radius*circle_radius)
print("The area of the circle is:", circle_area, "cm^2", "or", (circle_area/10000), "m^2")



#Divider to distinguish the two sections
print("-"*40)
print("Beginning of single input section:")
print("-"*40)



#Single input and added measurement labels in cm^2 and m^2
side = float(input("What is the side length in cm? "))
square_area = side*side
circle_area = math.pi*(side*side)
cube_volume = (side*side*side)
sphere_volume = ((4/3)*math.pi*(side*side*side))

print("The area of a square with this side is:", square_area, "cm^2", "or", (square_area/10000), "m^2")
print("The area of a circle with this radius is:", circle_area, "cm^2", "or", (circle_area/10000), "m^2")
print("The volume of a cube with this side length is:", cube_volume, "cm^3", "or", (cube_volume/10000), "m^3")
print("the volume of a sphere with this radius is:", sphere_volume, "cm^3", "or", (sphere_volume/10000), "m^3")