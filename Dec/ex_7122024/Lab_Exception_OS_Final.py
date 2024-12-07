class xyz:

    def f1(self):
        try:
            a=int(input("Enter the value \n"))

        except Exception as e:
            print("Enter the correct integer value only of a")

        else:
            print(a)

        finally:
            print("Finally: Anyhow I will be printed...!")

obj_ref=xyz()
obj_ref.f1()