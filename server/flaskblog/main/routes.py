from flask import Blueprint
from flask import render_template, url_for, request


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')



