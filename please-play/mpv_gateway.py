import subprocess


BASE_URL = 'https://www.youtube.com/'


def play(yt_id, args):
    playback_args = ['mpv']

    yt_type = 'playlist?list=' if args.playlist else 'watch?v='
    playback_args.append(BASE_URL + yt_type + yt_id)

    if not args.video:
        playback_args.append('--no-video')
    if args.repeat:
        playback_args.append('--loop-playlist')

    subprocess.call(playback_args)
