class Player:
    def __init__(self, name):
        self.name = name
        self.dice1 = None
        self.dice2 = None
        self.dice3 = None
        self.dice4 = None
        self.dice5 = None
        self.dice6 = None
        self.chance = None
        self.brelan = None
        self.carre = None
        self.full = False
        self.petite_suite = False
        self.grande_suite = False
        self.yams = False

    def get_sous_total1(self):
        return self.dice1 + self.dice2 + self.dice3 + self.dice4 + self.dice5 + self.dice6

    def get_bonus(self):
        return 35 if(self.get_sous_total1() > 63) else 0

    def get_total1(self):
        return self.get_sous_total1() + self.get_bonus()

    def get_total2(self):
        total = 0
        total += self.chance
        total += self.brelan
        total += self.carre
        if (self.full): total += 25
        if (self.petite_suite): total += 30
        if (self.grande_suite): total += 40
        if (self.yams): total += 50
        return total

    def get_total_final(self):
        return self.get_total1() + self.get_total2()
