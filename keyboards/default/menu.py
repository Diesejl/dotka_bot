from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/start")
        ],
        [
            KeyboardButton(text="/help")
        ]
    ], resize_keyboard=True
)
