class person:
# Attribute - What you have?
    id= None
    name= None
    age=None
    email= None
    height= None
    gender = None
    phone_no = None
    address = None


#Behaviour - what you can do?

    def talk(self):
        print("I can talk")

    def sleep(self, name): # Arg with no Return
        print("Sleep", name)

    def sleep2(self, name): # Arg wih Return
        print("I am a Method !!")
        return None

    def walk(self):
        print("I am Walking")

    def walk_return(self):  # No Arg with Return
        return ("I am walking")



# Create an object of the class
# ObjectRef = ClassName() -> Object
geeta = person()
geeta.name = "Geeta Sharma"
geeta.gender= "Female"