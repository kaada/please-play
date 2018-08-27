import subprocess
import fnmatch
import os

def search(song_name):
    print('Searching for: {}'.format(song_name))

    music = None

    music = search_local(song_name)
    if music is None:
        music = search_youtube(song_name)

    return music


def search_local(song_name):
    BASE_PATH = '/Users/kaada/Music/flac'
    print('Searching {}'.format(BASE_PATH), end='')

    r = []
    for root, _, files in os.walk(BASE_PATH, topdown=False):
        for name in files:
            if fnmatch.fnmatch(name, '*{}*.flac'.format(song_name)):
                r.append(os.path.join(root, name))

    if r:
        print(' => {}'.format(r[0]))
        return r[0]
    else:
        print(' => File not found')


def search_youtube(song_name):
    r = 'https://www.youtube.com/watch?v=yuyV6G6atoQ'
    print('Searching {}'.format('YouTube'), end='')
    print(' => {}'.format(r))
    return r
