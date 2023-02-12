from smtplib import SMTP_SSL, ssl


def send_email(smtp_server,
               port,
               sender_email,
               mail_password,
               receiver_email,
               message):
    """Функция отправки email сообщения."""
    context = ssl.create_default_context()

    with SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, mail_password)
        server.sendmail(sender_email, receiver_email, message)
