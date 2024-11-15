# Problem find the max between 3 numbers

# logic building

# User inputs - num1, num2, num3 -> int
#O/p -> int or String with max number.

#Logic ? If else - 1 condition,
# Syntax
# if condition 1:
#    print("do 1")
#elif condition 2:
# #   print("do 2")
# elif conditiion3:
#     print("do 3")
# else:
#     print("do for else")

num1=int(input("Enter the num1\n"))
num2 = int(input("Enter the num2\n"))
num3 = int(input("Enter the num3\n"))


if num1 > num2 and num1 > num3:
    print("Max is", num1)
elif num2 > num1 and num2 > num3:
    print("Max is", num2)
else:
    print("Max is",num3)