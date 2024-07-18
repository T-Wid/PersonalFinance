from datetime import datetime

date_format = '%d-%m-%Y'
CATEGORIES = {'I': 'Income', 'E': 'Expense'}


# Asking user for information to pass into the CSV. Using the current days date as a default
def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print('Invalid date format. Please enter the date in the correct format dd-mm-yyyy format.')
        return get_date(prompt, allow_default)


def get_amount():
    try:
        amount = float(input('Enter amount: '))
        if amount <= 0:
            raise ValueError('Amount must be greater than 0.')
        return amount
    except ValueError as e:
        print(e)
        return get_amount()


def get_category():
    category = input('Enter the category of spending here: ("I" for income or "E" for expense.)').upper()
    if category in CATEGORIES:
        return CATEGORIES[category]

    print('Invalid category. Please enter "I" for income or "E" for expense.')
    return get_category()


def get_description():
    return input('Enter a description of the transaction here: ')
