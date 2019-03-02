from flask import request, Blueprint

home = Blueprint('home', __name__)

@home.route("/")
@home.route("/home")
def index():
    return 'Hello, World!'
