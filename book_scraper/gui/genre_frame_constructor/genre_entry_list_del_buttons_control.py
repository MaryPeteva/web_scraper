from Tkconstants import END


class GenresEntryListDelButtonsControl(object):

    def __init__(self, genres_list_to):
        self.genres_list_new = genres_list_to

    def _del_item_list_genres(self):
        selection = self.genres_list_new.curselection()
        if selection:
            self.genres_list_new.delete(selection[0])

    def _del_all_list_genres(self):
        self.genres_list_new.delete(0, END)
