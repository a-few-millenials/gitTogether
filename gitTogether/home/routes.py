from flask import request, Blueprint, jsonify

home = Blueprint('home', __name__)

@home.route("/")
@home.route("/home")
def index():
    test = {
        'test': 'Hello, World',
    }
    return jsonify(test)

@home.route("/about")
def about():
    return jsonify({'page': 'About us!'})
