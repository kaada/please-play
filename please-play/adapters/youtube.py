import os
import sys
import requests
import json
from urllib.parse import urlencode

from media_file import MediaFile

BASE_URL = 'https://www.googleapis.com/youtube/v3/search?'

DEBUG = False

def search(search_key, playlist=False):
    query = {
        'q': search_key.replace(' ', '+'),
        'maxResults': 10,
        'safeSearch': 'none',
        'part': 'id,snippet',
        'type': 'playlist' if playlist else 'video',
        # YouTubes music category.
        # Comment out to get standard search results.
        #'videoCategoryId': 10,
        'key': os.environ['GOOGLE_API_KEY']
    }
    query_string = BASE_URL + urlencode(query)

    try:
        r = requests.get(query_string)
    except requests.exceptions.RequestException as e:
        if DEBUG:
            print(f'An error occured during search for YouTube data: \n{e}')
        return

    try:
        data = json.loads(r.content.decode('latin1'))
        result_videos = data['items']
    except (KeyError, TypeError) as e:
        if DEBUG:
            print(f'An error occured during parsing of YouTube data: \n{e}')
            print(f'YouTube returned data:\n---\n{r.status_code} -> {r.content}\n---')
        return

    if data['pageInfo']['totalResults'] == 0:
        if DEBUG:
            print(f'No results found for {search_key}.\nPlease change your search key.')
        return

    found = []
    for v in result_videos:
        media_file = MediaFile(v['snippet']['title'],\
                               f"https://youtube.com/watch?v={v['id']['videoId']}",\
                               '► ')
        found.append(media_file)

    return found
