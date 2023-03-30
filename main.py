import logging
from aiogram.utils import executor

from core import settings
from core.utils import commands
from core.my_bot import bot, dp
from core.handlers import basic, tasks, registration


async def on_startup(_):
    await bot.set_webhook(settings.URL_DOMAIN)
    await commands.set_commands(bot)
    await bot.send_message(chat_id=settings.ADMIN_ID, text='Бот запущен')
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - [%(levelname)s] - %(name)s - '
                               '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')


async def on_shutdown(_):
    await bot.delete_webhook()
    await bot.send_message(chat_id=settings.ADMIN_ID, text='Бот остановлен')

registration.register_handler_registration(dp)
tasks.register_handler_tasks(dp)
basic.register_handler_basic(dp)


executor.start_webhook(
    dispatcher=dp,
    webhook_path=settings.URL_PATH,
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    skip_updates=True,
    host=settings.SERVER_HOST,
    port=settings.SERVER_PORT
)
