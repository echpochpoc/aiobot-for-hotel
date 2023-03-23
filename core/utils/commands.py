from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы'
        ),
        BotCommand(
            command='create',
            description='Создать задание'
        ),
        BotCommand(
            command='reg',
            description='Начать регистрацию'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
