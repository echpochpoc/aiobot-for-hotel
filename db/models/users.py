from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger
from .base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    def __init__(self, telegram_id, full_name, post):
        self.telegram_id = telegram_id
        self.full_name = full_name
        self.post = post

    telegram_id = Column(BigInteger(), unique=True)
    full_name = Column(String(300), nullable=True)
    post = Column(Integer(), ForeignKey('posts.id'))
