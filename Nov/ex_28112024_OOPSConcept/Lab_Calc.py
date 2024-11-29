class Clac:

    def __init__(self,a,b):

        self.a=a
        self.b=b


    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return  self.a/self.b


calc_ref= Clac(3,4)

output_sum = calc_ref.sum()
output_sub = calc_ref.sub()
output_mul = calc_ref.mul()
output_div = calc_ref.div()

print(output_sum,output_sub,output_mul,output_div)