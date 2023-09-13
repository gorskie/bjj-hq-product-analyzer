import sqlite3
from make_requests import make_request
from database import insert_record
from BJJHQProduct import BJJHQProduct
from MockSoup import MockSoup
from bs4 import BeautifulSoup
from datetime import datetime as dt


def webscrape(url, db_name):
    """
    Takes a url as a string and inserts a new deal from the page
    """
    response = make_request(url) # disable for testing
    raw_soup = BeautifulSoup(response.text, 'html.parser')
    # raw_soup = MockSoup().get_soup()
    product = BJJHQProduct(raw_soup)

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # if title is not None and price is not None and desc is not None: # TODO: add handling to prevent None sfrom ever loading in the class
    insert_record(cursor, product)

    conn.commit()
    conn.close()
