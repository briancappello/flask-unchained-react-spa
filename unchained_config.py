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
