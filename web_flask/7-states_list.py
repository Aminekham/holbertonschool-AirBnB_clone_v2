#!/usr/bin/python3
"""Flask with data engine"""
from flask import Flask
from flask import render_templates
from models import storage

app = Flask(__name__)


@app.route('/stetes_list', strict_slashes = False)
def states_list():
    states = dict()
    states = storage.all(state)
    final_list = list()
    final_list = states.values()
    return(render_templates('7-states_list.html', states = final_list))


@app.teardown_appcontext()
def close():
    storage.close()

if __name__ == '__main__':
    app.run(host=0.0.0.0, port=5000)
