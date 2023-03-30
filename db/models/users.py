from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger
from .base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    telegram_id = Column(BigInteger(), unique=True)
    full_name = Column(String(300), nullable=True)
    post = Column(Integer(), ForeignKey('posts.id'))