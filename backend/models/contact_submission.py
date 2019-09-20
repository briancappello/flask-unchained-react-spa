from flask_unchained.bundles.sqlalchemy import db


class ContactSubmission(db.Model):
    name = db.Column(db.String(64), info=dict(required=True))
    email = db.Column(db.String(64), info=dict(required=True))
    message = db.Column(db.Text, info=dict(required=True))
