FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \ 
    build-essential \
    gcc \
    python3-dev \
    wget \
    unzip \
    chromium \
    chromium-driver \
    && apt-get clean

COPY . /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=8443

CMD ["python", "bot_fetch_gic.py"]
