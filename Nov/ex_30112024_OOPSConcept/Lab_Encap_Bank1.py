class Bank:

    def __init__(self,acc_no,balance):
        self.balance = balance # public
        self.__account_number = acc_no # Private


    def check_balance(self):
        print(self.balance)


    def deposit(self,amount):
        self.balance = self.balance + amount

    def public_function(self):
        self.__internal_private_method()
    def show_me_account_number(self, is_auth):
        if is_auth == True:
            print(self.__account_number)
        else:
            print("Not Allowed")

    def __internal_private_method(self):
        print("private Method, can be access by only class")

hdfc = Bank(723828323,1023)
hdfc.deposit(2122)
hdfc.check_balance()
print(hdfc.balance)
#print(hdfc.__account_number)
hdfc.show_me_account_number(False)
#hdfc.__internal_private_method()
hdfc.public_function()