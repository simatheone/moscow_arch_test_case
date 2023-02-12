from datetime import date
from typing import Generator

from .db import session
from .models import Task, User


def get_all_tasks_and_user_emails_for_today() -> Generator:
    """
    Селектор получения email'ов пользователей, названий
    и описаний заданий из базы данных. Возвращает объект генератор.
    """
    date_today = date.today()
    tasks = (
        session.query(User.email, Task.title, Task.description)
        .join(Task, User.id == Task.user_id)
        .filter(Task.due_date == date_today)
        .all()
    )
    for task in tasks:
        yield task
