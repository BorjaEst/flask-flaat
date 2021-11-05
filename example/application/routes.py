import flask_flaat
from flask_smorest import Blueprint

from . import authorization, models, database

# -------------------------------------------------------------------
# Resource blueprint routes -----------------------------------------
resource_blp = Blueprint('resource', __name__)


@resource_blp.route('public', methods=['GET'])
@resource_blp.response(204)
def public_endpoint():
    pass


@resource_blp.route('users', methods=['GET'])
@resource_blp.response(204)
@authorization.login_required
def users_endpoint():
    pass


@resource_blp.route('admins', methods=['GET'])
@resource_blp.response(204)
@authorization.admin_required
def admins_endpoint():
    pass


# -------------------------------------------------------------------
# User blueprint routes ---------------------------------------------
user_blp = Blueprint('users', __name__)


@user_blp.route('register', methods=['GET', 'POST'])
@user_blp.response(204)
@flask_flaat.scope_required('email')
def register():
    user = models.User(
        sub=flask_flaat.current_userinfo['body']['sub'],
        iss=flask_flaat.current_userinfo['body']['iss'],
        email=flask_flaat.current_userinfo['email'],
    )
    database.session.add(user)
    database.session.commit()
    pass

@user_blp.route('login', methods=['GET'])
@user_blp.response(204)
def login():
    flask_flaat.login_user()
    pass


@user_blp.route('logout', methods=['GET'])
@user_blp.response(204)
@authorization.login_required
def logout():
    flask_flaat.logout_user()
    pass
