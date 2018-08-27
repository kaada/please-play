#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse
import webbrowser

import youtube_search
import mpv_gateway
import playlist

BASE_URL = 'https://youtube.com/'


def main(args):

    #load search keys
    if args.file:
        args.searchkeys = playlist.fetch_songs(args.file)

    elif args.ytplaylist:
        args.searchkeys = [args.ytplaylist]

    #get youtube results
    youtube_results = []
    for s in args.searchkeys:
        search_result = youtube_search.search(s, \
                True if args.ytplaylist else False)
        if search_result:
            youtube_results.append(search_result)

    #print search results
    if args.search:
        if len(args.searchkeys) == 1:
            print_search_results(youtube_results[0], \
                    True if args.ytplaylist else False)
            sys.exit(0)
        else:
            print('Error: Please enter one search key only')
            sys.exit(1)

    #choose number
    playlist_data = []
    if args.number:
        if len(args.searchkeys) == 1 and 1 <= args.number <= len(youtube_results[0]):
            playlist_data.append(youtube_results[0][args.number-1])
        else:
            if len(args.searchkeys) != 1:
                print('Error: Cannot specify number with multiple search keys')
            if not 1 <= args.number <= len(youtube_results[0]):
                    print('Error: Please enter a number in range {}-{}'.format(1, \
                            len(youtube_results[0])))
            sys.exit(1)
    else:
        for r in youtube_results:
            playlist_data.append(r[0])

    #get and print playlist/video name(s) and id(s)
    yt_ids = []
    if args.open:
        if args.ytplaylist:
            print('Opening: {}'.format( \
                    get_playing_string(playlist_data[0], True)))
            yt_ids.append(get_playlist_id(playlist_data[0]))
        else:
            print('Opening: {}'.format( \
                    get_playing_string(playlist_data[0], False)))
            yt_ids.append(get_video_id(playlist_data[0]))

    elif args.ytplaylist:
        print('Playing YouTube Playlist{}:\n- {}'.format( \
                ' (on repeat)' if args.repeat else '',
                get_playing_string(playlist_data[0], True)))
        yt_ids.append(get_playlist_id(playlist_data[0]))

    else:
        print('Playing song(s){}:'.format(' (on repeat)' if args.repeat else ''))
        for s in playlist_data:
            print('- {}'.format(get_playing_string(s, False)))
            yt_ids.append(get_video_id(s))

    if args.open and len(yt_ids) <= 2:
        url = BASE_URL + ('playlist?list=' if args.ytplaylist else 'watch?v=') + yt_ids[0]
        webbrowser.open(url)
        sys.exit(0)

    #fire and forget
    mpv_gateway.play(BASE_URL, yt_ids, args.ytplaylist, args.video, args.repeat)

def get_playing_string(playlist_data, isplaylist):
    playing_title = get_media_title(playlist_data)

    if isplaylist:
        playing_id = get_playlist_id(playlist_data)
    else:
        playing_id = get_video_id(playlist_data)

    return '{} ({})'.format(playing_title, playing_id)


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
    parser.add_argument('searchkeys', nargs='*', metavar='string', type=str, help='name of the song(s) to play')
    parser.add_argument('-pl', '--ytplaylist', metavar='string', type=str, help='name of the YouTube playlist to play')
    parser.add_argument('-f', '--file', metavar='string', type=str, help='name of the file with song(s) (i.e. playlist) to play') 
    parser.add_argument('-s', '--search', action='store_true', help='list the YouTube results')
    parser.add_argument('-n', '--number', type=int, help='number of the YouTube result to play')
    parser.add_argument('-v', '--video', action='store_true', help='show video')
    parser.add_argument('-r', '--repeat', action='store_true', help='play output on repeat')
    parser.add_argument('-o', '--open', action='store_true', help='open video in browser')
    args = parser.parse_args()

    main(args)
