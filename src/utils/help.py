""" helper function to Database """

from src.utils.db import DataBase, create_connection
import pandas as pd
import datetime

connection, cursor = create_connection()
db = DataBase(connection, cursor)


# FIX: create class here
class DBHelper:

    def __init__(self) -> None:
        pass

    def create_report(self, *args):
        """ Create a user report in the database """
        db.insert_data("report_status", *args)


    def get_report_csv(self, columns, condition):
        """ Get a user report from the database """
        results = db.select_data("report_status", columns, condition)
        df = pd.DataFrame(results, columns=['timestamp', 'channel_id', 'reported_user', 'reported_by', 'reported_to', 'reason'])
        df["timestamp"] = df["timestamp"].apply(lambda x: datetime.datetime.fromtimestamp(x))
        df = df[['timestamp', 'reason']]
        return df

