FROM python:3.11-slim

WORKDIR /app

# 先に依存関係だけコピー → キャッシュが効いて速い
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリ本体をコピー
COPY app ./app

# コンテナ起動時にAPIを立ち上げる
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]