
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import os
current_dir = os.path.dirname(__file__)
os.chdir(current_dir)

from fetcher import fetch_playback_info

# main window initiation ====================
root = Tk()
root.title("Spotify Visualizer")
root.iconbitmap("./app_icon.ico")

root.state("zoomed")
root.resizable(True, True)
root.configure(bg="red")
# variables =================================


# functions =================================


# frames - widgets - buttons ================
main_canvas = Canvas(root, bg="purple", highlightthickness=0, width=50, height=50)
main_canvas.place(x=0, y=0, relwidth=1, relheight=1)


# ===========================================
if __name__=="__main__":
    root.mainloop()