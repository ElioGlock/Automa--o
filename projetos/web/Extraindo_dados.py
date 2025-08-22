import requests
from bs4 import BeautifulSoup
import pandas as pd


def scrapping_uf(uf:str):
    uf_url = f"https://www.ibge.gov.br/cidades-e-estados/{uf}.html"
    browsers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
    page = requests.get(uf_url, headers = browsers)
    soup = BeautifulSoup(page.content,"html.parser")
    indicators = soup.select(".indicador")
    uf_dict = {
        dado.select(".ind-label")[0].text: dado.select(".ind-value")[0].text
        for dado in indicators
    }
    return uf_dict
state = scrapping_uf("sp")

for indicator in state:
    if ']' in state[indicator]:
        state[indicator] = state[indicator].split(']')[0][:-8]
    else: 
        state[indicator] =  state[indicator]
    # print(indicator,state[indicator])
    
data_frame= pd.DataFrame(state.values(),index = state.keys())
print(data_frame)