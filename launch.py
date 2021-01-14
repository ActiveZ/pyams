import os
from functions_combinaisons import *
from player import Player

os.system('cls')  # attention, sur ubuntu, remplacer par os.system('clear')


tirage = roll_dice(5)
print("tirage: ", tirage)

# print("petite suite: ", is_petite_suite([6,2,3,4,4,5]))
# print("grande suite: ", is_grande_suite([1,3,2,4,5]))
# print("brelan: ", is_brelan([6,6,6,6,4]))
# print("carre: ", is_carre([1,1,1,1,4]))
# print("full: ", is_full([3,3,2,2,2]))
# print("yams: ", is_yams([2,2,2,2,2]))
# print("chance: ", is_chance([2,2,2,2,2]))

# print("petite suite: ", is_petite_suite(tirage))
# print("grande suite: ", is_grande_suite(tirage))
# print("brelan: ", is_brelan(tirage))
# print("carre: ", is_carre(tirage))
# print("full: ", is_full(tirage))
# print("yams: ", is_yams(tirage))
# print("chance: ", is_chance(tirage))

print("combinaisons 1:", is_combinaison1(tirage))
print("combinaisons 2:", is_combinaison2(tirage))


p1 = Player("Joueur 1")
p1.dice1 = 3
p1.dice2 = 6
p1.dice3 = 9
p1.dice4 = 12
p1.dice5 = 15
p1.dice6 = 18
p1.brelan = 20
p1.carre = 20
p1.full = True
p1.petite_suite = True
p1.grande_suite = True
p1.yams = True
p1.chance = 20

print ( p1.toString())
