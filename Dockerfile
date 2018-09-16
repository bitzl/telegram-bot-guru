FROM python:3.7-alpine

WORKDIR /app
COPY . /app

RUN pip install pipenv
 && pipenv install

ENTRYPOINT pipenv run python guru.py
