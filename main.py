import pandas as pd
import matplotlib
import csv
from datetime import datetime

# set up a class with multiple methods to make working with CSV file easy
from pandas import DataFrame


class CSV:
    # class variable since it is used only w/in class
    CSV_FILE = 'finance_data.csv'
    COLUMNS = ['date', 'amount', 'category', 'description']
    # decorator to give access to class itself - not instance
    @classmethod
    # initialize the csv file
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

# Test:
# CSV.initialize_csv()

    @classmethod
    def add_entry(cls, date, amount, category, description):
        # Using a dictionary to write into columns
        new_entry = {
            'date': date,
            'amount': amount,
            'category': category,
            'description': description
        }
        with open(cls.CSV_FILE, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)