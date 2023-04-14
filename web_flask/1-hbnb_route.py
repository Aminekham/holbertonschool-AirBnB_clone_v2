#!/usr/bin/python3

"""starting with two routes"""

from flask import Flask

app = Flask(__name__)

# route page


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"

# hbnb page


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)