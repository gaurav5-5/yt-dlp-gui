yt-dlp-gui
----------

A simple frontend for [yt-dlp](https://www.github.com/yt-dlp/yt-dlp) made in python+tkinter

Building
--------

To build the executable file, 

1. clone the repository
```bash
git clone https://www.github.com/gaurav5-5/yt-dlp-gui
```

2. `cd` to cloned repository

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