from flask import Blueprint, render_template, session

blueprint = Blueprint('workflow', __name__)


@blueprint.route('/')
def index():
    if 'username' in session:
        return render_template('landing-page.html', is_authenticated=True)
    else:
        return render_template('landing-page.html', is_authenticated=False)
