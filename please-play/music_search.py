from adapters import local, youtube

def search(song_name):
    #print('Searching for: {}'.format(song_name))

    MAX_FROM_SOURCE = 3
    medias = []

    local_files = local.search(song_name)
    if local_files:
        medias.extend(local_files[:MAX_FROM_SOURCE])

    youtube_files = youtube.search(song_name)
    if youtube_files:
        medias.extend(youtube_files[:MAX_FROM_SOURCE])

    return medias
