from random import randint
from aiogram.types import Message, CallbackQuery

from keyboards.inline.keyboards_yes_no import keyboard_yn
from loader import dp, bot


@dp.message_handler(lambda message: message.text and 'прислать рандомный мемчик' in message.text.lower())
async def text_handler(message: Message):
    kb = keyboard_yn("yes", "no")
    await message.answer(f"Так {message.from_user.first_name},"
                         f" ты хочешь получить рандомный пост из паблика @Valejnick? Уверен?",
                         reply_markup=kb)


@dp.callback_query_handler(lambda c: c.data == 'yes')
async def process_callback_button1(callback_query: CallbackQuery):
    kb = keyboard_yn("yes", "no")
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(chat_id=callback_query.message.chat.id,
                             message_id=callback_query.message.message_id)
    await bot.forward_message(callback_query.message.chat.id, from_chat_id="-1001215778140",
                              message_id=randint(1, 10000))
    await bot.send_message(callback_query.message.chat.id, text=f"Эй, {callback_query.from_user.first_name} хочешь еще?",
                           reply_markup=kb)
