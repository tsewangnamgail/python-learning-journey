import math

# Volume of Cylinder
r = float(input("Enter radius of cylinder: "))
h = float(input("Enter height of cylinder: "))

cylinder_volume = math.pi * r * r * h

# Volume of Sphere
r2 = float(input("Enter radius of sphere: "))

sphere_volume = (4 / 3) * math.pi * r2 ** 3

# Area of Triangle
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))

triangle_area = 0.5 * base * height

print("Volume of Cylinder:", cylinder_volume)
print("Volume of Sphere:", sphere_volume)
print("Area of Triangle:", triangle_area)