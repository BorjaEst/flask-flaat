import functools

import flask
import flask_login
import flaat


from .extensions import login_manager
from .models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@login_manager.request_loader
def load_user_from_request(request):
    access_token = flaat.tokentools.get_access_token_from_request(request)
    if access_token is None:
        return None
    info = flaat.tokentools.get_accesstoken_info(access_token)
    user_id = (info['body']['sub'], info['body']['iss'])
    return User.query.get(user_id)


def valid_admin():
    True


def login_required():
    """Decorator to enforce a valid login."""
    def wrapper(original_func):
        @functools.wraps(original_func)
        def decorated(*args, **kwargs):
            return original_func(*args, **kwargs)
        return flask_login.login_required(decorated)
    return wrapper


def admin_required():
    """Decorator to enforce a valid admin."""
    def wrapper(original_func):
        @functools.wraps(original_func)
        def decorated(*args, **kwargs):
            if valid_admin():
                return original_func(*args, **kwargs)
            else:
                flask.abort(403)
        return login_required()(decorated)
    return wrapper
