"""Flask Unchained React SPA"""

from flask_wtf.csrf import generate_csrf
from flask_unchained import AppBundle, FlaskUnchained, session


class BackendBundle(AppBundle):
    def before_init_app(self, app: FlaskUnchained):
        app.url_map.strict_slashes = False

    def after_init_app(self, app: FlaskUnchained):
        app.jinja_env.add_extension('jinja2_time.TimeExtension')

        @app.before_request
        def enable_session_timeout():
            # set session to use Config.PERMANENT_SESSION_LIFETIME
            session.permanent = True
            # and reset the session timer on every request
            session.modified = True

        # send CSRF token in the cookie
        @app.after_request
        def set_csrf_cookie(response):
            if response:
                response.set_cookie('csrf_token', generate_csrf())
            return response
