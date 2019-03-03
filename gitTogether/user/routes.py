from flask import Blueprint, request

user = Blueprint('user', __name__)

@user.route('/user', methods=('GET',))
def get_users():
    return ({'page': 'Users'})

""" Examples of methods to be placed here

@user.route('/user', methods=('GET',))
def get_users():
    try:
        users = users.get_users()
    except IntegrityError:
        raise OSError

    return users
"""
