print("___Start Program___")

try:
    num1=int(input("Enter the number1:"))
    num2=int(input("Enter the number2:"))
    c=num1/num2
    print("Result is ",c)
except Exception as e:
    print(e)

print("___End of the program___")