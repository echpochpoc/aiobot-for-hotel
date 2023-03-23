from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

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
        ],
        [
            KeyboardButton(text='/cancel')
        ],
        [
            KeyboardButton(text='❌Назад')
        ]
    ],
    resize_keyboard=True
)

cancel_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/cancel')
        ],
        [
            KeyboardButton(text='❌Назад')
        ]
    ],
    resize_keyboard=True
)

delete_kb = ReplyKeyboardRemove()
