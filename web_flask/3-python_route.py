#!/usr/bin/python3
"""
Hello module is a simple module to say hello
"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """
    hello hbnb
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ display hbnb """
    return "HBNB"


@app.route('/c/<text>')
def c_with_params(text):
    """ display path"""
    text_n = text.replace('_', ' ')
    return "C {}".format(text_n)


@app.route("/python", defaults={'text': 'is cool'})
@app.route("/python/<text>")
def python_with_params(text):
    """ display path python"""
    text_n = text.replace('_', ' ')
    return f'Python {escape(n_text)}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
