#!/usr/bin/python3
"""Sript that starts a Flask web app with 7 routes"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbn():
    """return Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """function to return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text_var(text):
    """function to display text variable passed in"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythontext(text="is cool"):
    """function displays python with text"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def my_number(n):
    """return n is a number if it is int"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_number(n):
    """display html if n is int"""
    n = str(n)
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    """return html about n if even or odd"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)
