from adapters import local, youtube

def search(song_name):
    print('Searching for: {}'.format(song_name))

    music = None

    music = local.search(song_name)
    if music is None:
        music = youtube.search(song_name)

    return music
