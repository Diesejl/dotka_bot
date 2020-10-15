from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/start"),
            KeyboardButton(text="/help"),
            KeyboardButton(text="Dota 2 quiz"),
        ],
        [
            KeyboardButton(text="Прислать рандомный мемчик")
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)
