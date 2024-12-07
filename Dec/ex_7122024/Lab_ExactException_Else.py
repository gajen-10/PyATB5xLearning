try:
    n1=int(input("Enter the number1:"))
    n2=int(input("Enter the number2:"))
    c=n1/n2


except ZeroDivisionError as e:
    print(e)

except ValueError as e:
    print(e)

else:
    print("Reslut", c)
