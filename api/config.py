from dotenv import load_dotenv
from os import getenv, path
from pathlib import Path
from sys import exit

dotenv_path = Path(__file__).resolve().parent.parent / '.env'
if not dotenv_path.exists():
    print('error: dotenv path not found')
    print(f'resolved path: {dotenv_path}')
    exit(1)

load_dotenv(dotenv_path)


class Config:
    """Stores Flask configuration variables loaded from .env"""

    SECRET_KEY = getenv('SECRET_KEY')
    FLASK_ENV = getenv('FLASK_ENV')

    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL')
    SQLALCHEMY_ECHO = getenv('SQLALCHEMY_ECHO', 'true').lower() == 'true'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
