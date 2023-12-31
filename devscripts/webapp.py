from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def display_deals():
    conn = sqlite3.connect('scraped_data.db') # TODO: pull this db name out of here and into dotenv
    cursor = conn.cursor()

    # Retrieve data from the database
    cursor.execute('SELECT * FROM deals')
    deals = cursor.fetchall()

    conn.close()

    return render_template('index.html', deals=deals)
