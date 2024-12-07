class LowbalanceException(Exception):

    def __init__(self,message):
        self.message = message
        super().__init__(message)

balance = 100
withdraw = int(input("Enter the withdrawal amount\n"))

if withdraw > balance:
    raise LowbalanceException("Enter amount less than balance amount")

else:
    print("Balance Amount:",(balance-withdraw))

