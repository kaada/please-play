import subprocess


def play(BASE_URL, youtube_ids, ytplaylist, video, repeat):
    playback_args = ['mpv']

    if ytplaylist:
        playback_args.append(BASE_URL + 'playlist?list=' + youtube_ids[0])
    else:
        for youtube_id in youtube_ids:
            playback_args.append(BASE_URL + 'watch?v=' + youtube_id)

    if not video:
        playback_args.append('--no-video')
    if repeat:
        playback_args.append('--loop-playlist')

    subprocess.call(playback_args)
