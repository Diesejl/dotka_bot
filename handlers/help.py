from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from misc import dispatcher


@dispatcher.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Если на меня не забьют, то позднее добавится функционал связанный с Dota 2',
        'Список команд: ',
        '/start - Начать диалог',
        '/help - Получить справку',
        '/about - О боте',
        '/Game - Игра'
    ]
    await message.answer('\n'.join(text))
