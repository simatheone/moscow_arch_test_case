from microservice.db_selectors import get_all_tasks_and_user_emails_for_today
from microservice.email_service import send_email
from microservice.logger_config import logger
from microservice.settings import settings

EMAIL = 0
SUBJECT = 1
BODY = 2


def check_smtp_server_config(server, port, email, password):
    """
    Проверяет настройки smtp сервера, email и password от
    почтового аккаунта.

    При отсутствии какой-либо конфигурации, в лог записывает информация
    об ошибке (уровень critical) и возвращается False. Иначе возвращается True.
    """
    if not server:
        logger.critical('Нет информации о хосте для создания SMTP Сервера.')
        return False

    if not port:
        logger.critical('Нет информации о порте для создания SMTP Сервера.')
        return False

    if not email:
        logger.critical('Нет информации о email отправителя.')
        return False

    if not password:
        logger.critical('Нет информации о пароле для логина в почту')
        return False
    return True


def run():
    """
    Главная управляющая функция.
    """
    smtp_server = settings.smtp_server
    smtp_port = settings.smtp_port
    sender_email = settings.sender_email
    mail_password = settings.mail_password

    if not check_smtp_server_config(smtp_server,
                                    smtp_port,
                                    sender_email,
                                    mail_password):
        exit()
    logger.info('Все конфигурационные параметры настроены.')

    tasks_generator = get_all_tasks_and_user_emails_for_today()

    receiver_email = None
    message = None
    for data in tasks_generator:
        receiver_email = data[EMAIL]
        message_subject = data[SUBJECT]
        message_body = data[BODY]

        message = (f'Subject: {message_subject}\n\n'
                   f'{message_body}')

        try:
            send_email(smtp_server,
                       smtp_port,
                       sender_email,
                       mail_password,
                       receiver_email,
                       message)
            completion_message = (
                'Отправлено сообщение пользователю с email: '
                f'<{receiver_email}>'
            )
            logger.info(completion_message)
        except Exception as error:
            error_message = f'Сбой в работе программы. Ошибка: {error}'
            logger.error(error_message)
            exit()
    logger.info('Все задания отправлены получателям.')


if __name__ == '__main__':
    run()
