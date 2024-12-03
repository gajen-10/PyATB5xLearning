class grandfather:

    gold = "2Kg"

    def bhk1(self):
        print("1 BHK")

class father(grandfather):

    diamond = "22 Karat"

    def bhk2(self):
        print("2 BHK")


class son(father):

    btc = "1btc"

    def bhk3(self):
        print("3 BHK")

s = son()
s.bhk3()
s.bhk2()
s.bhk1()

f = father()
f.bhk2()
print(f.diamond)

g = grandfather()
g.bhk1()
print(g.gold)