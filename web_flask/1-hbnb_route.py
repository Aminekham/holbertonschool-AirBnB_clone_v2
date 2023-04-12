#!/usr/bin/python3
"""
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:

/: display “Hello HBNB!”
/hbnb: display “HBNB”

"""
from flask import Flask

app = Flask(__name__)

strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Printing Hello HBNB"""
    return("Hello HBNB!")


@app.route('/hbnb')
def hello_hbnb():
    """Printing HBNB"""
    return("HBNB")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')