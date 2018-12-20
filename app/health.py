from flask import Blueprint

from .database import db

blueprint = Blueprint('health', __name__, url_prefix='/health')


@blueprint.route('/')
def check_application():
    return "All good. You don't need to be authenticated to call this."


@blueprint.route('/db')
def check_database_connection():
    message = "Unable to connect to the database."

    try:
        result = db.engine.execute('SELECT 1')
        if result.scalar() == 1:
            message = "All good. Database is up."
    except Exception as ex:
            print(message, ex)

    return message
