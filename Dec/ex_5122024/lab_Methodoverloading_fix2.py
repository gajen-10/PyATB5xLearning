class parent:

    def home(self):
        print("1 BHK")


class son(parent):

    def town(self):
        print("occupied entire town")
    def home(self):
        print("3 BHK")


s= son()
s.town()
s.home()