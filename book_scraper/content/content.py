# -*- coding: utf-8 -*-
from book_scraper.database.database import DataBase


class Content(object):
    """
        Interafce class to collect parsed data from BookContentParser and DataBase.
        Provides loosly coupling between BookContentParser and DataBase and could be used for maangement of
        multiple scraping items
    """
    def __init__(self):
        self._content = {}

    def add(self, genre, title, price, rating, available, description, upc):
        self._content[upc] = []
        self._content[upc].append(title)
        self._content[upc].append(genre)
        self._content[upc].append(price)
        self._content[upc].append(rating)
        self._content[upc].append(available)
        self._content[upc].append(description)

    def export_to_db(self):
        database = DataBase()
        for key, value in self._content.items():
            title = value[0]
            genre = value[1]
            price = value[2]
            rating = value[3]
            available = value[4]
            description = value[5]
            database.add_item(title, genre, price, rating, available, description, key)

    def reset(self):
        self._content.clear()

    def view(self):
        for k, v in self._content.items():
            print('{} {}'.format(k, v))
