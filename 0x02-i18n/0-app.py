#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """ first route """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
