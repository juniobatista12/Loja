FROM python:3.11.4-slim-bullseye

WORKDIR /src

RUN apt update \
    && apt install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

ADD ./backend /src/

RUN pip install -r requirements.txt


CMD uvicorn app.main:app --host 0.0.0.0 --port 8000
