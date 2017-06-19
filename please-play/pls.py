#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

import youtube_search
import mpv_gateway


def main(args):
    youtube_results = youtube_search.search(args.searchkey, \
            True if args.playlist else False)

    if args.search:
        print_search_results(youtube_results, True if args.playlist else False)
        sys.exit(0)

    if args.number and not 1 <= args.number <= len(youtube_results):
        print('Please enter a number in range {}-{}'.format(1, len(youtube_results)))
        sys.exit(1)
    data = youtube_results[args.number-1 if args.number else 0]

    print('Playing {}: {}'.format('YouTube playlist' if args.playlist else 'song', \
            get_media_title(data)))
    yt_id = get_playlist_id(data) if args.playlist else get_video_id(data)
    mpv_gateway.play(yt_id, args)


def get_media_title(media_data):
    return media_data['snippet']['title']


def get_video_id(video_data):
    return video_data['id']['videoId']


def get_playlist_id(playlist_data):
    return playlist_data['id']['playlistId']


def print_search_results(youtube_results, playlist):
    for i, v in enumerate(youtube_results, 1):
        print('{}: {} ({})'.format(i, get_media_title(v), \
            get_playlist_id(v) if args.playlist else get_video_id(v)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Play music from YouTube.')
    parser.add_argument('searchkey', metavar='string', type=str, help='name of the song or playlist to play')
    parser.add_argument('-pl', '--playlist', action='store_true', help='name of the YouYube playlist to play')
    #TODO: parser.add_argument('-f', '--file', action='store_true', help='name of the file with song(s) (i.e. playlist) to play') 
    parser.add_argument('-s', '--search', action='store_true', help='list the YouTube results')
    parser.add_argument('-n', '--number', type=int, help='number of the YouTube result to play')
    parser.add_argument('-r', '--repeat', action='store_true', help='play input on repeat')
    parser.add_argument('-v', '--video', action='store_true', help='show video')
    args = parser.parse_args()

    main(args)
