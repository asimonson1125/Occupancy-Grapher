FROM docker.io/python:3.8-buster
LABEL maintainer="Andrew Simonson <asimonson1125@gmail.com>"

WORKDIR /app
ADD ./collector /app
WORKDIR /app/collector
COPY ./requirements.txt requirements.txt
RUN apt-get -yq update && \
    pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "scheduler.py" ]