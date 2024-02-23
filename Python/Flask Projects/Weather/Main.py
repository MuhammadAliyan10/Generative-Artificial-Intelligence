from flask import Flask as flask
from flask import request

app = flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)