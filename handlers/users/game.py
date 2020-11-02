from random import choice
from aiogram.types import Message, PollAnswer, CallbackQuery
from data.dotaheroes import HEROES
from data.text_locale_ru import QUESTION_AGAIN_LIST, QUESTION_HERO_LIST
from data.usa_state_capital import CAPITALS
from data.usa_state_pictures import STATE_MAPS
from data.list_of_answers import make_list_of_answers
from keyboards.inline import keyboard_yn
from loader import dp, bot


@dp.message_handler()
async def text_handler(message: Message):
    if 'usa capitals quiz' in message.text.lower():
        kb = keyboard_yn("start_quiz_states", "no")
        await message.answer(f"Итак '{message.from_user.first_name}',"
                             f" ты запускаешь не простую игру типа quiz по столицам штатов", reply_markup=kb)
    elif 'usa maps quiz' in message.text.lower():
        kb = keyboard_yn("start_quiz_state_maps", "no")
        await message.answer(f"Итак '{message.from_user.first_name}',"
                             f" ты запускаешь интересную игру типа quiz по угадыванию штатов", reply_markup=kb)
    else:
        kb = keyboard_yn("start_quiz", "no")
        await message.answer(f"Итак '{message.from_user.first_name}', "
                             f"ты запускаешь простую игру типа quiz по персонажам из Dota 2", reply_markup=kb)


@dp.poll_answer_handler()
async def some_poll_answer_handler(poll_answer: PollAnswer):
    kb = keyboard_yn(dp.polls_storage.pop(poll_answer.poll_id), "no")
    await bot.send_message(poll_answer.user.id, text=choice(QUESTION_AGAIN_LIST), reply_markup=kb)


@dp.callback_query_handler(lambda c: c.data == 'start_quiz')
async def process_callback_button1(callback_query: CallbackQuery):
    hidden_hero = choice(list(HEROES.keys()))
    list_of_heroes = make_list_of_answers(HEROES, hidden_hero, picture_quiz=True)
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(chat_id=callback_query.message.chat.id,
                             message_id=callback_query.message.message_id)
    await bot.send_photo(callback_query.message.chat.id, photo=HEROES.get(hidden_hero))
    poll = await bot.send_poll(callback_query.message.chat.id, question=choice(QUESTION_HERO_LIST),
                               options=list_of_heroes, type="quiz", correct_option_id=list_of_heroes.index(hidden_hero),
                               is_anonymous=False, explanation="Еще?", open_period=10)
    dp.polls_storage = {poll.poll.id: 'start_quiz'}


@dp.callback_query_handler(lambda c: c.data == 'start_quiz_states')
async def process_callback_button2(callback_query: CallbackQuery):
    hidden_state = choice(list(CAPITALS.keys()))
    list_of_capitals = make_list_of_answers(CAPITALS, hidden_state)
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(chat_id=callback_query.message.chat.id,
                             message_id=callback_query.message.message_id)
    await bot.send_photo(callback_query.message.chat.id, photo=STATE_MAPS.get(hidden_state))
    poll = await bot.send_poll(callback_query.message.chat.id, question=f"Выбери столицу штата {hidden_state}",
                               options=list_of_capitals, is_anonymous=False, type="quiz",
                               correct_option_id=list_of_capitals.index(CAPITALS.get(hidden_state)), explanation="Еще?",
                               open_period=20)
    dp.polls_storage[poll.poll.id] = 'start_quiz_states'


@dp.callback_query_handler(lambda c: c.data == 'start_quiz_state_maps')
async def process_callback_button1(callback_query: CallbackQuery):
    hidden_state = choice(list(STATE_MAPS.keys()))
    list_of_states = make_list_of_answers(STATE_MAPS, hidden_state, picture_quiz=True)
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(chat_id=callback_query.message.chat.id,
                             message_id=callback_query.message.message_id)
    await bot.send_photo(callback_query.message.chat.id, photo=STATE_MAPS.get(hidden_state))
    poll = await bot.send_poll(callback_query.message.chat.id, question="Что это за штат?", options=list_of_states,
                               type="quiz", correct_option_id=list_of_states.index(hidden_state),
                               is_anonymous=False, explanation="Еще?", open_period=20)
    dp.polls_storage = {poll.poll.id: 'start_quiz_state_maps'}
