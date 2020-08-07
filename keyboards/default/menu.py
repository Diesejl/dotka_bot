from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="/help")], [KeyboardButton(text="/game")]], resize_keyboard=True
)
