#start docker with python3.11
FROM python:3.11-slim

# setup linux python

ENV PYTHONUNBEFFERED = 1

# update linux kernel

RUN apt-get update && apt-get -y install gcc libpq-dev

# create Work Directory

WORKDIR /app

# copy requirements.txt file

COPY requirements.txt /app/requirements.txt

# install required packages

RUN pip install -r requirements.txt

# copy folder project

COPY . /app/






