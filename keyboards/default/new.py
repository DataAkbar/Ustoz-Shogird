from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ustoz kerak"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
