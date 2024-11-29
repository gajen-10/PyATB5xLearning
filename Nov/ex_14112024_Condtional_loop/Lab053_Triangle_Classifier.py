# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is
# equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

s1 = int(input("Enter length of first side: "))
s2 = int(input("Enter length of second side: "))
s3 = int(input("Enter length of third side: "))

if s1 > 0 and s2 > 0 and s3 > 0:
    if s1+s2 > s3 and s1+s3 > s2 and s2+s3 > s1:
        if s1 == s2 and s2 == s3:
            print("It is equilateral")
        elif (s1 == s2 and s1 != s3) or (s1 == s3 and s2 != s3) or (s2 == s3 and s1 != s2):
            print("It is Isosceles")
        elif (s1 != s2 and s2 != s3) and (s1 != s3):
            print(" It is scalene")