""" script to create the database tables 

this script is used to create the database tables for the bot

"""
from src.utils.db import DataBase, create_connection
from src.utils.utils import DATABASE_URL

connection, cursor = create_connection(DATABASE_URL)
db = DataBase(connection, cursor)

# report_status table
db.create_table("report_status", """
                                datetime timestamp NOT NULL,
                                channel_id numeric NOT NULL,
                                reported_user varchar(100) NOT NULL,
                                reported_by varchar(100) NOT NULL,
                                reported_to varchar(100) NOT NULL,
                                reason varchar(255) NOT NULL""")



# remind_me_table
# notes_table 
