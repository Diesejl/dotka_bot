# -*- coding: utf-8 -*-
from aiogram import types
from aiogram.types import ContentType
from config import *
from misc import dispatcher, bot
import random
from media_shit import dotaheroes


@dispatcher.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """ `/start` """
    text = f"Привет, {message.from_user.full_name}! Я бот и меня еще пилят, пока я ничего не умею"
    await bot.send_message(message.chat.id, text, reply_markup=keyboard())


@dispatcher.message_handler(commands=['help'])
async def send_help(message: types.Message):
    """ `/help` """
    text = f"{message.from_user.full_name}, ты серьезно, какая нах помощь?" \
           f" Мне бы кто помог этого бота написать..."
    await bot.send_message(message.chat.id, text)


@dispatcher.message_handler(commands=['about'])
async def send_help(message: types.Message):
    """ `/about` """
    text = "Если на меня не забьют, то позднее добавится функционал связанный с Dota 2"
    await bot.send_message(message.chat.id, text)


@dispatcher.message_handler(content_types=ContentType.PHOTO)
async def send_text_for_pic(message: types.Message):
    text = "О, это же пикча! Не вкуриваю че там, но ок"
    await bot.send_message(message.chat.id, text)


@dispatcher.message_handler(lambda message: message.text and 'шпак' in message.text.lower())
async def send_text_handler(message: types.Message):
    text = "шпак? шпак пес сутулый"
    await bot.send_message(message.chat.id, text)


@dispatcher.message_handler(lambda message: message.text and 'kek' in message.text.lower())
async def send_kek_command(message: types.message):
    text = "kek"
    await bot.send_message(message.chat.id, text)


@dispatcher.message_handler(commands=['reg'])
async def check_user_name(message: types.Message):
    text = "Тебя зовут " + message.from_user.full_name + "?"
    await bot.send_message(message.chat.id, text, reply_markup=yn_keyboard())


# @dispatcher.callback_query_handler()
# async def callback_worker(call):
#     if call.data == "yes":
#         await bot.send_message(call.message.chat.id, 'Окай пёс!'  );
#     elif call.data == "no":
#         await bot.send_message(call.message.chat.id, 'Ну ладно, значит буду звать тебя мешок с костями');

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


async def send_to_admin():
    await bot.send_message(chat_id=ADMIN_ID, text="Бот запущен")


def keyboard():
    """Основная клавиатура внизу"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/help')
    btn2 = types.KeyboardButton('/about')
    btn3 = types.KeyboardButton('/reg')
    btn4 = types.KeyboardButton('/game')
    markup.add(btn1, btn2, btn3, btn4)
    return markup


def yn_keyboard():
    """Клавиатура ДА, НЕТ"""
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_yes, key_no)
    return keyboard


# def random_hero():
#     """Метод для выбора героев наугад"""
#     heroChoiсe = random.choice(list(dotaheroes.HEROES.keys()))
#     return heroChoiсe


def answer_keyboard(chosenHero):
    """Клавиатура выбора ответа"""
    call1, call2, call3, call4 = "False", "False", "False", "False"
    heroList = [chosenHero]
    while len(heroList) != 4:
        heroKek = random.choice(list(dotaheroes.HEROES.keys()))
        if heroKek not in heroList:
            heroList.append(heroKek)
        print(heroKek)
    heroList.sort()
    if heroList[0] == chosenHero: call1 = "True"
    if heroList[1] == chosenHero: call2 = "True"
    if heroList[2] == chosenHero: call3 = "True"
    if heroList[3] == chosenHero: call4 = "True"
    print(heroList)
    print(call1, call2, call3, call4)
    btn1 = types.InlineKeyboardButton(heroList[0], callback_data=call1)
    btn2 = types.InlineKeyboardButton(heroList[1], callback_data=call2)
    btn3 = types.InlineKeyboardButton(heroList[2], callback_data=call3)
    btn4 = types.InlineKeyboardButton(heroList[3], callback_data=call4)
    btn5 = types.InlineKeyboardButton("Exit this shitty game", callback_data='/start')
    keyboard = types.InlineKeyboardMarkup().add(btn1, btn2, btn3, btn4, btn5)
    return keyboard
