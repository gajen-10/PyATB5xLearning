# problem to the max between two

# Logic Building formula

#1. user inputs -> two integers
#2. o/p -> int 1 which ever is greate max number it will return.
#31.4 or 43.23 --> float


num1 = float(input("Enter the num1\n"))
num2 = float(input("Enter the num2\n"))

if num1 >= num2:
    print("Max is ", num1)
else:
    print("Max is ", num2)

# Edge cases - num1 == num2 --> Handled.
# String -> User string--> Abc, ten --> we can handle this by try and except - we will learn this in future.
#-ve value ->