from flask import Blueprint, render_template

from .database import db

blueprint = Blueprint('health', __name__, url_prefix='/health')


@blueprint.route('/')
def check_application():
    return render_template('error.html',
                           message="All good. You don't need to be authenticated to call this",
                           header='Hurrey..!!!'), 400


@blueprint.route('/db')
def check_database_connection():
    message = "Unable to connect to the database."
    header = "Error"

    try:
        result = db.engine.execute('SELECT 1')
        if result.scalar() == 1:
            header = "Hurrey..!!!"
            message = "All good. Your database is up."
    except Exception as ex:
            print(message, ex)

    return render_template('error.html', message=message, header=header), 400

