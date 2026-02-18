from db_config import create_connection, close_connection

if __name__ == "__main__":
    connection = create_connection()
    close_connection(connection)
