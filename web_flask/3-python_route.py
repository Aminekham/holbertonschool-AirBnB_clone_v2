#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text
variable (replace underscore _ symbols with a space )
/python/<text>: display “Python ”, followed by the value
of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”
"""
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
