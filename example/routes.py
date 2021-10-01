from flask import Blueprint, Response


public_blp = Blueprint('public', __name__)
user_blp = Blueprint('users', __name__)
admin_blp = Blueprint('admins', __name__)


@public_blp.route('', methods=['GET'])
def public_endpoint():
    return Response('', status=204, mimetype='application/json')


@user_blp.route('', methods=['GET'])
def users_endpoint():
    return Response('', status=204, mimetype='application/json')


@admin_blp.route('', methods=['GET'])
def admins_endpoint():
    return Response('', status=204, mimetype='application/json')
