import yfinance as yf
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta

def calculate_change_3m(ticker):
    # Obter o ticker do Yahoo Finance
    stock = yf.Ticker(ticker)
    
    # Obter os dados históricos de mercado para o período de 3 meses
    hist = stock.history(period="3mo")

    # Garantir que temos dados suficientes
    if hist.empty:
        return 0

    # Calcular a variação percentual do preço de fechamento
    start_price = hist['Close'].iloc[0]
    end_price = hist['Close'].iloc[-1]
    change_percent = ((end_price - start_price) / start_price) * 100

    return change_percent

def get_change_3m(stock_code):
    stock = adjust_b3_ticker(stock_code)
    ticker = stock + ".SA"  # Adicione ".SA" ao ticker para corresponder ao formato do yfinance
    change_3m = calculate_change_3m(ticker)
    return change_3m

def add_change_3m_to_df(df):
    """
    Adiciona a coluna 'Change3M' a um DataFrame com informações sobre ações.

    Parâmetros:
    df (pd.DataFrame): O DataFrame de entrada contendo informações sobre as ações.

    Retorna:
    pd.DataFrame: O DataFrame atualizado com a coluna 'Change3M' adicionada.
    """
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(get_change_3m, row['StockCode']): index for index, row in df.iterrows()}
        changes_3m = []

        for future in as_completed(futures):
            index = futures[future]
            try:
                change_3m = future.result()
            except Exception as e:
                change_3m = None  # Ou alguma forma de lidar com erros
                print(f"Erro ao calcular mudança de 3 meses para o índice {index}: {e}")
            changes_3m.append((index, change_3m))

    # Ordena os resultados de changes_3m de volta à ordem original do DataFrame
    changes_3m.sort(key=lambda x: x[0])
    df['Change3M'] = [change[1] for change in changes_3m]
    return df

def adjust_b3_ticker(ticker):
    import re

    # Regex to find the pattern of four letters followed by a number
    pattern = re.compile(r'^[A-Za-z]{4}\d{1}')
    
    # Search for the pattern in the provided ticker
    match = pattern.match(ticker)
    
    if match:
        # Return the matched pattern
        return match.group(0)
    else:
        # Return an error message or default value if the expected pattern is not found
        return "Invalid ticker"