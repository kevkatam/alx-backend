#!/usr/bin/env python3
"""
flask app module
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """configures languages available in our app """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


babel = Babel(app)


app.config.from_object(Config)


@app.route('/')
def index() -> str:
    """renders template"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
