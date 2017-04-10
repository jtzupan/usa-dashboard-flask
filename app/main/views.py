import os
from flask import Flask, render_template, redirect, url_for, send_file
# from . import main
import job_scheduler

main = Flask(__name__)


@main.route("/")
def index():
    return render_template('index.html')


@main.route("/aboutUs/")
def aboutUs():
    return render_template('aboutUs.html')


@main.route("/contact/")
def contact():
    return 'contact us page'


@main.route("/download/", methods=["GET", "POST"])
def download():
    return render_template('downloads.html')


@main.route('/return-file/')
def return_file():
    filepath = os.path.join('data', 'det', 'sampleData.txt')
    return send_file(filepath, attachment_filename='sampleData.txt', as_attachment=True)


if __name__ == '__main__':
    main.run(debug=True)
