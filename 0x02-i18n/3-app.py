#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template, request
from flask_babel import Babel
import gettext


class Config:
    """ Class Config """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ determine the best match with our supported languages"""
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    """ First Route"""
    home_title = gettext('home_title')
    home_header = gettext('home_header')
    return render_template('3-index.html',
                           home_title=home_title, home_header=home_header)


if __name__ == '__main__':
    app.run()
