import os
from flask import Flask, render_template, redirect, url_for
# from . import main


main = Flask(__name__)


@main.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    main.run(debug=True)
