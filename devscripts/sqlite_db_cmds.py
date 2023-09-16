import sqlite3
from datetime import datetime as dt

# Create a SQLite database and a table to store the scraped data
def save_and_exit_connxn(conn):
    conn.commit()
    conn.close()


def exit_connxn(conn):
    conn.close()


def list_tables(cursor):
    return [i[0] for i in cursor.execute("SELECT distinct name FROM sqlite_master WHERE type='table';").fetchall()]


def table_exists(cursor, table):
    try:
        cursor.execute(f"SELECT distinct name FROM sqlite_master WHERE type='table' and name = '{table}';")
        try:
            return cursor.fetchone()[0] == table
        except TypeError as err: 
            # print(f"ERROR! {err}")
            return False

    except sqlite3.OperationalError as err:
        # print(f"ERROR! {err}")
        return False


def create_table(cursor, table, mode='r'):
    if mode == 'w':
        drop_table(cursor, table)
        
    # FIXME: these defaults don't work the way I thought they did, replace with working vars
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS {} (
                title TEXT NOT NULL,
                price INT NOT NULL,
                description TEXT NOT NULL,
                product_date DATE NOT NULL,
                row_cre_id TEXT DEFAULT SESSION_USER NOT NULL,
                row_cre_tmst DATETIME DEFAULT CURRENT_DATETIME NOT NULL,
                row_mod_id TEXT DEFAULT SESSION_USER NOT NULL,
                row_mod_tmst DATETIME DEFAULT CURRENT_DATETIME NOT NULL
            )
        '''.format(table))
    print(f"Created table: {table}.")


def drop_table(cursor, table):
    if table_exists(cursor, table):
        cursor.execute(f"drop table '{table}'")
        print(f"Dropped table: {table}.")
    else:
        print(f"Could not drop table {table} because {table} does not exist.")


def record_exists(cursor, table, product):
    query = f"SELECT * FROM {table} WHERE title = '{product.get_product_name()}';"
    return len(cursor.execute(query).fetchall()) > 0


def insert_record(cursor, table, product):
    title, price, desc, product_date = product.get_product_name(), product.get_price(), product.get_desc(), product.get_product_date()
    max_date = get_max_date(cursor, table, title)

    # TODO: Finish adding the sale_date to the product class
    if not record_exists(cursor, table, product) or max_date < product_date:
        cursor.execute(f'INSERT INTO {table} (title, price, description, product_date) VALUES (?, ?, ?, ?)',
                        (title, price, desc, product_date))
        
        print(f"Added deal to {table}:\nTitle: {title}\nPrice: {price}\nDescription: {desc}\nSale Date: {product_date}")

    elif max_date == product_date:
        print(f"Could not create deal for {title} for product_date == {product_date} because it already exists!")

    else:
        print(f"Something went wrong. {max_date} != {product_date}")


def get_max_date(cursor, table, title):
    # print("Getting max date...")
    query = f"SELECT MAX(product_date) FROM {table} WHERE title = '{title}'"
    result = cursor.execute(query).fetchall()[0][0]
    return dt.date(dt.strptime(result, '%Y-%m-%d')) if result is not None else dt.date(dt.today())
