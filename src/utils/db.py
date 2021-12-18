""" 
python class for database CRUD operations

    
"""
import sqlite3
import psycopg2

def create_connection(DATABASE_URL):
    """
    Create a connection to the database

    args:
        DATABASE_URL: database url
    
    returns:
        connection: connection to the database
        cursor: cursor to the database
    """
    connection = None
    cursor = None
    try: # get the database connection from postgres ur
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        return connection, cursor
    except (Exception, psycopg2.DatabaseError) as error:
        return connection, cursor
    
class DataBase:
    """ Postgresql Database class 
    
    methods:
        - create_table - create a table in the database
        - insert_data - insert data into a table in the database
        - select_data - select data from a table in the database
        - update_data - update data in a table in the database
        - delete_data - delete data from a table in the database
        - drop_table - drop a table in the database
    """
    
    def __init__(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor
    

    def create_table(self, table_name, table_columns):
        """
        Create a table in the database
        """
        try:
            sql_query = "CREATE TABLE IF NOT EXISTS {} ({})".format(table_name, table_columns)
            self.cursor.execute(sql_query)
            self.connection.commit()
            print("Table {} created successfully".format(table_name))
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    

    def insert_data(self, table_name, *args):
        """
        Insert data into the database
        """
        try:
            sql_query = "INSERT INTO {} VALUES {}".format(table_name, args)
            self.cursor.execute(sql_query)
            self.connection.commit()
            print("Data inserted successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    
    
    def select_data(self, table_name, condition):
        """
        Select data from the database
        """
        try:
            sql_query = "SELECT * FROM {} WHERE {}".format(table_name, condition)
            self.cursor.execute(sql_query)
            return self.cursor.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    

    def update_data(self, table_name, data, condition):
        """
        Update data in the database
        """
        try:
            sql_query = "UPDATE {} SET {} WHERE {}".format(table_name, data, condition)
            self.cursor.execute(sql_query)
            self.connection.commit()
            print("Data updated successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    

    def delete_data(self, table_name, condition):
        """
        Delete data from the database
        """
        try:
            sql_query = "DELETE FROM {} WHERE {}".format(table_name, condition)
            self.cursor.execute(sql_query)
            self.connection.commit()
            print("Data deleted successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


    def count_data(self, table_name, condition):
        """
        Count data from the database
        """
        try:
            sql_query = "SELECT COUNT(*) FROM {} WHERE {}".format(table_name, condition)
            self.cursor.execute(sql_query)
            return self.cursor.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
