from datetime import datetime

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime


Base = declarative_base()

class UserMessages(Base):
    __tablename__ = 'user_messages'
    __tableargs__ = {'extend_existing': True}

    id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    user_id = Column(Integer, comment='id сотрудника в Telegram')
    body = Column(String, comment='Текст сообщения')
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.id} {self.user_id} {self.body} {self.created_at}'