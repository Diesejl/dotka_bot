# -*- coding: utf-8 -*-
from aiogram import types
from dotka_bot.misc import dispatcher, bot
import random
from dotka_bot.media_shit import dotaheroes

# Ответ пользователя на кнопку /start
@dispatcher.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """ `/start` """
    text = f"Привет, {message.from_user.full_name}! Я бот и меня еще пилят, пока я ничего не умею"
    await bot.send_message(message.chat.id, text, reply_markup=keyboard())


# Ответ пользователя на кнопку /about
@dispatcher.message_handler(commands=['about'])
async def send_help(message: types.Message):
    """ `/about` """
    text = "Если на меня не забьют, то позднее добавится функционал связанный с Dota 2"
    await bot.send_message(message.chat.id, text)

# Ответ пользователя на кнопку /game
@dispatcher.message_handler(commands=['game'])
async def ask_game(message: types.Message):
    text = message.from_user.full_name + ", Какой перс изображен на пикче?"
    hero = random.choice(list(dotaheroes.HEROES.keys()))
    await bot.send_photo(message.chat.id, photo=dotaheroes.HEROES.get(hero))
    await bot.send_message(message.chat.id, text, reply_markup=answer_keyboard(hero))
    print("your hero is: ", hero)


@dispatcher.callback_query_handler(lambda call: call.data == "True")
async def callback_worker(call):
    await bot.send_message(call.message.chat.id, 'Верно!')


@dispatcher.callback_query_handler(lambda call: call.data == "False")
async def callback_worker(call):
    await bot.send_message(call.message.chat.id, 'Не верно!')


def keyboard():
    """Основная клавиатура внизу"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('about')
    btn2 = types.KeyboardButton('game')
    markup.add(btn1, btn2)
    return markup


# # Хэндлер на команду /start
# @dispatcher.message_handler(commands=["start"])
# async def cmd_start(message: types.Message):
#     poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     poll_keyboard.add(types.KeyboardButton(text="Создать викторину",
#                                            request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ)))
#     poll_keyboard.add(types.KeyboardButton(text="Отмена"))
#     await message.answer("Нажмите на кнопку ниже и создайте викторину!", reply_markup=poll_keyboard)

# Хэндлер на текстовое сообщение с текстом “Отмена”
# @dispatcher.message_handler(lambda message: message.text == "Отмена")
# async def action_cancel(message: types.Message):
#     remove_keyboard = types.ReplyKeyboardRemove()
#     await message.answer("Действие отменено. Введите /start, чтобы начать заново.", reply_markup=remove_keyboard)

def random_hero():
    """Метод для выбора героев наугад"""
    hero_choice = random.choice(list(dotaheroes.HEROES.keys()))
    return hero_choice


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
    btn5 = types.InlineKeyboardButton("Exit this shitty game", callback_data='/start')
    game_keyboard = types.InlineKeyboardMarkup().add(btn1, btn2, btn3, btn4, btn5)
    return game_keyboard
