from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="USA capitals quiz"),
            KeyboardButton(text="Dota 2 heroes quiz"),
        ],
        [
            KeyboardButton(text="Прислать рандомный мемчик")
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)
