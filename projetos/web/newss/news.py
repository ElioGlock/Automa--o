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
        self.all_sites = ["cnn_news","cnn_tech","infomoney","bbc_news","bbc_tech"]

        self.screen = 0
        self.kill = False
        
        self.news = self._read_file("news") if "news" in os.listdir() else []
        self._update_file(self.news,"news")
        self.sites = self._read_file("sites") if "sites" in os.listdir() else []
        self._update_file(self.sites,"sites")
        
        for site in self.all_sites:
            self.dict_site[site] = Site(site)
        
        self.news_thread = Thread(target=self.update_news, daemon=True)
        self.news_thread.start()
        
    def _update_file(self,lista,mode= "news"): #cria um arquivo pra salvar a lista
        with open(mode, "wb") as fp:
            pickle.dump(lista,fp)   
        
    def _read_file(self,mode= "news"):  # lê o arquivo criado acima e serve para armazenar dados
        with open(mode, "rb") as fp:
            n_list = pickle.load(fp)
            return n_list
    def update_news(self):
        
        while not self.kill:
            print("update")
            for site in self.all_sites:
                self.dict_site[site].update_news()
                for key,value in self.dict_site[site].news.items():
                    dict_aux ={}
                    dict_aux["data"] = datetime.now()
                    dict_aux["fonte"] = site
                    dict_aux["materia"] = key
                    dict_aux["link"] = value
                    if len(self.news) == 0:
                        self.news.insert(0,dict_aux)
                        continue
                    add_news = True
                    for news in self.news:
                        if dict_aux["materia"] == news["materia"] and dict_aux["fonte"] == news["fonte"]:
                            add_news = False
                            break
                    if add_news:
                         self.news.insert(0,dict_aux)
            self.news = sorted(self.news, key =lambda d:d["data"], reverse= True)
            self._update_file(self.news,"news")
           
            time.sleep(5)       
    
    def windows(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, "images", "icon.png")

        self.window = tk.Tk()
        self.window.title("News")
        self.window.geometry("500x400")
        icon = tk.PhotoImage(file=icon_path)
        self.window.iconphoto(True,icon)
        self.window.config(background="#364153")
        while True:
            os.system("cls")
            match self.screen:
                    case 0:
                        title = tk.Label(
                        self.window,
                        text="Today's News",
                        anchor="center",
                        font=("Helvetica",18),
                        foreground="white",
                        background="#364153")
                        title.pack(ipady=10)
                        
                        button_bbc_news = tk.Button(
                            self.window,text="bbc_news",
                            )
                        button_bbc_news.pack()
                    case 1:
                        title = tk.Label(
                        self.window,
                        text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        anchor="center",
                        font=("Helvetica",18),
                        foreground="white",
                        background="#364153")
                        title.pack(ipady=10)
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
            
            self.window.mainloop() 
        
            
                    
                
            
self = App_News()
self.windows()
# self.update_news()








