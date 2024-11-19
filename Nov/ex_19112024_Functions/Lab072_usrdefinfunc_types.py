# user defined
# 1. They can't return --> non return
# 2. They can return something
# 3. No Return type and with default argument
# 4. Argument + return type
#1. They can't return --> non return
# No Return and No parameter / Arguments - NRNP

def greet():
    print("Hello")

greet()

# 2. No Return Type and with argument

def greet_by_name(name):
    print("Hello, ", name)

greet_by_name("Gajendran")


# 3. No Return type and with default argument

def say_hello_default_arg(name="Gajen"):
    print("Hello ", name.upper())

say_hello_default_arg("Fund")
say_hello_default_arg()


def multiple_args(name1="A",name2="B"):
    print("Multiple --->", name1, name2)

multiple_args()
multiple_args(name1="Gajen")
multiple_args(name1="Gajen",name2="dran")


# 4. Argument + return type

def sum_of_two(a,b):
    return a+b

result= sum_of_two(2,8)
print(result)

def sum_of_two_number_with_default(num1=100, num2=200):
    return  num1+num2

result= sum_of_two_number_with_default(num1=32,num2=34)
print(result)
result = sum_of_two_number_with_default()
print(result)