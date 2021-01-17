FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir unittest

COPY unittest unittest 
COPY library unittest/library

RUN touch .env
RUN rm -rf .env

CMD [ "pytest", "unittest" ]
