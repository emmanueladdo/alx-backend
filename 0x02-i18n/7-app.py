#!/usr/bin/env python3
"""
BASIC FLASK APP
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union
app = Flask(__name__)
babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Class for babel config"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """this method force the Locale of the app"""
    if request.args.get('locale'):
        requested_lang = request.args.get('locale')
        if requested_lang in app.config['LANGUAGES']:
            return requested_lang
    if g.user:
        requested_lang = g.user.get('locale')
        if requested_lang in app.config['LANGUAGES']:
            return requested_lang
    requested_lang = request.headers.get('locale', None)
    if requested_lang:
        if requested_lang in app.config['LANGUAGES']:
            return requested_lang
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """
    this function returns a user dictionary or
    None if the ID
    cannot be found or if login_as was not passed
    """
    userId = request.args.get('login_as', None)
    if userId:
        return users.get(int(userId))
    return None


@app.before_request
def before_request():
    """Executes before any requestes"""
    g.user = get_user()


@app.route('/')
def index_page():
    """function that returns the index page"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
