#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ Class Config """

    LANGUAGES = ["en", "fr"]
    DEFAULT_LOCALE = 'en'
    DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
bable= Babel(app)


@app.route('/')
def index():
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
