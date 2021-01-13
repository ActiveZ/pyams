import random

# -------------- TIRAGE ------------------

# lancement des dés (n = nb de dés)
def roll_dice(n):
    result = []
    for i in range(n): result.append(random.randint(1,6))
    return result


# ------------ COMBINAISONS 1 -------------

# retourne les combinaisons possibles de la partie 1 du score
def is_combinaison1(dice):
    result = {
        "dice 1": dice.count(1),
        "dice 2": dice.count(2) * 2,
        "dice 3": dice.count(3) * 3,
        "dice 4": dice.count(4) * 4,
        "dice 5": dice.count(5) * 5,
        "dice 6": dice.count(6) * 6
    }
    return result


# ------------ COMBINAISONS 2 -------------

# retourne 30 si petite suite, sinon 0
def is_petite_suite(dice):
    ps1 = [1,2,3,4]
    ps2 = [2,3,4,5]
    ps3 = [3,4,5,6]
    result = (all(i in dice for i in ps1)) or (all(i in dice for i in ps2)) or (all(i in dice for i in ps3))
    return 30 if (result) else 0


# retourne 40 si grande suite, sinon 0
def is_grande_suite(dice):
    gs1 = [1,2,3,4,5]
    gs2 = [2,3,4,5,6]
    result = (all(i in dice for i in gs1)) or (all(i in dice for i in gs2))
    return 40 if(result) else 0


# retourne la somme des dés du brelan, sinon 0
def is_brelan(dice):
    result = 0
    for i in range(1,7):
        if (dice.count(i) > 2): result = i * 3
    return result


# retourne la somme des dés du carré, sinon 0
def is_carre(dice):
    result = 0
    for i in range(1,7):
        if (dice.count(i) > 3): result = i * 4
    return result


# retourne 25 si full, sinon 0
def is_full(dice):
    tmp_dice = dice.copy()
    result = 0
    b = is_brelan(tmp_dice)
    if (b):
        for i in range(3): tmp_dice.remove(b/3)  # enlever les 3 valeurs du brelan
        if (tmp_dice[0] == tmp_dice[1]): result = 25
    return result


# retourne 50 sy yams, sinon 0
def is_yams(dice):
    result = 0
    for i in range(1,7):
        if (dice.count(i) == 5): result = 50
    return result


# retourne la somme des dés
def is_chance(dice):
    return sum(dice)


# retourne un tableaux des combinaisons réussie avec le tirage et les valeurs
def is_combinaison2(dice):
    result = {
        # dice_combinaison: is_combinaison(dice),
        "brelan": is_brelan(dice),
        "carre": is_carre(dice),
        "full": is_full(dice),
        "petite_suite": is_petite_suite(dice),
        "grande_suite": is_grande_suite(dice),
        "yams": is_yams(dice),
        "chance": is_chance(dice)
    }
    return result