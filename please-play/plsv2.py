#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import argparse

import name_parse
import music_search
import play_file


def main(args):
    raw_song_name = ' '.join(args.searchkey)
    print('Processing search key: {}'.format(raw_song_name))

    processed_song_name = parse_song_name(raw_song_name)

    music_file = get_music_file(processed_song_name, args.number)

    play(music_file)


def parse_song_name(raw_song_name):
    """Tries to convert raw (inputted) song name to exact name, based on online information, if available."""
    return name_parse.parse(raw_song_name)


def get_music_file(song_name, number):
    """Checks if the music file is on disk. If not, retrieves it from external sources."""
    if not number: # TODO: move value to function definition
        number = 0
    return music_search.search(song_name, number)

def play(music_file):
    """Plays the music file with the preferred music player, e.g. mpv.."""
    #play_file.play(music_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plays the given song from the best source available.')
    parser.add_argument('searchkey', nargs='*', metavar='string', type=str, help='name of the song(s) to play')
    parser.add_argument('-n', '--number', type=int, help='number of the YouTube result to play')

    args = parser.parse_args()

    main(args)
