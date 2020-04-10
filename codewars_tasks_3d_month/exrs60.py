"""
https://www.codewars.com/kata/58ce8725c835848ad6000007

https://www.codewars.com/kata/5deeb1cc0d5bc9000f70aa74

https://www.codewars.com/kata/5da9af1142d7910001815d32
"""


def potatoes(potato0, weight0, potato1):
    return weight0 * (100 - potato0) // (100 - potato1)


def zombie_shootout(zombies, distance, ammo):
    if distance * 2 < min(ammo + 1, zombies):
        return f"You shot {distance * 2} zombies before being eaten: overwhelmed."
    elif ammo < zombies:
        return f"You shot {ammo} zombies before being eaten: ran out of ammo."
    else:
        return f"You shot all {zombies} zombies."


def get_score(lst):
    scores = {
        0: 0,
        1: 40,
        2: 100,
        3: 300,
        4: 1200
    }
    return sum(scores[line] *
               (sum(lst[0:i]) // 10 + 1)
               for i, line in enumerate(lst))
