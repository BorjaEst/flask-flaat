from flask import Blueprint, Response

# -------------------------------------------------------------------
# Resource blueprint routes -----------------------------------------
resource_blp = Blueprint('resource', __name__)


@resource_blp.route('public', methods=['GET'])
def public_endpoint():
    return Response('', status=204, mimetype='application/json')


@resource_blp.route('users', methods=['GET'])
def users_endpoint():
    return Response('', status=204, mimetype='application/json')


@resource_blp.route('admins', methods=['GET'])
def admins_endpoint():
    return Response('', status=204, mimetype='application/json')


# -------------------------------------------------------------------
# User blueprint routes ---------------------------------------------
user_blp = Blueprint('users', __name__)


@user_blp.route('login', methods=['GET'])
def login():
    pass


@user_blp.route('logout', methods=['GET'])
def logout():
    pass
