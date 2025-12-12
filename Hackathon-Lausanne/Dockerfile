# Base image Python
FROM python:3.12-slim

# Imposta cartella lavoro
WORKDIR /app

# Copia tutti i file locali
COPY . /app

# Installa librerie
RUN pip install --no-cache-dir streamlit PyPDF2 faiss-cpu sentence-transformers openai beautifulsoup4

# Espone la porta di Streamlit
EXPOSE 8501

# Comando per avviare Streamlit
CMD ["streamlit", "run", "streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]
