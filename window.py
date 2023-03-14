
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter

import pyautogui
pyautogui.PAUSE = 0.05

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
root.attributes("-fullscreen", False)

# variables ==================================
sign_in_img_id = None
main_img_id = None
bg_img_id = None
shadow_img_id = None
album_name = "" # download new artowrk when this var changes

# images ====================================
shadow_img = ImageTk.PhotoImage(Image.open("./pictures/shadow.png"))
sign_in_img = ImageTk.PhotoImage(Image.open("./pictures/sign_in.png"))
sign_in_img_hovered = ImageTk.PhotoImage(Image.open("./pictures/sign_in_hovered.png"))
main_img = None
bg_img = None

# functions =================================
def sync_up() -> None:

    global album_name    
    if album_name=="": # first run
        
        sign_in_canvas.destroy()
        place_main_img("./pictures/loading.png")
    
    fetch_playback_info()

    playback_info = None
    with open("./playback_data.json", "r") as f: playback_info = json.load(f)

    if len(playback_info)==1:

        album_name = ""
        img_path = "./pictures/{}.png".format(playback_info["message"])
        place_main_img(img_path)
        return

    # if track is an ad...
    
    # Normal playback state, successfully got playback info
    current_album = playback_info["item"]["album"]["name"]

    if current_album != album_name:

        album_name = current_album
        artwork_url = playback_info["item"]["album"]["images"][0]["url"]
        download_artwork(artwork_url)
        place_main_img("./pictures/artwork.png")
    
def fetch_loop():

    sync_up()
    root.after(2000, fetch_loop)

def place_main_img(img_path: str) -> None:

    global main_img, main_img_id
    global bg_img, bg_img_id
    global shadow_img, shadow_img_id

    main_img = Image.open(img_path)

    bg_img = main_img.resize((root.winfo_width(), root.winfo_width()), resample=0)
    bg_img = bg_img.filter(ImageFilter.GaussianBlur(20))

    bg_img = ImageTk.PhotoImage(bg_img)
    main_img = ImageTk.PhotoImage(main_img)

    main_canvas.delete(main_img_id)
    main_canvas.delete(bg_img_id)
    main_canvas.delete(shadow_img_id)

    bg_img_id = main_canvas.create_image(root.winfo_width()//2, root.winfo_height()//1.5, image=bg_img)
    main_img_id = main_canvas.create_image(root.winfo_width()//2, root.winfo_height()//2, image=main_img)
    shadow_img_id = main_canvas.create_image(root.winfo_width()//2, root.winfo_height()//2, image=shadow_img)

    main_canvas.lift(shadow_img_id) # bring to top
    main_canvas.lift(main_img_id) # bring to top

def download_artwork(img_url: str) -> None:

    print("Downloading new album artwork...", end="\r")

    with open("./pictures/artwork.png", "wb") as f:
        f.write(requests.get(img_url).content)

    print(" "*50, end="\r")
    print("Download done.")

def sign_in_action(event) -> None:

    fetch_playback_info()
    sign_in_canvas.delete("all")
    sign_in_canvas.destroy()
    fetch_loop()

def sign_in_hover(event) -> None:

    sign_in_canvas.itemconfig(sign_in_img_id, image=sign_in_img_hovered)

def sign_in_leave_hover(event) -> None:

    sign_in_canvas.itemconfig(sign_in_img_id, image=sign_in_img)

def toggle_fullscreen(event) -> None:

    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

    if root.attributes("-fullscreen"): root.config(cursor="none")
    else: root.config(cursor="arrow")

def quit() -> None:

    if os.path.exists("./pictures/artwork.png"): os.remove("./pictures/artwork.png")

    root.destroy()

def escape(event) -> None:

    if root.attributes("-fullscreen"):
        toggle_fullscreen(event)
        return
    
    quit()

def space(event) -> None:

    pyautogui.press("playpause")

def right_arrow(event) -> None:

    pyautogui.press("nexttrack")

def left_arrow(event) -> None:

    pyautogui.press("prevtrack")

def up_arrow(event) -> None:

    for _ in range(5): pyautogui.press("volumeup")

def down_arrow(event) -> None:

    for _ in range(5): pyautogui.press("volumedown")

# frames - widgets - buttons ================
main_canvas = Canvas(root, bg="purple", highlightthickness=0, width=50, height=50)
main_canvas.place(x=0, y=0, relwidth=1, relheight=1)

shadow_img_id = main_canvas.create_image(root.winfo_width()//2, root.winfo_height()//2, image=shadow_img)

sign_in_canvas = Canvas(root, bg="yellow", highlightthickness=0, width=240, height=70)

if not os.path.exists("./.cache"): # user's first time opening the app

    sign_in_canvas.place(relx=0.5, rely=0.7, anchor=CENTER)
    place_main_img("./pictures/first_run.png")
    sign_in_img_id = sign_in_canvas.create_image(sign_in_img.width()//2, sign_in_img.height()//2, image=sign_in_img)

    # Bindings ==================================
    sign_in_canvas.bind("<Enter>", sign_in_hover) # hover on
    sign_in_canvas.bind("<Leave>", sign_in_leave_hover) # hover off
    sign_in_canvas.bind("<Button-1>", sign_in_action) # click

else: # not the user's first run
    place_main_img("./pictures/loading.png")
    fetch_loop()

root.bind("<f>", toggle_fullscreen)
root.bind("<Escape>", escape)
root.bind("<space>", space)
root.bind("<Right>", right_arrow)
root.bind("<Left>", left_arrow)
root.bind("<Up>", up_arrow)
root.bind("<Down>", down_arrow)
root.bind("<Double-Button-1>", toggle_fullscreen)
# ===========================================
# if __name__=="__main__": root.mainloop()