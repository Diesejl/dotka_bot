import logging
from dotka_bot import config
from aiogram import Bot, Dispatcher

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN)
dispatcher = Dispatcher(bot)
