# create program to sum of three number from the user input
# if user doesn't enter any number', use default as 100, 200, 300

n1=int(input("Enter the num1:"))
n2= int(input("Enter the num2: "))
n3= int(input("Enter the num3: "))

def sum_three_num(num1=100,num2=200,num3=300):

    return num1 + num2 + num3
    # result=num1+num2+num3
    # print(result)
# sum_three_num(23,45,23)
# sum_three_num()

result=sum_three_num(n1,n2,n3)
print(result)

result1=sum_three_num()
print(result1)

result2=sum_three_num()
result2=sum_three_num(13)
result2=sum_three_num(23,4,23)
result2=sum_three_num(23,43)

print(result2)