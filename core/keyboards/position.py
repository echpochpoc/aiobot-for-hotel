from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

position_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Сантехник'),
            KeyboardButton(text='Слесарь'),
            KeyboardButton(text='Электрик')
        ],
        [
            KeyboardButton(text='Монтер'),
            KeyboardButton(text='Кладовщик'),
        ]
    ],
    resize_keyboard=True, one_time_keyboard=True
)
