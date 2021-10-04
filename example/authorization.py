import functools

import flask
import flask_flaat

from .extensions import login_manager
from .models import User


@login_manager.user_loader
def load_user(user_subiss):
    return User.query.get(user_subiss)


def valid_admin():
    True


def login_required(route):
    """Decorator to enforce a valid login."""
    @functools.wraps(route)
    def decorated(*args, **kwargs):
        return route(*args, **kwargs)
    return flask_flaat.login_required(decorated)


def admin_required(route):
    """Decorator to enforce a valid admin."""
    @functools.wraps(route)
    def decorated(*args, **kwargs):
        if valid_admin():
            return route(*args, **kwargs)
        else:
            flask.abort(403)
    return login_required(decorated)
