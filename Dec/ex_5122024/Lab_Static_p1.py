# static variable
# A static methos is a method that belongs to a
# class rather instnace of the class

class o:

    @staticmethod
    def sum(a,b):
        return a+b

    def sub(self,a,b):
        return a-b

obj_Ref=o()
result=obj_Ref.sub(7,3)
print(result)

print(o.sum(2,3))

