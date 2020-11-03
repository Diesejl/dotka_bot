from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name} бот еще в разработке,"
                         f"так что часто бывает недоступен. Доступные кнопки располагаются чуть ниже",
                         reply_markup=menu)


@dp.message_handler(commands="kekus")
async def kill_menu(message: Message):
    remove_kb = ReplyKeyboardRemove()
    await message.answer(text="ok...", reply_markup=remove_kb)
