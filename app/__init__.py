import os
from flask import Flask
from app import health, workflow
from flask_assets import Environment, Bundle

from .database import db
from .errors import *


def create():
    app = Flask(__name__)
    app.config.from_object(os.getenv('FLASK_CONFIG', 'config.DevelopmentConfig'))

    with app.app_context():
        db.init_app(app)
        db.create_all()

    # apply blueprints to the app
    app.register_blueprint(health.blueprint)
    app.register_blueprint(workflow.blueprint)

    # register error handlers
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
