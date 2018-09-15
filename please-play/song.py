import music_search

class Song:
    def __init__(self, title, populate_song):
        self.title = title

        if populate_song:
            self.populate(self.title)

    def populate(self):
        self.medias = music_search.search(self.title)

    def get_title(self):
        return self.title

    def get_medias(self):
        if self.medias:
            return self.medias
