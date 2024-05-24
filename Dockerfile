
FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y netcat-openbsd \
    && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
