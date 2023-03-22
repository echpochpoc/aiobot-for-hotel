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
        ]
    ],
    resize_keyboard=True
)

cancel_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/cancel')
        ]
    ],
    resize_keyboard=True
)


cancel_btn = KeyboardButton('/cancel')
back_btn = KeyboardButton('❌Назад')


delete_kb = ReplyKeyboardRemove()
