#db_connection.py
import pymysql
from pymysql.err import MySQLError
import os

def get_db_connection():
    try:
        conn = pymysql.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', ''),
            db=os.getenv('DB_NAME', 'student_management_db'),
            cursorclass=pymysql.cursors.DictCursor
        )
        return conn
    except MySQLError as e:
        print(f"Error: {e}")
        return None
