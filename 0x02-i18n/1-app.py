#!/usr/bin/env python3
"""
setup a basic Flask app
"""

from flask_babel import Babel
from flask import Flask, render_template


class Config:
    """class Config babel"""
    LANGUAGES = ["en", "fr"]
    DEFAULT_LOCAL = "en"
    TIME_ZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@app.route("/")
def home() -> str:
    """The route of flask app"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
