""" script to create the database tables 

this script is used to create the database tables for the bot

"""
from src.utils.db import DataBase, create_connection

connection, cursor = create_connection()

db = DataBase(connection, cursor)

# report_status table

db.create_table("report_status", """channel_id int NOT NULL,
                                reported_user varchar(255) NOT NULL,
                                reported_by varchar(255) NOT NULL,
                                reported_to varchar(255) NOT NULL,
                                reason varchar(255) NOT NULL""")
