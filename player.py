import html


class Player:
    def __init__(self, name):
        self.name = name
        self.dice1 = 0
        self.dice2 = 0
        self.dice3 = 0
        self.dice4 = 0
        self.dice5 = 0
        self.dice6 = 0
        self.chance = 0
        self.brelan = 0
        self.carre = 0
        self.full = False
        self.petite_suite = False
        self.grande_suite = False
        self.yams = False

    def get_sous_total1(self):
        return self.dice1 + self.dice2 + self.dice3 + self.dice4 + self.dice5 + self.dice6

    def get_bonus(self):
        return 35 if(self.get_sous_total1() > 62) else 0

    def get_total1(self):
        return self.get_sous_total1() + self.get_bonus()

    def get_total2(self):
        total = self.chance + self.brelan + self.carre
        if (self.full): total += 25
        if (self.petite_suite): total += 30
        if (self.grande_suite): total += 40
        if (self.yams): total += 50
        return total

    def get_total_final(self):
        return  self.get_total1() + self.get_total2()

    def toString(self):
        txt = "Name: " + self.name +"\n"
        txt += html.unescape("&#9856;") + " : " + ("" if (self.dice1 < 1) else str(self.dice1)) +"\n"
        txt += html.unescape("&#9857;") + " : " + ("" if (self.dice2 < 1) else str(self.dice2)) +"\n"
        txt += html.unescape("&#9858;") + " : " + ("" if (self.dice3 < 1) else str(self.dice3)) +"\n"
        txt += html.unescape("&#9859;") + " : " + ("" if (self.dice4 < 1) else str(self.dice4)) +"\n"
        txt += html.unescape("&#9860;") + " : " + ("" if (self.dice5 < 1) else str(self.dice5)) +"\n"
        txt += html.unescape("&#9861;") + " : " + ("" if (self.dice6 < 1) else str(self.dice6)) +"\n"
        txt += "Sous-total : " + str(self.get_sous_total1()) + "\n"
        txt += "Bonus : " + str(self.get_bonus()) + "\n"
        txt += "TOTAL 1 : " + str(self.get_total1()) + "\n"
        txt += "Brelan : " + ("" if (self.brelan < 1) else str(self.brelan)) + "\n"
        txt += "Carré : " + ("" if (self.carre < 1) else str(self.carre)) + "\n"
        txt += "Full : " + ("25" if (self.full) else "") + "\n"
        txt += "Petite suite : " + ("30" if (self.petite_suite) else "") + "\n"
        txt += "Grande suite : " + ("40" if (self.grande_suite) else "") + "\n"
        txt += "Yams : " + ("50" if (self.yams) else "") + "\n"
        txt += "Chance : " + ("" if (self.chance < 1) else str(self.chance)) + "\n"
        txt += "TOTAL 2 : " + str(self.get_total2()) + "\n"
        txt += "TOTAL FINAL : " + str(self.get_total_final())

        return txt

# p1 = Player("Joueur 1")
# print ( p1.toString())