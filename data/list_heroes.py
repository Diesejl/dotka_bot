from random import choice
from data.dotaheroes import HEROES
from data.usa_state_capital import CAPITALS


def make_list_of_heroes(hidden_hero):
    list_of_heroes = [hidden_hero]
    while len(list_of_heroes) != 6:
        new_hero = choice(list(HEROES.keys()))
        if new_hero not in list_of_heroes:
            list_of_heroes.append(new_hero)

    list_of_heroes.sort()
    return list_of_heroes


def make_list_of_capitals(hidden_state):
    print(hidden_state)
    hidden_capital = CAPITALS.get(hidden_state)
    print(hidden_capital)
    list_of_capitals = [hidden_capital]
    while len(list_of_capitals) != 6:
        new_capital = choice(list(CAPITALS.values()))
        if new_capital not in list_of_capitals:
            list_of_capitals.append(new_capital)

    list_of_capitals.sort()
    return list_of_capitals
