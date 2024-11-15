
# Logic Building Formula

# 1 --> User Inputs --> Score or marks -> int
# 2 -> O/p _> str -> A or B...



num1= int(input("Enter the Score\n"))

if num1 >= 90 and num1 <= 100:
    print(" A grade !!!")
elif num1 >= 80 and num1 <= 89:
    print("B Grade !!!")
elif num1 >= 70 and num1 <= 79:
    print("C Grade !!!")
elif num1 >= 60 and num1 <= 69:
    print("D Grade !!!")
elif num1 >= 100 or num1 <= -1:
    print("You can't get grade")
else:
    print("Grade F !!!")