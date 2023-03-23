from core.my_bot import bot
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from core.keyboards import position_kb, cancel_kb, delete_kb


class Registration(StatesGroup):
    photo = State()
    fullname = State()
    position = State()
    description = State()


async def start_registration(message: types.Message):
    await message.reply('Вы начали процесс регистрации\n'
                        'Загрузите фото.', reply_markup=cancel_kb)
    await Registration.photo.set()


async def cancel_registration(message: types.Message, state: FSMContext):
    if state is None:
        return
    await message.reply('Вы прервали процесс регистрации.', reply_markup=delete_kb)
    await state.finish()


async def check_photo(message: types.Message):
    await message.reply('Это не фотография!')


async def load_photo(message: types.Message, state: FSMContext):
    await message.answer('Введите ваше ФИО')
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id
    await Registration.next()


async def load_fullname(message: types.Message, state: FSMContext):
    if message.text == '❌Назад':
        await message.reply('Загрузите новое фото')
        await Registration.photo.set()
    else:
        fullname = message.text.strip().split()
        print(fullname)
        if len(fullname) < 2 or len(fullname) > 3:
            await message.reply('Попробуйте снова!')
        else:
            await message.answer('Выберете вашу должность', reply_markup=position_kb)
            async with state.proxy() as data:
                data['fullname'] = message.text
            await Registration.next()


async def load_position(message: types.Message, state: FSMContext):
    if message.text == '❌Назад':
        await message.reply('Введите новое ФИО', reply_markup=cancel_kb)
        await Registration.fullname.set()
    else:
        position_list = ['Сантехник', 'Слесарь', 'Электрик', 'Монтер', 'Кладовщик']
        if message.text not in position_list:
            await message.reply('Нет такой должности!')
        else:
            await message.answer('Введите описание', reply_markup=cancel_kb)
            async with state.proxy() as data:
                data['position'] = message.text
            await Registration.next()


async def load_description(message: types.Message, state: FSMContext):
    if message.text == '❌Назад':
        await message.reply('Выберете новую должность', reply_markup=position_kb)
        await Registration.position.set()
    else:
        async with state.proxy() as data:
            data['description'] = message.text
        await message.answer('Регистрация завершена!', reply_markup=delete_kb)
        await bot.send_photo(chat_id=message.from_user.id,
                             photo=data['photo'],
                             caption=f"{data['fullname']}\n"
                                     f"{data['position']}\n\n"
                                     f"{data['description']}")
        await state.finish()


def register_handler_registration(dp: Dispatcher):
    dp.register_message_handler(start_registration, commands=['reg'], state=None)
    dp.register_message_handler(cancel_registration, commands=['cancel'], state='*')
    dp.register_message_handler(check_photo, lambda message: not message.photo, state=Registration.photo)
    dp.register_message_handler(load_photo, content_types=['photo'], state=Registration.photo)
    dp.register_message_handler(load_fullname, state=Registration.fullname)
    dp.register_message_handler(load_position, state=Registration.position)
    dp.register_message_handler(load_description, state=Registration.description)
