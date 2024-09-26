FROM python:3.12-slim

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app/

RUN python manage.py makemigrations


EXPOSE 8000
