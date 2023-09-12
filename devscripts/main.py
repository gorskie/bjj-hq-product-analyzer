import argparse
from webscrape import webscrape
from database import create_database
from webapp import app

def main():
    parser = argparse.ArgumentParser(description='Web Scraping and Database Flask App')
    parser.add_argument('--wipe', action='store_true', help='Wipe the database before launching the application')
    args = parser.parse_args()

    if args.wipe:
        create_database()  # Wipe the database by recreating it
        print("Database wiped.")

    webscrape()  # Scrape data and insert into the database
    app.run(debug=True)  # Start the Flask web application

if __name__ == '__main__':
    main()