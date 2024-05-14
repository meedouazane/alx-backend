#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template, request, g
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    """ determine the best match with our supported languages  """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale
    header = request.headers.get('locale', None)
    if header in app.config['LANGUAGES']:
        return header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ Infer appropriate time zone """
    try:
        tzone = request.args.get('timezone')
        if tzone in Config.BABEL_DEFAULT_TIMEZONE:
            return pytz.timezone(tzone).zone
        if g.user:
            tzone2 = g.user.get('timezone')
            if tzone2 and tzone2 in Config.BABEL_DEFAULT_TIMEZONE:
                return pytz.timezone(tzone2).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return request.accept_languages.best_match(
                Config.BABEL_DEFAULT_TIMEZONE)


def get_user():
    """ returns a user dictionary or None """
    login_as = request.args.get('login_as')
    if not login_as:
        return None
    return users.get(int(login_as))


@app.before_request
def before_request():
    """ executed before all other functions """
    g.user = get_user()


@app.route('/')
def index():
    """ First Route"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
