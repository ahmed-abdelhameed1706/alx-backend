#!/usr/bin/env python3
""" basic app """
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """Config class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route("/")
def index():
    """index function"""
    return render_template("5-index.html")


@babel.localeselector
def get_locale():
    """get locale function"""
    if (
        request.args.get("locale")
        and request.args.get("locale") in app.config["LANGUAGES"]
    ):
        return request.args.get("locale")
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user():
    """get user"""
    if request.args.get("login_as"):
        user_id = int(request.args.get("login_as"))
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """before request"""
    user = get_user()
    if user:
        g.user = user


if __name__ == "__main__":
    app.run(debug=True)
