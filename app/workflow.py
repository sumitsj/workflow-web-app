from flask import Blueprint, render_template


blueprint = Blueprint('workflow', __name__)


@blueprint.route('/')
def index():
    return render_template('landing-page.html')
