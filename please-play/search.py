#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import json


API_KEY = 'AIzaSyAY5s5JYon64zMOIlhCsHG1toZF0YB3a88'
BASE_URL= 'https://www.googleapis.com/youtube/v3/search?'


def search(song):
    query = {
        'q': song.replace(' ', '+'),
        'maxResults': 10,
        'safeSearch': "none",
        'part': 'id,snippet',
        'type': 'video',
        #'videoCategoryId': 10,
        'key': API_KEY
    }
    query_string = BASE_URL + '&'.join('{}={}'.format(key, val) for key, val in query.items())

    try:
        r = requests.get(query_string)
        data = json.loads(r.content)
        result_videos = data['items']
    except (requests.exceptions.RequestException, KeyError) as e:
        print('An error occured during searching and parsing: {}'.format(e))
        sys.exit(1)

    return result_videos
