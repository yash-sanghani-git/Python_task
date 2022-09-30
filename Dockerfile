FROM python:3.9.3-slim
ENV PYTHONUNBUFFERED=1
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2 \
    && apt-get -y install default-libmysqlclient-dev \
    && apt-get install -y libgdal-dev g++ --no-install-recommends

RUN mkdir -p /task
ENV HOME=/task
WORKDIR $HOME
COPY ./task $HOME


RUN pip install --upgrade pip

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache -r /requirements.txt