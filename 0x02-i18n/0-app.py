#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Renders the index.html template."""
    return render_template(
            'index.html', title='Welcome to Holberton', header='Hello world'
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
