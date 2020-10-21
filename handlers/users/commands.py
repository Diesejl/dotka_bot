from aiogram.types import CallbackQuery

from keyboards.default import menu
from loader import dp, bot


@dp.callback_query_handler(lambda c: c.data == 'no')
async def cancel_button(callback_query: CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(chat_id=callback_query.message.chat.id,
                             message_id=callback_query.message.message_id)
    await bot.send_message(callback_query.message.chat.id, text="Ну ок, го обратно в меню тогда", reply_markup=menu)
