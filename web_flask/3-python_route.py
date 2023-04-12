#!/usr/bin/python3
"""a second routing variable"""
from flask import Flask

app = Flask(__name__)

strict_slashes = False


@app.route('/')
def hello_HBNB():
    """This is a route that maps the root URL to a view function named hello_HBNB(), which returns the string "Hello HBNB!" """
    return("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    """This is a route that maps the URL "/hbnb" to a view function named hbnb(), which returns the string "HBNB"."""
    return("HBNB")


@app.route('/c/<text>')
def text(text):
    """This is a route that maps URLs with a format of "/c/<text>" to a view function named text(), which takes in a variable text and returns a 
    string that begins with "C " followed by the value of text with underscores replaced with spaces."""
    t = text.replace("_", " ")
    return("C {}".format(t))


@app.route('/python/<text>')
def text(text = 'is cool'):
    """This is a route that maps URLs with a format of "/python/<text>" to a view function named text(), 
    which takes in an optional variable 
    text (with a default value of "is cool") and returns a string that begins with "C " 
    followed by the value of text with underscores replaced with spaces."""
    t = text.replace("_", " ")
    return("C {}".format(t))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
