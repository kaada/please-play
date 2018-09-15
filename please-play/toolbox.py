import re
import codecs
import errno

def load_playlist_file(file_path):
    try:
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

    except OSError as e:
        if e.errno == errno.ENOENT:
            print("Error: File '{}' not found".format(e.filename))
        else:
            print(e)
        exit(1)
