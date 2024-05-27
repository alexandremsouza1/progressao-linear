import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_data():
    # Obtém a URL do arquivo .env
    url = os.getenv("URL")
    
    # Verifica se a URL foi definida no arquivo .env
    if url is None:
        raise ValueError("URL não definida no arquivo .env")
    
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data['Data'])
    return df
