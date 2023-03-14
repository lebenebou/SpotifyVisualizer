
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

import json
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
sign_in_img_id = None
main_img_id = None

# images ====================================
shadow_img = ImageTk.PhotoImage(Image.open("./pictures/shadow.png"))
sign_in_img = ImageTk.PhotoImage(Image.open("./pictures/sign_in.png"))
sign_in_img_hovered = ImageTk.PhotoImage(Image.open("./pictures/sign_in_hovered.png"))

# functions =================================
def sync_up() -> None:

    sign_in_canvas.destroy()

def sign_in_action(event) -> None:

    fetch_playback_info()
    sign_in_canvas.delete("all")
    sign_in_canvas.destroy()
    sync_up()

def sign_in_hover(event) -> None:

    sign_in_canvas.itemconfig(sign_in_img_id, image=sign_in_img_hovered)

def sign_in_leave_hover(event) -> None:

    sign_in_canvas.itemconfig(sign_in_img_id, image=sign_in_img)

# frames - widgets - buttons ================
main_canvas = Canvas(root, bg="purple", highlightthickness=0, width=50, height=50)
main_canvas.place(x=0, y=0, relwidth=1, relheight=1)

main_canvas.create_image(root.winfo_width()/2, root.winfo_height()/2, image=shadow_img)
sign_in_canvas = Canvas(root, bg="yellow", highlightthickness=0, width=240, height=70)


if not os.path.exists("./.cache"):

    sign_in_canvas.place(relx=0.5, rely=0.7, anchor=CENTER)
    sign_in_img_id = sign_in_canvas.create_image(240//2, 70//2, image=sign_in_img)

# Bindings ==================================
sign_in_canvas.bind("<Enter>", sign_in_hover) # hover on
sign_in_canvas.bind("<Leave>", sign_in_leave_hover) # hover off
sign_in_canvas.bind("<Button-1>", sign_in_action) # click
    
# ===========================================
if __name__=="__main__": root.mainloop()