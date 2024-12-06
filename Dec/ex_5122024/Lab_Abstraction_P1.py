from abc import ABC, abstractmethod

class ANimal():

    def __init__(self,name):
        self.name= name

    @abstractmethod
    def makesound(self):
        pass

class dog(ANimal):
    def makesound(self):
        print("Bow Bow...")

d=dog("pitbull")
d.bark()
