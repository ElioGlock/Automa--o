import tkinter as tk

import os
# path
script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, "images", "icon.png")

window = tk.Tk()
window.title("News")
window.geometry("500x400")
icon = tk.PhotoImage(file=icon_path)
window.iconphoto(True,icon)
window.config(background="#364153")

title = tk.Label(
    window,
    text="Today's News",
    anchor="center",
    font=("Leoscar",18),
    foreground="white",
    background="#364153",

    )
    
title.pack(ipady=10)



window.mainloop()