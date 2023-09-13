from bs4 import BeautifulSoup
# TODO: add reference to BeautifulSoup so it's in scope
class MockSoup():
    fname = 'devscripts/soup_08-10-2023_2009.txt'

    def __init__(self):
        with open(self.fname, 'r') as f:
            self.raw_soup = BeautifulSoup(f, 'html.parser')


    def get_soup(self):
        return self.raw_soup