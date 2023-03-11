FROM python:3.10.9-alpine3.17
LABEL maintainer="Mateusz Furman <furman.mateusz.outlook.com>"

ENV PYTHONNUMBUFFERED 1

COPY requirements.txt /requirements.txt
COPY ./app /app

WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home app

ENV PATH="/py/bin:$PATH"

USER app
