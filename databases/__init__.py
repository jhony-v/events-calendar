import pymysql.cursors
from config import CONFIG_DATABASE_MYSQL

mysqlConnection = pymysql.Connection(**CONFIG_DATABASE_MYSQL)