from sys import argv
import json
import requests

BASE_URL = 'https://itunes.apple.com/search?term='


def parse(query):
    """print(BASE_URL + query)
    r = requests.get(BASE_URL + query)
    print(r)
    return r"""
    print('Looking up: {}'.format(query))
    return query

def parse_json(json_content):
    data = json.loads(r.content.decode('latin1'))
    return data

if __name__ == "__main__":
    r = parse('+'.join(argv[1:]))
    j = parse_json(r)
    results = j['results']
    print(len(results))
    r1 = results[0]
    print('{} - {}'.format(r1['artistName'], r1['trackName']))
