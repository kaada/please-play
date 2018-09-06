import subprocess
import re
import os
import fnmatch

from song import Song

def search(song_name, number):
    BASE_PATH = '/Users/kaada/Music/flac'
    print('Searching {}'.format(BASE_PATH))

    regex = re.compile(r'(?i).*{}.*\.flac'.format(song_name))

    found = []
    for root, _, files in os.walk(BASE_PATH, topdown=False):
        for name in files:
            if fnmatch.fnmatch(name.lower(), '*{}*.flac'.format(song_name.lower())):
                found.append(Song(name, os.path.join(root, name)))

    if found:
        for index, song in enumerate(found):
            print('{}: {}'.format(index, song.title))

        if number > len(found) - 1:
            print('Number specified {} is out of bounds {}.'.format(number, len(found) - 1))
            exit(1)
        print('{} => {}'.format(number, found[number].title))
        return found[number]
    else:
        print('=> File not found')
