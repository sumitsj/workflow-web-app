import os
from flask import Flask
from app import health

from .database import db


def create():
    app = Flask(__name__)
    app.config.from_object(os.getenv('FLASK_CONFIG', 'config.DevelopmentConfig'))

    with app.app_context():
        db.init_app(app)
        db.create_all()

    # apply blueprints to the app
    app.register_blueprint(health.blueprint)

    return app
