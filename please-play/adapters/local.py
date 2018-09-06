import subprocess
import re
import os
import fnmatch

def search(song_name):
    BASE_PATH = '/Users/kaada/Music/flac'
#    print('Searching {}'.format(BASE_PATH), end='')

    regex = re.compile(r'(?i).*{}.*\.flac'.format(song_name))

    found = []
    for root, _, files in os.walk(BASE_PATH, topdown=False):
        for name in files:
            if fnmatch.fnmatch(name.lower(), '*{}*.flac'.format(song_name.lower())):
                found.append(os.path.join(root, name))

    if found:
        print(' => {}\nand\n{}'.format(found[0], found))
        return found[0]
    else:
        print(' => File not found')
