from random import randint

from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from loader import dp, bot


@dp.message_handler(Command(['random_Meme', 'Хочу кекнуть']))
async def get_random_meme(message: Message):
    await bot.forward_message(message.chat.id, from_chat_id="-1001215778140", message_id=randint(1, 10000))