a= 10

class person:
    b=11 # Instance Variable - Belong to class

    def prin_info(self):
        c = 20 # Local Variabe
        print(c)
        print(self.b)

        global a
        print(a)

        a = "Hello"
        print(a)



object_ref= person()
object_ref.prin_info()