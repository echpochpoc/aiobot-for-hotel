from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models.base import Base
from core import settings

storage = MemoryStorage()
bot = Bot(settings.BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)

engine = create_engine(f'postgresql+psycopg2://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}'
                       f'@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}')

Base.metadata.create_all(engine)
session_factory = sessionmaker(bind=engine)
