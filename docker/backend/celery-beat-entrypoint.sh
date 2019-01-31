#!/bin/sh

test -e celerybeat.pid && rm celerybeat.pid
test -e celerybeat-schedule && rm celerybeat-schedule

celery beat -A celery_app.celery -l info
