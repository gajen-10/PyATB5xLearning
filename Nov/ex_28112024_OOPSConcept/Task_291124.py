class PyATB:

    def __init__(self, name, age, city, job, experience):
        self.name = name
        self.age = age
        self.city = city
        self.job = job
        self.experience = experience

        # self.name=input("Enter the name: \n")
        # self.age=input("Enter the age: \n")
        # self.city=input("Enter the city: \n")
        # self.job=input("Enter the Job: \n")
        # self.experience=input("Enter the number of years os experience: \n")



    def print_Stud_Info(self):
        print(f"Name: {self.name}\n",f"Age: {self.age}\n",f"City: {self.city}\n",f"Job: {self.job}\n", f"Experience:{self.experience}\n")


stud1 = PyATB("Gajendran",28,"Chennai","Maual Tester",7)
stud2 = PyATB("Raj",28,"Kolkata"," Tester",2)
stud3 = PyATB("Eswar",35,"Calicut"," Automation Tester",12)
stud1.print_Stud_Info()
stud2.print_Stud_Info()
stud3.print_Stud_Info()