from random import choice
from data import dotaheroes


def make_list_heroes(chosen_hero):
    hero_list = [chosen_hero]
    while len(hero_list) != 6:
        hero_kek = choice(list(dotaheroes.HEROES.keys()))
        if hero_kek not in hero_list:
            hero_list.append(hero_kek)
        print(hero_kek)
    hero_list.sort()
    return hero_list
