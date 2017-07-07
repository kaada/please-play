#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

import youtube_search
import mpv_gateway


def main(args):

    #load search keys
    if args.file:
        with open(args.file) as f:
                for line in f:
                    args.searchkeys.append(line.rstrip('\n'))

    if args.ytplaylist:
        args.searchkeys = [args.ytplaylist]

    #get youtube results
    youtube_results = []
    for s in args.searchkeys:
        search_result = youtube_search.search(s, \
                True if args.ytplaylist else False)
        youtube_results.append(search_result)

    #print search
    if args.search:
        if len(args.searchkeys) == 1:
            print_search_results(youtube_results[0], \
                    True if args.ytplaylist else False)
            sys.exit(0)
        else:
            print('Error: Please enter one search key only')

    #choose number (0 by default)
    list_of_song_data = []
    if args.number:
        if len(args.searchkeys) != 1:
            print('Error: Cannot use number with multiple search keys')
        elif not 1 <= args.number <= len(youtube_results[0]):
            print('Error: Please enter a number in range {}-{}'.format(1, \
                    len(youtube_results[0])))
        else:
            list_of_song_data.append(youtube_results[0][args.number-1])
    else:
        for r in youtube_results:
            list_of_song_data.append(r[0])

    #print playback info
    print('Playing {}:\n\t{}'.format('YouTube playlist' if args.ytplaylist \
            else 'song(s)', \
            '\n\t'.join([get_media_title(d) for d in list_of_song_data])))

    #get playlist/video id(s)
    yt_ids = []
    if args.ytplaylist:
        yt_ids.append(get_playlist_id(list_of_song_data[0]))
    else:
        for d in list_of_song_data:
            yt_ids.append(get_video_id(d))

    mpv_gateway.play(yt_ids, args.ytplaylist, args.video, args.repeat)


def get_media_title(media_data):
    return media_data['snippet']['title']


def get_video_id(video_data):
    return video_data['id']['videoId']


def get_playlist_id(playlist_data):
    return playlist_data['id']['playlistId']


def print_search_results(youtube_results, playlist):
    for i, v in enumerate(youtube_results, 1):
        print('{}: {} ({})'.format(i, get_media_title(v), \
            get_playlist_id(v) if args.ytplaylist else get_video_id(v)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Play music from YouTube.')
    parser.add_argument('searchkeys', nargs='*', metavar='string', type=str, help='name of the song or playlist to play')
    parser.add_argument('-pl', '--ytplaylist', metavar='string', type=str, help='name of the YouYube playlist to play')
    parser.add_argument('-f', '--file', metavar='string', type=str, help='name of the file with song(s) (i.e. playlist) to play') 
    parser.add_argument('-s', '--search', action='store_true', help='list the YouTube results')
    parser.add_argument('-n', '--number', type=int, help='number of the YouTube result to play')
    parser.add_argument('-r', '--repeat', action='store_true', help='play input on repeat')
    parser.add_argument('-v', '--video', action='store_true', help='show video')
    args = parser.parse_args()

    main(args)
