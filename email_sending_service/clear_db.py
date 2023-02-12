from microservice.models import Task, User


def clear_all_tables_from_data():
    """Удаляет данные из таблиц: User, Task."""
    User.clear_table()
    Task.clear_table()


if __name__ == '__main__':
    clear_all_tables_from_data()
