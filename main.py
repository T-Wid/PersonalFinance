import pandas as pd
import matplotlib
import csv
from datetime import datetime

# set up a class with multiple methods to make working with CSV file easy
from pandas import DataFrame


class CSV:
    # class variable since it is used only w/in class
    CSV_FILE = 'finance_data.csv'

    # decorator to give access to class itself - not instance
    @classmethod
    # initialize the csv file
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df: DataFrame = pd.DataFrame(columns=['date', 'amount', 'category', 'description'])
            df.to_csv(cls.CSV_FILE, index=False)


# Test:
CSV.initialize_csv()
