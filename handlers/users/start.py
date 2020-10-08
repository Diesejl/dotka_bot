from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}")
