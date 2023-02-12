from datetime import date, timedelta

from faker import Faker

from microservice.models import Task, User


def fill_tables_with_test_data():
    """
    Заполняет базу тестовыми данными и пользователем
    с реальным email адресом.

    Для создания будущих заданий используется timedelta(days=1)
    для смещения даты при каждой итерации на единицу.

    На каждого тестового пользователя, кроме первого, создается
    по два задания на день.
    """
    fake = Faker()
    date_today = date.today()
    delta = timedelta(days=1)
    create_email_receiver(due_date=date_today)

    # цикл начинается с 2, так как первого пользователя
    # добавили в функции create_email_receiver
    for number in range(2, 11):
        User.seed(fake)
        for _ in range(2):
            Task.seed(fake, date_today, number)
        date_today += delta


def create_email_receiver(due_date):
    """
    Создает пользователя, которому будет выслан email.
    При запуске запрашивается email адрес, на который пользователь
    хочет получить тестовую задачу.
    """
    email = input(
        'Укажите email адрес, на который вы хотите '
        'получить тестовое письмо: '
    )
    if not email:
        print(
            'Необходимо указать email для будущей отправки сообщений!'
        )
        return create_email_receiver(due_date)

    user = User(email=email,
                first_name='Test',
                last_name='User')

    task = Task(title='Test subject',
                description='Test body for email',
                due_date=due_date,
                user_id=1)
    user.save()
    task.save()


if __name__ == '__main__':
    fill_tables_with_test_data()
