FROM node:13.8-alpine3.11

RUN apk add --no-cache git

COPY ./package.json /flask/package.json

WORKDIR /flask

RUN npm install

COPY ./frontend /flask/frontend

COPY ./docker/frontend/frontend-entrypoint.sh /frontend-entrypoint.sh
