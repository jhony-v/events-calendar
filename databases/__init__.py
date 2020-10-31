from config import CONFIG_DATABASE_MYSQL
import mysql.connector 

mysqlConnection = mysql.connector.connect(**CONFIG_DATABASE_MYSQL)

