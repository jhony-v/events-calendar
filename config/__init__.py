from os import environ, path
from dotenv import load_dotenv

baseDir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(baseDir, '../.env'))

CONFIG_JWT_KEY = environ.get('JWT_KEY')

CONFIG_DATABASE_MYSQL = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "db": "calendar_events",
    "charset": "utf8"
}
