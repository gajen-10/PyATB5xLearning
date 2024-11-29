class Dog:
    #A
    name = None
    breed = None
    height = None
    weight = None
    # B

    def __init__(self,name,breed):
        print("PC")
        self.name = name
        self.breed = breed
    def bark(self):
        print("Barking")

    def sleep(self):
        print("Sleep")

    def talk(self):
        pass

#Object Ref
chow = Dog("chow","mastiff")
print(chow.name)
chow.sleep()
print(id(chow))

# Dog() - Object
# chow --> Object Ref

mow = Dog("mow","husky")
print(mow.name)
mow.sleep()
print(id(mow))


