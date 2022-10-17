FROM python:3.9

WORKDIR /app

COPY requirements /app/requirements

RUN pip install -r requirements.txt
COPY . /app

RUN start.sh