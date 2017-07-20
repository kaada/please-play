import re
import codecs


def fetch_songs(file_path):
    with codecs.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:

        if file_path.endswith('.m3u'):
            if not 'EXTM3U' in f.readline():
                print('Error: The .m3u-file has no song information (EXTINF-fields are missing)')
                exit(1)
            reg = re.compile('#EXTINF:\d+,([^\r\n]+)')
        else:
            reg = re.compile('([^\r\n]+)')

        songs = []
        for line in f:
            match = re.search(reg, line)
            if match:
                songs.append(match.group(1))

        return songs
