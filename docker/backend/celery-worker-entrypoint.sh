#!/bin/sh

celery worker -A celery_app.celery -l info
