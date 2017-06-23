import subprocess

BASE_URL = 'https://www.youtube.com/'


def play(youtube_id, args):
    playback_args = ['mpv']

    youtube_type = 'playlist?list=' if args.playlist else 'watch?v='
    playback_args.append(BASE_URL + youtube_type + youtube_id)

    if not args.video:
        playback_args.append('--no-video')
    if args.repeat:
        playback_args.append('--loop-playlist')

    subprocess.call(playback_args)
