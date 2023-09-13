import argparse
import sqlite3
from webscrape import webscrape
from database import create_database
from datetime import datetime as dt
from webapp import app

def main():
    parser = argparse.ArgumentParser(description='Web Scraping and Database Flask App')
    parser.add_argument('--wipe', action='store_true', help='Wipe the database before launching the application')
    args = parser.parse_args()

    db_name = 'scraped_data.db' # pull this out later

    mode = 'w' if args.wipe else 'r'
    create_database(db_name, mode)
    
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    url = 'http://bjjhq.com'

    webscrape(url, db_name)  # Scrape data and insert into the database
    app.run(debug=True, use_reloader=False)  # Start the Flask web application

if __name__ == '__main__':
    main()