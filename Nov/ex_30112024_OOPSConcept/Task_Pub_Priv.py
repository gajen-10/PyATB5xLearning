class emp:

    def __init__(self,name,address,empaccno):
        self.name = name
        self.addr = address
        self.__empaccno = empaccno

    def empdetails(self):
        print(self.name)
        print(self.addr)
        print(self.__empaccno)
        self.__empbankpwd()

    def __empbankpwd(self):
        print(self.__empaccno)
        print("empcardnumber")

emp1 = emp("Gajen","chennai","232312")
emp1.empdetails()
#emp1.__empbankpwd()