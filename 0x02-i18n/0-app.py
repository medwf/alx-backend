#!/usr/bin/env python3
"""
setup a basic Flask app 
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """The route of flask app"""
    return render_template(
        "0-index.html",
        tittle="Welcome to Holberton",
        h1="Hello world"
    )


if __name__ == "__main__":
    app.run()
