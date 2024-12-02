# Web Automation - Selenium
# Page - We are going to automate

class VWOLoginPage:

    def __init__(self,email_arg,password_arg):
        self.email = email_arg
        self.password= password_arg

    def login_confirm(self):
        if self.email == "gajendranm.be@gmail.com" and self.password == "Pass123" :
            print("Allowed, Login Success")
        else:
            print("Login Failed")

# email = input("Enter the email \n")
# password = input("Enter the password \n")
#

# email = #Read from test data - Excel, CSV or ENV file
# password = #Read from test data - Excel,CSV or ENV file


# vwo_obj = VWOLoginPage(email, password)
# vwo_obj.login_confirm()

Gajen = VWOLoginPage("gajendranm.be@gmail.com","Pass123")
Gajen.login_confirm()