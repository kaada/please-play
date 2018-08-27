import subprocess
import fnmatch
import os

BASE_PATH = '/Users/USERNAME/Music/'

r = []
for root, _, files in os.walk(BASE_PATH, topdown=False):
    for name in files:
        if fnmatch.fnmatch(name, '*SONG NAME*.flac'):
            r.append(os.path.join(root, name))

subprocess.call(['mpv', *r])
