import mysql.connector
from mysql.connector import Error


class SQL_function():
    def create_db_connection(host_name, user_name, user_password, db_name):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

        return connection

    def execute_query(connection, query, varlist=None):
        cursor = connection.cursor(buffered=True)
        try:
            if varlist is None:
                cursor.execute(query)
            else:
                cursor.execute(query, varlist)
            connection.commit()
            return cursor
        except Error as err:
            print(f"Error: '{err}'")
            return cursor

    def executemany_query(connection, query, varlist=None):
        cursor = connection.cursor(buffered=True)
        try:
            if varlist is None:
                cursor.executemany(query)
            else:
                cursor.executemany(query, varlist)
            connection.commit()
            return cursor
        except Error as err:
            print(f"Error: '{err}'")
            return cursor