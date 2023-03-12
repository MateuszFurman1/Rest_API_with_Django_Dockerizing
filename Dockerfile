FROM python:3.10-slim-buster
LABEL maintainer="Mateusz Furman <furman.mateusz.outlook.com>"
ENV PYTHONUNBUFFERED=1
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
