from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from .base import BaseModel


class Task(BaseModel):
    __tablename__ = 'tasks'

    def __init__(self, title, photo, description, date_create):
        self.title = title
        self.photo = photo
        self.description = description
        self.date_create = date_create

    title = Column(String(50), nullable=False)
    photo = Column(Text())
    description = Column(String(300))
    date_create = Column(DateTime(), default=datetime.now)
