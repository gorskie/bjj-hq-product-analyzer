import sqlite3
import requests
from bs4 import BeautifulSoup
def webscrape():
    url = 'https://www.bjjhq.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    deal_titles = soup.find_all(class_='right')

    conn = sqlite3.connect('scraped_data.db')
    cursor = conn.cursor()

    for item in deal_titles:
        h1_element = item.find('h1')
        price_element = item.find('div', class_='buydiv inactive')
        description = item.find('div', class_='desclist')

        if h1_element is not None and description is not None and price_element is not None:
            title = h1_element.text.strip()
            price = price_element.text.strip()
            desc = description.text.strip()

            # Insert the data into the database
            cursor.execute('INSERT INTO deals (title, price, description) VALUES (?, ?, ?)',
                           (title, price, desc))

    conn.commit()
    conn.close()
