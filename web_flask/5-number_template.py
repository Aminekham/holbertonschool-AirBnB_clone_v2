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
from flask import Flask, render_template


app = Flask(__name__)

strict_slashes = False


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    a = text.replace("_", " ")
    return f"C {a}"


# @app.route('/python/', defaults={'is cool'})
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>')
def python(text='is cool'):
    b = text.replace("_", " ")
    return f"Python {b}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    if type(n) is int:
        return("{} is a number".format(n))


@app.route('/number_template/<n>')
def number_template(n):
    return render_template('5-number.html', name=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
