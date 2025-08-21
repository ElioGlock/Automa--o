import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin, urlparse


class Site:
    def __init__(self,site):
        self.site = site
        self.news = {}
    def update_news(self):
        if self.site == "infomoney":
            uf_url = f"https://www.infomoney.com.br/economia/"
            browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
            page = requests.get(uf_url, headers = browsers)
            soup = BeautifulSoup(page.content,"html.parser")
            info = soup.find_all(class_="hover:underline")
            dict_info = {}
            for data in info:
                news = data.get_text(strip=True)
                news_link = data.get("href") 
                if len(news) >26:
                    dict_info[news]=news_link
                    
            # for k,v in dict_info.items():
            #     print(f"{k}:{v}\n")
            self.news = dict_info
        if self.site == "cnn_news":
            uf_url = f"https://www.cnnbrasil.com.br/nacional/brasil/"
            browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
            page = requests.get(uf_url, headers = browsers)
            soup = BeautifulSoup(page.content,"html.parser")
            
            life_h2 = soup.find_all(class_="text-gray-950 hover:underline")
            life_h3 = soup.find_all(class_="flex w-fit hover:underline")
            dict__options_life = {}
            for new in life_h2:
                dict__options_life[new.h2.text] = new.get("href")
            for new in life_h3:
                dict__options_life[new.h3.text] = new.get("href")
                
            # for k,v in dict__options_life.items():
            #     print(f"{k}:{v}\n")
                self.news = dict__options_life
        if self.site == "cnn_tech":
            uf_url = f"https://www.cnnbrasil.com.br/tecnologia/"
            browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
            page = requests.get(uf_url, headers = browsers)
            soup = BeautifulSoup(page.content,"html.parser")
            
            tech_h3 = soup.find_all(class_="text-gray-950 hover:underline")
            tech_h2 = soup.find_all(class_=" flex w-fit hover:underline")
            dict__options_tech = {}
            for i in tech_h2:
                dict__options_tech[i.h2.text] = i.get("href")
            for i in tech_h3:
                dict__options_tech[i.h3.text] = i.get("href")
            # for k,v in dict__options_tech.items():
            #     print(f"{k}:{v}\n")
            
            self.news = dict__options_tech    
        if self.site == "bbc_news":
            uf_url = f"https://www.bbc.com/news"
            browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
            page = requests.get(uf_url, headers = browsers)
            soup = BeautifulSoup(page.content,"html.parser")
            
            
            dict__options_bbc_news = {}
            
            bbc_news_h2 = soup.find_all(class_="sc-8a623a54-0 hMvGwj")
            for new_bbc in bbc_news_h2:
                h2 = new_bbc.text
                link = new_bbc.get("href")
                if len(h2) > 33:
                    new_key = h2.split(".")[0]
                    dict__options_bbc_news[new_key] =  link
                    
            # for k,v in dict__options_bbc_news.items():
            #     print(f"{k}:{v}\n")
            self.news = dict__options_bbc_news
    
                        
        if self.site == "bbc_tech":
            uf_url = f"https://www.bbc.com/innovation"
            browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
            page = requests.get(uf_url, headers = browsers)
            soup = BeautifulSoup(page.content,"html.parser")
            
            
            dict__options_bbc_tech = {}
            
            bbc_tech_h2 = soup.find_all(class_="sc-8a623a54-0 hMvGwj")
            for new_bbc in bbc_tech_h2:
                h2 = new_bbc.text
                link = new_bbc.get("href")
                if len(h2) > 33:
                    new_key = h2.split(".")[0]
                    dict__options_bbc_tech[new_key] = link
                        
            # for k,v in dict__options_bbc_tech.items():
            #     print(f"{k}:{v}\n")
            self.news = dict__options_bbc_tech
            
            
# teste = Site("bbc_tech")
# teste.update_news()
        


   

