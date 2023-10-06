from config import dbconfig
import mysql.connector


def to_db():
    database = 'Library'
    connection = mysql.connector.connect(
        host=dbconfig["mysql"]["host"],
        user=dbconfig["mysql"]["user"],
        password=dbconfig["mysql"]["password"]
    )
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
    cursor.execute(f"USE {database}")
    return cursor, connection
