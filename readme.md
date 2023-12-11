yt-dlp-gui
----------

A simple frontend for [yt-dlp](https://www.github.com/yt-dlp/yt-dlp) made in python+tkinter

Requirements
------------

1. `pyinstaller`
2. Ensure that the [yt-dlp](https://www.github.com/yt-dlp/yt-dlp) executable is either accessible from `PATH` or in the same directory as the `ytgui` executable file


Usage
-----
1. Select audio format to be extracted from the `--AUDIO--` drop-down
2. if you want to keep the video file,
    - Check the `Keep Video?` checkbox
    - Choose the file format to store the downloaded video in from the `--VIDEO--` dropdown
3. Paste the [YouTube](https://www.youtube.com) for a video inside the `URL` field
4. Click `Download`

Building
--------

To build the executable file, 

1. clone the repository
```bash
git clone https://www.github.com/gaurav5-5/yt-dlp-gui
```

2. `cd` to cloned repository
```bash
cd yt-dlp-gui
```

3. Create a new virtual environment, activate it and install pyinstaller
```bash
python -m venv .venv
./.venv/Scripts/Activate
python -m pip install pyinstaller
```

3. Run the `build` task of the Makefile
```bash
make build
```

4. The built executable file will be inside `dist/ytgui`