class parent:

    gold = "2kg"

    def BHK2(self):

        print("2 BHK")

class child(parent):
    diamond = "Diamond"

    def BHK3(self):
        print("3 BHK")

p = parent()
p.BHK2()

c = child()
c.BHK3()
c.BHK2()
print(c.gold)