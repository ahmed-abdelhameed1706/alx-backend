#!/usr/bin/env python3
""" basic app """
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from datetime import datetime
import pytz


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
    g.time = format_datetime()
    return render_template("index.html")


@babel.localeselector
def get_locale():
    """get locale function"""
    if (
        request.args.get("locale")
        and request.args.get("locale") in app.config["LANGUAGES"]
    ):
        return request.args.get("locale")
    if g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user.get("locale")
    if request.headers.get("Accept-Language"):
        languages = request.headers.get("Accept-Language").split(",")
        if languages and languages[0] in app.config["LANGUAGES"]:
            return languages[0]
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
    g.user = user


@babel.timezoneselector
def get_timezone():
    """get timezone"""
    if request.args.get("timezone"):
        try:
            timezone = pytz.timezone(request.args.get("timezone"))
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user and g.user.get("timezone"):
        try:
            timezone = pytz.timezone(g.user.get("timezone"))
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return pytz.timezone(app.config["BABEL_DEFAULT_TIMEZONE"])


if __name__ == "__main__":
    app.run(debug=True)
