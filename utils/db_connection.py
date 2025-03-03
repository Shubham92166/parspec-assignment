import pymysql
import os
from pymysql import MySQLError
from dotenv import load_dotenv

load_dotenv()

# Replace with your MySQL server details
DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT")),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_DATABASE"),
}

def get_db_connection():
    try:
        # Establishing a connection to the database
        connection = pymysql.connect(**DATABASE_CONFIG)
        return connection
    except MySQLError as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
