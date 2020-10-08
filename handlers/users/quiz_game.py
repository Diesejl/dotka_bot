from random import choice

from aiogram.dispatcher.filters import Command
from aiogram.types import poll, Message, ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType, PollType, \
    InlineKeyboardButton

from data import dotaheroes
from data.list_heroes import make_list_heroes
from loader import dp, bot


@dp.message_handler(Command(['quiz']))
async def cmd_quiz(message: Message):
    hero = choice(list(dotaheroes.HEROES.keys()))
    hero_list = make_list_heroes(hero)
    await bot.send_photo(message.chat.id, photo=dotaheroes.HEROES.get(hero))
    await bot.send_poll(message.chat.id, question="Что это за персонаж?", options=hero_list,
                        is_anonymous=False, type="quiz", correct_option_id=hero_list.index(hero))


# # Хэндлер на команду /start
# @dp.message_handler(Command(['quiz']))
# async def cmd_start(message: Message):
#     poll_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     poll_keyboard.add(KeyboardButton(text="Создать викторину",
#                                      request_poll=KeyboardButtonPollType(type=PollType.QUIZ)))
#     poll_keyboard.add(KeyboardButton(text="Отмена", callback_data='cancel'))
#     await message.answer("Нажмите на кнопку ниже и создайте викторину!", reply_markup=poll_keyboard)
#
