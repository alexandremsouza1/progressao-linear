import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def train_model(X, y):
    # Dividindo os dados em conjuntos de treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    
    # Contagem das classes
    count_class_0 = (y_train == 0).sum()
    count_class_1 = (y_train == 1).sum()
    
    # Se houver desbalanceamento, resample da classe majoritária
    if count_class_0 != count_class_1:
        # Determinando a classe majoritária e minoritária
        majority_class = 0 if count_class_0 > count_class_1 else 1
        minority_class = 1 if majority_class == 0 else 0
        
        # Identificando amostras da classe majoritária
        idx_majority_class = np.where(y_train == majority_class)[0]
        
        # Resampling da classe majoritária
        idx_resampled = np.random.choice(idx_majority_class, size=count_class_1, replace=False)
        
        # Concatenando os índices das amostras balanceadas
        idx_balanced = np.concatenate((idx_resampled, np.where(y_train == minority_class)[0]))
        
        # Balanceando os dados de treinamento
        X_train_balanced, y_train_balanced = X_train.iloc[idx_balanced], y_train.iloc[idx_balanced]
    else:
        # Se não houver desbalanceamento, não é necessário fazer resampling
        X_train_balanced, y_train_balanced = X_train, y_train
    
    # Treinando o modelo de regressão logística
    model = LogisticRegression()
    model.fit(X_train_balanced, y_train_balanced)
    
    # Fazendo previsões no conjunto de teste
    y_pred = model.predict(X_test)
    
    # Calculando a acurácia do modelo
    accuracy = accuracy_score(y_test, y_pred)
    
    # Calculando a matriz de confusão
    conf_matrix = confusion_matrix(y_test, y_pred)
    
    # Calculando o relatório de classificação
    class_report = classification_report(y_test, y_pred)
    
    return model, accuracy, conf_matrix, class_report

# Chame a função train_model(X, y) passando seus dados X e y
