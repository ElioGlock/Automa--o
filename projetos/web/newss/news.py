from script import *
import tkinter as tk
import os
from threading import Thread
import time
from datetime import datetime
import sys
import pickle
import webbrowser
from math import ceil
from pytimedinput import timedInput

class App_News:
    def __init__(self):
        self.dict_site = {}
        self.all_sites = ["cnn","infomoney","bbc"]
        self.screen = 0
        
        self.news = self._read_file("news") if "news" in os.listdir() else []
        self._update_file(self.news,"news")
        self.sites = self._read_file("sites") if "sites" in os.listdir() else []
        
    def _update_file(self,lista,mode= "news"): #cria um arquivo pra salvar a lista
        with open(mode, "wb") as fp:
            pickle.dump(lista,fp)   
        
    def _read_file(self,mode= "news"):  # lê o arquivo criado acima e serve para armazenar dados
        with open(mode, "wb") as fp:
            n_list = pickle.load(fp)
            return n_list
    

self = App_News()


# path
# script_dir = os.path.dirname(os.path.abspath(__file__))
# icon_path = os.path.join(script_dir, "images", "icon.png")

# window = tk.Tk()
# window.title("News")
# window.geometry("500x400")
# icon = tk.PhotoImage(file=icon_path)
# window.iconphoto(True,icon)
# window.config(background="#364153")

# title = tk.Label(
#     window,
#     text="Today's News",
#     anchor="center",
#     font=("Leoscar",18),
#     foreground="white",
#     background="#364153",

#     )
    
# title.pack(ipady=10)



# window.mainloop()