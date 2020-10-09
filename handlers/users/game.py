from random import choice
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, PollAnswer
from data.dotaheroes import HEROES
from data.list_heroes import make_list_of_heroes
from loader import dp, bot


@dp.message_handler(Command(['game']))
async def cmd_quiz(message: Message):
    hidden_hero = choice(list(HEROES.keys()))
    list_of_heroes = make_list_of_heroes(hidden_hero)
    await bot.send_photo(message.chat.id, photo=HEROES.get(hidden_hero))
    await bot.send_poll(message.chat.id, question="Что это за персонаж?", options=list_of_heroes,
                        is_anonymous=False, type="quiz", correct_option_id=list_of_heroes.index(hidden_hero),
                        explanation="Еще?", open_period=10)


@dp.poll_answer_handler()
async def handle_poll_answer(quiz_answer: PollAnswer):
    print(f"У юзера выбран вариант {quiz_answer.option_ids[0]},")
