from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from .base import BaseModel


class UserTask(BaseModel):
    __tablename__ = 'users_tasks'

    user_id = Column(Integer(), ForeignKey('users.id'))
    task_id = Column(Integer(), ForeignKey('tasks.id'))
    date_done = Column(DateTime())
