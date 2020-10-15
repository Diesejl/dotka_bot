from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def keyboard_yn(call1, call2):
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text="Да", callback_data=call1)
    button2 = InlineKeyboardButton(text="Нет", callback_data=call2)
    keyboard.add(button1, button2)
    return keyboard
