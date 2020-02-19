from aiogram import executor
from handlers.commands import *

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True, on_startup=send_to_admin)
