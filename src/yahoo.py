import yfinance as yf

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

def add_change_3m_to_df(df):
    """
    Adiciona a coluna 'Change3M' a um DataFrame com informações sobre ações.

    Parâmetros:
    df (pd.DataFrame): O DataFrame de entrada contendo informações sobre as ações.

    Retorna:
    pd.DataFrame: O DataFrame atualizado com a coluna 'Change3M' adicionada.
    """
    changes_3m = []

    for index, row in df.iterrows():
        stock = adjust_b3_ticker(row['StockCode'])
        ticker = stock + ".SA"  # Adicione ".SA" ao ticker para corresponder ao formato do yfinance
        change_3m = calculate_change_3m(ticker)
        changes_3m.append(change_3m)
    
    df['Change3M'] = changes_3m
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