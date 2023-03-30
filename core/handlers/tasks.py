import db.queries
from core.my_bot import bot
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from core.keyboards import position_kb, cancel_kb, delete_kb
from db.models import Task


class CreateTask(StatesGroup):
    photo = State()
    title = State()
    description = State()
    user = State()
    worker = State()


async def create_reminder(message: types.Message):
    await message.reply('Вы начали создание задачи.\n'
                        'Загрузите фото.', reply_markup=cancel_kb)
    await CreateTask.photo.set()


async def cancel_reminder(message: types.Message, state: FSMContext):
    if state is None:
        return
    await message.reply('Вы закончили создание задачи.', reply_markup=delete_kb)
    await state.finish()


# Проверка на загрузку фотографии
async def check_photo(message: types.Message):
    await message.reply('Это не фотография!')


async def load_photo(message: types.Message, state: FSMContext):
    await message.answer('Введите название задачи')
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id
    await CreateTask.next()


async def load_title(message: types.Message, state: FSMContext):
    if message.text == '❌Назад':
        await message.reply('Загрузите новое фото')
        await CreateTask.photo.set()
    else:
        await message.answer('Введите краткое описание задачи')
        async with state.proxy() as data:
            data['title'] = message.text
        await CreateTask.next()


async def load_description(message: types.Message, state: FSMContext):
    if message.text == '❌Назад':
        await message.reply('Введите новое название задачи')
        await CreateTask.title.set()
    else:
        await message.answer('Введите как вас зовут')
        async with state.proxy() as data:
            data['description'] = message.text
        await CreateTask.next()


async def load_user(message: types.Message, state: FSMContext):
    if message.text == '❌Назад':
        await message.reply('Введите новое краткое описание задачи')
        await CreateTask.description.set()
    else:
        await message.answer('Выберете кому назначается задача', reply_markup=position_kb)
        async with state.proxy() as data:
            data['user'] = message.text
        await CreateTask.next()


async def load_worker(message: types.Message, state: FSMContext):
    if message.text == '❌Назад':
        await message.reply('Введите заново как вас зовут', reply_markup=cancel_kb)
        await CreateTask.user.set()
    else:
        position_list = ['Сантехник', 'Слесарь', 'Электрик', 'Монтер', 'Кладовщик']
        if message.text not in position_list:
            await message.reply('Нет такой должности!')
        else:
            async with state.proxy() as data:
                data['worker'] = message.text
            new_task = Task(
                title=data['title'],
                photo=data['photo'],
                description=data['description']
            )
            db.queries.create_new_task(new_task)
            await message.answer('Задача создана!', reply_markup=delete_kb)
            await bot.send_photo(chat_id=message.from_user.id,
                                 photo=data['photo'],
                                 caption=f"{data['title']}\n"
                                         f"{data['description']}\n\n"
                                         f"От: {data['user']}\n"
                                         f"Кому: {data['worker']}")
            await state.finish()


def register_handler_tasks(dp: Dispatcher):
    dp.register_message_handler(create_reminder, commands=['create'], state=None)
    dp.register_message_handler(cancel_reminder, commands=['cancel'], state='*')  # state='*' учитывать все состояния
    dp.register_message_handler(check_photo, lambda message: not message.photo, state=CreateTask.photo)
    dp.register_message_handler(load_photo, content_types=['photo'], state=CreateTask.photo)
    dp.register_message_handler(load_title, state=CreateTask.title)
    dp.register_message_handler(load_description, state=CreateTask.description)
    dp.register_message_handler(load_user, state=CreateTask.user)
    dp.register_message_handler(load_worker, state=CreateTask.worker)
