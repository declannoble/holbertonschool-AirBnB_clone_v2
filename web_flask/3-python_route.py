#!/usr/bin/python3
"""This module starts a Flask web application and display HBNB"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Returns the string Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """Returns the string HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cIsFun(text):
    """returns value of text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonIsCool(text='is cool'):
    """returns value of text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def isItaNumber(n):
    """returns n variable only if it is an integer"""
    if type(n) is int:
        return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numberTemplate(n):
    """returns a html page if n is an integer"""
    if type(n) is int:
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numCheck(n):
    """checks if n is odd or even and displays html page as result"""
    if type(n) is int:
        return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
