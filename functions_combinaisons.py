import random


def roll_dice(n):
    result = []
    for i in range(n): result.append(random.randint(1,6))
    return result


def is_brelan(dice):
    result = 0
    for i in range(1,7):
        if (dice.count(i) > 2): result = i * 3
    return result


def is_carre(dice):
    result = 0
    for i in range(1,7):
        if (dice.count(i) > 3): result = i * 4
    return result


def is_full(dice):
    result = 0
    b = is_brelan(dice)
    if (b):
        for i in range(3): dice.remove(b/3)  # enlever les 3 valeurs du brelan
        if (dice[0] == dice[1]): result = 25
    return result


def is_yams(dice):
    result = 0
    for i in range(1,7):
        if (dice.count(i) == 5): result = 50
    return result


def is_petite_suite(dice):
    ps1 = [1,2,3,4]
    ps2 = [2,3,4,5]
    ps3 = [3,4,5,6]
    result = (all(i in dice for i in ps1)) or (all(i in dice for i in ps2)) or (all(i in dice for i in ps3))
    return 30 if (result) else 0


def is_grande_suite(dice):
    gs1 = [1,2,3,4,5]
    gs2 = [2,3,4,5,6]
    result = (all(i in dice for i in gs1)) or (all(i in dice for i in gs2))
    return 40 if(result) else 0


