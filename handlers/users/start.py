from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name} бот еще в разработке,"
                         f"так что часто бывает недоступен. Доступные кнопки располагаются чуть ниже",
                         reply_markup=menu)
