#!/usr/bin/env python3
"""
Mock logging in
"""

from flask import Flask, render_template, g
from flask_babel import Babel, _
import pytz

app = Flask(__name__)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    Determine the best match language based on the request or URL parameter.
    """
    if 'locale' in request.args:
        if request.args['locale'] in app.config['LANGUAGES']:
            return request.args['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(user_id):
    """
    Retrieve user information from the mock user table.
    """
    return users.get(user_id)


@app.before_request
def before_request():
    """
    Execute before all other functions to find and set the logged-in user.
    """
    user_id = request.args.get('login_as')
    if user_id:
        user = get_user(int(user_id))
        g.user = user
    else:
        g.user = None


@app.route('/')
def index():
    """
    Renders the index.html template with appropriate welcome message.
    """
    if g.user:
        welcome_message = _('logged_in_as', username=g.user['name'])
    else:
        welcome_message = _('not_logged_in')
    return render_template('5-index.html', welcome_message=welcome_message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
