
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

import json
import requests
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
album_name = "" # download new artowrk when this var changes

# images ====================================
shadow_img = ImageTk.PhotoImage(Image.open("./pictures/shadow.png"))
sign_in_img = ImageTk.PhotoImage(Image.open("./pictures/sign_in.png"))
sign_in_img_hovered = ImageTk.PhotoImage(Image.open("./pictures/sign_in_hovered.png"))
main_img = None
bg_img = None

# functions =================================
def sync_up() -> None:

    if album_name=="": # first run
        
        sign_in_canvas.destroy()
        place_main_img("./pictures/loading.png")
    
    fetch_playback_info()

    root.after(2000, sync_up)

def place_main_img(img_path: str) -> None:

    global main_img, main_img_id

    main_img = ImageTk.PhotoImage(Image.open(img_path))
    main_img_id = main_canvas.create_image(root.winfo_width()/2, root.winfo_height()/2, image=main_img)

def download_artwork(img_url: str) -> None:

    print("Downloading album artwork...", end="\r")

    with open("./pictures/artwork.png", "wb") as f:
        f.write(requests.get(img_url).content)

    print("Download done.")

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

if not os.path.exists("./.cache"): # user's first time opening the app

    sign_in_canvas.place(relx=0.5, rely=0.7, anchor=CENTER)
    place_main_img("./pictures/first_run.png")
    sign_in_img_id = sign_in_canvas.create_image(sign_in_img.width()//2, sign_in_img.height()//2, image=sign_in_img)

    # Bindings ==================================
    sign_in_canvas.bind("<Enter>", sign_in_hover) # hover on
    sign_in_canvas.bind("<Leave>", sign_in_leave_hover) # hover off
    sign_in_canvas.bind("<Button-1>", sign_in_action) # click

else:
    sync_up()
    
# ===========================================
if __name__=="__main__": root.mainloop()