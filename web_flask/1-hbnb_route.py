#!/usr/bin/python3
"""
Having two routes
"""
from flask import Flask

strict_slashes = False
app = Flask(__name__)

@app.route('/')
def hello_hbnb():
    return("Hello HBNB!")
@app.route('/hbnb')
def hello_hbnb():
    return("HBNB")

if __name__ == '__main__':
    app.run()