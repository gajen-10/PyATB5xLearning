


class car:


    def __init__(self):
        self.password ="Raj" #public instance variable
        self.__password_secure = "pass123"  # private instance variable

    def change_password(self):
        self.__password_secure="12345"

# object_ref = car()
# print(object_ref.password)
# object_ref.password = "RAM"
# print(object_ref.password)

object_ref = car()
print(object_ref.password)

print("---")

object_ref.change_password()
print(object_ref.__password_secure)