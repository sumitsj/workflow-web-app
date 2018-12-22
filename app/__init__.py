import os
from flask import Flask
from flask_assets import Environment, Bundle


def create():
    app = Flask(__name__)
    app.config.from_object(os.getenv('FLASK_CONFIG', 'config.DevelopmentConfig'))

    # initialise database
    from .database import db
    with app.app_context():
        db.init_app(app)
        db.create_all()

    # apply blueprints to the app
    from app.blueprints import auth
    from app.blueprints import health
    from app.blueprints import workflow
    app.register_blueprint(health.blueprint)
    app.register_blueprint(workflow.blueprint)
    app.register_blueprint(auth.blueprint)

    # register error handlers
    from .errors import internal_error
    from .errors import not_found_error
    from .errors import handle_bad_request
    app.register_error_handler(400, handle_bad_request)
    app.register_error_handler(404, not_found_error)
    app.register_error_handler(500, internal_error)

    # Bundling and Minification
    assets = Environment(app)
    js = Bundle("js/jquery-3.3.1.js", "js/materialize.js", "js/main.js", filters='jsmin', output='dist/scripts.js')
    css = Bundle("css/materialize.css", "css/main.css", filters='cssmin', output='dist/styles.css')

    assets.register('js_all', js)
    assets.register('css_all', css)

    return app
