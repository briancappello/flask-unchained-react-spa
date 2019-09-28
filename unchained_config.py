import os


ROOT_PATH = os.path.abspath(os.path.dirname(__file__))


def folder_or_none(folder_name):
    folder = os.path.join(ROOT_PATH, folder_name)
    return folder if os.path.exists(folder) else None


# kwargs to pass to the FlaskUnchained constructor
TEMPLATE_FOLDER = folder_or_none('templates')
STATIC_FOLDER = folder_or_none('static')
STATIC_URL_PATH = '/static' if STATIC_FOLDER else None

BUNDLES = [
    'flask_unchained.bundles.admin',
    'flask_unchained.bundles.api',
    'flask_unchained.bundles.mail',
    'flask_unchained.bundles.celery',  # must be after mail bundle to send async email
    'flask_unchained.bundles.session',
    'flask_unchained.bundles.sqlalchemy',
    'py_yaml_fixtures',

    'bundles.blog',
    'bundles.security',
    'backend',  # app bundle must be last
]
