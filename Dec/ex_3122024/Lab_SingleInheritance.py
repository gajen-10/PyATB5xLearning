class Father:

    key = "1 BHK"

    def car(self):
        print("Father has a car ---> Alto !!")
        print(self.key)

class Son(Father):

    key2 = "2BHK"

    def suv(self):
        print("MG Hector, Black")
        print(self.key2)


f = Father()
f.car()

s = Son()
s.suv()
s.car()