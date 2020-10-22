from random import choice
from aiogram.types import Message, PollAnswer, CallbackQuery
from data.dotaheroes import HEROES
from data.usa_state_capital import CAPITALS
from data.list_heroes import make_list_of_heroes, make_list_of_capitals
from keyboards.inline import keyboard_yn
from loader import dp, bot


@dp.message_handler(lambda message: message.text and 'dota 2 heroes quiz' in message.text.lower())
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
    await bot.delete_message(chat_id=callback_query.message.chat.id,
                             message_id=callback_query.message.message_id)
    await bot.send_photo(callback_query.message.chat.id, photo=HEROES.get(hidden_hero))
    poll = await bot.send_poll(callback_query.message.chat.id, question="Что это за персонаж?", options=list_of_heroes,
                               type="quiz", correct_option_id=list_of_heroes.index(hidden_hero),
                               is_anonymous=False, explanation="Еще?", open_period=10)
    dp.polls_storage = {poll.poll.id: 'start_quiz'}


@dp.poll_answer_handler()
async def some_poll_answer_handler(poll_answer: PollAnswer):
    kb = keyboard_yn(dp.polls_storage.pop(poll_answer.poll_id), "no")
    await bot.send_message(poll_answer.user.id, text="Повторить 🥃?", reply_markup=kb)


@dp.message_handler(lambda message: message.text and 'usa capitals quiz' in message.text.lower())
async def text_handler(message: Message):
    kb = keyboard_yn("start_quiz_states", "no")
    await message.answer(f"Итак {message.from_user.first_name},"
                         f" ты запускаешь не простую игру типа quiz по столицам штатов",
                         reply_markup=kb)


@dp.callback_query_handler(lambda c: c.data == 'start_quiz_states')
async def process_callback_button2(callback_query: CallbackQuery):
    hidden_state = choice(list(CAPITALS.keys()))
    list_of_capitals = make_list_of_capitals(hidden_state)
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(chat_id=callback_query.message.chat.id,
                             message_id=callback_query.message.message_id)
    poll = await bot.send_poll(callback_query.message.chat.id, question=f"Выбери столицу штата {hidden_state}",
                               options=list_of_capitals, is_anonymous=False, type="quiz",
                               correct_option_id=list_of_capitals.index(CAPITALS.get(hidden_state)), explanation="Еще?",
                               open_period=20)
    dp.polls_storage[poll.poll.id] = 'start_quiz_states'
    print(dp.polls_storage)
