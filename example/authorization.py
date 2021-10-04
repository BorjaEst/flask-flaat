import flask_flaat

from .extensions import login_manager
from .models import User


@login_manager.user_loader
def load_user(user_subiss):
    return User.query.get(user_subiss)


def login_required(route):
    """Decorator to enforce a valid login."""
    return flask_flaat.login_required(route)


def admin_required(route):
    """Decorator to enforce a valid admin."""
    return flask_flaat.group_required(
        group='admins',
        claim='groups',
    )(route)
