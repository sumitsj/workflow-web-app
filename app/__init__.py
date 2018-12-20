from flask import Flask
from app import health


def create():
    app = Flask(__name__)

    # apply blueprints to the app
    app.register_blueprint(health.blueprint)

    return app
