import os
from pathlib import PurePath
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine


DEBUG = os.environ.get('DEBUG') or False
ENV = os.environ.get('ENV') or 'development'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = PurePath(__file__).parent.parent

load_dotenv(PROJECT_DIR.joinpath('config', '.env'))
load_dotenv(find_dotenv(), override=True)


TOKEN = os.environ.get('TOKEN')

postgres_bot_str = 'postgresql://postgres:test1234@host.docker.internal/bot'

conn = create_engine(postgres_bot_str)