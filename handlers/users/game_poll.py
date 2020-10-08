from aiogram.dispatcher.filters.builtin import Command
import random
from data import dotaheroes
from loader import dp, bot
from keyboards.inline.keyboard import answer_keyboard
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery


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
@dp.callback_query_handler(text="cancel")
async def action_cancel(call: CallbackQuery):
    await call.answer("Действие отменено. Введите /start, чтобы начать заново.", show_alert=True)
    await call.message.edit_reply_markup()


def random_hero():
    """Метод для выбора героев наугад"""
    hero_choice = random.choice(list(dotaheroes.HEROES.keys()))
    return hero_choice


