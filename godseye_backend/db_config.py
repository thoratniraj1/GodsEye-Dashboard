from mysql.connector import Error
from dotenv import load_dotenv
import os
import mysql.connector
load_dotenv()  # Load environment variables from .env file

def create_connection():
    """Create a connection to the local MySQL database"""
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def close_connection(connection):
    """Close the database connection"""
    if connection.is_connected():
        connection.close()
        print("Connection closed")


