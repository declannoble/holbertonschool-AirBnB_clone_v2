#!/usr/bin/python3
"""This module starts a Flask web application and displays states
"""
from flask import Flask
from flask import escape
from flask import render_template
from models import *

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def display_cities_by_state():
    """displays cities by state"""
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(self):
    """removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
