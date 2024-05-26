import requests
import pandas as pd

def fetch_data():
    url = "https://api.infomoney.com.br/ativos/top-alta-baixa-por-ativo/acao?sector=Todos&orderAtributte=Low&pageIndex=1&pageSize=1000&search="
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data['Data'])
    return df