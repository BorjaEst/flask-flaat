from flask import Blueprint, Response, request

import flask_flaat
from . import authorization

# -------------------------------------------------------------------
# Resource blueprint routes -----------------------------------------
resource_blp = Blueprint('resource', __name__)


@resource_blp.route('public', methods=['GET'])
def public_endpoint():
    return Response('', status=204, mimetype='application/json')


@resource_blp.route('users', methods=['GET'])
@authorization.login_required()
def users_endpoint():
    return Response('', status=204, mimetype='application/json')


@resource_blp.route('admins', methods=['GET'])
@authorization.admin_required()
def admins_endpoint():
    return Response('', status=204, mimetype='application/json')


# -------------------------------------------------------------------
# User blueprint routes ---------------------------------------------
user_blp = Blueprint('users', __name__)


@user_blp.route('login', methods=['GET'])
def login():
    user = authorization.load_user_from_request(request)
    flask_flaat.login_user(user)
    return Response('', status=204, mimetype='application/json')


@user_blp.route('logout', methods=['GET'])
def logout():
    flask_flaat.logout_user()
    return Response('', status=204, mimetype='application/json')
