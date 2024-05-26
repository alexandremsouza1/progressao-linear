from data_fetcher import fetch_data
from data_processor import process_data
from model import train_model

def main():
    data = fetch_data()
    X, y = process_data(data)
    model, accuracy, conf_matrix, class_report = train_model(X, y)
    print(f"Accuracy: {accuracy}")
    print("Confusion Matrix:")
    print(conf_matrix)
    print("Classification Report:")
    print(class_report)

    data['Probabilidade_Subida'] = model.predict_proba(X)[:, 1]
    print(data[['StockCode', 'Probabilidade_Subida']])

if __name__ == "__main__":
    main()
