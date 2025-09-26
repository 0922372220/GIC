FROM python:3.10-slim

# Cài các gói cần thiết
RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    unzip \
    curl \
    chromium \
    chromium-driver \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Đặt biến môi trường cho Selenium + Chromium
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER=/usr/bin/chromedriver
ENV PATH="$CHROMEDRIVER:$PATH"

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Render sẽ inject PORT
ENV PORT=8443

CMD ["python", "bot_fetch_gic.py"]
