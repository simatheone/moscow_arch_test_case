from sqlalchemy import Column, Date, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .db import Base


class User(Base):
    email = Column(String(255), unique=True, nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    task = relationship('Task')

    @classmethod
    def seed(cls, fake):
        """
        Метод для заполнения модели User тестовыми данными
        и сохранением в базу.
        """
        user = User(email=fake.email(),
                    first_name=fake.first_name(),
                    last_name=fake.last_name())
        user.save()


class Task(Base):
    title = Column(String(256), nullable=False)
    description = Column(Text, nullable=False)
    due_date = Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))

    @classmethod
    def seed(cls, fake, due_date, user_id):
        """
        Метод для заполнения модели Task тестовыми данными
        и сохранением в базу.
        """
        task = Task(title=fake.catch_phrase(),
                    description=fake.text(max_nb_chars=500),
                    due_date=due_date,
                    user_id=user_id)
        task.save()
