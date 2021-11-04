import flask_flaat
from flask import current_app, abort
from flask_flaat import login_required, current_userinfo

from .extensions import login_manager
from .models import User

__all__ = ['login_required', 'admin_required']


@login_manager.user_loader
def load_user(current_userinfo):
    return User.query.get((
        current_userinfo['body']['sub'],
        current_userinfo['body']['iss'],
    ))


@flask_flaat.scope_required('eduperson_entitlement')
def is_admin():
    any_of = current_app.config['ADMIN_ENTITLEMENTS']
    entitlements = current_userinfo['eduperson_entitlement']
    return not set(any_of).isdisjoint(entitlements)


def admin_required(route):
    def decorated_view(*args, **kwargs):
        if not is_admin():
            abort(403)
        return route(*args, **kwargs)
    return login_required(decorated_view)
