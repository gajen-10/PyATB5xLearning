num1=int(input("Enter the number1:"))    # ValueError: invalid literal for int() with base 10: 'a'
num2=int(input("Enter the number2:"))
c=num1/num2                              # ZeroDivisionError: division by zero
print("Result is ",c)