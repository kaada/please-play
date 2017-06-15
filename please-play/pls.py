#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import subprocess
import requests

import search

def pls(args):
    print('args:', args)

    youtube_results = search.search(args.song)
    if args.search:
        print_search_results(youtube_results)
    else:
        video_data = youtube_results[args.number-1 if args.number else 0]
        play_video(video_data)

def play_video(video_data):
    print('Playing song: {}'.format(video_data['snippet']['title']))
    youtube_url = 'https://www.youtube.com/watch?v=' + get_video_id(video_data)
    subprocess.call(['mpv', '--no-video', youtube_url])

def get_video_id(video_data):
    return video_data['id']['videoId']

def print_search_results(youtube_results):
    for i, v in enumerate(youtube_results, 1):
        print('{}: {} ({})'.format(i, v['snippet']['title'], v['id']['videoId']))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Play music from YouTube.')
    parser.add_argument('-s', '--search', action='store_true', help='list the YouTube results')
    parser.add_argument('-n', '--number', type=int, help='number of the YouTube result to play')
    parser.add_argument('song', nargs='?', metavar='string', type=str, help='name of the song to play')
    args = parser.parse_args()

    pls(args)
