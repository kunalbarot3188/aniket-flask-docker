FROM python:3.8-slim

WORKDIR /app

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && pip install mysqlclient \
    && pip install Flask

COPY . /app

EXPOSE 5000

CMD ["python","Vaseapp.py" ]
