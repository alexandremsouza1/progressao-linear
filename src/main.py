from data_fetcher import fetch_data
from data_processor import process_data
from yahoo import add_change_3m_to_df
from model import train_model

def main():
    data = fetch_data()
    new_data = add_change_3m_to_df(data)
    X, y = process_data(new_data)
    model, accuracy, conf_matrix, class_report = train_model(X, y)
    print(f"Accuracy: {accuracy}")
    print("Confusion Matrix:")
    print(conf_matrix)
    print("Classification Report:")
    print(class_report)

    # Adiciona a probabilidade de subida ao DataFrame
    data['Probabilidade_Subida'] = model.predict_proba(X)[:, 1]

    # Ordena os dados pela maior probabilidade de subida
    data_sorted = data.sort_values(by='Probabilidade_Subida', ascending=False)

    # Salva os dados ordenados em um arquivo result.txt
    data_sorted[['StockCode', 'Probabilidade_Subida']].to_csv('result.txt', index=False)

if __name__ == "__main__":
    main()
