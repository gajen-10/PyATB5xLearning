class Calc:

    def sum(self,*args):

        for i in args:
            print(i)

c=Calc()
c.sum(10)
c.sum(10,20)
c.sum(3,4,5,3)
c.sum(34,56,323,21)