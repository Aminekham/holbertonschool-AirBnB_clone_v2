#!/usr/bin/python3
"""
Having two routes
"""
from flask import Flask

app = Flask(__name__)

strict_slashes = False

@app.route('/')
def hello_hbnb():
    return("Hello HBNB!")
@app.route('/hbnb')
def hello_hbnb():
    return("HBNB")

if __name__ == '__main__':
    app.run()