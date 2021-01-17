FROM python:3.8-alpine

EXPOSE 5000/tcp

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

RUN touch .env
RUN rm -rf .env
RUN rm -rf unittest

CMD [ "python", "./app.py" ]