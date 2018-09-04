import subprocess


def play(location, repeat=False):
    playback_args = ['mpv', location, '--no-video']

    if repeat:
        playback_args.append('--loop-playlist')

    subprocess.call(playback_args)
