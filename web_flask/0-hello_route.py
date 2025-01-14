#!/usr/bin/python3
"""
First webapp using flask
"""
from flask import Flask

app = Flask(__name__)

strict_slashes = False


@app.route("/")
def hello_world():
    return("Hello HBNB!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
