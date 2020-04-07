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

        play(s)

def play(song):
    """Plays the song with the preferred music player, e.g. mpv.."""

    print('---')
    print(f'Playing song: {song.get_title()}')

    medias = song.get_medias()
    if medias:
        for media in medias: 
            print(media)

        #TODO: media file analysis
        best_media = medias[0]
        play_file.play(best_media.get_source())
    else:
        print(f'No media file found for "{song.get_title()}".')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plays the given song from the best source available.')
    parser.add_argument('searchkey', nargs='*', metavar='string', type=str, help='name of the song(s) to play')
    parser.add_argument('-n', '--number', type=int, help='number of the YouTube result to play')
    parser.add_argument('-pl', '--playlist', metavar='string', type=str, help='name of playlist to play')

    args = parser.parse_args()

    main(args)
