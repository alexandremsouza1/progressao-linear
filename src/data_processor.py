import pandas as pd
import numpy as np

def process_data(df):
    # Calcular a mediana de ChangeDay
    median_change = df['ChangeDay'].median()

    # Criar a coluna 'Up' com base se 'ChangeDay' é maior que a mediana
    df['Up'] = np.where(df['ChangeDay'] > median_change, 1, 0)

    features = ['ChangeDay', 'Change12M', 'Volume']
    X = df[features]
    y = df['Up']
    return X, y
