from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: Message):
    text = [
        'Доступный функционал:',
        ' ',
        '1. /start - Запуск бота и отображение кнопок.',
        '2. /help - Получить справку',
        '3. Запустить quiz по героям из Dota 2',
        '4. Запросить мемес с паблика @Valejnick'
    ]
    await message.answer('\n'.join(text))
