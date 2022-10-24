""" helper function to Database """
from numpy import delete
import pandas as pd
import datetime

from src.utils.db import DataBase, create_connection
from src.utils.utils import DATABASE_URL

connection, cursor = create_connection(DATABASE_URL)
db = DataBase(connection, cursor)

report_status_table = "report_status"


class DBHelper:

    """
    Helper functions for the database

    methods:
        - create_report - create a report of a user in the database
        - get_report_csv - get a report of a user from the database
    """

    def __init__(self) -> None:
        pass

    def create_report(self, *args):
        """ Create a user report in the database

        Arguments:
            args {list} -- list of columns to be inserted
        """
        db.insert_data(report_status_table, *args)

    def get_report_csv(self, condition):
        """ Get a user report from the database

        Arguments:
            columns {list} -- list of columns to be selected
            condition {str} -- condition to be applied
        """
        try:
            results = db.select_data("report_status", condition)

            df = pd.DataFrame(results, columns=['timestamp_UTC', 'guild_id', 'reported_user', 'reported_by', 'reported_to', 'reason'])
            return_df = df[['timestamp_UTC', 'reported_user', 'reported_by', 'reason']]
        except Exception as e:
            print(e)
        return return_df

    def get_report_count(self, condition):
        """ Get the number of reports in the database

        Arguments:
            condition {str} -- condition to be applied
        """
        counts = db.count_data(report_status_table, condition)
        return counts[0][0]

    def delete_user_report(self, condition):
        """ Delete a user report from the database

        Arguments:
            condition {str} -- condition to be applied
        """
        db.delete_data(report_status_table, condition)
