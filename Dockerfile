FROM python:3.7-alpine
WORKDIR /usr/src/app
RUN apk add build-base
RUN apk add libffi-dev openssl-dev
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt

COPY . .
