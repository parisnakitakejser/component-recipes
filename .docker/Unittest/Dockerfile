FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir tests
RUN mkdir tests/project

COPY tests tests
COPY project tests/project

RUN touch .env
RUN rm -rf .env

CMD [ "pytest" ]
