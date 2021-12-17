""" 
python class for database CRUD operations
"""
import os
import psycopg2

from src.utils.utils import DATABASE_URL

def create_connection():
    """
    Create a connection to the database
    """
    connection = None
    cursor = None
    try: # get the database connection from postgres url
        #connection = psycopg2.connect("postgresql://{}:{}@{}:{}/{}".format(config['user'], config['password'], config['host'], config['port'], config['database']))
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        return connection, cursor
    except (Exception, psycopg2.DatabaseError) as error:
        return connection, cursor
    
class DataBase:
    """ Postgresql Database class """
    
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
    
    
    def select_data(self, table_name, columns, condition):
        """
        Select data from the database
        """
        try:
            self.cursor.execute(
                "SELECT {} FROM {} WHERE {}".format(
                    columns,
                    table_name,
                    condition))
            return self.cursor.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    
    def update_data(self, table_name, data, condition):
        """
        Update data in the database
        """
        try:
            self.cursor.execute(
                "UPDATE {} SET {} WHERE {}".format(
                    table_name,
                    data,
                    condition))
            self.connection.commit()
            print("Data updated successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    
    def delete_data(self, table_name, condition):
        """
        Delete data from the database
        """
        try:
            self.cursor.execute(
                "DELETE FROM {} WHERE {}".format(
                    table_name,
                    condition))
            self.connection.commit()
            print("Data deleted successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    
    def drop_table(self, table_name):
        """
        Drop a table from the database
        """
        try:
            self.cursor.execute(
                "DROP TABLE IF EXISTS {}".format(
                    table_name))
            self.connection.commit()
            print("Table {} dropped successfully".format(table_name))
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
