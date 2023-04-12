#!/usr/bin/python3
"""a second routing variable"""
from flask import Flask

app = Flask(__name__)

strict_slashes = False


@app.route('/')
def hello_HBNB():
    return("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    return("HBNB")


@app.route('/c/<text>')
def text(text):
    t = text.replace("_", " ")
    return("C {}".format(t))


@app.route('/python/<text>')
def text(text = 'is cool'):
    t = text.replace("_", " ")
    return("C {}".format(t))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
