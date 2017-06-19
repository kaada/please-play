import subprocess


def play(video_id, args):
    playback_args = ['mpv', 'https://www.youtube.com/watch?v=' + video_id]

    if not args.video:
        playback_args.append('--no-video')
    elif args.repeat:
        playback_args.append('--loop-playlist')

    subprocess.call(playback_args)
