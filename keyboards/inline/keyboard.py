import random
from aiogram import types
from data import dotaheroes


# def answer_keyboard(chosen_hero):
#     """Клавиатура выбора ответа"""
#     call1, call2, call3, call4 = "False", "False", "False", "False"
#     hero_list = [chosen_hero]
#     while len(hero_list) != 4:
#         hero_kek = random.choice(list(dotaheroes.HEROES.keys()))
#         if hero_kek not in hero_list:
#             hero_list.append(hero_kek)
#         print(hero_kek)
#     hero_list.sort()
#     if hero_list[0] == chosen_hero:
#         call1 = "True"
#     if hero_list[1] == chosen_hero:
#         call2 = "True"
#     if hero_list[2] == chosen_hero:
#         call3 = "True"
#     if hero_list[3] == chosen_hero:
#         call4 = "True"
#     print(hero_list)
#     print(call1, call2, call3, call4)
#     btn1 = types.InlineKeyboardButton(hero_list[0], callback_data=call1)
#     btn2 = types.InlineKeyboardButton(hero_list[1], callback_data=call2)
#     btn3 = types.InlineKeyboardButton(hero_list[2], callback_data=call3)
#     btn4 = types.InlineKeyboardButton(hero_list[3], callback_data=call4)
#     btn5 = types.InlineKeyboardButton("Exit this shitty game", callback_data='cancel')
#     game_keyboard = types.InlineKeyboardMarkup().add(btn1, btn2, btn3, btn4, btn5)
#     return game_keyboard


def answer_keyboard(chosen_hero):
    """Клавиатура выбора ответа"""
    call1, call2, call3, call4 = "False", "False", "False", "False"
    hero_list = [chosen_hero]
    while len(hero_list) != 4:
        hero_kek = random.choice(list(dotaheroes.HEROES.keys()))
        if hero_kek not in hero_list:
            hero_list.append(hero_kek)
        print(hero_kek)
    hero_list.sort()
    if hero_list[0] == chosen_hero:
        call1 = "True"
    if hero_list[1] == chosen_hero:
        call2 = "True"
    if hero_list[2] == chosen_hero:
        call3 = "True"
    if hero_list[3] == chosen_hero:
        call4 = "True"
    print(hero_list)
    print(call1, call2, call3, call4)
    btn1 = types.InlineKeyboardButton(hero_list[0], callback_data=call1)
    btn2 = types.InlineKeyboardButton(hero_list[1], callback_data=call2)
    btn3 = types.InlineKeyboardButton(hero_list[2], callback_data=call3)
    btn4 = types.InlineKeyboardButton(hero_list[3], callback_data=call4)
    btn5 = types.InlineKeyboardButton("Exit this shitty game", callback_data='cancel')
    game_keyboard = types.InlineKeyboardMarkup().add(btn1, btn2, btn3, btn4, btn5)
    return game_keyboard
