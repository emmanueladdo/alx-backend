#!/usr/bin/env python3
"""
BASIC FLASK APP
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _, lazy_gettext

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Class for babel config"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """uses request accept best match"""
    if request.args.get('locale'):
        request_lang = request.args.get('locale')
        if request_lang in app.config['LANGUAGES']:
            return request_lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index_page():
    """function that returns the index page"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
