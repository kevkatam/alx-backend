#!/usr/bin/env python3
"""
flask app module
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


app = Flask(__name__)


class Config:
    """configures languages available in our app """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> Union[str, None]:
    """ defines the locale to use """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """ returns user dictionary or NONE if id can't be found """
    user_id = request.args.get('login_as', None)
    if user_id is None or int(user_id) not in users:
        return None
    return users.get(int(user_id))


@app.before_request
def before_request():
    """ uses get_user to find a user and set it as a global on
        flask.g.user
    """
    g.user = get_user()


@app.route('/', strict_slashes=False)
def index() -> str:
    """renders template"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
