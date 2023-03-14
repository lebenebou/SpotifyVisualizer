
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

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
# variables =================================


# functions =================================


# frames - widgets - buttons ================
main_canvas = Canvas(root, bg="purple", highlightthickness=0, width=50, height=50)
main_canvas.place(x=0, y=0, relwidth=1, relheight=1)
shadow_img = ImageTk.PhotoImage(Image.open("./pictures/shadow.png"))
main_canvas.create_image(root.winfo_width()/2, root.winfo_height()/2, image=shadow_img)

sign_in_button = ttk.Button(text="Sign In with Spotify")
sign_in_button.place(x=root.winfo_width()/2, y=root.winfo_height()/2, anchor=CENTER)
# ===========================================
if __name__=="__main__":
    root.mainloop()