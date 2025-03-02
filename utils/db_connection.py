import pymysql
from pymysql import MySQLError

# Replace with your MySQL server details
DATABASE_CONFIG = {
    "host": "localhost",  # MySQL host (do not include the port number here)
    "port": 3306,         # MySQL port
    "user": "root",       # MySQL username
    "password": "root",   # MySQL password
    "database": "parspec",  # Your database name
}

def get_db_connection():
    try:
        # Establishing a connection to the database
        connection = pymysql.connect(**DATABASE_CONFIG)
        return connection
    except MySQLError as e:
        print(f"Error while connecting to MySQL: {e}")
        return None
