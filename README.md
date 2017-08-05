# please-play
A lightweight terminal based YouTube music player

## How to use:

1. Install dependencies:

    ```brew install mpv```
    
    
    ```python setup.py install```
    
(Or by using pacman/apt-get/++)

2. Play whatever song you want:

    ```python pls.py "wonder woman theme"```
    
3. If you are not satisfied;

    List the results, and choose something else.

    ```python pls.py "wonder woman theme" -s```

    ```python pls.py "wonder woman theme" -n 7```

## Optional arguments:
Youtube playlists can be specified by the argument ```-pl```:

    ```python pls.py -pl "pokemon indigo league music"```

A file/playlist (raw/m3u) with song names, seperated by newlines, can be loaded with ```-f```:

    ```python pls.py -f FILE_LOCATION```
    

Please check out ```python pls.py -h``` for additional features and arguments.
