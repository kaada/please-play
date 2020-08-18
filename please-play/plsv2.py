#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse

import name_parse
import music_search
import play_file
import song
from playlist import Playlist
import toolbox


def main(args):

    if args.playlist:
        songs = toolbox.load_playlist_file(args.playlist)
        pl = Playlist(songs)
    else:
        raw_song_name = ' '.join(args.searchkey)
        pl = Playlist([raw_song_name])

    for s in pl.get_songs():
        s.populate()

        if args.search:
            s.print_medias()
            continue

        play_song(s, args.repeat)

def play_song(song, repeat=False):
    """Plays the song with the preferred music player, e.g. mpv.."""

    print('---')
    print(f'Playing song: {song.get_title()}')

    medias = song.get_medias()
    if medias:
        #TODO: media file analysis
        selected_media = medias[0]
        print(selected_media)
        play_file.play(selected_media.get_source(), repeat)
    else:
        print(f'No media file found for "{song.get_title()}".')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plays the given song from the best source available.')
    parser.add_argument('searchkey', nargs='*', metavar='string', type=str, help='name of the song(s) to play')
    parser.add_argument('-n', '--number', type=int, help='number of the YouTube result to play')
    parser.add_argument('-pl', '--playlist', metavar='string', type=str, help='name of playlist to play')
    parser.add_argument('-s', '--search', action='store_true', help='list the results')
    parser.add_argument('-r', '--repeat', action='store_true', help='play output on repeat')

    args = parser.parse_args()

    main(args)
