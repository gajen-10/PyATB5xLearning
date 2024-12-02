class person:

    def __init__(self,name):
        self.name = name


    def walk(self):
        return self.name

amit = person("amit")
pramod = person("pramod")

print(amit.name)
print(pramod.name)

print("who is walking: ", amit.walk())
print("who is walking" , pramod.walk())