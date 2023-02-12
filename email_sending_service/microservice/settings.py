import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent.parent
ENV_DIR = BASE_DIR / '.env'

load_dotenv(ENV_DIR)


class Settings:
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = os.getenv('SMTP_PORT')
    sender_email = os.getenv('SENDER_EMAIL')
    mail_password = os.getenv('MAIL_PASSWORD')
    database_uri = os.getenv('SQLALCHEMY_DATABASE_URI')


settings = Settings()
