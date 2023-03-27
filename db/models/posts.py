from sqlalchemy import Integer, String, Column
from .base import BaseModel


class Post(BaseModel):
    __tablename__ = 'posts'

    title = Column(String(50), nullable=False)
    description = Column(String(300))

