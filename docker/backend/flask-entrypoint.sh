#!/bin/sh

test -e backend/config.py || (
   echo "WARNING: config.py not found, using default" &&\
   cp backend/config.example.py backend/config.py
)

until flask db upgrade
do
    echo "Waiting for postgres ready..."
    sleep 2
    flask db init
    flask db migrate -m 'create initial tables'
done

flask db import-fixtures
flask blog import-articles --reset
flask run --host 0.0.0.0 --port 5000
