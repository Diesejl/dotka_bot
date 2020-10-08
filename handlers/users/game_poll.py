from aiogram.dispatcher.filters.builtin import Command
import random
from data import dotaheroes
from loader import dp, bot
from keyboards.inline.keyboard import answer_keyboard
from aiogram.types import Message, ReplyKeyboardRemove


@dp.message_handler(Command(['game']))
async def ask_game(message: Message):
    text = message.from_user.full_name + ", Какой перс изображен на пикче?"
    hero = random.choice(list(dotaheroes.HEROES.keys()))
    await bot.send_photo(message.chat.id, photo=dotaheroes.HEROES.get(hero))
    await bot.send_message(message.chat.id, text, reply_markup=answer_keyboard(hero))
    print("your hero is: ", hero)


@dp.callback_query_handler(lambda call: call.data == "True")
async def callback_worker(call):
    await bot.send_message(call.message.chat.id, 'Верно!')


@dp.callback_query_handler(lambda call: call.data == "False")
async def callback_worker(call):
    await bot.send_message(call.message.chat.id, 'Не верно!')


# Хэндлер на текстовое сообщение с текстом “Отмена”
@dp.message_handler(lambda message: message.text == "Отмена")
async def action_cancel(message: Message):
    remove_keyboard = ReplyKeyboardRemove()
    await message.answer("Действие отменено. Введите /start, чтобы начать заново.", reply_markup=remove_keyboard)


def random_hero():
    """Метод для выбора героев наугад"""
    hero_choice = random.choice(list(dotaheroes.HEROES.keys()))
    return hero_choice


# # Хэндлер на команду /start
# @dp.message_handler(commands=["start"])
# async def cmd_start(message: Message):
#     poll_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     poll_keyboard.add(KeyboardButton(text="Создать викторину",
#                                            request_poll=KeyboardButtonPollType(type=PollType.QUIZ)))
#     poll_keyboard.add(KeyboardButton(text="Отмена"))
#     await message.answer("Нажмите на кнопку ниже и создайте викторину!", reply_markup=poll_keyboard)

