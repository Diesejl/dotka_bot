from random import choice
from aiogram.types import Message, PollAnswer, CallbackQuery
from data.dotaheroes import HEROES
from data.list_heroes import make_list_of_heroes
from keyboards.inline import keyboard_yn
from loader import dp, bot


@dp.message_handler(lambda message: message.text and 'dota 2 quiz' in message.text.lower())
async def text_handler(message: Message):
    kb = keyboard_yn("start_quiz", "no")
    await message.answer(f"Итак {message.from_user.first_name},"
                         f" ты запускаешь простую игру типа quiz по персонажам из gota 2",
                         reply_markup=kb)


@dp.callback_query_handler(lambda c: c.data == 'start_quiz')
async def process_callback_button1(callback_query: CallbackQuery):
    hidden_hero = choice(list(HEROES.keys()))
    list_of_heroes = make_list_of_heroes(hidden_hero)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_photo(callback_query.message.chat.id, photo=HEROES.get(hidden_hero))
    await bot.send_poll(callback_query.message.chat.id, question="Что это за персонаж?", options=list_of_heroes,
                        is_anonymous=False, type="quiz", correct_option_id=list_of_heroes.index(hidden_hero),
                        explanation="Еще?", open_period=10)
