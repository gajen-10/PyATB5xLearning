class car:
    def __init__(self,o_name,o_make,o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model



    def start_engine(self):
        print("Starting car with name:" + self.name)
        print("Starting car with make:" + self.make)
        print("Starting car with model:" + self.model)


lambo = car("lambo","V6","2024")
lambo.start_engine()

print("----")

maruti = car("Maruti","1.5", "2020")
maruti.start_engine()

