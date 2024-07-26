#!/usr/bin/python3

""" starts a flask application"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)

def home():
    """
    flask app
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
