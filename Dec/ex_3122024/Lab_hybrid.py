class A:

    def methodA(self):
        return "A Method"

class B(A):

    def methodB(self):
        return "B Method"

class C(A):

    def methodC(self):
        return  "C method"

class D(B,C):

    def methodD(self):
        return "D Method"

d = D()
print(d.methodA())
print(d.methodB())
print(d.methodC())
print(d.methodD())