# wrie a python program to calculate the area of a circle given its radius using the formula
#  area=pi*r^2
import math

#Step 1 Figure out the input and output
#input -> r -> data type -> float
#pi =3.14
# power - pow or ** -> any
# o/p -> float - area, print area

#Step2
# rough logic= area = 3.14 * pow(r,2)

#Step3
radius =  float(input("Enter the radius of the circle\n"))
print(radius)
area=3.14 * (radius**2)
print(f"Area of the circle: {area}")

# print(math.pi)
# area = math.pi * math.pow(radius,2)
# print(f"Area of circle {area}")

# print(3.14  * (float(input("Enter radisu of the circle\n"))**2))

