#!/usr/bin/env python3
"""A Basic Flask app.
"""
from flask_babel import Babel, _
from flask import Flask, render_template, request, g
from typing import Union, Dict


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page.
    """
    try:
        locale = g.user.get('locale', '')
    except AttributeError:
        locale = ''
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user() -> Union[Dict, None]:
    """methods that return user dict"""
    try:
        userId = int(request.args.get('login_as', '0'))
    except TypeError:
        return None
    if userId in users:
        return users[userId]
    return None


@app.before_request
def before_request() -> None:
    """this function set user to global on g.user"""
    g.user = get_user()


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
