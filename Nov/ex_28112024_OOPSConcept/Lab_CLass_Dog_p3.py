class Dog:
    #A
    name = None
    breed = None
    height = None
    weight = None
    # B

    def __init__(self):
        print("I will be called")
    def bark(self):
        print("Barking")

    def sleep(self):
        print("Sleep")

    def talk(self):
        pass

#Object Ref
chow = Dog()

# Dog() - Object
# chow --> Object Ref

mow = Dog()
bow = Dog()
rancho = Dog()

