from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Main_Menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Suzish havzasi uchun ro\'yxatdan o\'tish.'),
        ],
    ],
    resize_keyboard=True
)


location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Asosiy menu'),
            KeyboardButton(text='Manzil'),
        ],
    ],
    resize_keyboard=True
)
