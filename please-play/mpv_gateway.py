import subprocess

def play(source, repeat=False):
    playback_args = ['mpv', source, '--no-video']

    if repeat:
        playback_args.append('--loop-playlist')

    subprocess.call(playback_args)
