from abc import ABC,abstractmethod

class Father(ABC):

    def __init__(self,name):
        self.name=name

    @abstractmethod
    def loan(self):
        pass

class son(Father):

    def loan(self):
        print("1L given")

s=son("Gajendran")
s.loan()