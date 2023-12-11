import os

import tkinter as tk
import tkinter.ttk as ttk
from typing import List

# +-------------------+
# | +------------+    |
# | | v filetype |    |
# | +------------+    |
# |                   |
# | Link              |
# | +---------------+ |
# | | url           | |
# | +---------------+ |
# |                   |
# |    +--------+     |
# |    | submit |     |
# |    +--------+     |
# +-------------------+

class Ytgui:

    _window: tk.Tk

    _aftypes: List[str] = ["--AUDIO--","aac","alac","flac","m4a","mp3","opus","wav"]
    _vftypes: List[str] = ["--VIDEO--","3gp","flv","mp4","ogg","webm"]

    _ft_var: tk.StringVar
    _lnk_var: tk.StringVar
    _vft_var: tk.StringVar
    _kvid_var: tk.BooleanVar

    _msg_label: ttk.Label

    def __init__(self) -> None:
        self._window = tk.Tk()
        self._window.title("yt-dlp frontend")

        self._ft_var = tk.StringVar(self._window)
        self._lnk_var = tk.StringVar(self._window)
        self._vft_var = tk.StringVar(self._window)
        self._kvid_var = tk.BooleanVar(self._window)

        self._ft_var.set("mp3")
        self._lnk_var.set("")
        self._kvid_var.set(tk.FALSE)
        self._vft_var.set("")

        self._msg_label = ttk.Label(
            self._window,
            text="",
            font=("Arial",10)
        )

    def call_dl(self):
        cmd = "yt-dlp --quiet "
        cmd+= f"--extract-audio --audio-format {self._ft_var.get()} "
        cmd+= f"{"--keep-video" if self._kvid_var.get() else "--no-keep-video"} "
        cmd+= f"{"--format "+self._vft_var.get()+" " if self._kvid_var.get() else ""}"
        cmd+= f"{self._lnk_var.get()}"

        msg:str = os.popen(cmd).read()

        if "error" in msg.lower():
            self._msg_label.configure(text=msg, foreground="red")
        else: 
            self._msg_label.configure(text="Download Successful!!", foreground="green")

    def display(self):

        ft_label = ttk.Label(
            self._window,
            text="File Type",
            font=("Arial", 11)
        )
        ft_label.grid(row=0,column=0,padx=5,pady=5,sticky="w")

        ft_ddown = ttk.OptionMenu(
            self._window,
            self._ft_var,
            *self._aftypes
        )
        ft_ddown.grid(row=0,column=1,padx=5,pady=5,sticky="w")

        vft_ddown = ttk.OptionMenu(
            self._window,
            self._vft_var,
            *self._vftypes,
        )
        vft_ddown.configure(state="disabled")
        vft_ddown.grid(row=0,column=2,padx=5,pady=5,sticky="w")

        kvid_chk = ttk.Checkbutton(
            self._window,
            text="Keep Video?",
            command=lambda: vft_ddown.configure(state="normal" if self._kvid_var.get() else "disabled"),
            variable=self._kvid_var
        )
        kvid_chk.grid(row=0,column=3,padx=5,pady=5,columnspan=1,sticky="ew")

        lnk_label = ttk.Label(
            self._window,
            text="URL",
            font=("Arial",11)
        )
        lnk_label.grid(row=1,column=0,padx=5,pady=5,sticky="w")

        lnk_entry = ttk.Entry(
            self._window,
            width=40,
            textvariable=self._lnk_var,
            font=("Arial", 11)
        )
        lnk_entry.grid(row=1,column=1,columnspan=3,padx=5,pady=5,sticky="w")

        submit_btn = ttk.Button(
            self._window,
            text="Download",
            command=self.call_dl
        )
        submit_btn.grid(row=2,column=1,columnspan=2,rowspan=2,padx=5,pady=5,sticky="w")

        self._msg_label.grid(row=3,column=0,columnspan=4,padx=5,pady=5,sticky="w")

        self._window.mainloop()

if __name__ == "__main__":
    ytg = Ytgui()
    ytg.display()
