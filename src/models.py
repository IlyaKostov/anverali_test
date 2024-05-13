from sqlalchemy import Column, Integer, String

from src.db import Base


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    task_text = Column(String)
