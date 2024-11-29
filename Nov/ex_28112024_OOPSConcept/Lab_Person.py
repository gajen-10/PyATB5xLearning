class person:

    def __init__(self):
        print("I will be caled")
        self.name= input("Enter the Name:\n")
        self.age= input("Enter the age: \n")
        self.phone= input("Enter the phone number: \n")
        self.occupation= input("Enter the occupation: \n")


    def name_of_the_function_to_display(self):
        print(f"Name is {self.name}", f"Age is {self.age}", f"Phone Number: {self.phone}" ,
              f"Occupation is {self.occupation}")


person1 = person()
person1.name_of_the_function_to_display()