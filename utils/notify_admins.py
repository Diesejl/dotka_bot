from misc import dispatcher, bot
from config import ADMIN_ID


async def send_to_admin_start(dispatcher):
    await bot.send_message(chat_id=ADMIN_ID, text="Bot is working")


async def send_to_admin_stop(dispatcher):
    await bot.send_message(chat_id=ADMIN_ID, text="bot stopped")
