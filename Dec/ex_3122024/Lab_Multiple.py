class father:

    def home(self):
        print("THis is father home")
    def father_money(self):
        return 5

class mother:

    def home(self):
        print("THis is Mother home")
    def mother_money(self):
        return 7

class son(mother,father):

    def print_info(self):
        print("son")

s = son()
print(s.father_money())
print(s.mother_money())
s.home()
