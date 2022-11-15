# -*- coding: utf-8 -*-
import json

from book_scraper.book_link_parser.book_link_parser import BookLinkParser
from book_scraper.cli_input_arguments.cli_input_arguments import InputArguments
from book_scraper.book_content_parser.book_content_parser import BooksContentParser
from book_scraper.database.database import DataBase
from book_scraper.articles.items import Items


class Books(Items):
    """
        Books class, organizes retrieving, parsing, collecting and representing all data from the given site
    """
    def __init__(self, args, genres_object):
        super(Books, self).__init__()
        self._data = DataBase()
        self._genres = genres_object
        self._from_input = args
        self._links = BookLinkParser(self._genres)
        self._search = BooksContentParser()
        self.default_key = "upc"

    def collect(self):
        """
            Orchestration of all operations step-by-step from raw data to parsed and structured information about every
            book from selection
        """
        links = self._links.collect(self._from_input.genres, self._from_input.books)
        content = self._search.collect(self._from_input.filter, links)
        content.export_to_db()
        sorting = self._from_input.sort
        sort_type = self._from_input.sort_type
        book_title = self._from_input.book_title
        keywords = self._from_input.keywords
        if book_title:
            self.fill_searched_items()
            for word in book_title:
                self.filter('title', word)
            self.print_items()
            return
        if keywords:
            self.fill_searched_items()
            for word in keywords:
                self.filter('description', word)
            self.print_items()
            return
        if sorting:
            self.fill_searched_items()
            if sort_type:
                self.sort_data(sorting, sort_type != 'ascending')
                self.print_items()
                return
            else:
                self.sort_data(sorting)
                self.print_items()
                return

        else:
            self.fill_searched_items()
            self.print_items()


