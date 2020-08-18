import music_search

class Song:
    def __init__(self, title, populate_song):
        self.title = title
        self.medias = []

        if populate_song:
            self.populate(self.title)

    def populate(self):
        self.medias = music_search.search(self.title)

    def get_title(self):
        return self.title

    def get_medias(self):
        return self.medias

    def print_medias(self):
        print(f'Showing results for: {self.get_title()}')

        medias = self.get_medias()
        if medias:
            for m in medias:
                print(m)
        else:
            print(f'No media found for "{self.get_title()}". Try to repopulate the song.')
