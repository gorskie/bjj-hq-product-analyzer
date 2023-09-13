import sqlite3
from datetime import datetime as dt

# Create a SQLite database and a table to store the scraped data
def create_database(db_name, mode='r'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create a table to store the data
    table = 'deals'
    create_table(cursor, table, mode)

    conn.commit()
    conn.close()


def create_table(cursor, table, mode='r'):
    if mode == 'w':
        drop_table(cursor, table)
        
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS {} (
                title TEXT NOT NULL,
                price TEXT NOT NULL,
                description TEXT NOT NULL,
                product_date DATE NOT NULL
            )
        '''.format(table))
    print(f"Created table: {table}.")


def drop_table(cursor, table):
    # TODO: add handling if the table doesnt already exist
    cursor.execute(f"drop table {table}")
    print(f"Dropped table: {table}.")


def insert_record(cursor, product):
    title, price, desc = product.get_product_name(), product.get_price(), product.get_desc()
    max_date = get_max_date(cursor, title)
    today = dt.today()

    if max_date is None or max_date < today:
        cursor.execute('INSERT INTO deals (title, price, description, product_date) VALUES (?, ?, ?, ?)',
                        (title, price, desc, today))
        print(f"Added deal to deals:\nTitle: {title}\n Price: {price}\nDescription: {desc}")
    elif max_date == today:
        print(f"Could not create deal for {title} because it already exist!")


def get_max_date(cursor, title):
    cursor.execute('SELECT MAX(product_date) FROM deals WHERE title = \'{title}\'')
    results = cursor.fetchall()
    return results[0][0]

