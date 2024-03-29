#!/usr/bin/env python3
"""
BASIC FLASK APP
"""

from flask import Flask, render_template, request
from flask_babel import Babel
from typing import Union
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Class for babel config"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> Union[str, None]:
    """uses request accept best match"""
    # Check if the 'locale' parameter is in the request args
    if 'locale' in request.args:
        # Get the value of the 'locale' parameter
        requested_locale = request.args['locale']

        # Check if the requested_locale is a supported language
        if requested_locale in app.config['LANGUAGES']:
            return requested_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index_page():
    """function that returns the index page"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
