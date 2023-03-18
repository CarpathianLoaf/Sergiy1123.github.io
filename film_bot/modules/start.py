from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_hi1 = KeyboardButton('🔎пошук')

greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi1)
