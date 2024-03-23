#!/usr/bin/python3
"""Sript that starts a Flask web app with 6 routes"""

from flask import Flask

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
def var_num_template(n):
        """function to display number in html page"""
        return render_template("5-number.html", n=n)


if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)
