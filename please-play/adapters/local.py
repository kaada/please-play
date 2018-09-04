import subprocess
import re
import os

def search(song_name):
    BASE_PATH = '/Users/kaada/Music/flac'
#    print('Searching {}'.format(BASE_PATH), end='')

    regex = re.compile(r'(?i).*{}.*\.flac'.format(song_name))

    r = []
    for root, _, files in os.walk(BASE_PATH, topdown=False):
        print(files)
        found = filter(regex.match, files)
        print([f for f in found])
        if found:
            return os.path.join(root, found[0])

    if r:
        print(' => {}'.format(r[0]))
        return r[0]
    else:
        print(' => File not found')
