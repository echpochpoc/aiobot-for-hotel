from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from core import settings

bot = Bot(settings.BOT_TOKEN)
dp = Dispatcher(bot)
