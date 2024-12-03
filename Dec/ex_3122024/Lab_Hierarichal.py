class father:

    def BHK1(self):
        print("1 BHK")

class Raj(father):

    def BHK2(self):
        print("2 BHK")

class Ram(father):

    def BHK3(self):
        print("3 BHK")

class lucky(father):

    def no_home(self):
        print("No House")

R = Ram()
R.BHK3()
R.BHK1()

Ra = Raj()
Ra.BHK2()
Ra.BHK1()

l = lucky()
l.no_home()
l.BHK1()
