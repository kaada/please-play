import subprocess
import fnmatch
import os

def search(song_name):
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
