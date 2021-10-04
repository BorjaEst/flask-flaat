from flask import Blueprint, Response

from . import authorization
from .extensions import login_manager

# -------------------------------------------------------------------
# Resource blueprint routes -----------------------------------------
resource_blp = Blueprint('resource', __name__)


@resource_blp.route('public', methods=['GET'])
def public_endpoint():
    return Response('', status=204, mimetype='application/json')


@resource_blp.route('users', methods=['GET'])
@authorization.login_required
def users_endpoint():
    return Response('', status=204, mimetype='application/json')


@resource_blp.route('admins', methods=['GET'])
@authorization.admin_required
def admins_endpoint():
    return Response('', status=204, mimetype='application/json')


# -------------------------------------------------------------------
# User blueprint routes ---------------------------------------------
user_blp = Blueprint('users', __name__)


@user_blp.route('login', methods=['GET'])
@login_manager.login
def login(user):
    return Response('', status=204, mimetype='application/json')


@user_blp.route('logout', methods=['GET'])
@login_manager.logout
def logout(user):
    return Response('', status=204, mimetype='application/json')
