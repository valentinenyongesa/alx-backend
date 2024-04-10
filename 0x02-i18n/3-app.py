#!/usr/bin/env python3
"""
Parametrize templates
"""

from flask import Flask, render_template
from flask_babel import Babel, _  # Import the _ function for translation

app = Flask(__name__)

babel = Babel(app)


class Config:
    """
    Configuration class for setting Babel's default locale and timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Determine the best match language based on the request.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Renders the index.html template with parametrized messages.
    """
    return render_template(
            '3-index.html', title=_('home_title'), header=_('home_header')
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
