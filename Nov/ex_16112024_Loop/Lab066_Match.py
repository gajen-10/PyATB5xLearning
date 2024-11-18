# Match statement --> # Switch in Java
# match the top and execute
# Pythn > 3.10

# match variable:
# case pattern1:
    # code block
# case pattern2:
    # code block

# Write a program to ask the user which browser he wants to  run automation.

browser_name = input("Enter the browser name: ")

match browser_name:
    case "firefox":
        print("Starting Firefox !!!")
    case "chrome":
        print("Execute the chrome code")
    case "edge":
        print("Execute the Edge code")
    case "safari":
        print("Execute the safari code")
    case _:
        print("Browser not found")