from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: Message):
    text = [
        '/start - Начать диалог',
        '/help - Получить справку',
        '/game - Первая версия Dota 2 heroes quiz',
        '/quiz - Вторая версия Dota 2 heroes quiz'
    ]
    await message.answer('\n'.join(text))
