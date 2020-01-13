.. _quickstart:

QuickStart
==========

Clone & Configure
-----------------

.. code:: bash

    git clone git@github.com:briancappello/flask-unchained-react-spa.git
    cd flask-unchained-react-spa
    cp backend/config.example.py backend/config.py            # edit if needed
    cp frontend/app/config.example.js frontend/app/config.js  # edit if needed

Running with Docker
-------------------

.. code:: bash

    docker-compose up --build


Running Locally
---------------

This assumes you're on a reasonably standard \*nix system. Windows *might* work if you know what you're doing, but you're on your own there.

.. code:: bash

    # install dependencies into a virtual environment
    mkvirtualenv -p /path/to/python3 flask-unchained-react-spa
    pip install -r requirements-dev.txt

    # run db migrations
    flask db upgrade

    # load db fixtures (optional)
    flask db import-fixtures

    # start frontend dev server:
    npm install
    npm run start

    # start backend dev server:
    flask run

    # start backend celery worker (currently only required for sending emails):
    flask celery worker
