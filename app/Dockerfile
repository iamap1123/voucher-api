FROM python:3.11.9-slim

EXPOSE 5000

WORKDIR /app

ADD . /app
RUN apt-get update && \
    apt-get dist-upgrade && \
    apt-get install -y pkg-config default-libmysqlclient-dev \
        build-essential libmariadb-dev && \
    pip install mysqlclient && \
    apt-get purge -y pkg-config default-libmysqlclient-dev build-essential
RUN pip install -r requirements.txt

CMD python app.py
