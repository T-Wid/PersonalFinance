import pandas as pd
import matplotlib
import csv
from datetime import datetime
from data_entry import get_date, get_amount, get_description, get_category, date_format

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
        print("Entry added successfully.")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df['date'] = pd.to_datetime(df['date'], format=CSV.date_format)
        start_date = datetime.strptime(start_date, CSV.date_format)
        end_date = datetime.strptime(end_date, CSV.date_format)

        # bitwise &, needed when using pandas df and mask rather than 'AND'
        mask = (df['date'] >= start_date & (df['date'] <= end_date))

        # using loc to find matches with the criteria of mask
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print('No transactions were found in the given timeframe.')
        else:
            print(f'Transactions from {start_date.strftime(CSV.date_format)}) to {end_date.strftime(CSV.date_format)}')
            print(filtered_df.to_string(index=False, formatter={'date': lambda x: x.strftime(CSV.date_format)}))
            total_income = filtered_df[filtered_df['category'] == 'Income']['amount'].sum()
            total_expense = filtered_df[filtered_df['category'] == 'Expense']['amount'].sum()
            print('\nSummary')
            print(f'Total Income: ${total_income:.2f}')
            print(f'Total Expense: ${total_expense:.2f}')
            print(f'Net Earnings: ${(total_income - total_expense):.2f}')

        return filtered_df



def add():
    CSV.initialize_csv()
    date = get_date('Enter the date of the transaction (dd-mm-YY), program will default to current date:',
                    allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)


add()
