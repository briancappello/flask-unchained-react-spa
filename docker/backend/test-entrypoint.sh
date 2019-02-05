#!/bin/sh

psql -c "DROP DATABASE IF EXISTS flask_test;" -h postgres -U postgres
psql -c "CREATE DATABASE flask_test;" -h postgres -U postgres
psql -c "CREATE USER flask_test WITH PASSWORD 'flask_test';" -h postgres -U postgres
psql -c "GRANT ALL PRIVILEGES ON DATABASE flask_test TO flask_test;" -h postgres -U postgres

tox -c tox.docker.ini
