FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    libssl-dev \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py tailwind install

COPY . /app/