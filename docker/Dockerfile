FROM ubuntu:latest

RUN apt update && apt install -y python3 python3-pip sqlite3
RUN pip3 install flask

COPY ./src /app
COPY ./setup.sh /setup

WORKDIR /app
CMD flask run --host 0.0.0.0 -p 5000