from random import choice
from data.dotaheroes import HEROES


def make_list_of_heroes(hidden_hero):
    list_of_heroes = [hidden_hero]
    while len(list_of_heroes) != 6:
        new_hero = choice(list(HEROES.keys()))
        if new_hero not in list_of_heroes:
            list_of_heroes.append(new_hero)

    list_of_heroes.sort()
    return list_of_heroes
