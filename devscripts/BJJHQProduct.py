from datetime import datetime as dt
from devscripts.format_datetime import format_datetime
# TODO: Add the sale_date to the product class from the site data, if possible
class BJJHQProduct():
    
    def __init__(self, site_soup):
        """ where site_text is the raw html text of bjjhq.com """
        if site_soup is not None:
            self.data = site_soup
            self.extract_data()
    

    def set_data(self, data):
        """ in case data is None for some reason and we need to assign it after construction"""
        self.data = data


    def extract_data(self):
        self.product_name = self.extract_product_name()
        self.price = self.extract_price()
        self.desc = self.extract_desc()
        self.product_date = self.extract_product_date()


    def extract_product_name(self):
        return str(self.data.h1.get_text())
    

    def extract_price(self):
        return str([elem.text for elem in self.data.find_all('em') if elem.text.strip()[0] == '$'][0]).strip('$')
    

    def extract_desc(self):
        return str(self.data.find('div', class_="desclist").find('p').text.strip())


    # TODO: this is a placeholder. this will work for now but need to extract this from the site data
    def extract_product_date(self):
        return dt.date(dt.today())
    

    def get_product_name(self):
        return self.product_name


    def get_price(self):
        return self.price
    

    def get_desc(self):
        return self.desc
    

    def get_product_date(self):
        return self.product_date