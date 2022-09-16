#!/usr/bin/python3
"""This module starts a Flask web application and displays states
"""
from flask import Flask
from flask import escape
from flask import render_template
from models import *

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def statesList():
    """displays states"""
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tearDownDB(self):
    """removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
