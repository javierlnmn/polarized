FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    libssl-dev \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/

COPY ./theme/static_src/package.json ./theme/static_src/package-lock.json /data/
WORKDIR /data/
RUN npm install
ENV PATH /data/node_modules/.bin:$PATH

COPY . /data/app/
WORKDIR /data/app/

RUN pip install --no-cache-dir -r requirements.txt
