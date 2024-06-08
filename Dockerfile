# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie o conteúdo do seu diretório atual para o diretório de trabalho no contêiner
COPY . .

# Comando para rodar a aplicação
CMD ["python", "src/main.py"]
