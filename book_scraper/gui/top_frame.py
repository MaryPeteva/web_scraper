import tkFileDialog
from Tkconstants import SE
from Tkinter import LabelFrame, Button
from turtle import pd

from book_scraper.gui.GUI_Input_data_selector import GUIInputDataSelector
from book_scraper.gui.GUI_verification_input import GUIInputVerificator
from book_scraper.book_genre_parser.book_link_genre_parser import BookGenresParser
from book_scraper.gui.books_frame.book_frame_constructor_mixin import BookScraperApplicationBooksFrameMixin
from book_scraper.gui.filter_frame_constructor.filter_constructor_mixin import \
    BookScraperApplicationExclusionFiltersMixin
from book_scraper.gui.genre_frame_constructor.genre_frame_constructor_mixin import \
    BookScraperApplicationGenreFrameConstructorMixin
from book_scraper.gui.search_frame_constructor.search_frame_constructor import BookScraperApplicationSearchFrameMixin
from book_scraper.gui.sort_frame_constructor.sort_frame import BookScraperApplicationSortFrame
from book_scraper.verified_input_data.verified_input_data import VerifiedInputData
from book_scraper.books import Books
from book_scraper.database.database import DataBase
from book_scraper.articles.items import Items


class BookScraperApplicationBaseFrame(object):
    """
        Main frame constructor of the GUI.
    """

    def __init__(self, return_result):
        self._sort = None
        self._search = None
        self._filter = None
        self._genres = None
        self._books = None
        self._result = return_result
        self.__label_frame = None

    def construct(self,root, genres):
        """
            Constructor for main method of GUI
        """
        self._genre_parser = genres
        self.__label_frame = LabelFrame(root, text="Book Scraper")
        self.__label_frame.grid(padx=5, pady=5, ipady=5)
        self._books = BookScraperApplicationBooksFrameMixin().construct(self.__label_frame)
        self._genres = BookScraperApplicationGenreFrameConstructorMixin(self._genre_parser.genres().content().keys())\
                                                                            .construct(self.__label_frame)
        self._filter = BookScraperApplicationExclusionFiltersMixin().construct(self.__label_frame)
        self._search = BookScraperApplicationSearchFrameMixin().construct(self.__label_frame)
        self._sort = BookScraperApplicationSortFrame().construct(self.__label_frame)


        self.titles_text = Button(self.__label_frame, text="SEARCH", command=self._search_button_on)
        self.titles_text.grid(row=9, column=0, padx=5, ipadx=14, pady=5, sticky=SE)
        self.titles_text = Button(self.__label_frame, text="OPEN FILE", command=self.open_events_db)
        self.titles_text.grid(row=10, column=0, padx=5, ipadx=7, pady=5, sticky=SE)


    def _search_button_on(self):
        """
            Scraping and parsing data method
        """
        verified_input_data = VerifiedInputData()
        GUIInputVerificator(self._books, self._genres, self._filter).verify(verified_input_data)
        GUIInputDataSelector(self._search, self._sort).select(verified_input_data)
        self._genres_parser = BookGenresParser()
        self._genres = self._genres_parser.genres().content().keys()
        self.books = Books(verified_input_data, self._genres_parser)
        self.books.collect()

    def open_events_db(self, verified_input_data):
        file_path_string = tkFileDialog.askopenfilename()
        verified_input_data.book_title = pd.read_json(file_path_string, encoding='utf-8')



