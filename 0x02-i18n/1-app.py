#!/usr/bin/env python3
""" Basic Flask app """
from datetime import timezone
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """ Class Config """

    LANGUAGES = ["en", "fr"]
    DEFAULT_LOCALE = 'en'
    DEFAULT_TIMEZONE = timezone.utc


bable= Babel(app, locale_selector=Config.DEFAULT_LOCALE, timezone_selector=Config.DEFAULT_TIMEZONE)


@app.route('/')
def index():
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
