import functools

import flask_flaat
from flask import current_app

from .extensions import login_manager
from .models import User


@login_manager.user_loader
def load_user(user_info):
    return User.query.get((
        user_info['body']['sub'],
        user_info['body']['iss'],
    ))


def login_required(route):
    """Decorator to enforce a valid login."""
    @functools.wraps(route)
    def decorated_function(*args, **kwargs):
        return flask_flaat.login_required(
            route
        )(*args, **kwargs)
    return decorated_function


def admin_required(route):
    """Decorator to enforce a valid admin."""
    @functools.wraps(route)
    def decorated_function(*args, **kwargs):
        return flask_flaat.group_required(
            group=current_app.config['ADMINS_GROUP'],
            claim=current_app.config['ADMINS_CLAIM'],
        )(route)(*args, **kwargs)
    return decorated_function
