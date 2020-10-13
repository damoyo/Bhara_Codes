class Cat:
    def __init__(self,  colour, name): #custom constructor
        self.name = name
        self.colour = colour

    def make_noise(self):
        print("Meow Meow")

    def eats_rat(self):
        print("eat")

cat1 = Cat("Black", "Puffy")
cat2 = Cat("White", "Mewmew")
cat1.make_noise()
cat2.make_noise()