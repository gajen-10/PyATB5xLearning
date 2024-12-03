class A:

    def method(self):
        print("A Method")

class B:

    def method(self):
        print("B Method")

class c(A,B):
    pass

C_ref = c()
C_ref.method()