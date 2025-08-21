from script import *
import tkinter as tk
from tkinter import ttk
import os
from threading import Thread
import time
import datetime
import sys
import pickle
import webbrowser
from math import ceil
from pytimedinput import timedInput

class News_get:
    def __init__(self):
        self.dict_site = {}
        self.all_sites = ["cnn_news","cnn_tech","infomoney","bbc_news","bbc_tech"]
        
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
        elementos_vistos = set()
        while not self.kill:
            print("update")
            for site in self.all_sites:
                self.dict_site[site].update_news()
                for key,value in self.dict_site[site].news.items():
                    dict_aux ={}
                    dict_aux["data"] = datetime.datetime.now()
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
            
            self.filtered_news = [i for i in self.news if i["fonte"] == "cnn_news"]
            self.filter_more_news = [i["materia"] for i in self.filtered_news]
            
            for elemento in self.filter_more_news:
                if elemento not in elementos_vistos:
                    elementos_vistos.add(elemento)
                    print(elemento)
                       
            
            time.sleep(15)
            

        
        
        
class App_news(tk.Tk,News_get):
    def __init__(self):
        super().__init__()
        self.title("NEWS")
        self.geometry("500x400")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, "images", "icon.png")
        icon = tk.PhotoImage(file=icon_path)
        self.iconphoto(True,icon)
        style = ttk.Style()
        style.configure("My.TButton",
                background="#364153", 
                font=("Helvetica", 12, "bold"))
        style.map("My.TButton",
          background=[("active", "#149ACF")])
       

        # Cria um container principal para os frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (PaginaInicial, bbc_news):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # Posiciona todos os frames no mesmo lugar (empilhados)
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_frame("PaginaInicial")

    def mostrar_frame(self, page_name):
        '''Traz o frame para a frente'''
        frame = self.frames[page_name]
        frame.tkraise()

# --- Classes para cada "página" ---

class PaginaInicial(tk.Frame,tk.Tk):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(background="#364153")
        label_title = ttk.Label(
                        self,
                        text="Today's News",
                        anchor="center",
                        font=("Helvetica",18,"bold"),
                        foreground="white",
                        background="#364153")
        label_title.pack(pady=10, padx=10)
        
        site_list = ["BBC_NEWS", "BBC_TECH", "INFOMONEY", "CNN_NEWS", "CNN_TECH"]
        link_button_site_list = ["bbc_news", "bbc_tech", "infomoney", "cnn_news", "cnn_tech"]


        for site, link in zip(site_list, link_button_site_list):
            button = ttk.Button(self, text=f"{site}",
                                command=lambda l=link: controller.mostrar_frame(l),
                                style="My.TButton"
            )
            button.pack(pady=10, side="top")
        
       
class bbc_news(tk.Frame,tk.Tk,News_get):
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        
        self.time_label = ttk.Label(self, text="",
                        anchor="center",
                        font=("Helvetica",14,"bold"),
                        foreground="white",
                        background="#364153")
        self.time_label.pack(pady=10, padx=10)
        self.update_time()
        
        self.config(background="#364153")
        self.controller = controller
        label = ttk.Label(self, text=f"")
        label.pack(pady=10, padx=10)

        botao = ttk.Button(self, text="Voltar para a Página Inicial",
                           command=lambda: controller.mostrar_frame("PaginaInicial"),
                            style="My.TButton")
        botao.pack()
    def update_time(self):
        # Obtém o tempo atual
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Atualiza o texto do Label
        self.time_label.config(text=f"Último update: {time}")
        
        self.after(15000, self.update_time) 
        
    def display_news(self):
        self.news_class = News_get()
        self.news_class.update_news()
        self.filtered_news = [i for i in self.news_class.news if i["fonte"] in self.news_class.sites]
        
        label = ttk.Label(self, text=f"{self.filtered_news}")
        label.pack(pady=10, padx=10)
        



# --- Executa a aplicação ---
if __name__ == "__main__":
    news =News_get()
    app = App_news()
    
    
    app.mainloop()
    news.filter_news()
    
    
    
    



