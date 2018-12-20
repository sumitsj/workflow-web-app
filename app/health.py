from flask import Blueprint


blueprint = Blueprint('health', __name__, url_prefix='/health')


@blueprint.route('/')
def check_application():
    return "All good. You don't need to be authenticated to call this."


@blueprint.route('/db')
def check_database_connection():
    return "Unable to connect to the database."
