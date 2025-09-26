FROM python:3.10-slim

WORKDIR /app

# Cài dependencies hệ thống
RUN apt-get update && \
    apt-get install -y build-essential gcc python3-dev && \
    apt-get clean

# Copy code
COPY . /app

# Cài Python packages
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Env mặc định (Render sẽ override)
ENV PORT=8443

CMD ["python", "bot_fetch_gic.py"]
