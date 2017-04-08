import os
from flask import Flask, render_template, redirect, url_for
# from . import main


main = Flask(__name__)


@main.route("/")
def index():
    return render_template('index.html')


@main.route("/aboutUs/")
def aboutUs():
    return 'about us page'


@main.route("/contact/")
def contact():
    return 'contact us page'


@main.route("/data/")
def data():
    return 'Data Page'


if __name__ == '__main__':
    main.run(debug=True)
