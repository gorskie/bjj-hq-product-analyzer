import sqlite3

# Create a SQLite database and a table to store the scraped data
def create_database():
    conn = sqlite3.connect('scraped_data.db')
    cursor = conn.cursor()

    # Create a table to store the data
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS deals (
            title TEXT,
            price TEXT,
            description TEXT
        )
    ''')

    conn.commit()
    conn.close()
