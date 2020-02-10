FROM python:3.6-alpine3.8

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache shadow
RUN useradd --user-group --create-home --home-dir /flask --shell /bin/false flask

RUN apk add --no-cache linux-headers make gcc musl-dev libxml2-dev libxslt-dev libffi-dev postgresql postgresql-dev git

WORKDIR /flask/src

COPY ./requirements.txt requirements.txt
COPY ./requirements-dev.txt requirements-dev.txt

RUN pip install --no-cache-dir -U pip
RUN pip install --no-cache-dir -r requirements-dev.txt

USER flask

RUN mkdir -p /flask/.cache /flask/.local/share

COPY ./docker/backend/docs-entrypoint.sh /
COPY ./docker/backend/celery-beat-entrypoint.sh /
COPY ./docker/backend/celery-worker-entrypoint.sh /
COPY ./docker/backend/flask-entrypoint.sh /flask-entrypoint.sh
COPY ./docker/backend/test-entrypoint.sh /test-entrypoint.sh
