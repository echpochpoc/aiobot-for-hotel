from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from core import settings

storage = MemoryStorage()
bot = Bot(settings.BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)
