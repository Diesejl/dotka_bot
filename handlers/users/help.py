from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: Message):
    text = [
        '/start - Запуск бота и отображение кнопок.',
        '/help - Получить справку',
        '/game - Dota 2 heroes quiz',
        '/random_Meme - прислать рандомный мемес из канала @Valejnick'
    ]
    await message.answer('\n'.join(text))
