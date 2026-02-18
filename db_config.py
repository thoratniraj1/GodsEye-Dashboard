from mysql.connector import Error

import mysql.connector

def create_connection():
    """Create a connection to the local MySQL database"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='GodsEye1234@',
            database='godseye'
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


