from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/start"),
            KeyboardButton(text="/help"),
            KeyboardButton(text="/game"),
        ],
        [
            KeyboardButton(text="/random_Meme")
        ]
    ], resize_keyboard=True
)
