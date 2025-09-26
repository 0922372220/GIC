FROM python:3.10-bullseye

RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    build-essential \
    wget \
    curl \
    unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=8443

CMD ["python", "bot_fetch_gic.py"]
