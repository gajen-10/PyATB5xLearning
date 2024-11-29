class Clac:

    def __init__(self):
        print("DC")


    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self,a,b):
        return  a/b


calc_ref= Clac()
a= float(input("Enter the value of A: "))
b= float(input("Enter the value of B: "))

output_sum = calc_ref.sum(a , b)
output_sub = calc_ref.sub(a , b)
output_mul = calc_ref.mul(a , b)
output_div = calc_ref.div(a , b)

print(output_sum,output_sub,output_mul,output_div)