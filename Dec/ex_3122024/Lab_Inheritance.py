class Father:

    key = "1 BHK"

    def car(self):
        print("Father has car --> Alto !!")
        print(self.key)

class son:

    key2 = "2 BHK"

    def suv(self):
        print("MG Hector,  Black")
        print(self.key2)

F = Father()
F.car()

s = son()
s.suv()