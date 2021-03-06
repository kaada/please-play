import os
import sys
import requests
import json
from urllib.parse import urlencode

BASE_URL = 'https://www.googleapis.com/youtube/v3/search?'


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
        print('An error occured during search for YouTube data: \n{}'.format(e))
        sys.exit(1)

    try:
        data = json.loads(r.content.decode('latin1'))
        result_videos = data['items']
    except (KeyError, TypeError) as e:
        print('An error occured during parsing of YouTube data: \n{}'.format(e))
        print('YouTube returned data:\n---\n{} -> {}\n---'.format(r.status_code, r.content))
        sys.exit(1)

    if data['pageInfo']['totalResults'] == 0:
        print('No results found. Please change your search key.')
        sys.exit(1)

    return result_videos
