import subprocess
import fnmatch
import os

BASE_PATH = '/Users/okaada/Music/flac/'

r = []
for root, _, files in os.walk(BASE_PATH, topdown=False):
    for name in files:
        if fnmatch.fnmatch(name, '*ABBA*.flac'):
            r.append(os.path.join(root, name))
print(r)
subprocess.call(['mpv', *r])
