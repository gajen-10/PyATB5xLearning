# Checking for a Leap Year

# Leap day occurs in each year that is a multiple of 4, except for years evenly divisible by 100 but not by 400.
#  2024 → Yes

Leap_yr = int(input("Enter the year : \n"))

if (Leap_yr % 4 == 0 and Leap_yr % 100 != 0) or (Leap_yr % 400 == 0):
    print("Entered year is Leap Year")
else:
    print("Entered year is not Leap Year")
