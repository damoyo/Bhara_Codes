import rat

class House:
    def __init__(self, colour, bedrooms): #custom constructor
        self.name = bedrooms
        self.colour = colour
        self.ratlist = []

    def number_rats(self):
        return (len(self.ratlist))

    def add_rat(self, rat):
        self.ratlist.append(rat)

    def print_rat_colors(self):
        for rat in self.ratlist:
            print(rat.colour)



rat1 = rat.Rat("Black", 12)
rat2 = rat.Rat("White", 10)
#rat1.make_noise()
#rat2.make_noise()
House1 = House("Black", 3)
House2 = House("White", 2)
House1.add_rat(rat1)
House1.add_rat(rat2)
print(House1.number_rats())
House1.print_rat_colors()
