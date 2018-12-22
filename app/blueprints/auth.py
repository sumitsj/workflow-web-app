from flask import Blueprint, render_template, request, redirect, session

blueprint = Blueprint('auth', __name__)


@blueprint.route('/login', methods=["POST"])
def login():
    username = request.form['username']
    password = request.form['password']
    if username.lower() == 'sumit' and password.lower() == 'sumit8855':
        session['username'] = username
        return redirect('/')
    else:
        return render_template('error.html', title='Unauthorized', message='Invalid Username or Password.',
                               header='Unauthorized'), 401
