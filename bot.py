from aiogram import executor
from handlers import *
from utils.notify_admins import *

if __name__ == '__main__':
    executor.start_polling(dispatcher, on_startup=send_to_admin_start, on_shutdown=send_to_admin_stop,
                           skip_updates=True)
