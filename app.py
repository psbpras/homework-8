"""
This module contains a simple Flask application.
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    """Return a simple greeting."""
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
