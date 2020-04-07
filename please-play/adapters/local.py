import subprocess
import re
import os
from fnmatch import fnmatch

from media_file import MediaFile

def search(song_name):
    BASE_PATH = '/Users/kaada/Music/flac'

    #TODO: Fix problem where "The Beatles - X" and "Beatles - X" does not return an exact match.
    #TODO: Implement e.g. levenshtein distance for partial matching of strings.
    song_matches = []
    for root, _, files in os.walk(BASE_PATH, topdown=False):
        for file_name in files:
            #TODO: cleanup
            if (fnmatch(file_name.lower(), f'*{song_name.lower()}*.flac')
            or (fnmatch(root.lower(), f"*{song_name.split(' - ')[0].lower()}*")
                    and fnmatch(file_name.lower(), f"*{song_name.split(' - ')[-1].lower()}*"))):
                song_matches.append(MediaFile(file_name, os.path.join(root, file_name), '💻'))

    return song_matches
