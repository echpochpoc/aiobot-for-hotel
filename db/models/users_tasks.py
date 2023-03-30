from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from .base import BaseModel


class UserTask(BaseModel):
    __tablename__ = 'users_tasks'

    def __init__(self, user_id, task_id, date_done):
        self.user_id = user_id
        self.task_id = task_id
        self.date_done = date_done

    user_id = Column(Integer(), ForeignKey('users.id'))
    task_id = Column(Integer(), ForeignKey('tasks.id'))
    date_done = Column(DateTime())
