FROM docker.io/python:3.8-buster
LABEL maintainer="Andrew Simonson <asimonson1125@gmail.com>"

WORKDIR /app
ADD ./server /app
COPY ./requirements.txt requirements.txt
RUN apt-get -yq update && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/src

CMD [ "gunicorn", "app:app" ]