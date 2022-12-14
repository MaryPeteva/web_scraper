from Tkinter import Button

from genre_entry_list_del_buttons_control import \
    GenresEntryListDelButtonsControl


class BookScraperApplicationGenresDelButtons(object):

    def __init__(self, genres_list_to):

        super(BookScraperApplicationGenresDelButtons, self).__init__(genres_list_to)
        self.__label_frame_genres = None
        self.genres_list_new = None

    def _del_control(self, frame, genres_list_to):
        self.__label_frame_genres = frame
        self.genres_list_new = genres_list_to
        del_control_functions = GenresEntryListDelButtonsControl(self.genres_list_new)._del_item_list_genres
        del_all__control_function = GenresEntryListDelButtonsControl(self.genres_list_new)._del_all_list_genres

        self.select_genre_button_del = Button(self.__label_frame_genres, text="DEL", command=del_control_functions)
        self.select_genre_button_del.grid(padx=8, ipadx=15)
        self.select_genre_button_del_all = Button(self.__label_frame_genres, text="DEL ALL",
                                                  command=del_all__control_function)
        self.select_genre_button_del_all.grid(padx=1, ipadx=2)

    
    
    