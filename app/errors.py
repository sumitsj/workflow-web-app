from flask import render_template


def handle_bad_request(e):
    return render_template('error.html', title='Error', message='Bad Request.',
                           header='400 Error'), 400


def not_found_error(error):
    return render_template('error.html', title='Error', message='This is not the web page you are looking for.',
                           header='404 Error'), 404


def internal_error(error):
    return render_template('error.html', title='Error', message='Unknown error. Please contact administrator.',
                           header='500 Error'), 500
