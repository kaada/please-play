import subprocess
import re
import os
import fnmatch

from media_file import MediaFile

def search(song_name):
    BASE_PATH = '/Users/kaada/Music/flac'
    ACCEPT_PARTIAL_MATCH = True
    #print('Searching {}'.format(BASE_PATH))

    regex = re.compile(r'(?i).*{}.*\.flac'.format(song_name))

    exact_match, partial_match = [], []
    for root, _, files in os.walk(BASE_PATH, topdown=False):
        for name in files:
            if fnmatch.fnmatch(name.lower(), f'*{song_name.lower()}*.flac'):
                exact_match.append(MediaFile(name, os.path.join(root, name), '💻'))
            if fnmatch.fnmatch(name.lower(), f"*{song_name.split('-')[-1].lower()}*.flac"):
                partial_match.append(MediaFile(name, os.path.join(root, name), '💻'))

    if exact_match:
        return exact_match
    elif ACCEPT_PARTIAL_MATCH and partial_match:
        return partial_match
    #else:
    #    print('Not found on 💻.')
