#!/usr/bin/env python3
""" Basic Flask app """
from datetime import UTC
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """ Class Config """

    LANGUAGES = ["en", "fr"]


bable= Babel(app, locale_selector=Config.LANGUAGES[0], timezone_selector=UTC)


@app.route('/')
def index():
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
