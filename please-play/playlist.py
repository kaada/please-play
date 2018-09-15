from song import Song

class Playlist:
    def __init__(self, songs, populate_songs=False):
        self.songs = []

        for s in songs:
            song = Song(s, populate_songs)

            self.songs.append(song)

    def get_songs(self):
        return self.songs
