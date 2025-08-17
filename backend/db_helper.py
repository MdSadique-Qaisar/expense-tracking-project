import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger('db_helper')

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = "Zxmnbv@12*",
        database = 'expense_manager'
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()

    cursor.close()
    connection.close()

def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with date : {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute('select * from expenses where expense_date=%s', (expense_date,))
        expenses = cursor.fetchall()
        return expenses

def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called with date : {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("delete from expenses where expense_date=%s",(expense_date,))

def insert_expense(expense_date, amount, category, notes):
    logger.info(f"insert_expense called with date : {expense_date}, amount : {amount}, category : {category}, notes : {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("insert into expenses (expense_date, amount, category, notes) values (%s, %s, %s, %s)",(expense_date, amount, category, notes))

def fetch_expenses_summary(start_date, end_date):
    logger.info(f"fetch_expenses_summary called with start_date : {start_date}, end_date : {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute('''select category, sum(amount) as total, (sum(amount)/sum(sum(amount)) over()) * 100 as percentage
                          from expenses 
                          where expense_date between %s and %s
                          group by category''',
                        (start_date,  end_date)
                       )
        data = cursor.fetchall()
        return data

if __name__ == '__main__':
    expenses = fetch_expenses_for_date('2024-08-30')
    # for expense in expenses:
    print(expenses)
    # insert_expense('2024-08-25', 40, 'Food', 'Eat tasty samosa chat')
    # delete_expenses_for_date('2024-08-25')
    summary = fetch_expenses_summary("2024-08-01", "2024-08-05")
    for expense in summary:
        print(expense)